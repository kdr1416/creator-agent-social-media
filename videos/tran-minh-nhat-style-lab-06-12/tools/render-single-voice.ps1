param(
  [Parameter(Mandatory=$true)][string]$ProjectPath,
  [Parameter(Mandatory=$true)][string]$NarrationPath,
  [string]$OutputName = 'warm-doodle.mp4',
  [string]$FfmpegPath = 'ffmpeg',
  [string]$HyperframesVersion = '0.8.170'
)
$ErrorActionPreference = 'Stop'
$projectRoot = (Resolve-Path -LiteralPath $ProjectPath).Path
$voiceFile = (Resolve-Path -LiteralPath $NarrationPath).Path
$entry = Join-Path $projectRoot 'index.html'
$derived = Join-Path $projectRoot 'render-src/visual-only.html'
New-Item -ItemType Directory -Path (Join-Path $projectRoot 'render-src') -Force | Out-Null
$renderDir = Join-Path $projectRoot 'renders'
$pictureFile = Join-Path $renderDir 'visual-only.mp4'
$finalFile = Join-Path $renderDir $OutputName
if ([System.IO.Path]::GetFileName($OutputName) -ne $OutputName) { throw 'OutputName must be a file name within renders/.' }
if (Test-Path -LiteralPath $finalFile) { throw "Refusing to replace existing output: $finalFile" }
$html = [System.IO.File]::ReadAllText($entry)
$pattern = '(?s)<audio\b[^>]*>.*?</audio>'
if ([regex]::Matches($html,$pattern).Count -ne 1) {
  throw 'This fallback supports exactly one supplied narration track, not multi-track mixes.'
}
$pictureHtml = [regex]::Replace($html,$pattern,'')
$pictureHtml = $pictureHtml.Replace('assets/','../assets/')
if ((Test-Path -LiteralPath $derived) -and [System.IO.File]::ReadAllText($derived) -ne $pictureHtml) {
  throw "Refusing to replace a different derivative: $derived"
}
[System.IO.File]::WriteAllText($derived,$pictureHtml,[System.Text.UTF8Encoding]::new($false))
New-Item -ItemType Directory -Path $renderDir -Force | Out-Null
$previousPath = $env:PATH
if (Test-Path -LiteralPath $FfmpegPath) {
  $FfmpegPath = (Resolve-Path -LiteralPath $FfmpegPath).Path
  $env:PATH = (Split-Path -Parent $FfmpegPath) + ';' + $env:PATH
}
Push-Location -LiteralPath $projectRoot
try {
  & npx --yes "hyperframes@$HyperframesVersion" render --composition render-src/visual-only.html --quality delivery --fps 30 --workers 2 --output $pictureFile
  if ($LASTEXITCODE -ne 0) { throw 'HyperFrames picture render failed.' }
  & $FfmpegPath -n -i $pictureFile -i $voiceFile -map '0:v:0' -map '1:a:0' -c:v copy -c:a aac -b:a 192k -movflags +faststart $finalFile
  if ($LASTEXITCODE -ne 0) { throw 'Narration mux failed.' }
  Write-Output "Created $finalFile. Verify streams, source hashes and timing before delivery."
} finally { Pop-Location; $env:PATH = $previousPath }

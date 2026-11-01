$ErrorActionPreference = "Stop"
Set-Location "$PSScriptRoot\.."

New-Item -ItemType Directory -Force -Path build\renders\intermediate | Out-Null

$plan = @(
  @{id='S01'; frames=181},
  @{id='S02'; frames=115},
  @{id='S03'; frames=128},
  @{id='S04'; frames=121},
  @{id='S05'; frames=171},
  @{id='S06'; frames=174},
  @{id='S07'; frames=140},
  @{id='S08'; frames=164},
  @{id='S09'; frames=224},
  @{id='S10'; frames=184},
  @{id='S11'; frames=205},
  @{id='S12'; frames=106},
  @{id='S13'; frames=136},
  @{id='S14'; frames=206}
)

$concatList = "build\renders\intermediate\concat.txt"
if (Test-Path $concatList) { Remove-Item $concatList }

$totalTarget = 0
foreach ($item in $plan) {
  $sid = $item.id
  $f = $item.frames
  $totalTarget += $f
  $src = "build\scenes\$sid\renders\pilot.mp4"
  $dst = "build\renders\intermediate\$sid.mp4"
  Write-Host "Encoding $sid ($f frames)..."
  & ffmpeg -y -i $src -frames:v $f -an -c:v libx264 -crf 15 -preset fast -pix_fmt yuv420p -r 30 $dst 2>$null
  $cnt = (& ffprobe -v error -select_streams v:0 -count_packets -show_entries stream=nb_read_packets -of default=nokey=1:noprint_wrappers=1 $dst).Trim()
  Write-Host "  $sid -> Target: $f, Packets: $cnt"
  "file '$sid.mp4'" | Out-File -FilePath $concatList -Append -Encoding ascii
}

Write-Host "Total target frames: $totalTarget"

# Concat to clean video
Write-Host "Concatenating clean video..."
$cleanVideo = "build\renders\VIDEO-33-clean.mp4"
& ffmpeg -y -f concat -safe 0 -i $concatList -c copy $cleanVideo 2>$null
$cleanPackets = (& ffprobe -v error -select_streams v:0 -count_packets -show_entries stream=nb_read_packets -of default=nokey=1:noprint_wrappers=1 $cleanVideo).Trim()
$cleanDuration = (& ffprobe -v error -show_entries format=duration -of default=nokey=1:noprint_wrappers=1 $cleanVideo).Trim()
Write-Host "Clean Video: $cleanPackets packets, duration: $cleanDuration s"

# Mux master with source_audio.wav
Write-Host "Muxing master video with original source audio..."
$masterVideo = "build\renders\VIDEO-33-master.mp4"
& ffmpeg -y -i $cleanVideo -i inputs\source_audio.wav -c:v copy -c:a aac -b:a 256k -shortest $masterVideo 2>$null
$masterPackets = (& ffprobe -v error -select_streams v:0 -count_packets -show_entries stream=nb_read_packets -of default=nokey=1:noprint_wrappers=1 $masterVideo).Trim()
$masterDuration = (& ffprobe -v error -show_entries format=duration -of default=nokey=1:noprint_wrappers=1 $masterVideo).Trim()
Write-Host "Master Video: $masterPackets packets, duration: $masterDuration s"

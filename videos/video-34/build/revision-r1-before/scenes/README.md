# Independent scenes

Create a directory per ID from inputs/scene-manifest.json when production is authorized.
HyperFrames: standalone composition entry (normally index.html), a paused seekable
GSAP timeline, IDs matching its root, and local assets. Set canvas dimensions from
project_manifest.json and picture duration from the cumulative frame plan.
Remotion: TSX entry + composition ID, dimensions/FPS/frame duration from the same
configuration/plan via props or calculateMetadata; source need not be index.html.

Configure explicit local render_argv in each record or project renderers. Commands
run with the source file's parent as cwd. Keep intermediate engine outputs outside
scene source directories (e.g. build/) so fingerprints remain stable. The only
excluded generated file in a scene source fingerprint is its declared render output.

No scene source or media is bundled: this template must not manufacture a pilot.

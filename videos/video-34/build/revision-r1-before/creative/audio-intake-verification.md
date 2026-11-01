# Video-34 — Codex intake verification

Date: 2026-11-01. Status: technical intake passed; not creative/pilot approval.

## Measured from actual project files

- Master: `inputs/Generated Audio November 01, 2026 - 5_35PM.wav`.
- SHA256: `6b92d56bb90f3c4e702903d53d098d7c1765daf716879e8de60826a3110425c1`.
- PCM WAV, mono, 16-bit, 24,000 Hz, 2,232,960 samples, 93.040000 s.
- 17 contiguous scenes cover the entire master, with no gaps/overlaps.
- Scene duration range: 3.105042–8.939250 s.
- Raw ASR contains 20 segments; word file contains 375 entries. All word bounds
  are within the master and word starts are monotonic. Ten words have probability
  below 0.5; this is a review signal, not an accuracy score for the whole transcript.
- Each of the 16 internal cuts starts at a zero-valued sample. RMS measured in
  a 40 ms window centered on each cut is approximately −81.55 to −49.18 dBFS.

Detailed cut sample values and measurements: `audio-intake-verification.json`.
Master, raw ASR, word timestamps, supplied transcript and scene bounds were not
modified. ASR was not rerun and all 93 s were not independently audited by ear.

Zero-valued cuts and low local energy reduce discontinuity risk; they do not prove
that clicks/pops are completely eliminated in every independent export/playback.
That requires inspection of actual scene audio/render outputs. Likewise, ASR word
timestamps are not a claim of sample-exact word alignment.

## Content check before prominent advertising claims

S13 contains the supplied claim about approximately VND 3.8 billion and four
generations. Do not turn that number into an unqualified all-in price graphic
without a documented package scope, exchange-rate basis, family composition and
included/excluded costs from the brand.

The current [official Residency Malta MPRP page](https://residencymalta.gov.mt/legal-framework-mprp-2/)
describes the possibility of including up to four generations, subject to eligibility.
It also lists separate administration/contribution, property, donation, dependant,
insurance and residence-card requirements. It does not establish the supplied VND
3.8 billion figure as an all-in price for four generations. The official page states
administration €60,000, contribution €37,000, donation €2,000, plus qualifying rent
or purchase and other applicable charges. No currency conversion was performed.

Keep the supplied voice untouched. S13 price scope remains pending confirmation;
no silent rewrite of narration or corrected_text was made. Lifestyle/general
comparisons in the script should be presented as an illustrative editorial story,
not as a guarantee about every resident's experience or a family's immigration outcome.

## Confirmed preferences and brand capture

- User selected vertical 9:16 for Reels/TikTok/Shorts.
- User identified the avatar of [Esora Immi](https://www.facebook.com/esoraimmi68)
  as the logo; no reference video supplied.
- Public Facebook profile and its avatar photo were viewed directly in browser.
  Original JPEG downloaded at 2046×2048 and copied unchanged to
  `assets/brand/esora-avatar-original.jpg`; provenance/hash is in `assets/ledger.json`.
- Asset is a raster logo on its blue background, not a transparent/vector master.
  No AI redraw, recolor, background removal or upscale was performed.

Approval remains pending. No scene assets were generated and no scene was rendered.
The backup of changed ledger/state is in `build/intake-before-creative-20261101/`.

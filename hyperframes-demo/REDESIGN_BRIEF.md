# Structural Redesign Brief — Scene 6

> Scope: Scene 6 only. This file is not a global video template and must not be copied to other scenes. Global routing, text economy, composition and motion rules come from `.agents/skills/fk-edu-motion-explainer/SKILL.md`.

## Routing

- `render_mode`: `HF_ONLY`
- `routing_reason`: The idea is a precise graphic relationship between additional people/passports and additional financial proof. It does not require natural character performance.
- `asset_contract`: Separate transparent family cutout or static illustration, three passport/document layers, one orange financial shape, optional quiet brand mark, and a clean background. Do not use a flattened full-frame poster as the animation source.
- `hf_signature_motion`: passport object grouping → reactive displacement/reveal of the financial shape.
- `hf_supporting_motion`: one mask or discrete text reveal.
- `flow_action`: none by default.
- `flow_camera`: none.
- `overlay_zone`: not applicable; HyperFrames owns the full canvas.
- `handoff`: passport grouping directly triggers the financial shape and final phrase.

Use `HYBRID` only if the approved concept specifically needs believable hands placing the passports. In that case, Flow generates only the clean organic plate with no text, labels, logos or numbers; HyperFrames still owns the passport relationship graphic and all exact copy.

## Rejected result

The current composition is still a poster stack: persistent brand pill at the top, centered badges/cards in the upper half, and a centered family below. The timeline repeats opacity + small Y/scale entrances. Calling the layout "free-floating" does not change that structure because the main phrases remain boxed.

## Required concept

Explain **more accompanying family members require additional proof of funds** with one transformation and minimal copy.

- Duration: 4.2 seconds, vertical 720×1280.
- Opening: a close or medium shot of passports/documents, with the family grouped off-center. Avoid the centered poster composition.
- Build: one passport is joined by two more. Use object grouping as the signature motion; do not label each passport.
- Transform: the passport group displaces or reveals one orange financial block. The movement itself shows cause and effect.
- Resolve: show only `THÊM NGƯỜI → THÊM TÀI CHÍNH`. Use a mask reveal or discrete word replacement; remove intermediate graphics that compete with this phrase.
- Final hold: family/documents plus the single core phrase. Maximum two information groups. Keep the bottom 200px free.

## Optional Flow direction for `HYBRID` fallback only

Do not generate a Flow background for the default `HF_ONLY` route. Use this fallback only when natural hand interaction is essential and separated HyperFrames layers cannot convey it.

Suggested 4.2s action structure:

`0–1.4s: One passport is placed into the foreground from the left. Camera remains stable. 1.4–3.0s: Two more passports are placed beside it one at a time while the family remains grouped on the left. 3.0–4.2s: Hands withdraw and all documents hold still, leaving clean space on the right for graphics. No generated text, numbers, logos, labels, or watermark.`

## Acceptance gate

- Replace the current `.floating-content` vertical stack; do not adapt it.
- Main copy must not be inside bordered/filled cards. No category chip, explanatory subtext, passport labels, proof badge or second paraphrase.
- Total visible scene copy: six words (`THÊM NGƯỜI → THÊM TÀI CHÍNH`), plus an optional quiet brand mark.
- Use object-grouping plus reactive displacement/reveal as the signature motion. Opacity + Y/scale may only support it.
- Use no decorative connector unless it has two necessary visible anchors. Prefer direct contact/displacement.
- The final proof frame must differ from the rejected frame in subject position, text region, information structure, and motion family.
- Inspect opening, transformation, and final frames plus full playback before render.
- Do not reuse this scene's passport/grouping concept as the default structure for other scenes; route every scene independently through the global skill.

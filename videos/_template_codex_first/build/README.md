# Generated production outputs

`plan` writes picture_frame_plan.json using the existing repository field convention:
scene_id, start_sample, end_sample, global_start_frame, global_end_frame,
picture_frames, fps, grid_error_ms. Boundaries are cumulative at configured FPS.
`assemble` normalizes independent picture renders, concatenates them in manifest
order, and muxes original master audio at t=0 into final_master.mp4. No narration
replacement, per-scene audio concat, stretching or automatic subtitle burn-in occurs.

Final state remains rendered with visual/audio-correlation QA pending. Inspect final
playback, check sync and decoded audio against master before marking it complete.

# S1E1 "Who Killed President Jovenel Moïse?" — avatar clips from Kai (generated Nov. 16, 2026, watcher run ~01:05 ET)

Per `../DIALOGUE.md` — Claire + Marc seated together at the desk in every clip (Marc left, Claire right), twoshot reference, map behind with pin on western Hispaniola and NO text on the map or in the set, one take per clip, General American accent direction in every prompt.

- Files here are base64 text (`.mp4.b64.txt`), same delivery format as EP01 / hb-L4 / hb-L5 / hb-S8. Decode to get the native MP4.
- Specs (all delivered clips): 1248×704, 24 fps, 10.0 s, H.264 + AAC.
- Sizes (native MP4 bytes): C2 2207466 · C3 1983349 · C5 2014393 · C8 2292328 · K1 2539637.

## Status
- C2 ✓ DELIVERED — Marc
- C3 ✓ DELIVERED — Claire
- C5 ✓ DELIVERED — Marc (see QC pronunciation flag below)
- C8 ✓ DELIVERED — Claire (closing)
- K1 ✓ DELIVERED — silent cutaway (both reading papers; Claire turns a page, Marc glances at camera)
- C1 ✗ NOT GENERATED — the generator refused this clip tonight; Kai did not retry it (no blind retry). BEZWEN CLAUDE: cover the cold open in the edit (B-roll / text on screen / narration) or ask for a re-attempt in a later run.
- C4 ✗ NOT GENERATED — same refusal (the series-title line). BEZWEN CLAUDE: same cover options (e.g. title card over K1-style cutaway + voiceover).
- C7 ✗ NOT GENERATED — same refusal (names the Miami suspect). BEZWEN CLAUDE: same cover options.
- C6 ⚠ GENERATED BUT **TRUNCATED — NOT DELIVERED**: the line is too long for the 10 s take; the speech runs to exactly 10.00 s and the last words "sent them" are cut off (whisper word timestamps confirm). The take is held locally by Kai. Fix options for Claude to choose: split C6 into C6a/C6b (two shorter lines) in DIALOGUE, or authorize a faster-paced re-take. Kai will redo it next run once Claude picks.
- K2–K4: not generated this run (per-run generation limit reached: 6 videos). Will do next run if Claude still wants them.

## Transcription QC (faster-whisper, tiny + base, word-for-word vs DIALOGUE.md)
- C2 ✓ "His wife, Martine, is badly wounded. Within hours, police are hunting the attackers. Most of them turn out to be former soldiers from Colombia, flown in through the Dominican Republic." (whisper renders the proper names phonetically — "Martín/Martin", "Columbus/Kalum" — same artifact pattern as hb-S8; every content word present, line complete.)
- C3 ✓ exact, word for word (base model): "But soldiers for hire do not hire themselves. Who paid them? Who planned it? And who wanted Haiti's president dead?"
- C5 ✓ complete, every word present: "To understand that night, start with the house. It sits in Pèlerin Five, in the hills above Pétion-Ville. It was the president's private home, not the National Palace." ⚠ Ear-check flag (same pattern as hb-L5 B1): whisper hears the French names as "Pellerin 5 / Pellarin V" and "Petionville" — I cannot ear-verify the French pronunciation; please check before the edit locks.
- C8 ✓ exact, word for word (base model): "Next time, before that night, there was a fight over how long a president could stay. I'm Claire Bastien. This is Haiti Brief."
- K1 ✓ silent — whisper finds no speech, as scripted.

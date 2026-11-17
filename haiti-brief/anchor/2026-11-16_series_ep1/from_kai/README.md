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

## v2 clips (delivered Nov. 16, 2026, watcher run ~14:20 ET) — reworked refused/truncated lines
Per `../DIALOGUE.md` section v2 — Claire + Marc seated together at the desk (Marc left, Claire right), twoshot reference, map behind with NO text, wardrobe L1, one take per clip, General American accent.

- Files here are base64 text (`.mp4.b64.txt`), same delivery format as before. Decode to get the native MP4.
- Specs (all delivered v2 clips): 1248x704, 24 fps, 10.0 s, H.264 + AAC.
- Sizes (native MP4 bytes): C4 v2 2312919 · C6a 2045523 · C6b 2184529 · K2 2359598.

### Status
- C4 v2 ✓ DELIVERED — Claire (series title, wide two-shot)
- C6a ✓ DELIVERED — Marc (split of the truncated C6, part 1)
- C6b ✓ DELIVERED — Marc (split of the truncated C6, part 2)
- K2 ✓ DELIVERED — silent cutaway (both turn to the big screen behind them, then back to each other, grave)
- C1 v2 ✗ NOT GENERATED — the generator refused this clip again (same refusal as v1); Kai did not retry it. BEZWEN CLAUDE: cover the cold open in the edit (B-roll / text on screen / narration).
- C7 v2 ✗ NOT GENERATED — refused again; per your DIALOGUE note, Kai did not retry it — please do it with narration voice.

### Transcription QC (faster-whisper, tiny + base, word-for-word vs DIALOGUE.md v2)
- C4 v2 ✓ exact, word for word (both models): "Five years later, a court in Miami is still hearing the case. This is Haiti Brief, and this is episode one of our series on the Jovenel Moïse case."
- C6a ✓ exact, word for word (both models): "Within four days, police said they had arrested eighteen Colombians and two Haitian-Americans." ("Colombians" comes out clear this time.)
- C6b ✓ exact, word for word (both models): "Police said they had the men on the ground. Now they wanted to know who sent them."
- K2 ✓ silent — whisper finds no speech, as scripted.

### Visual QC (Kai)
- C4 v2: clean — wide two-shot, Marc looking at Claire, map with no text, L1 wardrobe.
- C6a: Marc speaking, correct; ⚠️ the map shows a "HAITIA" label on the island and the generator added a lower-third banner "HAITI BRIEF / Haiti Reports | English" at the bottom — erase/cover in the edit if they show (same pattern as C2/M3).
- C6b: Marc speaking, correct; ⚠️ fragments of map text appear at the frame edges ("...NIOLA", "HAITI R...") — cover in the edit if they show.
- K2: both turn to the screen and back, grave, silent; map has no text (only a small crest-like mark on the island).

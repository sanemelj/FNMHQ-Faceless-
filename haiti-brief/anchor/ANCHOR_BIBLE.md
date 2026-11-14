# Haiti Brief — anchor & studio bible (Saneme, Nov. 14, 2026)

Kai generates the anchor (avatar) and the studio. Claude writes the scripts and prompts, then does the final edit
(footage, maps, source tags, captions, music). Reference image: `HaitiBrief_studio_ref_v1.webp`.

## Anchor (lock this; never change between episodes)
- Black woman, about 35-40, dark brown skin, hair pulled back in a low bun, small stud earrings.
- Navy blazer, white crew-neck top. No necklace, no logo pin.
- Broadcast-news delivery (network evening news): authoritative, crisp articulation, ~160-170 words/min, key words stressed, falling intonation at the end of every statement. Warm but never chatty.
- Sits centered behind the curved desk; hands rest on the desk; small natural head moves only.
- Name: **none for now** (Saneme decides). She never says her own name.

## Second presenter: the correspondent (man) — new, Saneme Nov. 14
- Black man, about 40, dark brown skin, short hair, short neat beard. Charcoal suit, light-blue shirt, no tie.
- **Stands** at the large map wall on the left of the studio (not at the desk). Explains with small hand gestures toward the map.
- Voice: TV correspondent style, same broadcast rules as the anchor, a little more energy when explaining.
- Role: explains the story. Kai generates all his lines on camera (with one consistent voice); in the edit Claude covers most of them with real footage, so he is seen 1-2 times per episode.
- Name: none for now (Saneme decides).

## Who says what
- **Anchor (woman, desk):** cold open, transitions, segments with no footage, sign-off. ~25% of the episode.
- **Correspondent (man):** the explanation, over real footage. ~75%.

## Studio: fixes before the next renders
1. The map pin must be **on Haiti** (Hispaniola, western half). In v1 it sits on Central America.
2. **No invented numbers on the side screens** (28°C, "Infrastructure 42%", "Remittances 35%", "+1.2%", the pie chart).
   A news channel cannot show fake data. Use plain panels: HAITI BRIEF logo, "Haiti · Diaspora", or leave them dark.
3. The city behind her is not Port-au-Prince. Use a neutral night skyline with no recognisable city, or a soft blur.
4. Desk text: "HAITI BRIEF" only, or "HAITI BRIEF · Haiti news in English". Drop "Haiti Reports" (too close to "James Reports").
5. Keep the right third of the wall plain: Claude puts maps and footage there in the edit.

## Motion and lip-sync (Saneme, Nov. 14)
- Every clip is generated **with its audio** (voice made together with the video), so lips, face and gestures match the words.
- Both presenters move like real people: breathing, blinks, head and shoulder moves, expressions that follow the meaning.
  Correspondent: hand gestures, turns to the map and back, 1-2 steps. Anchor: seated, leans in on key lines, small hand moves.
- Redo any clip with lip-sync drift, warped hands, extra fingers or a face that shifts.
- Claude's edit: whenever a presenter's face is on screen, the audio is that clip's own audio (never re-timed or swapped),
  so the lips always match. Footage covers the voice in between; cutting back to the presenter keeps the same audio track.

## Delivery to Claude (per episode)
- One clip per segment: `HaitiBrief_EPxx_Axx.mp4`, **1920x1080 (or 4K), 30 fps**, the anchor centered so Claude can crop a 9:16 Short.
- Read the script **word for word**. If a name is hard, use the phonetic spelling given in brackets.
- 1 s of silence before and after each segment (Claude trims).
- Put the clips in `haiti-brief/anchor/<episode folder>/from_kai/` and commit to `main`.

## YouTube rule
Saneme sets the AI label himself when posting (YouTube Studio: **Altered or synthetic content = Yes**).
Claude does **not** write anything about AI in the title, description or tags.

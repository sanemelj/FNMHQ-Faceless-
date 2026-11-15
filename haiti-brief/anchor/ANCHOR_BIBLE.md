# Haiti Brief — anchor & studio bible (Saneme, Nov. 14, 2026)

Kai generates the anchor (avatar) and the studio. Claude writes the scripts and prompts, then does the final edit
(footage, maps, source tags, captions, music). Reference image: `HaitiBrief_studio_ref_v1.webp`.

## Anchor (lock this; never change between episodes)
- Black woman, about 35-40, dark brown skin, hair pulled back in a low bun, small stud earrings.
- Navy blazer, white crew-neck top. No necklace, no logo pin.
- Accent: **General American English** (both presenters). Haitian and Salvadoran names follow the bracketed pronunciations.
- Broadcast-news delivery (network evening news): authoritative, crisp articulation, ~160-170 words/min, key words stressed, falling intonation at the end of every statement. Warm but never chatty.
- Sits centered behind the curved desk; hands rest on the desk; small natural head moves only.
- Name: **Claire Bastien** (Saneme, Nov. 14). Lower third: CLAIRE BASTIEN · Anchor.

## Second presenter: the correspondent (man) — new, Saneme Nov. 14
- Black man, about 42, deep brown skin, black cropped fade, short trimmed beard, dark brown eyes. Charcoal-gray suit, white shirt, deep-red tie (locked from Kai's reference sheet v1, Nov. 14).
- **Sits at the desk, LEFT seat, next to the anchor (RIGHT seat)**: layout from Saneme's image `HaitiBrief_two_anchor_layout_ref.webp` (Nov. 14). Each has a desk microphone and papers. Use the **studio v2 fixes** (pin on Port-au-Prince, no fake numbers; desk "HAITI BRIEF" + "Haiti Reports | English" is fine), not the screens of that image.
- Voice: TV correspondent style, same broadcast rules as the anchor, a little more energy when explaining.
- Role: explains the story. Kai generates all his lines on camera (with one consistent voice); in the edit Claude covers most of them with real footage, so he is seen 1-2 times per episode.
- Name: **Marc Valcourt** (Saneme, Nov. 14). Lower third: MARC VALCOURT · Correspondent.

## Who says what
- **Anchor (woman, desk):** cold open, transitions, segments with no footage, sign-off. ~25% of the episode.
- **Correspondent (man):** the explanation, over real footage. ~75%.

## Studio: fixes before the next renders
1. The map pin must be **on Haiti** (Hispaniola, western half). In v1 it sits on Central America.
2. **No invented numbers on the side screens** (28°C, "Infrastructure 42%", "Remittances 35%", "+1.2%", the pie chart).
   A news channel cannot show fake data. Use plain panels: HAITI BRIEF logo, "Haiti · Diaspora", or leave them dark.
3. The city behind her is not Port-au-Prince. Use a neutral night skyline with no recognisable city, or a soft blur.
4. Desk text: "HAITI BRIEF" with the line "Haiti Reports | English" under it: the YouTube channel is named **"Haiti Brief | Haiti Reports"** (Saneme, Nov. 14). The "Haiti Reports" line is OK.
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

## Aksan anglè ameriken (Saneme, Nov. 15)
**AKSAN (Saneme, 15 nov) — OBLIGATWA NAN CHAK PROMPT:** "Speak in a neutral **General American (U.S.) English** accent, like a U.S. network evening-news anchor: rhotic r's, American flap t ("matter" = MAD-er, "city" = SID-ee, "water" = WAH-der), American vowels. **No British, Caribbean, African or French accent.**" Nan hb-L4, "matter" te soti "mata": sa pa dwe rive ankò.

## Toujou ansanm (Saneme, Nov. 15)
Claire ak Marc toujou chita **ansanm nan menm biwo a** (Marc a gòch, Claire a dwat), nan chak klip, menm lè se youn sèl k ap pale. Pa gen klip kote yon prezantatè pou kont li. Foto referans: `refs/HaitiBrief_ref_twoshot.jpg`.

## Ka Jovenel Moïse (Saneme, Nov. 15)
Pa gen footage tribinal; se jounalis ki pale, e nou pa itilize imaj yo. Pou videyo sou pwosè Miami yo, **avatar yo pale plis** (Claire prezante, Marc rakonte temwayaj yo ak sous la), ak imaj kontèks ofisyèl oswa domèn piblik. Pa janm fè sanble yon akize koupab anvan vèdik.

## Kredi Kai (Saneme, Nov. 14)
Kai's generation credits are limited. Claude asks for a redo ONLY for a factual/script error or a defect the edit cannot hide. Minor issues (map labels, small face drift, a stutter) are fixed in the edit: cover with footage, no zoom on the face, blur/mask, trim.

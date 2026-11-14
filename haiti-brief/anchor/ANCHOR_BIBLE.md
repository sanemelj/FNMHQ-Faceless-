# Haiti Brief — anchor & studio bible (Saneme, Nov. 14, 2026)

Kai generates the anchor (avatar) and the studio. Claude writes the scripts and prompts, then does the final edit
(footage, maps, source tags, captions, music). Reference image: `HaitiBrief_studio_ref_v1.webp`.

## Anchor (lock this; never change between episodes)
- Black woman, about 35-40, dark brown skin, hair pulled back in a low bun, small stud earrings.
- Navy blazer, white crew-neck top. No necklace, no logo pin.
- Calm, serious, warm. American English, neutral accent, measured pace (~150 words/min).
- Sits centered behind the curved desk; hands rest on the desk; small natural head moves only.
- Name: **none for now** (Saneme decides). She never says her own name.

## Second presenter: the correspondent (man) — new, Saneme Nov. 14
- Black man, about 40, dark brown skin, short hair, short neat beard. Charcoal suit, light-blue shirt, no tie.
- **Stands** at the large map wall on the left of the studio (not at the desk). Explains with small hand gestures toward the map.
- Role: explains the story. Mostly **voice-over** (Claude makes his voice and audio files); on camera only 1-2 times per episode.
- On-camera clips: Claude sends the audio file `HaitiBrief_EPxx_Cxx.wav`; Kai lip-syncs the correspondent to that exact audio.
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

## Delivery to Claude (per episode)
- One clip per segment: `HaitiBrief_EPxx_Axx.mp4`, **1920x1080 (or 4K), 30 fps**, the anchor centered so Claude can crop a 9:16 Short.
- Read the script **word for word**. If a name is hard, use the phonetic spelling given in brackets.
- 1 s of silence before and after each segment (Claude trims).
- Put the clips in `haiti-brief/anchor/<episode folder>/from_kai/` and commit to `main`.

## YouTube rule
Saneme sets the AI label himself when posting (YouTube Studio: **Altered or synthetic content = Yes**).
Claude does **not** write anything about AI in the title, description or tags.

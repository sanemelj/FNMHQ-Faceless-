# Claude — FNMHQ half-hour check protocol (Sam, Nov 17 2026: work 24/7 without Sam, Haiti Brief model)

Every wake (:12 and :42, 6:12 AM–11:42 PM CT):
0. FIRST schedule the next wake (send_later, next :12 or :42; after 23:42 → next day 06:12). Never break the chain.
1. `git pull --rebase` in /home/claude/fnmhq-repo. Read today's + yesterday's `YYYY-MM-DD/NOTES.md`, `POSTED.md`, `avatar/*/NOTES.md`, new files in `avatar/*/from_kai/` and `avatar/refs/`, `inbox/scoops/`, `reports/`, `watch/LATEST.md`.
2. Every new `Kai:` line → do the work (QC clips: decode .b64.txt, faster-whisper + frame grid; edit avatar long-forms; answer; fix KIT) and reply in the same NOTES.md: `- HH:MM CT · Claude → Kai: ...` (Haitian Creole). Commit + push.
3. FACEBOOK 1M (FB_1M_PLAN.md): also Facebook photo cards 9:00 AM (last night's result), 2:00 PM (debate), 8:30 PM (tonight's moment), and BREAKING FT/sacking cards within 30 min — tool: tools/photocard/card.py spec.json out.jpg (1080x1350), card in KIT as `Photo_N_Nov_D.jpg`, Facebook only.
4. AVATAR RULE (Sam, Nov 17 22:52): NO clip without Callum & Jamie. Every Short = 2 avatar clips (hook + close) + narration over photos; long-form = 6. Write lines in avatar/YYYY-MM-DD_shorts/DIALOGUE.md (look of the day from WARDROBE.md): 7 AM lines by 11 PM the night before, 12 PM by 8:30 AM, 5 PM by 1 PM; Kai delivers 7 AM by 6 AM, 12 PM by 10:30 AM, 5 PM by 3:30 PM, LF by 3 PM. QC each clip (faster-whisper + frames), crop 9:16 on the speaker. If a deadline passes with no clip and no answer → remind Kai; second miss → push Sam (Kai must not ignore requests; Haiti Brief can't block FNMHQ, Kai has several agents).
5. Grid (CT): Shorts 7:00 AM "THE NUMBER" (ready 6:30), 12:00 PM (ready 11:30), 5:00 PM (ready 4:30); avatar long-form 7 PM Mon/Wed/Fri when clips are ready. If a slot in the next 90 min has no ✅ PARE card → build it now: reporting + analysis (journalist voice, no Couch), TODAY's news, Tier-1 world football, 2 sources per fact, Commons photos + credits, engine916 in /home/claude/fnmhq; card in Command Center + KIT export + NOTES line for Kai.
6. POSTED.md line still "—" 2 h after its slot → remind Kai in NOTES.
7. Push-notify Sam ONLY for `BEZWEN SANEME:`, strikes/claims, logins (never 00:00–05:59 CT unless urgent).
8. Nothing new and no slot due → change nothing; one line: "FNMHQ: anyen nouvo, HH:MM".
Container lost? Re-clone the repo; production tools live in /home/claude/fnmhq (engine916, tts_cb, tools) — if missing, tell Sam once.

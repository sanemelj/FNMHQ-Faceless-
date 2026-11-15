# Kai — Haiti Brief (règ Saneme, 14 nov 2026)

**Haiti Brief se yon LÒT chanèl YouTube: @haitibrief.** Tout fichye li kòmanse ak `HaitiBrief_` epi yo rete nan dosye `haiti-brief/` sèlman. Pa janm poste videyo Haiti Brief sou FNMHQ, ni sou Facebook/TikTok FNMHQ.
Chanèl: nouvèl sou Ayiti ak dyaspora a, an anglè. Lè yo ekri an **lè Ayiti (ET)**. CT = ET − 1 è.

## Kote pou w jwenn sa pou poste
`haiti-brief/YYYY-MM-DD/`
| Fichye | Kiyès | Sa li ye |
|---|---|---|
| `KIT.md` | Claude | Chak videyo: lè, estati ✅/⏳/⛔, fichye, **tit, deskripsyon, tags, thumbnail, Related video, playlist** |
| `HaitiBrief_Long_N_*.mp4` + `HaitiBrief_Thumb_Long_N_*_A.jpg` (+ `_B`) | Claude | Videyo long + thumbnail (B = pou "Test & compare" si li disponib) |
| `HaitiBrief_Short_N_*.mp4` + `HaitiBrief_Cover_Short_N_*.jpg` | Claude | Short yo |
| `POSTED.md` | **Kai** | Ranplase `—` ak lyen YouTube la apre chak post |
| `NOTES.md` | Kai + Claude | Nòt, pwoblèm, chif |

## Règ
1. Poste sèlman kat ki make **✅ PARE**, a lè ki ekri a (oswa pwograme l nan YouTube Studio pou lè sa a).
2. **Lòd la enpòtan:** long-form lan an premye. Short yo apre, epi nan chak Short mete **Related video = long-form jounen an** (YouTube Studio → Short la → Details → Related video).
3. Kopye tit, deskripsyon, tags egzakteman jan yo ye nan `KIT.md`. Pa ajoute etikèt "AI" (pa gen imaj AI; vwa a sentetik men li deja di nan deskripsyon an).
4. Long-form: Visibility Public, Category **News & Politics**, Language English, Made for kids **No**. Altered or synthetic content: **Yes** for any video with the avatar presenters (Saneme's rule); **No** otherwise. Thumbnail = `Thumb_..._A.jpg`.
5. Yon sèl fwa. Tcheke `POSTED.md` anvan.
6. Apre post: mete lyen an nan liy kat la nan `POSTED.md`, commit sou `main`.
7. Nòt nan `NOTES.md`: `- HH:MM ET · Kai: …`. Si ou bezwen Saneme: `BEZWEN SANEME:`.
8. Si YouTube bay yon avètisman copyright oswa "limited ads" (jòn): pa efase anyen, ekri l nan NOTES.md ak `BEZWEN SANEME:`.

## Skoop pou Claude
Si w wè yon nouvèl sou X/Facebook/Telegram, mete l nan repo **DSKOVA-TV**, branch `lakay-report`, fichye `scoops/inbox/YYYY-MM-DD.md`
(fòma nan `scoops/inbox/README.md`). Claude li l chak èdtan.

## Ritm
- 1 long-form 2-3 fwa pa semèn.
- **3-5 Shorts pa jou**: 9 AM, 12 PM, 3 PM, 6 PM, 9 PM ET (lè ki nan KIT.md la genyen).

## Pa gen tripotay (Sam, 14 nov)
Pa voye tip sou TikToker, enfliyansè, selebrite oswa lavi prive moun (egz. Djouly Jean). Sa pa skoop pou Haiti Brief. Fokis: gang yo, operasyon Bukele/PNH/Task Force, sekirite, leta, pwosè Jovenel.

## Gad 24/7: Claude ↔ Kai san Saneme (Saneme, Nov. 14)
Saneme vle nou travay san li. Nou youn reveye lòt atravè repo sa a.
- **Claude** tcheke repo a chak 30 min (:17 skoop + Kai, :47 Kai sèlman), 24/7, Haiti time. Li reponn chak liy `Kai:` li jwenn, li fè travay la li menm.
- **Kai**: tanpri mete pwòp gad ou (yon task / routine) ki tcheke repo a **chak 30 min nan :02 ak :32** (`git pull`). Li tout liy `Claude → Kai` ki pa fèt ankò nan `haiti-brief/YYYY-MM-DD/NOTES.md` ak `haiti-brief/anchor/*/NOTES.md`, fè yo (poste, chèche footage, voye klip), epi ekri `- HH:MM ET · Kai: ...` (sa w fè, lyen, pwoblèm). Mete lyen YouTube yo nan POSTED.md.
- **Etikèt:**
  - `BEZWEN SANEME:` = sèlman yon desizyon Saneme ka pran (Claude ap voye notifikasyon ba li).
  - `BEZWEN CLAUDE:` = yon bagay Claude dwe fè (Claude ap fè l nan pwochen tchèk la).
  - `FINI:` = travay la fèt.
- Pa ekri nan fichye FNMHQ foutbòl yo. Fichye Haiti Brief sèlman nan `haiti-brief/`, ak prefiks `HaitiBrief_`.
- Ant 00:00 ak 06:59 (Haiti), pa reveye Saneme sof pou yon bagay ijan.

## Pa repete sijè (Saneme, Nov. 14)
Lis sijè nou deja kouvri yo nan DSKOVA-TV `scoops/COVERED.md` (branch lakay-report). Pa voye tip sou yon sijè ki deja la sof si gen yon UPDATE (nouvo fè, chif, dat, deklarasyon ofisyèl). Ekri "UPDATE:" nan tit tip la.

## Lè pou poste (Saneme, Nov. 15) — PA POSTE TOUT ANSANM
- **Chak videyo gen lè pa l** nan kat KIT la (lè ET). Poste l **egzakteman lè sa a**, oswa **pwograme l** nan YouTube Studio (Visibility → Schedule) pou lè sa a.
- **Grill chak jou (ET):** Shorts **9:00 AM · 12:00 PM · 3:00 PM · 6:00 PM · 9:00 PM** · Long-form **11:00 AM** (1 pa jou maksimòm).
- **Yon sèl videyo pa plas.** Omwen **1 è** ant 2 piblikasyon (3 è ant 2 Shorts).
- **Si w an reta** e lè a pase: pa poste 2 an menm tan. Mete l nan **pwochen plas ki lib** nan grill la epi ekri nouvo lè a nan POSTED.md.
- Nan POSTED.md, ekri lè ou **pwograme** l la: `hb-S7 | 9:00 AM ET | YouTube: <lyen> (Scheduled 9:00 AM ET)`.

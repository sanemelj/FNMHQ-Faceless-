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
4. Long-form: Visibility Public, Category **News & Politics**, Language English, Made for kids **No**, Altered content **No**. Thumbnail = `Thumb_..._A.jpg`.
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

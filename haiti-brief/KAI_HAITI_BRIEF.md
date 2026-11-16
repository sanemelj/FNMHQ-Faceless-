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
- **Orè fiks (Saneme, Nov. 15) — lè yo PA chanje, sof pou yon skoop ijan (`BREAKING — POSTE KOUNYA`):**
  - **Shorts nouvèl:** 9:00 AM · 12:00 PM · 3:00 PM · 6:00 PM · 9:00 PM ET (chak jou, youn pa plas).
  - **Long-form nouvèl:** **11:00 AM ET** chak jou; **4:00 PM ET** sèlman jou ki gen gwo nouvèl.
  - **Seri "Who Killed President Jovenel Moïse?":** **chak jou 8:00 PM ET** jiskaske nou rive nan pwosè Sanon an (5 epizòd). Premye epizòd la soti kou klip C1–C8 yo rive (sib: madi 17 nov).
  - **Short "Trial Day" (pwosè Sanon):** chak jou tribinal la chita, **6:00 PM ET**. Claude ekri 2 klip avatar vè 3 PM ET; ou jenere yo touswit.
  - Lòt jou yo, 8:00 PM ET rete pou yon twazyèm long-form nouvèl sèlman si gen gwo nouvèl.
- **Yon sèl videyo pa plas.** Omwen **1 è** ant 2 piblikasyon (3 è ant 2 Shorts).
- **Si w an reta** e lè a pase: pa poste 2 an menm tan. Mete l nan **pwochen plas ki lib** nan grill la epi ekri nouvo lè a nan POSTED.md.
- Nan POSTED.md, ekri lè ou **pwograme** l la: `hb-S7 | 9:00 AM ET | YouTube: <lyen> (Scheduled 9:00 AM ET)`.

## Rapò 24 è pou chak long-form (Saneme, Nov. 15)
24 è apre chak long-form soti, ekri rapò a nan `haiti-brief/reports/` (modèl: `reports/README.md`), ak screenshot Overview, Reach ak **Audience retention**. Claude sèvi ak li pou chwazi pwochen sijè yo, ouvèti yo ak longè yo.
Prochen rapò: **hb-L2** (soti Nov. 14 ~7 PM ET → rapò Nov. 15 ~7 PM ET) · **hb-L3** (soti Nov. 14 ~10:50 PM ET → rapò Nov. 15 ~11 PM ET).

## Priyorite ak pozisyon (Saneme, Nov. 15)
- **Sijè yo, nan lòd:** (1) ensekirite Ayiti; (2) ka Jovenel Moïse (pwosè + seri a); (3) **imigrasyon pou Ayisyen Ozetazini ak Kanada** (TPS, parole, depòtasyon, azil, pwogram Kanada/Kebèk). Apre sa: lòt gwo nouvèl (match Grenadye yo, elatriye). Voye tip sou 3 premye yo an premye.
- **Nouvèl mond ak Etazini/Kanada (Sam, 16 nov):** nou kouvri tou gwo nouvèl mond lan (gè Ikrèn, elatriye) ak gwo nouvèl Etazini/Kanada, paske Ayisyen ki viv la yo konsène. Se sijè #4: li pa janm pran plas yon nouvèl Ayiti. Plas: Shorts 12 PM oswa 3 PM ET lè yo lib, oswa long-form 4 PM ET jou ki pa gen gwo nouvèl Ayiti. Pou imaj: chache videyo ofisyèl ak lisans ki pèmèt li (gouvènman ameriken: DVIDS, White House, State Dept = domèn piblik). Pa gen gosip (wayote, selebrite), pa gen kò. Ou ka voye tip sou yo tou, ak tag `WORLD`.
- **Imaj Ayiti (Saneme, Nov. 15):** lè w ap chèche foto/videyo Ayiti an jeneral, chèche **bèl kote yo** (plaj, mòn, Sitadèl, Jakmèl, Okap, otèl, bèl kay). Pa voye imaj bidonvil oswa povrete kòm imaj jeneral. Imaj difisil yo sèlman si evènman an te pase la menm.
- **Nou pou Ayiti.** Chanèl la an anglè, men se pou Ayisyen. Nou di verite a ak respè pou pèp la: nou kritike gang, lidè ak enstitisyon, pa pèp ayisyen an. Pa gen mo ki rabese peyi a.

## Facebook (Saneme, Nov. 15)
Saneme kreye yon paj Facebook Haiti Brief. **Chak Short poste sou YouTube poste tou sou paj Facebook la kòm Reel**, menm fichye a.
- Lè: menm lè ak YouTube nan kat KIT la (oswa jiska 1 è apre), youn pa plas, pa tout ansanm.
- Tèks: sèvi ak blòk **"Facebook"** nan kat KIT la (pi kout, pa gen #Shorts). Si kat la pa gen blòk Facebook, pran premye fraz deskripsyon YouTube la + 3 hashtag: #Haiti #HaitiNews #Bukele.
- Pa ekri anyen sou AI nan tèks la (tit, deskripsyon, hashtag).
- **Etikèt AI sou Facebook = menm jan ak YouTube (Saneme, Nov. 15).** Pou chak Reel, gade videyo a nan YouTube Studio: si **Altered or synthetic content = Yes** sou YouTube, aktive etikèt AI Meta a (**AI info / "Made with AI"**, nan paramèt avanse Reel la nan Meta Business Suite) sou Facebook. Si se **No** sou YouTube, pa mete l. Fè l tou pou Reel ki deja pwograme oswa pibliye yo (edit post la). Si Meta pa kite w chanje l sou yon post, ekri `BEZWEN SANEME:` ak lyen an.
- Nan POSTED.md ajoute lyen Facebook la sou menm liy lan: `hb-S7 | 9:00 AM ET | YouTube: <lyen> | FB: <lyen>`.
- Long-form yo: rete sou YouTube sèlman pou kounya (sof si Saneme di lòt bagay).

## Pa gen ton wobo (Sam, 15 nov) — RÈG
- **Pa janm** mete avètisman tankou "not legal advice", "consult a lawyer/attorney", "this is not financial advice", "for informational purposes only", "do your own research", nan deskripsyon, kòmantè pin, Facebook, oswa nan videyo. Se pawòl ki sonnen tankou yon wobo, e sa fè chanèl la pèdi kredibilite.
- Nou se jounalis: nou bay nouvèl la, moun a moun. Si gen yon fè ki itil moun (egz. "USCIS warns that notarios can't give immigration help"), nou di l kòm nouvèl, ak sous li.
- Si w wè youn nan yon KIT, retire l epi di m.

## AI envizib (Sam, 15 nov) — RÈG
Se sèlman etikèt AI a (YouTube "Altered content", Facebook "AI info") ki fè moun konnen. Pandan y ap gade, yo pa dwe menm imajine se AI. Pou chak klip avatar ou fè:
- Menm figi ak referans twoshot la; je yo bat; dan yo pa chanje; lèv yo swiv vwa a egzakteman; men gen 5 dwèt; menm rad, bijou, dekò ak limyè nan tout klip yo; anyen pa fonn, pa flote, pa chanje fòm; pa gen tèks AI nan dekò a (ekran, kat, papye).
- Vwa natirèl ak aksan ameriken (General American); respirasyon ak poz nòmal; pa gen ritm wobo.
- Tcheke klip la anvan w livre l: si gen yon glitch, di m nan NOTES (ki segonn, kisa) olye ou kite l pase.
- Lè w ap poste: pa janm ajoute avètisman ("not legal advice", elatriye) ni pawòl ki sonnen tankou yon wobo.

## Tit pou odyans ki pi laj la (Sam, 15 nov)
Nouvèl yo pa konsène Ayisyen sèlman. Lè yon nouvèl konsène tout moun (TPS, imigrasyon, Etazini), tit la pa di "Haitian" (egz.: "TPS Holders", pa "Haitian TPS Holders"). Lè se Ayiti vre (gang, Bukele an Ayiti, Jovenel), kenbe "Haiti".

## Paj Instagram pou swiv (Sam, 15 nov)
- **Greg Promo LLC** · **Passion Info Plus** · **LSV Media Production** (https://www.instagram.com/lsvmediaproduction — Luckson Saint-Vil, repòtè pwosè Jovenel la ki fyab).
- Lè yo poste yon skoop: voye l kòm tip (\`scoops/inbox/\`), epi telechaje **fichye orijinal la** (yt-dlp oswa telechajman dirèk) pou pa gen filigràn Instagram sou li.
- Pa efase logo/filigràn medya ki fè videyo a (Info Scoop, elatriye): nou kite l epi nou bay kredi ("Video: <non paj la>"). Mande pèmisyon lè w kapab.


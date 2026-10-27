# PCSX2: release- och katalogkontroll 2026-10-27

PCSX2:s senaste officiella release är `v2.9.146`, publicerad 2026-10-25.
Den uppfyller 48-månadersregeln.

Den aktuella svenska Qt-katalogen på `master` kontrollerades med SHA-256
`db1b69c560caa1df71fe9d6aa15d0a538d42f449cd31ffb9a1c5751c46c6866a`.
De två posterna i `pcsx2-achievements-review-20261026.ts` finns kvar och
skiljer sig från Git-katalogens måltext. Crowdins aktiva redigerare
kontrollerades 2026-10-27 och visar redan exakt dessa två svenska måltexter i
`AchievementLoginDialog`; någon ny uppladdning skulle därför skapa dubbletter.

De tio posterna i `pcsx2-new-menu-strings-20261026.ts` saknas i den aktuella
Git-katalogen. De är Crowdin-specifika strängar och kan därför inte markeras
som föråldrade på grundval av Git-jämförelsen; deras status ska följas i
Crowdin.

Crowdin-redigeraren kontrollerades därefter 2026-10-27. Sökningarna
`Game Properties (Edit)` och `Default Boot` visade samtliga tio poster med
exakt arkivets måltexter: två egenskapsmenyer, fyra varianter av
standardstart och fyra motsvarande poster för de två användargränssnitten.
Även dessa strängar är alltså redan införda och ska inte laddas upp igen.

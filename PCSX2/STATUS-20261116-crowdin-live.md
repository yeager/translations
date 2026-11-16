# PCSX2: Crowdin-status, 16 november 2026

En autentiserad Crowdin-kontroll av svenska (`sv-SE`) visar:

| Mått | Värde |
| --- | ---: |
| Fraser | 5 338 av 5 338 översatta |
| Ord | 28 497 av 28 497 översatta |
| Översättningsförlopp | 100 % |
| Godkännandeförlopp | 0 % |
| Godkända QA-kontroller | 3 794 |
| Felande QA-kontroller | 1 544 |

Det är sju fler översatta fraser än vid den föregående arkivkontrollen.
Crowdin rapporterar inga svenska översättningsluckor. QA-markeringarna är en
separat kö och får inte massändras utan radvis jämförelse med källtext,
kontext och aktiv måltext.

Statusen bekräftar sparade Crowdin-översättningar, inte att förslagen är
godkända eller ingår i en PCSX2-release.

## Riktad QA-uppföljning samma dag

Tre genomgångar av Crowdins QA-kö är arkiverade under
`2026-11-16-qa-sample-01`, `2026-11-16-qa-sample-02` och
`2026-11-16-qa-sample-03`. Den första gav en korrekt inskickad ändring för
`"Challenge"-läget` (Crowdin-översättning 450299). Den tredje visade tre
integritetskonflikter där korrekta, äldre förslag redan finns men senare,
felaktiga förslag konkurrerar med dem. Crowdins API avvisar en dubblett som
nytt inskick. Inga röster, historiska förslag eller aktiva val ändrades utan
en uttrycklig projektmetod.

En separat stavningsgranskning fann och rättade `Brazilien` till `Brasilien`
för sträng 4495 (`NTSC-B (Brazil)`). Ändringen sparades och återlästes som
Crowdin-översättning 450301. Deltafil och inskicksbevis finns i
`pcsx2-sv-brazil-ntsc-b-fix-20261116.xliff` respektive
`2026-11-16-spellcheck-brazil`.

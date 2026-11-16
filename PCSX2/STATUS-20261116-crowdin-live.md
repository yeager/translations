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

En ytterligare kontextgranskning rättade sex svengelska UI-termer för
dödzoner, maskinvarumipmapping, hårdvaruhämtning, texturförinläsning och
shadercache. De sparades och återlästes som Crowdin-översättningarna
450303–450313. Deltafil och kontrollresultat finns i
`pcsx2-sv-ui-terms-dodzons-hamtning-cache-20261116.xliff` respektive
`2026-11-16-ui-terms-dodzons-hamtning-cache`.

Tre ytterligare etiketter för dödzon sparades och återlästes som
Crowdin-översättningarna 450315, 450317 och 450319. De ersätter det
missvisande `dödläge` med den etablerade termen `dödzon`. En motsvarande
sträng, 7733, har redan ett korrekt äldre förslag men också ett senare
felaktigt förslag. Crowdin avvisar ett nytt identiskt inskick som dubblett;
inga röster eller historiska översättningar ändrades. Deltafil och
kontrollresultat finns i `pcsx2-sv-deadzone-labels-20261116.xliff` och
`2026-11-16-deadzone-labels`.

Etiketten `Deadzone` i helskärmsgränssnittet rättades också till `Dödzon`
och återlästes som Crowdin-översättning 450321. Underlag och kontroller finns
i `pcsx2-sv-deadzone-fullscreen-label-20261116.xliff` och
`2026-11-16-deadzone-fullscreen-label`.

Tre grafikinställningar där `download` syftar på intern GS-data rättades från
missvisande `nedladdning` till `hämtning`. De sparades och återlästes som
Crowdin-översättningarna 450323, 450325 och 450327. Deltafil och kontroller
finns i `pcsx2-sv-gs-hamtning-20261116.xliff` och
`2026-11-16-gs-hamtning`.

Ett senare riktat QA-urval bekräftade främst korrekta produktnamn och svenska
tekniska sammansättningar. Det fann en verklig satsavvikelse i statusen för
`Rich presence`; den slutliga formuleringen sparades och återlästes som
Crowdin-översättning 450331. Deltafil och granskning finns i
`pcsx2-sv-rich-presence-status-20261116.xliff` och
`2026-11-16-qa-sample-05`.

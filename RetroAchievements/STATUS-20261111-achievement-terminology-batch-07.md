# RetroAchievements: prestations-terminologi, batch 07

- Plattform: Crowdin, projekt `retroachievements` (id `734399`), språk `sv-SE`, fil-id `14`.
- Omfattning: 20 måltexter i 19 strängar, där singular och plural för en sträng räknas separat.
- Lokal delta: `retroachievements-sv-20261111-achievement-terminology-batch-07.json`.

Den här batchen tillämpar projektets etablerade UI-term *prestation* för
`achievement`. Den rättar böjningsformerna och den sammanhållna termen
*prestationsuppsättning*, utan att ändra produktnamn eller de orelaterade
stavningsvarningar som Crowdin ger för tekniska sammansättningar.

Kontroller: JSON-parse, l10n-lint på platt JSON-export (0 fel), Hunspell-SV
(endast platshållardelarna `count`, `earned` och `number`), kontroll av taggar
och platshållare, kontroll av em dash, diffkontroll och Gitleaks. `msgfmt` är
inte tillämpligt på JSON-deltat. Svlang analyserades men ger falska V2-larm för
korrekta bisatser, passiva former och platshållarled; den har därför inte
använts som ensam grund för ändringarna.

Arkivstatus: lokalt granskat, arkiverat och pushat till vårt arkiv.

Upstream-inskick: 20 Crowdin-förslag skapades via API den 11 november 2026,
med översättnings-id `89045` till `89083` (udda id:n, inklusive båda
pluralformerna för sträng `7825`). En efterföljande API-avläsning bekräftade
alla 20 måltexter. Samtliga är fortfarande förslag (`isApproved: false`);
godkännande, merge och publicerad projektversion är inte verifierade.

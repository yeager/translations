# RetroAchievements: ärende- och reservationsterminologi, batch 06

- Plattform: Crowdin, projekt `retroachievements` (id `734399`), språk `sv-SE`, fil-id `14`.
- Omfattning: Tre befintliga strängar i arbetsflödet för rapporterade prestationer.
- Lokal delta: `retroachievements-sv-20261111-ticket-terminology-batch-06.json`.

Granskningen ersätter *anspråk* med den kontextbundna termen *reservation*,
*biljett* med *ärende* och den äldre inkonsekventa termen *uppnåelse* med
RetroAchievements etablerade UI-term *prestation*. Den undviker en bred,
okontextualiserad ändring av andra strängar.

Kontroller: JSON-parse, l10n-lint på platt JSON-export (0 fel), svlang (10,0/10,
inga anmärkningar), Hunspell-SV (inga okända ord), kontroll av taggar och
platshållare, diffkontroll och Gitleaks. `msgfmt` är inte tillämpligt eftersom
detta är en JSON-deltafil och ingen gettext-katalog.

Arkivstatus: lokalt granskat och arkiverat. Upstream-inskick och resultat
dokumenteras först efter verifierad Crowdin-API-åtgärd; batchen är inte godkänd
eller publicerad genom denna lokala statuspost.

# KeePassXC, svensk granskningsstatus 2026-11-15

- Releasekontroll: KeePassXC `2.8.0`, publicerad 2026-10-21.
- Katalog: `share/translations/keepassxc_sv.ts` på uppströmsgrenen `develop`.
- Qt-kontroll: `lrelease` byggde 2 501 färdiga översättningar och inga
  ofärdiga.

## Riktad kontroll och inskick

PR [keepassxreboot/keepassxc#14102](https://github.com/keepassxreboot/keepassxc/pull/14102)
uppdaterar fyra svenska strängar:

- radbrytningarna i varningen för en databas från en nyare KeePassXC-version,
- tre Qt-menygenvägar som tidigare använde Å eller Ö som accelerator.

Menygenvägarna använder nu ASCII-tecken utan att ändra den synliga svenska
texten. PR:en är öppen och är en upstream-inskickning, inte en merge eller
utgåva.

## Kontroller

- `lrelease` passerade.
- `l10n-lint` rapporterar inga fel efter ändringen; 18 tidigare varningar
  finns kvar i den kompletta katalogen.
- svlang, `git diff --check` och Gitleaks passerade.
- Hunspell-sv kördes under den riktade granskningen; projekt- och
  formatnamn bedömdes manuellt.

Vid PR-verifieringen fanns inga CI-kontroller, kommentarer eller granskningar.
Merge-status var `BLOCKED`, vilket inte innebär en verifierad upstream-blockerare
utan att projektets mergekrav ännu inte är uppfyllda.

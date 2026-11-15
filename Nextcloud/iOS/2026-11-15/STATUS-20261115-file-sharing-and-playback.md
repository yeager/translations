# Nextcloud iOS: svensk komplettering

- Komponent: Nextcloud iOS (`o:nextcloud:p:nextcloud:r:ios`)
- Underlag: senaste utgåvan `35.2.2`, publicerad 29 oktober 2026
- Källa: officiell svensk Apple `.strings`-export från Transifex
- Omfattning: tolv strängar för filhantering, delning och uppspelning.

## Kontroll

- Före import: 777 översatta, 12 oöversatta, 789 totalt.
- Apple-syntax, källnycklar, svenska språkregler, Hunspell-sv och Gitleaks passerade.
- `l10n-lint` saknar Apple `.strings`-tolkning och tolkar därför resursnycklar som källtext. Dess platshållarvarning för `%d` var inte tillämplig; den riktiga källkontrollen bekräftade både `%d` och `%@`.
- Transifex importjobb: `f8813096-9a12-4fc3-b29e-f3c8f73c594c`, lyckades utan fel.
- Direktläsning efter import bekräftade samtliga tolv måltexter.
- Efter import: 789 översatta, 0 oöversatta, 789 totalt.

Importen är bekräftad. Eventuell extern granskning och publicering hanteras av Nextcloud/Transifex separat.

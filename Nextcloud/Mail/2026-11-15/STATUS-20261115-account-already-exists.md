# Nextcloud Mail: svensk komplettering

- Komponent: Nextcloud Mail (`o:nextcloud:p:nextcloud:r:mail`)
- Underlag: senaste taggen `v5.13.2` från 15 november 2026
- Källa: officiell svensk PO-export från Transifex
- Ändrad sträng: `Account already exists` -> `Kontot finns redan`

## Kontroll

- Före import: 1 087 översatta, 1 oöversatt, 1 088 totalt.
- Lokal kontroll: `msgfmt --check`, `svlang check`, `l10n-lint` och Gitleaks passerade.
- Transifex importjobb: `a32a9b42-cad9-45e9-ba59-3fda58d49c1d`, lyckades utan fel.
- Direktläsning efter import bekräftade `Kontot finns redan`.
- Efter import: 1 088 översatta, 0 oöversatta, 1 088 totalt.

Importen är bekräftad. Eventuell extern granskning och publicering hanteras av Nextcloud/Transifex separat.

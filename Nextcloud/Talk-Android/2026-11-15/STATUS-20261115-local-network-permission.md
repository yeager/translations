# Nextcloud Talk för Android: svensk komplettering

- Komponent: Nextcloud Talk för Android (`o:nextcloud:p:nextcloud:r:android-talk`)
- Underlag: senaste utgåvan `25.1.0`, publicerad 9 november 2026
- Källa: officiell svensk XML-export från Transifex
- Omfattning: tre strängar i behörighetsflödet för lokalt nätverk.

## Kontroll

- Före import: 903 översatta, 3 oöversatta, 906 totalt.
- XML-syntax, källnycklar, `svlang`, Hunspell-sv och Gitleaks passerade.
- `l10n-lint` stöder inte Android XML och kördes därför bara som formatkontroll utan tillämpliga regler.
- Gitleaks fick en träff i den nedladdade upstream-exporten. Den egna XML-deltan kontrollerades separat utan träffar.
- Transifex importjobb: `85e7b075-8d62-4942-bbfc-fa30b042d991`, lyckades utan fel.
- Direktläsning efter import bekräftade samtliga tre måltexter.
- Efter import: 906 översatta, 0 oöversatta, 906 totalt.

Importen är bekräftad. Eventuell extern granskning och publicering hanteras av Nextcloud/Transifex separat.

# Nextcloud settings-1 – svenska, 2026-11-12

- Komponent: `o:nextcloud:p:nextcloud:r:settings-1`.
- Omfattning: en ny inställningssträng om att välja e-postadress för aviseringar.
- Ändring: `Unable to choose this email for notifications` → `Det gick inte att välja den här e-postadressen för aviseringar`.
- Kontroller: l10n-lint, svlang och svengelska utan träffar; Hunspell utan träffar; egen kontroll av struktur, platshållare, em dash och tredubbla konsonanter; diffkontroll och Gitleaks godkända. `msgfmt` är inte tillämpligt för Transifex JSON-resurs.
- Upstream: en Transifex API-batch med en post accepterades med HTTP 200 och lästes tillbaka med exakt värde. Direktkontroll via REST-filter visade därefter inga oöversatta strängar i komponenten.
- Status: uppladdat och verifierat i Transifex. Upstream-granskning eller publicering är inte verifierad.

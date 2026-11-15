# Home Assistant Core – Overkiz Somfy-inloggning, svenska

Datum: 2026-11-15

Fem texter i Overkiz-integreringens Somfy-flöde har granskats som en
sammanhängande inloggningsdialog, sparats via Lokalise API och återlästs.

| Källa | Svenska |
| --- | --- |
| Password | Lösenord |
| Username | Användarnamn |
| The password of your Somfy account (app). | Lösenordet till ditt Somfy-konto (app). |
| The username of your Somfy account (app). | Användarnamnet till ditt Somfy-konto (app). |
| Enter your Somfy account credentials. All homes on your account will be discovered so you can choose one. | Ange inloggningsuppgifterna för ditt Somfy-konto. Alla hem på kontot upptäcks så att du kan välja ett. |

## Upstreamstatus

- Lokal granskning: klar.
- Sparad via Lokalise API: klar, fem översättningar.
- API-återläsning: klar. Rätt nyckel och översättnings-ID, målspråk `sv` och
  `is_unverified=false` för samtliga fem.
- Projektgranskning och release: inte verifierade.

## Kontroller

- `l10n-lint`, `svlang` och `hunspell-sv`: körs mot kontrollfilen.
- `msgfmt`: ej tillämpligt; katalogen är JSON-baserad och ingen PO-fil har
  exporterats.
- `git diff --check` och Gitleaks: körs före arkiveringens push.

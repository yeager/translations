# Arasaac, svenska

## Status 19 oktober 2026

CrowdIn-projektet `arasaac` har en aktiv JSON-resurs, `/master/app/translations/en.json`.

- Svenska: **1 451 av 1 451 fraser, 100 % översatt**.
- Den här batchen innehåller de 42 tidigare tomma strängarna.
- CrowdIn API svarade `201` för samtliga 42 översättningar och varje måltext lästes därefter tillbaka från API:t.
- Efter inskickningen rapporterar CrowdIn 1 403 passerade och 48 misslyckade QA-kontroller. De 48 träffarna fanns före batchen och är inte tomma strängar.

## Kvalitetskontroll

Batchen passerar `msgfmt --check`, `l10n-lint`, `svlang skrivregler`, Hunspell och Gitleaks utan relevanta träffar. Termer för alternativ och kompletterande kommunikation använder **AKK**.

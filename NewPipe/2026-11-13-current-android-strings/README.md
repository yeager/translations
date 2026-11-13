# NewPipe – aktuell svensk Android-katalog

Datum: 2026-11-13  
Komponent: `app/src/main/res/values-sv/strings.xml`  
Källversion: `v0.29.3`, publicerad 2026-11-10

## Granskning

Den svenska Android-resursfilen jämfördes med den aktuella engelska
källkatalogen. Före ändringen saknades fyra resursnamn. Katalogen täcker nu
samtliga 780 av 780 aktuella namn.

- två resolutionslistor med oförändrade formatvärden
- referensen till `Sök efter uppdateringar`
- informationen om Androids nya krav på utvecklarverifiering

Varningen visas vid appstart. Den beskriver att kravet först berör Brasilien,
Indonesien, Singapore och Thailand, och att en global utrullning planeras till
2027.

## Kontroller

- XML-syntax: godkänd
- Nyckeltäckning: 780/780
- `l10n-lint`: godkänd
- Hunspell-sv: inga stavfel i den nya brödtexten
- `svlang`: 10/10; endast produktnamnet NewPipe är okänt för frekvenslistan
- `git diff --check`: godkänd
- Gitleaks: godkänd
- Android-lint: inte körd lokalt eftersom Java Runtime saknas

## Upstream

Ändringarna är inskickade som
[TeamNewPipe/NewPipe#14036](https://github.com/TeamNewPipe/NewPipe/pull/14036).
PR:en är öppen; upstreamgranskning och merge återstår.

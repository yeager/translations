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

Den tidigare källkods-PR:n
[TeamNewPipe/NewPipe#14036](https://github.com/TeamNewPipe/NewPipe/pull/14036)
stängdes den 14 november 2026. NewPipe tar emot översättningar enbart via
Hosted Weblate, inte via pull requests.

Den enda aktuella oöversatta svenska strängen, `kao_dialog_warning`, skickades
in i Hosted Weblate samma dag. Efter inskicket visar komponenten 778/778
översatta strängar (en skrivskyddad referenssträng och inga oöversatta
strängar). Hosted Weblate gör sedan sin vanliga synkronisering till arkivet;
upstream-commit och release är ännu inte verifierade.

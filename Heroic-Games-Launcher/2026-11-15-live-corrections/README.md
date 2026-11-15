# Heroic Games Launcher, svenska livekorrigeringar

Datum: 15 november 2026

De tidigare arkiverade batcherna jämfördes mot Hosted Weblates aktuella
svenska JSON-filer. Av 15 äldre avvikelser är sju materiella rättningar:
singularformen *Omslagsbild*, mer idiomatiska instruktioner, den korta
etiketten *Extra*, korrekt satsstruktur samt ett borttaget avslutande blanksteg.
Övriga avvikelser är idiomatisk svenska eller beror på statusetiketternas
kontext och lämnas därför oförändrade.

Filerna är separerade per Weblate-komponent och innehåller sammanlagt sju
strängar. JSON-validering, `l10n-lint`, `git diff --check` och Gitleaks ska
köras före inskick. `msgfmt` är inte tillämpligt på i18next-JSON.

## Upstreamstatus

Den 15 november 2026 accepterade Hosted Weblates API fyra förslag för
`gamepage` och två för `login-page`. De är inskickade men väntar på granskning
och har därför inte ändrat den publicerade svenska katalogen. Förslaget för
`globals.status.preparing_login` innehåller endast borttagning av ett
avslutande blanksteg. Weblates JSON-import hoppade över posten och den
efterföljande filhämtningen visar att blanksteget fortfarande finns kvar.

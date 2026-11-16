# Weblate Website – svenska, 2026-11-16

## Omfattning

Fem svenska Website-strängar i Hosted Weblate har granskats rad för rad i sin faktiska betalnings- och säkerhetskontext och sparats direkt i Weblate.

## Ändringar

- `Select a country` → `Välj ett land`
- Texten om landskod före EU-momsregistreringsnummer har uppdaterats efter källändring.
- En HTML-formaterad säkerhetsrapporteringsinstruktion har översatts med samtliga tre Python-platshållare och länktaggar bevarade.
- Två betalningsmeddelanden har översatts och den felaktiga betydelsen ”betalningspåminnelse” har rättats till granskning av betalning.

## Verifierad status

- Lokal radgranskning: klar
- Sparat i Hosted Weblate: 5 av 5 strängar
- Uppladdning/import: ej tillämpligt; ändringarna sparades i Hosted Weblates webbgränssnitt
- Läskontroll efter sparning: Website visar 1 288 av 1 288 strängar, 100 %
- Sökningen `state:<translated` visar inga återstående strängar
- Upstreamgranskning och merge: ej tillämpligt för dessa direkt sparade Weblate-enheter

## Kontroller

- Platshållare och HTML i den formaterade strängen: manuellt jämförda och bevarade
- Diffkontroll: ändringshistorik i Hosted Weblate bekräftar den slutliga svenska texten för varje ändrad enhet
- `msgfmt`: ej tillämpligt; komponenten hanteras som Weblate-enheter, inte som en lokal gettext-fil
- `l10n-lint`, `svlang` och `hunspell-sv`: inga lokala exportfiler fanns tillgängliga för körning
- Gitleaks 8.30.1: godkänd, inga läckor i arkivposten

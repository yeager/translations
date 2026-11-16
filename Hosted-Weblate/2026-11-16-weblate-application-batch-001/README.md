# Weblate Application – svenska, batch 001, 2026-11-16

## Omfattning

Tio oöversatta Application-strängar har radgranskats i Hosted Weblate och sparats direkt i webbgränssnittet. Batchen omfattar felmeddelanden för Markdown, teckensnittsrendering, CSV- och XLSX-gränser samt administrativa inbjudningar och återställda projektkopior.

## Verifierad status

- Lokal radgranskning: klar
- Sparat i Hosted Weblate: 10 av 10 strängar
- Läskontroll efter sparning: oöversatta strängar minskade från 20 till 10
- Application: 5 897 av 5 966 översatta; 69 ofärdiga återstår, varav 10 är oöversatta och 59 behöver redigeras
- Uppladdning/import: ej tillämpligt; ändringarna sparades direkt i Hosted Weblate
- Upstreamgranskning och merge: ej tillämpligt för direkt sparade Weblate-enheter

## Kontroller

- Python-formatplatshållaren `%d` är bevarad i fyra berörda felmeddelanden
- Diffkontroll: Hosted Weblates strängstatus och ändringshistorik bekräftar sparningarna
- `msgfmt`: ej tillämpligt; komponenten hanteras som Weblate-enheter, inte som en lokal gettext-fil
- `l10n-lint`, `svlang` och `hunspell-sv`: inga lokala exportfiler fanns tillgängliga för körning
- Gitleaks 8.30.1: godkänd, inga läckor i arkivposten

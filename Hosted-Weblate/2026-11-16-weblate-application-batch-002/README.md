# Weblate Application – svenska, batch 002, 2026-11-16

## Omfattning

De återstående tio oöversatta Application-strängarna har radgranskats och sparats direkt i Hosted Weblate. Batchen omfattar åtkomstregler vid import, återställning av säkerhetskopia, pluralformer för massändring, gränser för förslagsuppladdning och mallrendering.

## Verifierad status

- Lokal radgranskning: klar
- Sparat i Hosted Weblate: 10 av 10 strängar
- Läskontroll efter sparning: oöversatta strängar minskade från 10 till 0
- Application: 5 907 av 5 966 översatta; 59 källändrade eller ofärdiga strängar återstår för radgranskning
- Uppladdning/import: ej tillämpligt; ändringarna sparades direkt i Hosted Weblate
- Upstreamgranskning och merge: ej tillämpligt för direkt sparade Weblate-enheter

## Kontroller

- Python-formatplatshållarna `%d`, `%(username)s` och `%(component)s` är bevarade
- Svenska pluralformer har granskats för båda formerna
- Diffkontroll: Hosted Weblates strängstatus bekräftar 0 oöversatta strängar
- `msgfmt`: ej tillämpligt; komponenten hanteras som Weblate-enheter, inte som en lokal gettext-fil
- `l10n-lint`, `svlang` och `hunspell-sv`: inga lokala exportfiler fanns tillgängliga för körning
- Gitleaks 8.30.1: godkänd, inga läckor i arkivposten

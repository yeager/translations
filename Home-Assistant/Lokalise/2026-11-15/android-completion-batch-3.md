# Home Assistant Companion för Android – svenska

Datum: 2026-11-15

Android-komponentens sista fyra tomma svenska strängar har granskats,
sparats via Lokalise API och återlästs.

| Källa | Svenska |
| --- | --- |
| Play wake sound | Spela upp aktiveringsljud |
| Swipe left from the right edge using one finger | Svep åt vänster från höger kant med ett finger |
| Swipe right from the left edge using one finger | Svep åt höger från vänster kant med ett finger |
| Using one finger from the edge | Med ett finger från kanten |

## Aktuell status

- Lokal granskning: klar.
- Sparad via Lokalise API: klar, fyra översättningar.
- API-återläsning: klar. Alla fyra har `sv` och `is_unverified=false`.
- Oöversatta strängar enligt Lokalises API-filter för svenska: **0**.
- Projektgranskning och release: inte verifierade.

## Kontroller

- `l10n-lint`, `svlang` och `hunspell-sv`: körs mot kontrollfilen.
- `msgfmt`: ej tillämpligt; katalogen är Android-XML i Lokalise men ingen
  exportfil har skapats i denna API-batch.
- `git diff --check` och Gitleaks: körs före arkiveringens push.

# Hosted Weblate – Documentation – Swedish batch 016

Datum: 2026-11-16
Projekt: [Weblate](https://hosted.weblate.org/projects/weblate/)
Komponent: [Documentation / Svenska](https://hosted.weblate.org/projects/weblate/documentation/sv/)

## Omfattning

Två radgranskade dokumentationssträngar om förrådstillägg och CDN-manifest.

## Status

- Lokal granskning: klar.
- Sparat upstream: ja, direkt i Hosted Weblate.
- reStructuredText-kontroll: fallerar för den andra raden eftersom källtextens avslutande ``::`` saknar ett efterföljande literalblock. Weblate visar ``Literal block expected; none found.`` Den svenska översättningen bevarar källtextens markup exakt.
- Upstream-granskning och merge: inte verifierat.

## Kontroller

- Diffkontroll: godkänd.
- Gitleaks: inga läckor.
- `msgfmt`: godkänd mot den faktiska svenska dokumentations-PO-filen från Weblates huvudgren.
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda eftersom lokal exporterad deltafil saknas.

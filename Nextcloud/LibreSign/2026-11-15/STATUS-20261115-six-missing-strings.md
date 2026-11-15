# LibreSign, svensk lokaliseringsstatus 2026-11-15

- Releasekontroll: LibreSign `v15.0.12`, publicerad 2026-11-04.
- Översättningskanal: Transifex-resursen `libresign` i Nextcloud-projektet.
- Utgångsläge: 1 703 av 1 709 svenska strängar var översatta; sex saknades.

## Inskick

Sex strängar skickades som en PO-deltafil genom Transifex REST API:

- tre feltexter för filuppladdning och signaturavslag,
- en kort appbeskrivning,
- LibreSigns längre Markdown-beskrivning,
- etiketten `Files - LibreSign`.

Asynkront importjobb: `e6bfb5f7-00b7-4691-b83c-135cfe0b0d1a`.
Transifex rapporterade `translations_created: 6` och `translations_updated: 0`.

## Verifiering

- Alla sex översättningar lästes tillbaka från Transifex API och matchade den
  inskickade deltan exakt.
- Live-status efter import: 1 709 av 1 709 översatta, noll oöversatta.
- `msgfmt`, svlang, l10n-lint och Gitleaks passerade utan fel på deltafilen.
- Hunspell-sv markerade bara projekt- och sammansättningsnamn som
  `LibreSign` och `indataformat`; de granskades manuellt.

Detta är en verifierad upstream-import. Gransknings- och publiceringsstatus
hanteras separat av Transifex och LibreSigns vanliga utgivningsflöde.

## Verktyg

svlangs installerade miljö saknade beroendet `polib` för PO-filer. Verktyget
installerades om med `polib` och kontrollen kördes därefter om utan fel.

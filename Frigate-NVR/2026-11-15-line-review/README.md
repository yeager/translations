# Frigate NVR – radgranskning

Påbörjad 2026-11-15. Granskningen jämför Frigates engelska katalog på
utvecklingsgrenen med den aktuella svenska katalogen som hämtas från Hosted
Weblate. Filerna i Frigates gitgren används som källkontext men inte som
auktoritativ svensk målkatalog, eftersom Weblate ännu inte har synkats tillbaka
till grenen.

## Batch 001

Radgranskade komponenter: `components-icons` (2), `components-input` (2),
`views-recording` (6), `components-auth` (10), `views-configeditor` (10),
`config-groups` (25), `config-validation` (26) och `components-player` (37).

Tre materiella rättningar:

- `views-configeditor`: konsekvent substantivform *Konfigurationsredigerare*
  i dokumenttitel och gränssnittsnamn.
- `config-validation`: *Role header* avser ett HTTP-huvud i proxyns
  `header_map`, inte en vanlig rubrik.

Kontroller före uppladdning: JSON-validering, `l10n-lint`, `git diff --check`
och Gitleaks. `msgfmt` är inte tillämpligt för i18next-JSON.

## Batch 002

Radgranskade komponenter: `components-camera` (50), `views-replay` (46) och
`views-search` (49). Inga ändringar behövdes i kamera- eller reprisvyn.

Två funktionella rättningar i `views-search`: exemplen `cameras:`, `before:`
och `after:` är filterkommandon som användaren ska skriva och får därför inte
översättas. De bekräftades mot Frigates implementation av textfilter.

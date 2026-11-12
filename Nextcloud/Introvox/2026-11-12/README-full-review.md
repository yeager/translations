# Nextcloud Introvox – komplett svensk lokalgranskning, 2026-11-12

- Komponent: `o:nextcloud:p:nextcloud:r:introvox`.
- Omfattning: samtliga 367 oöversatta svenska strängar har granskats rad för rad i 13 batcher. De sista 42 återanvänder en källtextidentisk Enterprise-granskning efter exakt nyckel- och källtextkontroll.
- Kontroller: pluralformer, platshållare, HTML och Markdown bevarade; l10n-lint per batch godkänd; svlang- och Hunspell-träffar dokumenterade som UI-fragment, markup, produktnamn eller formatnamn; diffkontroll och Gitleaks godkända. `msgfmt` är inte tillämpligt för JSON-resursen.
- Upstream: samtliga källsträngar är taggade `locked`; Transifex API avvisar uppdatering med HTTP 409.
- Status: komplett lokalt granskat och arkiverat som ett väntande delta. Inte uppladdat.

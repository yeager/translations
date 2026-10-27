# Flowview: aktuell deltajämförelse 2026-10-27

Komponenten kontrollerades mot aktuell katalog på `develop` (SHA-256
`34009039cc88cd5d3e1988d31b8690c71563ed84a834f23a80b1c8ce5df2f3e5`).
Den äldre filen `cacti-flowview-sv.final-fuzzy-review.delta.po` innehöll
fjorton poster. Tretton källsträngar finns inte längre i komponenten, medan
en hjälptext om offentliga internetregister fortfarande finns kvar och
skiljer sig från uppströms måltext.

Den nya, komponentvisa filen
`cacti-flowview-sv-live-jamford-20261027.po` innehåller endast denna enda
kvarvarande rättelse. Den är inte inskickad. `msgfmt`, `l10n-lint` (0 fel,
0 varningar), `svlang`, Hunspell-granskning och Gitleaks passerar. Hunspell
träffar endast produktnamnet Cacti.

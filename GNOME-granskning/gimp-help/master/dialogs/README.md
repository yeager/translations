# GIMP Help — dialogs (pågående)

- **Aktivitet:** https://l10n.gnome.org/vertimus/gimp-help/master/dialogs/sv/
- **Gren:** `master`
- **Senaste POT:** hämtad 2026-11-28; 3 407 aktiva poster; SHA-256 `c5aec982c9e18537036ffab48274bd10e8991e844cda46c00e298bf506665d71`
- **Damned Lies före arbetet:** 271 översatta, 834 fuzzy, 2 302 oöversatta
- **Lokal arbetskopia efter två batcher:** 466 översatta, 815 fuzzy, 2 126 tomma poster; 2 064 synliga strängar och 62 `@@image`-metadata återstår.
- **Radgranskat hittills:** 195 poster: 176 tidigare tomma översatta, 19 fuzzy granskade, 0 skarpa befintliga översättningar ändrade.

Original aktuell PO, POT, aktivitetssida, granskad PO och unified diff finns i denna katalog. Arbetsfilen är `gimp-help.master.dialogs.sv.working-2026-11-28.po`; detaljer per batch finns i arkivet `reviews/gnome-progress/`.

Batch 1 omfattade välkomstdialogen, symmetrimålning, sparadialogen och `%x`-variabeln. Batch 2 omfattade välkomstdialogen, ångringshistorik och verktygsförinställningar. Batch 3 omfattade verktygsförinställningsredigeraren och mallar. Batch 4 omfattade mallar, taggning och symmetrimålning. Batch 5 fortsatte med symmetrimålningens axlar och transformering. Batch 6 omfattade plattläggning, mandala, spara/exportera och samplingspunkter. Granskade poster förs löpande in i `swedish-tm`.

- `l10n-lint`: 0 fel, 146 varningar när tomma och fuzzy poster undantas; batch 2 tillför inga rapporterade fel. Varningarna gäller katalogens befintliga DocBook-/interpunktionstillstånd och ett skyddat kortkommando.
- DocBook-taggar, skyddade attribut och formatplatshållare jämfördes i batcherna utan avvikelser.
- `hunspell -d sv_SE`: batch 2 rapporterade `Mappinställningar`, bedömt som korrekt svensk sammansättning och dokumenterat undantag. Batch 1:s undantag finns i `hunspell-undantag-batch-01.md`.
- Kör `msgfmt --check` först när hela katalogen är klar.
- Inget har skickats till GNOME.

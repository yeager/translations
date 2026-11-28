# GIMP Help — dialogs (pågående)

- **Aktivitet:** https://l10n.gnome.org/vertimus/gimp-help/master/dialogs/sv/
- **Gren:** `master`
- **Senaste POT:** hämtad 2026-11-28; 3 407 aktiva poster; SHA-256 `c5aec982c9e18537036ffab48274bd10e8991e844cda46c00e298bf506665d71`
- **Damned Lies före arbetet:** 271 översatta, 834 fuzzy, 2 302 oöversatta
- **Lokal arbetskopia efter batch 9:** 534 översatta, 802 fuzzy, 2 071 tomma poster; 2 009 synliga strängar och 62 `@@image`-metadata återstår.
- **Radgranskat hittills:** 263 poster: 231 tidigare tomma översatta, 32 fuzzy granskade/rättade, 0 skarpa befintliga översättningar ändrade.

Original aktuell PO, POT, aktivitetssida, granskad PO och unified diff finns i denna katalog. Arbetsfilen är `gimp-help.master.dialogs.sv.working-2026-11-28.po`; detaljer per batch finns i arkivet `reviews/gnome-progress/`.

Batch 1 omfattade välkomstdialogen, symmetrimålning, sparadialogen och `%x`-variabeln. Batch 2 omfattade välkomstdialogen, ångringshistorik och verktygsförinställningar. Batch 3 omfattade verktygsförinställningsredigeraren och mallar. Batch 4 omfattade mallar, taggning och symmetrimålning. Batch 5 fortsatte med symmetrimålningens axlar och transformering. Batch 6 omfattade plattläggning, mandala, spara/exportera och samplingspunkter. Batch 7 fortsatte med samplingspunkternas färgvärden och färgmodeller. Batch 8 granskade hela avsnittet om snabbmasker och rättade den gemensamma rubriken “Activating the Dialog”. Batch 9 granskade 28 poster om fönsterhantering, fokus och fönsterpositioner. Granskade poster förs löpande in i `swedish-tm`.

- `l10n-lint`: 0 fel, 146 befintliga varningar när tomma och fuzzy poster undantas. Batch 8 och 9 kontrollerades separat mot motsvarande POT-utdrag: 0 fel och 0 varningar. Övriga varningar gäller katalogens befintliga DocBook-/interpunktionstillstånd och ett skyddat kortkommando.
- DocBook-taggar, skyddade attribut och formatplatshållare jämfördes i batcherna utan avvikelser.
- `hunspell -d sv_SE`: batch 8 flaggade `snabbmask` med böjningar, `markeringsmask` med böjningar och `8-bitarskanal`; detta är korrekta GIMP-termer och sammansättningar, dokumenterade i `hunspell-undantag-batch-08.md`. Batch 9 flaggade `namnlist` och böjningar, en etablerad term i GNOME TM dokumenterad i `hunspell-undantag-batch-09.md`. Tidigare batchers undantag finns i respektive notering.
- Kör `msgfmt --check` först när hela katalogen är klar.
- Inget har skickats till GNOME.

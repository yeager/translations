# GIMP Help — dialogs (pågående)

- **Aktivitet:** https://l10n.gnome.org/vertimus/gimp-help/master/dialogs/sv/
- **Gren:** `master` (enda grenen som behandlas)
- **Senaste POT:** hämtad 2026-11-28; 3407 aktiva poster; SHA-256 `c5aec982c9e18537036ffab48274bd10e8991e844cda46c00e298bf506665d71`
- **Damned Lies före arbetet:** 271 översatta, 834 fuzzy, 2 302 oöversatta
- **Lokal arbetskopia:** 352 översatta, 815 fuzzy, 2240 tomma poster; 2178 synliga texter och 62 `@@image`-metadata återstår.
- **Granskad batch:** 81 poster; 62 tomma poster översatta, 19 fuzzy-poster granskade; 0 tidigare skarpa översättningar ändrade.

Källfilerna från Damned Lies finns i `upstream-current-2026-11-28.sv.po` och `latest-current-2026-11-28.pot`. Arbetskatalogen är `gimp-help.master.dialogs.sv.working-2026-11-28.po`; jämförelsen med den aktuella serverfilen finns i `progress.diff`.

Batchen täcker välkomstdialogen, symmetrimålning, sparadialogen och en formatvariabel i titelformateringen. Tidigare lokala förslag användes som stöd men ersatte inte den aktuella serverfilen. Rättelser omfattar GNOME-termen `titellist`, borttagna dubbleringar, ett talintervall, definitionen av standardavvikelse och variabeln `%x`. Granskade poster har förts in i `swedish-tm` med källhänvisning.

- `l10n-lint`: 0 fel och 145 varningar på arbetsfilen med tomma/fuzzy-poster undantagna; den enda nya varningen gäller det skyddade kortkommandot `Ctrl+1-9`. Två befintliga varningar rättades. Damned Lies-PO:n hade 1 placeholder-varning för fuzzy-källposten `%x`; den korrigerades.
- DocBook-taggar och formatvariabler jämfördes för samtliga 81 poster utan avvikelser.
- `hunspell -d sv_SE`: träffar granskade och dokumenterade i `hunspell-undantag-batch-01.md`.
- `msgfmt --check` körs när hela katalogen är komplett.
- Inget har skickats till GNOME.

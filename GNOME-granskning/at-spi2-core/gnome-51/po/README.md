# at-spi2-core — gnome-51/po (sv)

- GNOME-aktivitet: https://l10n.gnome.org/vertimus/at-spi2-core/gnome-51/po/sv/
- Senaste POT hämtades 2026-11-27; SHA-256 `a8233c69d5b0f3742f31ca181a21e4859b43dbfaf0e8a0bbaef964a9430ec834`; 176 aktiva poster.
- Samtliga 176 strängar radgranskades. Alla 176 var redan översatta; inga nya strängar. 46 befintliga översättningar korrigerades, med den nyligen granskade `main/po`-katalogen som mall eftersom samtliga källnycklar är identiska. Terminologin verifierades mot `swedish-tm`.
- Slutresultat: 176 översatta, 0 fuzzy, 0 oöversatta.
- Formatkontroll: `msgcmp --use-fuzzy` mot senaste POT och `msgfmt --check --check-format` godkända. Egen kontroll omfattade meddelandenycklar, pluralformer, printf-platshållare, markup, radbrytningar och understreck/acceleratorer; 0 avvikelser. Inga nordiska acceleratorer förekommer.
- `l10n-lint --language sv`: 0 fel, 0 varningar, 176 kontrollerade poster.
- `hunspell-sv`: samtliga okända ord granskades; inga stavfel. Dokumenterade tekniska namn och ordlisteundantag finns i `hunspell-undantag.md`.
- Inskickad via Damned Lies API 2026-11-27 med kommentaren `Granskad och klar`. API-statistik och aktivitetssidan bekräftar 176/0/0. Den nedladdade sammanfogade PO-filen är identisk med den granskade katalogen.
- Last-Translator: Daniel Nylander <gnome@danielnylander.se>.

## A11y-terminologi, 2026-11-28

23 befintliga strängar korrigerades med samma granskade huvudöversättning som `main`; källnycklarna är identiska. `Accessible Role` heter *hjälpmedelsroll*. l10n-lint: 0 fel/varningar. Hunspell-undantag: `MDI`, `atk_object_get_parent()` och `accessible-table-caption-object`. `msgfmt --check --check-format` och `msgcmp --use-fuzzy` godkändes mot aktuell POT. Den tidigare inskickade versionen har inte uppdaterats; den lokala terminologikorrigeringen är oskickad. Se `at-spi2-core-gnome-51-a11y-terminology-2026-11-28.diff`.

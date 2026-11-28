# GNOME Commander – hjälp (main)

- Damned Lies: https://l10n.gnome.org/vertimus/gnome-commander/main/help/sv/
- Senaste POT hämtad: 2026-11-28; `POT-Creation-Date`: 2026-11-26 11:05+0000
- POT SHA-256: `fed74d407fb530b279cbf47e5c4ca2e4829859395901ff8c9bb9b639177ff004`
- Kanonisk utgångsfil: senaste sammanslagna PO från aktivitet **1581909** (2026-11-26 14:18 UTC), inte den cachade PO-länken.
- Den cachade filen och statistik-API:t visar 3 112 översatta, 4 fuzzy och 1 oöversatt; den senaste sammanslagna filen och aktivitetshistoriken visar 3 117/0/0. Den cachade filen sparas separat som `api-current-2026-11-28.sv.po`.
- Granskad fil: 3117 aktiva poster, 0 fuzzy, 0 oöversatta; 15 poster ändrade jämfört med senaste sammanslagna filen, 0 nya översättningar.
- Översättarhuvud: Daniel Nylander <gnome@danielnylander.se>.

## Granskningsresultat

Åtgärdade versionsnumret `#155` → `#115`, ersatte den felaktiga regex-exempeltoken `\tal` med den källtroget bevarade `\number`, bevarade `.bak` exakt i filnamnsmarkeringen, rättade felstavningen `onnehåller`, förbättrade texten för storleksvisning och musinstruktionen, samt rättade typografi och några tydliga meningsfel. Exif-fält, kommandon, filnamn, platshållare och markupelement behölls.

## Validering

- `msgcmp` mot senaste POT: godkänd; 3 117/3 117 katalognycklar matchar.
- `msgfmt --check --check-format`: godkänd.
- Platshållare och markup-taggar: inga avvikelser; `translator-credits`-posten är avsiktligen särskild.
- `l10n-lint --language sv --reference`: 0 fel och 5 varningar. Tre varningar om upprepade ord är förväntade menyvägar (`Markera → Markera alla`, två gånger, och `Visa → Visa dolda filer`). Två varningar gäller fullständiga svenska meningar där källtexten saknar avslutande punkt.
- `hunspell -d sv_SE`: stavningsunderlag sparat i `hunspell-unknown.txt`; tekniska identifierare, filnamn, kommandoradsflaggor, produktnamn, personnamn och historiska versions-/ändringsnoteringar är dokumenterade undantagskategorier i `hunspell-undantag.md`.

## Uppladdning och kontroll

- Reserverad via API: HTTP 200. Uppladdad 2026-11-28 00:01 UTC: HTTP 200, svar `{"result":"OK"}`.
- Kommentar `Granskad och klar` syns på aktivitetssidan; aktivitet **1582138**.
- Aktivitetshistoriken bekräftar 3 117/0/0 och tillståndet `Translated`.
- Statistik-API:t är fortfarande cachat vid 3 112/4/1. Aktivitet 1582138 och den nedladdade sammanslagna filen är verifierande källor.
- Den sammanslagna PO-filen skiljer sig endast i radbrytningar från uppladdningen. Alla 3 117 msgid/msgstr/pluralinnehåll är semantiskt identiska med den granskade filen. SHA-256: `cc14884ad7e32522af3ab7a42e0500002d2761cc4356f312edd6b700e2a790b6`.

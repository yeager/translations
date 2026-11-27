# Hunspell-undantag för Shotwell `master/po`

Kontrollen kördes med `hunspell -d sv_SE -l`. Råresultatet finns i `hunspell-sv-raw.txt`.

Rimliga undantag är projektnamn och varumärken (Shotwell, Flickr, Google, YouTube, Tumblr, Piwigo, Gallery3), tekniska namn och format (GTK+, OAuth, TLS, JPEG/JPEGXL, RAW, AVIF, HEIF, TIFF, PNG, BMP, WebP, PPI), kommandoradsflaggor och identifierare (`--help`, `--profile`, URI:er och filformat), personnamn och juridiska namn i copyright-/översättarkrediter samt svenska tekniska sammansättningar som Hunspell saknar. Stavningskontrollens kvarvarande fragment som `täll`, `ggar` och `rskorgen` uppstår när den delar upp acceleratorer markerade med `_`; dessa strängar kontrollerades i sitt sammanhang.

Katalogen granskades också visuellt i hela sin aktiva PO-omfattning; listan är inte ett godkännande av okända vanliga svenska ord.

# Hunspell-undantag — gimp-help/master/appendix

Kontrollen kördes med `hunspell -d sv_SE -l` på hela katalogens översättningar. De flaggade orden är huvudsakligen falska positiva från:

- DocBook/XML-element, attribut, `guilabel`- och `keycap`-markeringar, kommandon och inbäddade kodexempel;
- filnamn, bildhashar, URL:er, domännamn och tekniska format, till exempel XCF, SVG, EXIF, ICC, CMYK, YCbCr, L*a*b* och FreeType;
- egennamn och titlar som med avsikt behålls, exempelvis Argyll, GIMP, Cairo, Scribus, GNOME, APOD och externa publikationer;
- etablerade eller grammatiskt korrekta svenska fackord och sammansättningar, bland annat `gråskalelagermask`, `gråskalvärden`, `skuggåterhämtningsalgoritmer`, `tonmappningsalgoritmer`, `färgsampling`, `utökningsbar`, `färgutjämning`, `cellulära automater`, `efterbelysning`, `uppljusning`, `avflätning`, `färgomfång`, `ultradjupa` och `desktoppublicering`.

Kommandon, tangentnamn, URL:er och filnamn bevaras exakt. Källans bildmetadata-ID:n lämnas orörda. Korrigeringar av uppenbara kommandobrytningar och tangentnamnet `Tab` finns i diffen. Hunspell-utdata arkiveras i `hunspell-sv-raw.txt` för spårbarhet.

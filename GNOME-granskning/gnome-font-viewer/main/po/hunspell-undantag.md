# Hunspell-undantag

Kontrollerat med `hunspell -d sv_SE`. Flaggningarna nedan är rimliga tekniska termer eller sammansättningar i OpenType-fontmetadata, inte stavfel:

- `glyfer`, `glyfvarianter`, `färgglyfer`: OpenType-termen *glyph* skrivs *glyf* på svenska.
- `CJK-skiljetecken`, `Hojo-kanjiformer`, `JIS78-former`, `JIS83-former`, `JIS90-former`, `JIS2004-former`, `NLC-kanjiformer`, `kanaalternativ`, `jamoformer`, `Halantformer`, `Nuktaformer`, `Rakarformer`, `Reph-former`, `Vattu-varianter`: namn på skriftspecifika OpenType-funktioner.
- `Unicase`, `Akhand`: etablerade namn på OpenType-funktioner.
- `Fullbreddsformer`, `Halvbreddsformer`, `Versalhöga`: tekniska sammansättningar i typografi.
- `.ttf-format`: filändelse och formatbeteckning.
- `Aa`: exempeltext för förhandsvisningen.
- `nfo`: falsk flaggning från understrecksacceleratorn i `_Info`.

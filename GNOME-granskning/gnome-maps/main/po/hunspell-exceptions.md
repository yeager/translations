# Hunspell-undantag för GNOME Maps

`hunspell -d sv_SE -l` kontrollerade samtliga översatta singular- och pluralformer.
Följande markerade ord är avsiktliga och har kontrollerats i sammanhang:

- **Produktnamn, tjänster och organisationer:** GNOME, OpenStreetMap, GraphHopper, Transitous, Planetiler, Red Hat, Inc.
- **Protokoll, format och interna värden:** URI, Geo URI, Maps URI, `maps:`, OSM, XML, PNG, Plus Code, `metric`, `imperial`, `dark`, `1s`/`2s`/`3s`.
- **Fackord och svenska sammansättningar:** geokodningssökningen, kartruteleverantör, kartdataleverantör, OpenMapTiles-profil, OSM-element, rullstolstillgänglighet, monorail.
- **Tids- och måttenhetssymboler:** fm, em, h, min, s, mi. `mi` är symbolen för engelska miles och behålls som enhet, inte svensk mil.
- **Etablerad boendekategori:** Bed & Breakfast.
- **Egennamn:** Cao đai, Bahá’í, Shinto, Sikhism, Pastafarianism, Voodoo, Yazidism.
- **Korrekt acceleratorplacering:** `S_pårvagnar`, `Fär_jor`, `Å_ngra`; understrecket markerar en ASCII-bokstav, inte Å/Ä/Ö. Hunspell delar därför upp orden vid acceleratorn.

Inga okända ord bedömdes vara stavfel efter manuell kontroll.

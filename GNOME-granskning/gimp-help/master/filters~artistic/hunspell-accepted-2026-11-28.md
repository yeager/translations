# Hunspell-undantag — GIMP Help filters~artistic

Kontrollerad med Hunspell och ordlistan `sv_SE` (`/usr/share/hunspell/sv_SE`). Ordlistan rapporterade 36 unika token vid 49 träffar. De granskades manuellt. Inga olösta stavfel återstår.

- GIMP-/filtertermer: `Oljifiera`, `Konvolvera`, `Superpixelstorlek`, `Indatatyp`, `Toningsalternativ`, `Toningsjämnhet`.
- Giltiga svenska fackord och sammansättningar: `toningskarta`, `toningstrianglar`, `toningsriktning`, `oskärpekarta`, `Brusstyrka`, `Brusstyrkas`, `penselmasken`, `posteriseringseffekt`, `alfakanalområdet`, `randtexturens`, `glasblockseffekten`, `konstnärsduk`, `Gammakorrigeringen`, `mörkheten`, `Storlekskartredigerare`, `Storlekskartredigeraren`, `Orienteringskartredigeraren`, `Riktningskartredigerare`.
- Produktnamn och matematiska termer i PO:n: `GIMP`, `GIMPressionist`, `LIC`, `SLIC`, `Voronoi`, `k-means`, `Vortex`. Dessa filtrerades eller kontrollerades i kontext.
- Token som blir kvar när ordlistan delar sammansättningar vid bindestreck: `-klustring`, `-diagram`, `-skript`, `-effekt`, `-alternativ`, `minimi-`, `oskärpe-`.
- `s` kommer från genitivformen `GIMP:s`; XML-/entitetsdelar (`lt`, `gt`) togs bort före stavningskontrollen.

`Falta` var en felaktig äldre GIMP-TM-översättning av `Convolve` och korrigerades till `Konvolvera`.

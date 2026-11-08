# Blender UI – SPZ-läsdiagnostik

## Omfattning

16 tidigare ospårade strängar under `source/blender/io/spz/` har
kontrollerats i SPZ-formatets rubrik-, GZip- och NGSP-läsare.

## Resultat

Samtliga strängar lämnas oförändrade. `SPZ`, `SH`, `TOC`, `Zstd`, `Zlib`,
`GZip` och `NGSP` är format- eller bibliotekstermer. Svenska former som
`bråkbits`, `byteförskjutning`, `ström`, `positionsläsare` och
`alfakanalsläsare` uttrycker respektive diagnos korrekt. `magiskt värde`
följer den begreppsform som redan har granskats för SPZ-rubriken.

## Kontroller

Källhänvisningarna och läsarnas felvägar har jämförts med den aktuella
exporten. Ingen deltafil skapas, eftersom alla 16 måltexter är korrekta i
sin tekniska kontext.

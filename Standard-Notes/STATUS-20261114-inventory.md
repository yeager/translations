# Standard Notes: svensk lokaliseringsinventering, 14 november 2026

Standard Notes är en krypterad app för anteckningar och synkronisering. Den
senaste offentliga skrivbordsutgåvan är `@standardnotes/desktop@3.202.11`,
publicerad 23 oktober 2026, och uppfyller aktualitetskravet.

Projektet införde sin nuvarande lokalisering 2 november 2026. Den aktuella
grenen innehåller separata JSON-kataloger för webb och mobil. Båda
locale-konfigurationerna listar `en_US`, `zh_CN`, `fr_FR`, `de_DE`, `ja_JP`,
`pt_BR`, `es_LA` och `tr_TR`; svenska finns inte. Det finns ingen svensk
resurs som `sv`, `sv-SE` eller `sv_SE` i trädet, och ingen extern
översättningsplattform anges i projektets filer.

Lokaliseringen är dessutom kopplad till en intern funktionsutrullning i
projektets nyligen sammanslagna lokaliseringsarbete. Ingen svensk katalog,
lokal ändring, uppladdning eller upstream-PR har därför skapats här.

Nästa steg är att kontrollera med projektet om svenska kan läggas till i den
publika lokaliseringsutrullningen och vilket granskningsflöde som gäller för
de två JSON-katalogerna.

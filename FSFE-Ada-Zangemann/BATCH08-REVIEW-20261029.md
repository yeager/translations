# Ada & Zangemann – granskningsbatch 08

Fyra radgranskade rättelser för den svenska DocBook-översättningen.

| Källa | Ändring |
| --- | --- |
| Omslagsbildens alt-text | turtle-neck sweater är översatt till **polotröja** i stället för den onaturliga omskrivningen _tröja med sköldpaddshals_. |
| Illustration med lödkolv | Rättar den ofullständiga uppräkningen till _en lödkolv, en pensel och en burk_ och gör predikatet fullständigt. |
| Brödtext | Sänker felaktigt versal efter anföring. |
| Brödtext | Återställer tre förekomster av _skrev_ enligt källtextens tre _typed_. |

Kontroller: msgfmt --check, l10n-lint, svlang skrivregler och Hunspell med sv_SE körda utan relevanta fel. XML/DocBook-markup och egennamn är bevarade.

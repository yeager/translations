# Inkscape utvecklingsgren: kategorisering av Weblate-kontroller

Datum: 13 november 2026.

Samtliga 340 poster med Weblate-kontroller i `master/inkscape`, svenska, har lästs i enhetsvyn. Inga översättningar eller kontrollstatusar ändrades.

| Kontrolltyp | Antal | Bedömning |
| --- | ---: | --- |
| Oförändrad översättning | 264 | Filterförinställningar, CSS-färgnamn, skrivsystem, filformat och andra identifierare. |
| Tecken kring XML-taggar | 37 | Samtliga har samma uppsättning XML-taggar i källa och mål. |
| Flera versaler | 31 | Termnamn, förkortningar och korrekta svenska versaler, exempelvis `ID`, `CSS`, `GIMP`, `HTML5`, `PDF`, `PNG`, `SVG` och `ZIP`. |
| Omatchad slutpunkt | 5 | Svenska HPGL-hjälptexter har korrekt svensk meningsindelning trots brister i källans skiljetecken. |
| Identiska pluralformer | 2 | `lager` och `objekt` har samma form i singular och plural på svenska. |
| Python-brace-format | 1 | `{:d}` och `{}` är bevarade i motsvarande ordning. |

Kategoriseringen visar inga verifierade språk-, markup- eller platshållarfel. Inga kontroller har avfärdats automatiskt.

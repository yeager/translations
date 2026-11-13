# Inkscape 1.4.x: kategorisering av Weblate-kontroller

Datum: 13 november 2026.

Samtliga 331 poster som Weblate markerade med minst en fallerande kontroll har lästs via den publika enhetsvyn. Inga översättningar eller kontrollstatusar ändrades.

| Kontrolltyp | Antal | Bedömning |
| --- | ---: | --- |
| Oförändrad översättning | 250 | Filterförinställningar, CSS-färgnamn, skrivsystem, filformat och andra identifierare. Behålls tills enskild UI-kontext visar något annat. |
| Tecken kring XML-taggar | 42 | Samtliga 42 har samma uppsättning XML-taggar i källa och mål. Varningen beror på svensk ordföljd eller svenska pluraluttryck kring taggen. |
| Flera versaler | 33 | Termnamn, förkortningar och svenska versalregler, exempelvis `ID`, `CSS`, `GIMP`, `HTML5`, `PDF`, `PNG`, `SVG` och `ZIP`. |
| Omatchad slutpunkt | 5 | Källtexter från HPGL-tillägget saknar konsekvent punkt och ibland mellanrum; den svenska hjälpttexten har idiomatisk svensk meningsindelning. |
| Python-brace-format | 1 | `{:d}` och `{}` finns bevarade i motsvarande ordning; den automatiska kontrollen är inte ett formatfel. |

## Slutsats

Kategoriseringen visar inga verifierade språk-, markup- eller platshållarfel. Kontrollerna har inte avfärdats automatiskt, eftersom oförändrade översättningar och formella Weblate-varningar fortfarande kan behöva en individuell produktbedömning.

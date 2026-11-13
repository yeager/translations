# Inkscape 1.4.x: urval av Weblate-kontroller

Datum: 13 november 2026.

## Underlag

Weblate rapporterar 331 poster med minst en fallerande kontroll i komponenten `1-4-x/inkscape` på svenska. Weblates API exponerar inte kontrolltypen per enhet, så 50 poster lästes i den publika redigeringsvyn: de 25 första i sorteringen och 25 jämnt fördelade poster ur återstoden.

## Utfall i urvalet

| Kontrolltyp | Antal i urvalet | Bedömning |
| --- | ---: | --- |
| Oförändrad översättning | 42 | Filterförinställningar, CSS-färgnamn, skrivsystem, filformat och andra identifierare. Ingen automatisk ändring eller avfärdning. |
| Flera versaler | 4 | Svenska versalregler är avsiktligt annorlunda än engelska rubrikversaler. |
| Tecken kring XML-taggar | 3 | Markupen är intakt; kontrollen beror på svensk ordföljd kring `<b>`-taggar. |
| Omatchad slutpunkt | 1 | Svenskan avslutas idiomatiskt med punkt medan källan saknar den. |

Urvalet innehöll inga verifierade språkfel. Detta är inte en fullständig granskning av alla 331 kontroller, och inga kontroller har avfärdats eller ändrats automatiskt.

## Fortsatt arbete

Fortsätt med kontextuell manuell kontroll av återstående poster, särskilt andra kontrolltyper än oförändrad översättning. Behåll identifierare och standardspecifika namn när de är avsedda att vara oförändrade.

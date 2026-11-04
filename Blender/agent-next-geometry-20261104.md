# Blender Manual: kandidater — meshgeometri och avfasning

Datum: 2026-11-04
Källa: `exports/2026-11-04/blender-manual-manual-sv.po`
Avgränsning: 26 ännu ej förekommande poster från avsnitten *Bevel* och
*Bridge Edge Loops*.

## Kontext och terminologibeslut

Blender behandlar *Bevel* som avfasning och använder i den lokala UI-katalogen
bland annat `Hårdgör normaler`, `Begränsa överlappning`, `Yttre geringsfog`,
`Inre geringsfog`, `Utfyllnad`, `Breddtyp` och `Ytstyrka`. Operatorn *Bridge
Edge Loops* heter där `Brygga kantloopar`. Rekommendationerna nedan följer
alltså projektets egen UI-terminologi och ändrar inte produktnamn eller
kortkommandon.

## Kandidater

| Nr | Källa | Nuvarande svenska | Rekommenderad svenska | Motiv |
| ---: | --- | --- | --- | --- |
| 1 | `Width Type :kbd:\`M\`` | `Bredd Typ :kbd:\`M\`` | `Breddtyp :kbd:\`M\`` | UI använder sammansättningen *Breddtyp*. |
| 2 | `Harden Normals :kbd:\`H\`` | `Härda normalsorter :kbd:\`H\`` | `Hårdgör normaler :kbd:\`H\`` | Exakt belagd UI-term. |
| 3 | `Clamp Overlap :kbd:\`C\`` | `Överlappning av klämmor :kbd:\`C\`` | `Begränsa överlappning :kbd:\`C\`` | Exakt belagd UI-term och korrekt verbfunktion. |
| 4 | `Mark Seams off.` | `Markera sömmar.` | `Sömmarkering av.` | Bildtexten anger läge, inte en uppmaning. |
| 5 | `Mark Seams on.` | `Markera sömmar.` | `Sömmarkering på.` | Samma lägesform som föregående bildtext. |
| 6 | `Miter Outer :kbd:\`O\`` | `Miter Yttre :kbd:\`O\`` | `Yttre geringsfog :kbd:\`O\`` | Exakt UI-term och svensk ordföljd. |
| 7 | `Sharp outer miter (no extra geometry).` | `Skarp yttre gering.` | `Skarp yttre geringsfog (ingen extra geometri).` | Återger både fackterm och parentesens innebörd. |
| 8 | `Patch outer miter.` | `Lappa yttre gering.` | `Utfyllnad för yttre geringsfog.` | *Patch* är enumvärdet `Utfyllnad` i UI:t. |
| 9 | `Arc outer miter.` | `Båge yttre gering.` | `Bågformad yttre geringsfog.` | Naturlig svensk bildtext och UI-term. |
| 10 | `(Miter) Inner :kbd:\`I\`` | `Inre :kbd:\`I\`` | `Inre geringsfog :kbd:\`I\`` | Den svenska UI-termen måste vara tydlig även i manualen. |
| 11 | `Sharp inner miter (no extra geometry).` | `Skarp inre gering.` | `Skarp inre geringsfog (ingen extra geometri).` | Full teknisk betydelse och konsekvent term. |
| 12 | `Arc inner miter.` | `Båge inre gering.` | `Bågformad inre geringsfog.` | Konsekvent med yttre geringsfog. |
| 13 | `Intersection Type :kbd:\`N\`` | `Typ av korsning :kbd:\`N\`` | `Korsningstyp :kbd:\`N\`` | Naturlig svensk sammansättning. |
| 14 | `Cap off each edge with a flat face.` | tom | `Avsluta varje kant med en plan yta.` | Komplett beskrivning av avskärningsläget. |
| 15 | `Cutoff with a center face.` | `Metod för avskärning med en centeryta.` | `Avskärning med en centrerad yta.` | Bildtext, inte metodnamn; idiomatisk svenska. |
| 16 | `Face Strength` | `Ansiktsstyrka` | `Ytstyrka` | Exakt lokal UI-term. |
| 17 | `Do not set face strength.` | `Ställ inte in ansiktsstyrka.` | `Ställ inte in ytstyrka.` | Följer UI-termen. |
| 18 | `Use an auto-generated profile based on the *Profile Shape* setting.` | tom | `Använd en automatiskt skapad profil baserad på inställningen *Profilform*.` | Bevarar den synliga inställningens svenska namn. |
| 19 | `:menuselection:\`Edge --> Bridge Edge Loops\`` | `:menuselection:\`Kant --> Bridge Edge Loops\`` | `:menuselection:\`Kant --> Brygga kantloopar\`` | Exakt lokal operatorform. |
| 20 | `The last edge loop is not connected back to the first.` | `Hitta de kanter som är kopplade till detta toppunkt.` | `Den sista kantslingan ansluts inte tillbaka till den första.` | Återger den faktiska öppna slingans villkor. |
| 21 | `The last edge loop is connected back to the first.` | `Hitta de kanter som är kopplade till detta toppunkt.` | `Den sista kantslingan ansluts tillbaka till den första.` | Återger den slutna slingans villkor. |
| 22 | `Create the new edge loops in a straight line.` | `Skapa en gradient som bildar en rak linje.` | `Skapa de nya kantslingorna i en rak linje.` | Rätt objekt och semantik. |
| 23 | `Blend Path` | `Filer och sökvägar` | `Blanda längs bana` | Parameter för interpolering längs bryggans bana. |
| 24 | `Blend Surface` | `Blanda kvadrat` | `Blanda yta` | Parameter för interpolering över bryggans yta. |
| 25 | `Bridge result.` | `Bridge resultat.` | `Bryggresultat.` | Svensk sammansättning i bildtext. |
| 26 | `Bridging two edge loops with the same number of vertices:` | `Exempel på Bridge-verktyget mellan kantslingor med olika antal toppar.` | `Bryggning av två kantslingor med samma antal hörnpunkter:` | Korrigerar både antal och etablerad *hörnpunkt*-term. |

## Dubblettkontroll

Varje exakt källsträng ovan har jämförts med samtliga befintliga
`blender-manual-sv-review-batch-20261104-*.po`. Ingen av de 26 kandidaterna
finns i tidigare batcher. Batcherna 26 och 29–32 innehåller närliggande
avfasnings- respektive poserelaterat innehåll men inte dessa källsträngar.

## Nästa steg

Rapporten är ett urval för oberoende motgranskning. Ingen PO-deltafil har
skapats och ingen ändring har skickats upstream.

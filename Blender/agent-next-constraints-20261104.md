# Blender Manual: kandidater för granskningsbatch — Åtgärdsbegränsning

Datum: 2026-11-04
Källa: `exports/2026-11-04/blender-manual-manual-sv.po`
Avgränsning: 20 ännu ej batchade poster från
`animation/constraints/relationship/action.rst`.

## Kontext och terminologiskt beslut

En *Action Constraint* använder en animeringsåtgärd för att styra ett
objekt eller ett ben. Det är alltså en specifik Blender-begränsning, inte
en allmän begränsning av flera åtgärder. UI-exporten har den belagda formen
`Åtgärdsbegränsning` (`bpy.types.ActionConstraint`), vilken används här.
`Action` som formellt dataobjekt återges i löptext som *åtgärd*, medan
kod-, RST- och API-identifierare lämnas oförändrade. Animationens *Slot*
följer projektets beslut `slot`, inte `slott`.

Samtliga nedan saknar översättning i råexporten, utom där en befintlig
fuzzy-översättning uttryckligen visas. Sökning i samtliga
`blender-manual-sv-review-batch-20261104-*.po` gav ingen tidigare post med
platsen `relationship/action.rst`.

| Nr | Källa | Engelska | Råexport | Rekommenderad svenska | Motivering |
| --- | --- | --- | --- | --- | --- |
| 1 | `action.rst:6` | `Action Constraint` | `Begränsning av åtgärder` | `Åtgärdsbegränsning` | Följer den faktiska UI-etiketten och beskriver rätt datatyp. |
| 2 | `action.rst:8` | `The *Action* constraint evaluates the location, rotation, and scale inside a certain :doc:\`Action </animation/actions>\` at a certain frame, then applies those to an object or bone.` | *(tom)* | `Begränsningen *Åtgärd* utvärderar position, rotation och skala i en viss :doc:\`åtgärd </animation/actions>\` vid en viss bildruta och tillämpar sedan dem på ett objekt eller ben.` | Skiljer den synliga begränsningen från åtgärden som animeringsdata. |
| 3 | `action.rst:12` | `The frame can either be given directly, or it can be derived from a location coordinate, rotation angle, or scale factor of another object or bone. An example of the latter would be to use frame 0 of the Action if an :doc:\`Empty </modeling/empties>\` is at X = 0 and frame 100 if the Empty is at X = 10. If the Empty is then placed at X = 5, the constraint will interpolate this and evaluate frame 50.` | *(tom)* | `Bildrutan kan anges direkt eller härledas från en positionskoordinat, rotationsvinkel eller skalfaktor för ett annat objekt eller ben. Ett exempel på det senare är att använda bildruta 0 i åtgärden om en :doc:\`tom </modeling/empties>\` finns vid X = 0 och bildruta 100 om den tomma finns vid X = 10. Om den tomma sedan placeras vid X = 5 interpolerar begränsningen detta och utvärderar bildruta 50.` | `bildruta` är den etablerade animationstermen; länkmålet och samtliga värden bevaras. |
| 4 | `action.rst:21` | `The :doc:\`/animation/constraints/transform/copy_transforms\` may be a sufficient replacement if the Action is very simple.` | *(tom)* | `:doc:\`/animation/constraints/transform/copy_transforms\` kan vara en tillräcklig ersättning om åtgärden är mycket enkel.` | RST-målet lämnas exakt. |
| 5 | `action.rst:24` | `:doc:\`Drivers </animation/drivers/index>\` allow defining more complex mathematical relationships, again without setting up an Action.` | *(tom)* | `Med :doc:\`drivrutiner </animation/drivers/index>\` kan mer komplexa matematiska samband definieras, även utan att en åtgärd ställs in.` | Följer UI-översättningen `Drivrutiner`. |
| 6 | `action.rst:27` | `An alternative (if obscure) way of using this constraint is to reference an Action that animates properties of *other* constraints. The *Action* constraint will then apply these properties to the constraints that come after it, as long as their names match the ones in the Action.` | *(tom)* | `Ett alternativt, om än svåröverskådligt, sätt att använda begränsningen är att referera till en åtgärd som animerar egenskaper hos *andra* begränsningar. Begränsningen *Åtgärd* tillämpar då dessa egenskaper på de begränsningar som kommer efter den, förutsatt att deras namn överensstämmer med namnen i åtgärden.` | Återger den tekniska betydelsen av *obscure* utan att tillskriva funktionen fel. |
| 7 | `action.rst:38` | `Action constraint.` | `Begränsning av åtgärder` *(fuzzy)* | `Åtgärdsbegränsning.` | Matchar UI-termen och källa i singular. |
| 8 | `action.rst:41` | `The object or bone to use for calculating the Action frame. Not needed if *Evaluation Time* is used.` | *(tom)* | `Objektet eller benet som används för att beräkna åtgärdens bildruta. Behövs inte om *Utvärderingstid* används.` | `åtgärdens bildruta` förklarar att det är Action-datans tid. |
| 9 | `action.rst:44` | `Allows specifying the Action frame through a number rather than through a transform property of a *Target*. A value of 0 corresponds to *Frame Start* while 1 corresponds to *Frame End* (see below).` | *(tom)* | `Gör det möjligt att ange åtgärdens bildruta med ett tal i stället för med en transformeringsegenskap hos ett *mål*. Värdet 0 motsvarar *Bildrutestart*, medan 1 motsvarar *Bildruteslut* (se nedan).` | Bevarar UI-etiketterna som markerade namn och svenska motsvarar animationens språkbruk. |
| 10 | `action.rst:47` | `Like other properties, the *Evaluation Time* can be fixed, :doc:\`keyframed </animation/keyframes/introduction>\`, or controlled by a :doc:\`Driver </animation/drivers/introduction>\`. The latter can further make use of :doc:\`Custom Properties </files/custom_properties>\`.` | *(tom)* | `Precis som andra egenskaper kan *Utvärderingstid* vara fast, :doc:\`nyckelbildsatt </animation/keyframes/introduction>\` eller styras av en :doc:\`drivrutin </animation/drivers/introduction>\`. Det senare kan dessutom använda :doc:\`anpassade egenskaper </files/custom_properties>\`.` | Länkmål och ordklass bevaras; *keyframed* översätts som egenskap, inte som en knapp. |
| 11 | `action.rst:53` | `Specifies how the evaluated Action transformation is combined with the owner's original transformation (from its preceding constraints).` | `Anger hur den kopierade transformationen ska kombineras med den befintliga transformationen.` *(fuzzy)* | `Anger hur den utvärderade åtgärdens transformering kombineras med ägarens ursprungliga transformering (från dess föregående begränsningar).` | Återställer betydelsen av både *evaluated*, *owner* och orsaken inom parentes. |
| 12 | `action.rst:57` | `The Action's transformation replaces the owner's.` | `Den omvandling som ska tillämpas på ägaren.` *(fuzzy)* | `Åtgärdens transformering ersätter ägarens.` | Befintlig fuzzy-text beskriver inte ersättningen. |
| 13 | `action.rst:59` | `The Action's transformation is applied before the owner's. The result is the same as the owner's transformation if it were a child of the Action and there was no constraint.` | *(tom)* | `Åtgärdens transformering tillämpas före ägarens. Resultatet blir detsamma som ägarens transformering skulle bli om den vore underordnad åtgärden och ingen begränsning fanns.` | Återger transformeringsordningen utan att förväxla *child* med objektets namn. |
| 14 | `action.rst:62` | `If the "parent" is non-uniformly scaled and the "child" was originally rotated, the constraint will cause shearing, just like the default :ref:\`Inherit Scale Full <bpy.types.EditBone.inherit_scale>\` setting for bones.` | *(tom)* | `Om ”föräldern” är icke-likformigt skalad och ”barnet” ursprungligen roterades orsakar begränsningen skevning, precis som standardinställningen :ref:\`Ärv skala helt <bpy.types.EditBone.inherit_scale>\` för ben.` | Hierarkitermerna markeras som i källan och RST-identifieraren lämnas intakt. |
| 15 | `action.rst:66` | `Prevents shearing by scaling the "child" along its own axes instead of the axes of the "parent," just like the :ref:\`Inherit Scale Aligned <bpy.types.EditBone.inherit_scale>\` setting for bones.` | *(tom)* | `Förhindrar skevning genom att skala ”barnet” längs dess egna axlar i stället för ”förälderns” axlar, precis som inställningen :ref:\`Ärv skala justerad <bpy.types.EditBone.inherit_scale>\` för ben.` | Bevarar sambandet mellan skalning och vald axel. |
| 16 | `action.rst:70` | `Calculates each transform "channel" -- location, rotation, and scale -- separately from the others. The difference with *Before Original (Aligned)* is that the child's location is only affected by the parent's location, not by its rotation and scale.` | *(tom)* | `Beräknar varje transformerings”kanal” — position, rotation och skala — separat från de andra. Skillnaden jämfört med *Före ursprunglig (justerad)* är att barnets position endast påverkas av förälderns position, inte av dess rotation och skala.` | `kanal` är den belagda UI-termen; tankstreck används för inskottet. |
| 17 | `action.rst:74` | `Like *Before Original*, except the result is the transformation of the Action if it were a child of the owner.` | *(tom)* | `Som *Före ursprunglig*, men resultatet är åtgärdens transformering som om den vore underordnad ägaren.` | Den omvända hierarkin uttrycks utan att ändra lägets synliga namn. |
| 18 | `action.rst:84` | `For technical reasons, modes other than *After Original (Full)* and *After Original (Aligned)* may not work as expected on objects (not bones) without a parent.` | `Av tekniska skäl kan det hända att andra lägen än *After Original (Full)* och *After Original (Aligned)* inte fungerar som förväntat för begränsningar på *objekt* (inte ben) utan en förälder.` *(fuzzy)* | `Av tekniska skäl kan andra lägen än *Efter ursprunglig (hel)* och *Efter ursprunglig (justerad)* fungera oväntat på objekt (inte ben) utan en förälder.` | Felaktigt tillagt *begränsningar på* tas bort, medan begränsningen för objekt bevaras. |
| 19 | `action.rst:88` | `How strongly the constraint affects the owner.` | `Ändra kontrasten i texturen.` *(fuzzy)* | `Hur starkt begränsningen påverkar ägaren.` | Fuzzy-texten hör till en helt annan sträng. |
| 20 | `action.rst:95` | `The transform property (location/rotation/scale) and axis to use for calculating the Action frame.` | *(tom)* | `Transformeringsegenskapen (position/rotation/skala) och axeln som används för att beräkna åtgärdens bildruta.` | Tekniken och parentesens tre koordinatdelar bevaras. |

## Avsiktliga undantag

Poster som endast är delade, korta UI-etiketter (exempelvis `Target`,
`Channel`, `Action` och `Slot`) ingår inte i detta häfte. De ska i stället
hanteras i UI-katalogen med exakt API-/panelkontext. Särskilt gäller att
råexportens `Slott` strider mot projektets fastslagna term `slot`; den
frågan måste korrigeras konsekvent i en separat UI-batch.

## Kontrollspår

- Dubblettkontroll: inga tidigare batchposter med platsen
  `animation/constraints/relationship/action.rst`.
- Råexporten innehåller 58 kända dubblettdefinitioner och behandlas därför
  endast som läsunderlag; ingen helfilskontroll görs.
- Denna rapport är en kandidatlista och innehåller inga produktionsändringar.

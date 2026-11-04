# Blender Manual – större kandidatgranskning: armaturer

Datum: 2026-11-04  
Källa: `exports/2026-11-04/blender-manual-manual-sv.po` (råexport, endast
läsning)  
Omfattning: 35 säkra kandidater i
`animation/armatures/bones/editing/`. Ingen PO-fil har ändrats.

## Avgränsning och skydd

- Inga befintliga `blender-manual-sv-review-batch-*.po` innehåller någon av
  referenserna `bone_roll.rst`, `duplicate_rename.rst` eller `transform.rst`.
  Häftet överlappar därför inte tidigare batchar 1–28.
- RST-roller, referensmål, kortkommandon, literalvärden och API-identifierare
  nedan är oförändrade. Bara synlig svensk text ändras.
- Terminologibelägg: UI-råexporten innehåller bland annat *Bone Roll* →
  `Benrullning`, *Recalculate Roll* → `Beräkna om rullning`, *Clear Roll* →
  `Rensa rullning`, *Rest Position* → `Viloposition`, *Scale Radius* →
  `Skala radie` och *Align to Active Bone or Parent* →
  `Rikta in efter aktivt ben eller överordnat objekt`.
- `TERMINOLOGY.md` fastslår dessutom `data-block` → `datablock`, `vertex` →
  `hörnpunkt` i geometri- och verktygstext samt `keyframe` → `nyckelbildruta`.

## Kandidater

Varje block visar råexportens nuvarande `msgstr` och ett exakt förslag.
`#, fuzzy` ska tas bort först när respektive förslag har motgranskats.

### Benrullning

**`bone_roll.rst:7`** — UI-belägg för *benrullning* och *viloposition*.

```po
msgid "The bone roll is a part of a bone's :term:`rest pose` defining its default rotation around the bone's length. You can control the bone roll in *Edit Mode*."
# råexportens msgstr ""
msgstr "Benrullningen är en del av ett bens :term:`viloposition <rest pose>` och anger dess standardrotation kring benets längd. Du kan styra benrullningen i *redigeringsläge*."
```

**`bone_roll.rst:21`** — *roll* är `rullning` i Blender-UI:t.

```po
msgid "Automatically align the roll of all selected bones to various points of reference."
# råexportens msgstr ""
msgstr "Justerar automatiskt rullningen för alla markerade ben efter olika referenspunkter."
```

**`bone_roll.rst:24`** — återställer samtliga axelvärden som synlig text.

```po
#, fuzzy
msgid "Local (X, Z, -X, -Z) Tangent"
# råexportens msgstr "Lokal tangent"
msgstr "Lokal tangent (X, Z, -X, -Z)"
```

**`bone_roll.rst:30`** — återställer etikett och alla axelvärden.

```po
#, fuzzy
msgid "Global (X, Y, Z, -X, -Y, -Z) Axis"
# råexportens msgstr "+X, +Y, +Z, -X, -Y, -Z"
msgstr "Global axel (X, Y, Z, -X, -Y, -Z)"
```

**`bone_roll.rst:39`** — *3D cursor* följer etablerade UI-formen `3D-markör`.

```po
#, fuzzy
msgid "Align the roll of the selected bones such that their Z axis points at the 3D cursor."
# råexportens msgstr "Med roten placerad på den valda roten närmast 3D-markören."
msgstr "Justera rullningen för de markerade benen så att deras Z-axel pekar mot 3D-markören."
```

**`bone_roll.rst:41`**

```po
#, fuzzy
msgid "Change the result by 180°."
# råexportens msgstr "Ändra omslagsbild..."
msgstr "Ändrar resultatet med 180°."
```

**`bone_roll.rst:57`** — *Tweak* är en justering, inte ett urval.

```po
#, fuzzy
msgid "Tweak the roll of all selected bones."
# råexportens msgstr "Två utvalda ben."
msgstr "Justera rullningen för alla markerade ben."
```

**`bone_roll.rst:62`** — direkt UI-belägg: `Rensa rullning`.

```po
#, fuzzy
msgid "Clear Roll"
# råexportens msgstr "Rensa alla"
msgstr "Rensa rullning"
```

**`bone_roll.rst:67`** — RST-menysyntax bevarad; endast synliga menyord
översatta enligt UI-beläggen.

```po
#, fuzzy
msgid ":menuselection:`Armature --> Bone Roll --> Clear Roll`"
# råexportens msgstr ":menuselection:`Armature --> Bone Roll --> Set Roll`"
msgstr ":menuselection:`Armatur --> Benrullning --> Rensa rullning`"
```

**`bone_roll.rst:70`**

```po
#, fuzzy
msgid "Set the roll of all selected bones to 0°."
# råexportens msgstr "Väljer keyframes för de markerade handtagen."
msgstr "Ställer in rullningen för alla markerade ben på 0°."
```

### Radera och duplicera ben

**`delete.rst:17`** — nuvarande text är innehållsmässigt riktig men fuzzy;
gör den idiomatisk och godkänn först efter normal kontroll.

```po
#, fuzzy
msgid "This tool deletes selected bones, selected *joints* are ignored."
# råexportens msgstr "Detta verktyg tar bort valda ben, valda *leder* ignoreras."
msgstr "Verktyget tar bort markerade ben; markerade *leder* ignoreras."
```

**`duplicate_rename.rst:5`**

```po
#, fuzzy
msgid "Duplicate and Rename"
# råexportens msgstr "Duplicerat index"
msgstr "Duplicera och byt namn"
```

**`duplicate_rename.rst:10`** — RST-menysyntax bevarad.

```po
#, fuzzy
msgid ":menuselection:`Armature --> Duplicate and Rename`"
# råexportens msgstr ":menuselection:`Armatur --> Duplikat`"
msgstr ":menuselection:`Armatur --> Duplicera och byt namn`"
```

**`duplicate_rename.rst:12`**

```po
msgid "Duplicates the selected bones and automatically renames the copies by replacing part of their names."
# råexportens msgstr ""
msgstr "Duplicerar de markerade benen och byter automatiskt namn på kopiorna genom att ersätta delar av deras namn."
```

**`duplicate_rename.rst:14`** — API-referensen lämnas exakt oförändrad.

```po
msgid "This operator behaves similarly to :ref:`bpy.ops.armature.duplicate_move`, preserving parenting and connectivity relationships between duplicated bones where possible."
# råexportens msgstr ""
msgstr "Den här operatorn fungerar på liknande sätt som :ref:`bpy.ops.armature.duplicate_move` och bevarar, när det är möjligt, överordnings- och anslutningsrelationer mellan duplicerade ben."
```

**`duplicate_rename.rst:17`**

```po
#, fuzzy
msgid "The duplicated bones become selected and can immediately be repositioned."
# råexportens msgstr "Det duplicerade innehållet förblir markerat, vilket möjliggör omedelbar omplacering."
msgstr "De duplicerade benen markeras och kan genast flyttas till en ny position."
```

**`duplicate_rename.rst:19`** — *rig* lämnas som etablerad Blender-term i
förklarande text; det undviker den missvisande kroppsbetydelsen av *rigg*.

```po
msgid "This is useful for creating mirrored rigs, duplicated bone chains, or alternative naming variants."
# råexportens msgstr ""
msgstr "Detta är användbart när du skapar speglade riggar, duplicerade benkedjor eller alternativa namnvarianter."
```

**`duplicate_rename.rst:26`**

```po
msgid "Attempts to automatically flip directional suffixes in duplicated bone names."
# råexportens msgstr ""
msgstr "Försöker automatiskt vända riktningssuffixen i namnen på duplicerade ben."
```

**`duplicate_rename.rst:28`** — literalvärdena ``.L`` och ``.R`` skyddas.

```po
msgid "For example, names ending in ``.L`` may be renamed to ``.R``."
# råexportens msgstr ""
msgstr "Till exempel kan namn som slutar med ``.L`` bytas till ``.R``."
```

**`duplicate_rename.rst:30`**

```po
msgid "This is useful for creating mirrored left/right bone chains."
# råexportens msgstr ""
msgstr "Detta är användbart när du skapar speglade vänster-/högerbenkedjor."
```

**`duplicate_rename.rst:33`**

```po
#, fuzzy
msgid "Text to search for in the original bone names."
# råexportens msgstr "Den text som ska sökas i namn."
msgstr "Text att söka efter i de ursprungliga bennamnen."
```

**`duplicate_rename.rst:35`**

```po
#, fuzzy
msgid "Matching text is replaced in the duplicated bone names."
# råexportens msgstr "Material som ersätter det gamla materialet."
msgstr "Matchande text ersätts i de duplicerade bennamnen."
```

**`duplicate_rename.rst:38`**

```po
msgid "Replacement text inserted in place of the search term."
# råexportens msgstr ""
msgstr "Ersättningstext som infogas i stället för söktexten."
```

**`duplicate_rename.rst:40`**

```po
msgid "If left empty, the matching search term is removed from the duplicated bone names."
# råexportens msgstr ""
msgstr "Om fältet lämnas tomt tas den matchande söktexten bort från de duplicerade bennamnen."
```

### Transformera ben

**`transform.rst:21`** — etablerad Blender-hierarki: *parent* →
*överordnat ben*. Fackorden *Edit Mode* och *parented/connected* ska inte stå
kvar på engelska i löptext.

```po
msgid "As you know, bones can have two types of relationships: They can be parented, and in addition connected. Parented bones behave in *Edit Mode* exactly as if they had no relations. They can be moved, rotated, scaled, etc. without affecting their descendants. However, connected bones must always have parent's tips connected to child's roots, so by transforming a bone, you will affect all its connected parent/children/siblings."
# råexportens msgstr "Som du vet kan ben ha två typer av relationer: De kan vara \"parented\" och dessutom \"connected\". Föräldrade ben beter sig i *Redigera Mode* precis som om de inte hade några relationer. De kan flyttas, roteras, skalas osv. utan att deras underordnade påverkas. Anslutna ben måste dock alltid ha förälderns spetsar anslutna till barnets rötter, så om du transformerar ett ben kommer du att påverka alla dess anslutna föräldrar/barn/syskon."
msgstr "Ben kan ha två typer av relationer: de kan vara överordnade och dessutom anslutna. Överordnade ben beter sig i *redigeringsläge* som om de saknade relationer. De kan flyttas, roteras och skalas utan att deras underordnade ben påverkas. Anslutna ben måste däremot alltid ha det överordnade benets spets ansluten till det underordnade benets rot. När du transformerar ett ben påverkar du därför dess anslutna överordnade, underordnade och syskonben."
```

**`transform.rst:32`** — referensmålet skyddas, och *roll rotation* får den
UI-belagda termen `rullningsrotation`.

```po
msgid "Finally, you can edit in the *Transform* panel in the Sidebar region the positions and radius of both joints of the active selected bone, as well as its :ref:`roll rotation <armature-bone-roll>`."
# råexportens msgstr "Slutligen kan du i panelen *Transform* i Sidebar-regionen redigera positionerna och radien för båda lederna i det aktivt markerade benet, samt dess :ref:`roll rotation <armature-bone-roll>`."
msgstr "Slutligen kan du redigera positionerna och radien för båda lederna på det aktiva markerade benet i panelen *Transform* i sidofältet, samt dess :ref:`rullningsrotation <armature-bone-roll>`."
```

**`transform.rst:38`** — direkt UI-belägg, inklusive normal svensk versalisering.

```po
msgid "Scale Radius"
# råexportens msgstr "Skala Radie"
msgstr "Skala radie"
```

**`transform.rst:43`**

```po
msgid ":menuselection:`Armature --> Transform --> Scale Radius`"
# råexportens msgstr ":menuselection:`Armature --> Transform --> Scale Radius`"
msgstr ":menuselection:`Armatur --> Transformera --> Skala radie`"
```

**`transform.rst:88`** — återställer exakt kortkommando och gör meningen
grammatisk. UI-råexporten belägger *Bone Envelope* → *Benhölje*.

```po
#, fuzzy
msgid "You can alter the size of the Bone Envelope volume by clicking on the body of the bone you want to alter, :kbd:`Shift-Ctrl-Alt-S` then drag your mouse left or right and the Bone Envelope volume will alter accordingly."
# råexportens msgstr "Du kan ändra storleken på Bone Envelope-volymen genom att klicka på kroppen på det ben du vill ändra, :kbd:`Ctrl-Alt-S` dra sedan musen åt vänster eller höger så ändras Bone Envelope-volymen i enlighet med detta."
msgstr "Du kan ändra storleken på volymen *Benhölje* genom att klicka på kroppen på det ben du vill ändra, trycka på :kbd:`Shift-Ctrl-Alt-S` och sedan dra musen åt vänster eller höger. Volymen *Benhölje* ändras därefter i motsvarande grad."
```

**`transform.rst:91`** — RST-menysyntax skyddas; det inledande felaktiga
blanksteget i råexporten tas bort.

```po
msgid "You can also alter the Bone Envelope volume by selecting the Bone you wish to alter and then navigate to :menuselection:`Properties --> Bone --> Deform --> Envelope --> Distance` then enter a new value into it."
# råexportens msgstr "Du kan också ändra Bone Envelope-volymen genom att markera det ben du vill ändra och sedan navigera till :menuselection:` `Egenskaper --> Bone --> Deform --> Envelope --> Distance` och sedan ange ett nytt värde."
msgstr "Du kan också ändra volymen *Benhölje* genom att markera benet och sedan gå till :menuselection:`Egenskaper --> Ben --> Deformera --> Kuvert --> Avstånd` och ange ett nytt värde."
```

**`transform.rst:95`** — *vertices* följer dokumenterad Blender-term
`hörnpunkter`.

```po
msgid "Altering the Bone Envelope volume does not alter the size of the bone just the range within which it can influence vertices of child objects."
# råexportens msgstr "Om du ändrar volymen för Bone Envelope ändras inte benets storlek, bara det område inom vilket det kan påverka hörnpunkterna i underordnade objekt."
msgstr "Att ändra volymen *Benhölje* ändrar inte benets storlek, utan bara det område där det kan påverka hörnpunkter i underordnade objekt."
```

**`transform.rst:120`** — synligt UI-namn översätts, men `Bone.004` och
produktnamnet `B-Bone` lämnas orörda.

```po
msgid "The same armature in Object Mode and B-Bone visualization, with Bone.004's size scaled up."
# råexportens msgstr "Samma armatur i Object Mode och B-Bone-visualisering, med Bone.004:s storlek uppskalad."
msgstr "Samma armatur i objektläge och B-Bone-visualisering, med Bone.004:s storlek uppskalad."
```

**`transform.rst:126`** — direkt UI-/TM-belägg.

```po
#, fuzzy
msgid "Align to Active Bone or Parent"
# råexportens msgstr "Tilldela vikter till den aktiva gruppen."
msgstr "Rikta in efter aktivt ben eller överordnat objekt"
```

**`transform.rst:131`** — menyvägen har samma synliga operatornamn som
föregående sträng.

```po
#, fuzzy
msgid ":menuselection:`Armature --> Transform --> Align to Active Bone or Parent`"
# råexportens msgstr ":menuselection:`Armature --> Transform --> Align Bones`"
msgstr ":menuselection:`Armatur --> Transformera --> Rikta in efter aktivt ben eller överordnat objekt`"
```

### Symmetrisera

**`symmetrize.rst:20`** — *keyframes* följer den fastställda formen
`nyckelbildruta`; länkens RST-mål och datatypsnamnet `Action` ändras inte.

```po
msgid "Symmetrized bone and constraint properties are adjusted to mirror their behaviors. For bones with :doc:`Action Constraints </animation/constraints/relationship/action>`, keyframes are added to the target Action, ensuring symmetrical motion when the Action is activated."
# råexportens msgstr "Symmetriserade ben- och begränsningsegenskaper justeras för att spegla deras beteenden. För ben med :doc:`Action Constraints </animation/constraints/relationship/action>` läggs keyframes till i målåtgärden, vilket säkerställer symmetrisk rörelse när åtgärden aktiveras."
msgstr "Egenskaper för symmetriserade ben och begränsningar justeras så att deras beteenden speglas. För ben med :doc:`Action Constraints </animation/constraints/relationship/action>` läggs nyckelbildrutor till i målåtgärden, vilket säkerställer symmetrisk rörelse när åtgärden aktiveras."
```

## Nästa steg

Skapa högst två deltafiler på 17–18 poster vardera från detta underlag. För
varje delta: validera PO-syntax med `msgfmt --check`, kör `l10n-lint`,
`svlang`, Hunspell och `gitleaks`, och kontrollera diffen. De tre
övriga poster kan motgranskas direkt mot råexporten och UI-beläggen ovan.

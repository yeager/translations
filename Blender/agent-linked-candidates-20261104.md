# Kandidater: Blender Manual — länkade bibliotek

Avgränsning: `files/linked_libraries/library_overrides.rst` i råexporten.
Ingen råfil är ändrad. Nedanstående är förslag som huvudagenten måste
granska mot aktuell Blender-UI och terminologilistan innan de förs in i en
deltafil.

## Säkra kandidater

1. Rättar en trasig rubrik och följer den redan etablerade termen
   *biblioteksåsidosättning*.

   ```po
   msgid "Library overrides support:"
   msgstr "Biblioteksåsidosättningar har stöd för:"
   ```

2. Rättar ett kvarvarande dubbelt citationstecken efter extern RST-länk.

   ```po
   msgid ""
   "There are known issues that have to be addressed. See the `main task of "
   "the project "
   "<https://projects.blender.org/blender/blender/issues/73318>`__, for more "
   "details."
   msgstr ""
   "Det finns kända problem som måste åtgärdas. Se `projektets huvuduppgift "
   "<https://projects.blender.org/blender/blender/issues/73318>`__ för mer "
   "information."
   ```

3. Översätter rubriken idiomatiskt. Nuvarande `Korrekt layout för
   samlingar är viktigt` har fel genus.

   ```po
   msgid "Proper Collections Layout Matters"
   msgstr "En korrekt samlingslayout är viktig"
   ```

4. Rättar imperativformen `Åsidosätt hierarkier`, som annars läses som en
   uppmaning.

   ```po
   msgid "Override Hierarchies"
   msgstr "Åsidosättningshierarkier"
   ```

5. Gör rubriken konsekvent plural och tar bort ensamt oförklarat engelskt
   fackord.

   ```po
   msgid "Animation & Overrides"
   msgstr "Animering och åsidosättningar"
   ```

6. Översätter den fuzzy-markerade meningen utan att ändra sakinnebörden.

   ```po
   msgid ""
   "In general, an override can do much more with its animation data if no "
   "animation data exists in its linked reference data-block."
   msgstr ""
   "I allmänhet kan en åsidosättning göra betydligt mer med sina "
   "animationsdata om det inte finns några animationsdata i dess länkade "
   "referensdatablock."
   ```

7. Rättar både den engelska resten `overrides` och den felaktiga
   betydelsen `användbar` i ett användargränssnittsnära avsnitt.

   ```po
   msgid ""
   "That same operation can also be used to make existing overrides user-"
   "editable, after they have been created, or :ref:`cleared "
   "<bpy.ops.ui.override_idtemplate_clear>`"
   msgstr ""
   "Samma åtgärd kan också användas för att göra befintliga "
   "åsidosättningar redigerbara av användaren efter att de har skapats eller "
   ":ref:`rensats <bpy.ops.ui.override_idtemplate_clear>`."
   ```

8. Ersätter två engelska rester i beskrivningen av återställning.

   ```po
   msgid ""
   "Reset the selected overrides to their original values (from the linked "
   "reference data). Unlike with the *Clear* operation, the overrides remain "
   "fully editable, and are never deleted."
   msgstr ""
   "Återställ de valda åsidosättningarna till deras ursprungliga värden "
   "(från länkade referensdata). Till skillnad från åtgärden *Clear* förblir "
   "åsidosättningarna fullt redigerbara och raderas aldrig."
   ```

9. Rättar produktnamnets versalisering och en onödigt tung formulering.

   ```po
   msgid ""
   "Usually, this operation happens automatically when blender detects it is "
   "needed, on file load, unless it is disabled in the :doc:`Experimental "
   "Preferences </editors/preferences/experimental>`."
   msgstr ""
   "Vanligtvis utför Blender åtgärden automatiskt vid filinläsning när den "
   "behövs, om den inte har inaktiverats i :doc:`Experimentella inställningar "
   "</editors/preferences/experimental>`."
   ```

## Kandidat som kräver extra UI-kontroll

Följande har tydligt fel innehåll men använder interna Blender-begrepp
(`Armature obdata`, `Pose bones`). Den bör jämföras med den aktuella UI-
och dokumentationsterminologin före ändring:

```po
msgid ""
"The main one is probably posed (but not animated) armature objects, when "
"their Armature obdata itself is not overridden. The Pose bones of an "
"armature object are fully linked to the bones of its Armature obdata, if "
"the latter goes missing, the pose bones are definitively lost."
msgstr ""
"Den främsta risken gäller poserade, men inte animerade, armaturobjekt när "
"deras armatur-objektdata inte åsidosätts. Posbenen i ett armaturobjekt är "
"helt länkade till benen i armaturens objektdata. Om den senare försvinner "
"går posbenen definitivt förlorade."
```

Risk: `Armature` kan vara ett visningsnamn som ska lämnas oöversatt i
denna manualversion; den föreslagna sammansättningen måste därför inte
antas utan jämförelse med Blender-UI:t.

## Huvudgranskning

Kandidat 10 lämnas medvetet utanför nästa delta tills interna UI-namn har
kontrollerats. Kandidaterna 1–9 är rimliga utgångspunkter, men måste
fortfarande jämföras radvis med råexportens exakta RST-markeringar innan
de godkänns.

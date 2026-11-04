# Införandeplan: Blender Manual — åtgärder och slotar

Underlag: den oberoende kandidatutredningen och motgranskningen i
`agent-animation-candidates-20261104.md` respektive
`agent-animation-review-20261104.md`. Samtliga poster nedan är verifierade
mot den lokala råexporten och Blender UI-exporten. RST-roller och deras mål
ska bevaras exakt när en deltafil skapas.

| Referens | Exakt `msgid` | Slutlig `msgstr` |
| --- | --- | --- |
| `actions.rst:30` | `Action Slots` | `Åtgärdsslotar` |
| `actions.rst:32` | `The animation data inside an action is further organized into *Slots*. The slot describes *what the animation is for*. For example, you're animating a sphere that orbits a cube, standing in for a moon orbiting a (cubic) planet. These can be animated with one Action using two Slots, one named "Planet" and the other "Moon".` | `Animeringsdata i en åtgärd organiseras vidare i *slotar*. En slot beskriver *vad animeringen avser*. Du kan till exempel animera en sfär som kretsar kring en kub och föreställer en måne som kretsar kring en kubisk planet. Detta kan animeras med en åtgärd som använder två slotar, den ena med namnet "Planet" och den andra med namnet "Moon".` |
| `actions.rst:37` | `**In short: The Action name describes the animation, the Slot names describe the subjects of that animation.**` | `**Kort sagt: Åtgärdens namn beskriver animeringen, och slotarnas namn beskriver vad som animeras.**` |
| `actions.rst:39` | `Each action has a set of slots, and different animation data for each of those slots. An animated data-block then specifies both an action and a slot within that action, determining which animation data the data-block is animated by.` | `Varje åtgärd har en uppsättning slotar och olika animeringsdata för var och en av dem. Ett animerat datablock anger sedan både en åtgärd och en slot inom åtgärden, vilket bestämmer vilka animeringsdata datablocket animeras av.` |
| `actions.rst:45` | `Action selector and its accompanying slot selector in the properties of an object, for seeing and selecting which action and slot animate the object.` | `Åtgärdsväljaren och den tillhörande slotväljaren i ett objekts egenskaper, för att se och välja vilken åtgärd och vilken slot som animerar objektet.` |
| `actions.rst:131` | `:doc:\`F-Curves </editors/graph_editor/fcurves/introduction>\` are the fundamental unit of animation in Blender, and are the main kind of animation data that actions contain. Each F-Curve contains keyframes that define how a property (such as the X location of an object) should change over time.` | `:doc:\`F-kurvor </editors/graph_editor/fcurves/introduction>\` är den grundläggande enheten för animering i Blender och den huvudsakliga typen av animeringsdata som åtgärder innehåller. Varje F-kurva innehåller nyckelbilder som anger hur en egenskap, exempelvis ett objekts X-position, ska förändras över tid.` |
| `actions.rst:138` | `:doc:\`Graph Editor</editors/graph_editor/introduction>\`, displaying three F-Curves for three different properties.` | `:doc:\`Grafredigeraren </editors/graph_editor/introduction>\`, som visar tre F-kurvor för tre olika egenskaper.` |
| `actions.rst:148` | `The :doc:\`Dopesheet Editor's </editors/dope_sheet/introduction>\` channel list, with the animated channels of various bones grouped under their bone names.` | `Kanallistan i :doc:\`Dopebladet </editors/dope_sheet/introduction>\`, där de animerade kanalerna för olika ben är grupperade under bennamnen.` |
| `actions.rst:194` | `In addition to letting Blender automatically choose an action and slot for a data-block, you can also manually assign them. This can be used to assign existing animation to a data-block by selecting both the action and slot. It can also be used to specify an action for a data-block's keys to go into, by assigning the action but leaving the slot blank, in which case a new slot will be created when the first key is set.` | `Förutom att låta Blender automatiskt välja en åtgärd och en slot för ett datablock kan du även tilldela dem manuellt. Du kan då tilldela en befintlig animering till ett datablock genom att välja både åtgärden och sloten. Du kan också ange i vilken åtgärd ett datablocks nyckelbilder ska lagras genom att tilldela åtgärden men lämna sloten tom; då skapas en ny slot när den första nyckelbilden anges.` |
| `actions.rst:221` | `:ref:\`Speaker Animation Panel <object-speaker-properties-animation>\`` | `:ref:\`Högtalarens animeringspanel <object-speaker-properties-animation>\`` |
| `actions.rst:222` | `:ref:\`Movie Clip Animation Panel <clip-properties-animation>\`` | `:ref:\`Filmklippets animeringspanel <clip-properties-animation>\`` |
| `actions.rst:224` | `:ref:\`Node Group Animation Panel <node-group-properties-animation>\`` | `:ref:\`Nodgruppens animeringspanel <node-group-properties-animation>\`` |

Före införande ska respektive källa hämtas direkt från råexporten så att
radbrytning och eventuella ändringar i originaltexten inte gissas. Därefter
ska deltafilen kontrolleras med `msgfmt`, l10n-lint, svlang, Hunspell,
Gitleaks och `git diff --check`.

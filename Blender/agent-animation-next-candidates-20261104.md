# Kandidater: Blender Manual — fortsättning på `animation/actions.rst`

Källa: `exports/2026-11-04/blender-manual-manual-sv.po`, raderna för
`animation/actions.rst:201–263`. Avgränsning: poster som inte redan finns i
batch 25. Blender UI-katalogen har använts för *Åtgärdsredigerare*,
*Dopeblad*, *NLA-redigerare*, *Ersätt åtgärd* och *Omdirigera användare*.
Råexporten och befintliga deltafiler är orörda.

| Referens och exakt `msgid` | Föreslagen `msgstr` | Skäl |
| --- | --- | --- |
| `actions.rst:201` — `For each data-block in the properties editor there is an Animation panel with action and slot selectors. You can use these to assign actions and slots to a data-block.` | `För varje datablock i egenskapsredigeraren finns en animeringspanel med väljare för åtgärd och slot. Du kan använda dem för att tilldela åtgärder och slotar till ett datablock.` | Tar bort engelska UI-rester och följer terminologin för *action* och *slot*. |
| `actions.rst:207` — `The action and slot selector for Camera data in the :doc:\`Properties Editor </editors/properties_editor>\`.` | `Väljaren för åtgärd och slot för kameradata i :doc:\`egenskapsredigeraren </editors/properties_editor>\`.` | Rättar `Properties Redigerare` till idiomatisk svensk UI-term; RST-målet är oförändrat. |
| `actions.rst:210` — `For the active object you can also assign its action and slot in the action Editor's header.` | `För det aktiva objektet kan du även tilldela dess åtgärd och slot i åtgärdsredigerarens rubrik.` | `plats` är fel betydelse; UI har *Header* → `Rubrik`. |
| `actions.rst:220` — `:ref:\`Scene Animation Panel <scene-properties-animation>\`` | `:ref:\`Scenens animeringspanel <scene-properties-animation>\`` | Rättar den oidiomatiska sammansättningen och bevarar RST-målet. |
| `actions.rst:223` — `:ref:\`Mask Animation Panel <mask-properties-animation>\`` | `:ref:\`Maskens animeringspanel <mask-properties-animation>\`` | Återställer en kvarvarande engelsk referenstext. |
| `actions.rst:243` — `Switching the Action on Multiple Data-Blocks` | `Byta åtgärd för flera datablock` | Ersätter felaktig och fuzzy svensk rubrik. |
| `actions.rst:245` — `When working with an action that animates multiple data-blocks, you may need to swap out that action to a different one. And do that on all those data-blocks simultaneously, so that animation that belongs together, is swapped together. For this there are two options.` | `När du arbetar med en åtgärd som animerar flera datablock kan du behöva byta ut den mot en annan åtgärd. Det bör ske samtidigt för alla dessa datablock, så att animering som hör ihop byts ut tillsammans. Det finns två alternativ för detta.` | Oöversatt, men sammanhanget anges av den efterföljande dokumenterade åtgärden. |
| `actions.rst:250` — `Replace Action` | `Ersätt åtgärd` | Exakt bekräftad UI-etikett; ersätter fuzzy måltext. |
| `actions.rst:251` — `Looks at the action of the active object and swaps it on any object that is directly animated by it. This excludes usage in NLA strips and action constraints. It can be found in the :ref:\`Action Editor <bpy.ops.anim.replace_action>\`.` | `Använder åtgärden för det aktiva objektet och ersätter den för alla objekt som animeras direkt av den. Användning i NLA-remsor och åtgärdsbegränsningar omfattas inte. Funktionen finns i :ref:\`Åtgärdsredigeraren <bpy.ops.anim.replace_action>\`.` | Bevarar API-målet, lokaliserar synlig redigerartext och förtydligar objektet för ersättningen. |
| `actions.rst:255` — `Remap Users` | `Omdirigera användare` | Exakt bekräftad UI-etikett; nuvarande `Omforma` är semantiskt fel. |
| `actions.rst:256` — `Right click the action in the outliner and choose :ref:\`Remap Users <bpy.ops.outliner.id_operation>\`. This will replace the usage on *all* users, including NLA strips and action constraints. Use with caution.` | `Högerklicka på åtgärden i Outliner och välj :ref:\`Omdirigera användare <bpy.ops.outliner.id_operation>\`. Detta ersätter användningen hos *alla* användare, även NLA-remsor och åtgärdsbegränsningar. Använd med försiktighet.` | Bevarar RST-målet och omfattningen för *all users*. |
| `actions.rst:263` — `Actions can also be assigned to NLA strips within a data-block's NLA system. Please see the documentation for the :doc:\`NLA Editor </editors/nla/introduction>\` for how to animate data-blocks via the NLA system.` | `Åtgärder kan även tilldelas NLA-remsor i ett datablocks NLA-system. Se dokumentationen för :doc:\`NLA-redigeraren </editors/nla/introduction>\` för information om hur du animerar datablock via NLA-systemet.` | Korrigerar UI-etiketten och den engelskt påverkade formuleringen. |

## Risk- och kontrollnoteringar

- `Slot` används som *slot* enligt projektets terminologilista och tidigare
  dubbelgranskade batch 25.
- `Action Editor` och `NLA Editor` är synliga UI-namn; API-målen i `:ref:`
  och `:doc:` får inte ändras.
- Poster med samma `msgid` i flera manualfiler granskas inte mekaniskt som
  en global ändring. Deltafilen ska begränsas till de angivna
  `actions.rst`-referenserna.
- Kontrollera varje post i råexporten på nytt innan införande och kör
  `msgfmt`, l10n-lint, svlang, Hunspell, Gitleaks och `git diff --check`.

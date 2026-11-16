# Cataclysm-DDA, svensk terminologi

| Engelskt begrepp | Svensk rekommendation | Kontext och källa | Anmärkning |
| --- | --- | --- | --- |
| Autodoc | Autodoc | `src/activity_actor.cpp`, medicinsk automat | Egennamn på spelobjekt, översätts inte. Böjs som `Autodocs`. |
| bionic | bionik | Installation och borttagning i Autodoc | Sakterm i spelets medicinska gränssnitt. |
| bionic power | bionisk energi | Resurs för bionik | Särskilj från installerad `bionik`; avser energi som förbrukas. |
| `bionic_id` | `bionic_id` | Felmeddelande i källkod | Kodidentifierare, översätts inte. |
| achievement | prestation | `src/achievement.cpp` | Avser spelets uppnådda prestationer. |
| watcher | övervakare | Internt fel i prestationer | Teknisk betydelse i källans felmeddelande. |
| cycle (a firearm) | repetera | Vapenhantering | `repeterar manuellt` när mekanismen manövreras. |
| round | patron | Vapenhantering | Avser en ny laddad patron, inte en omgång. |
| venting (a firearm) | avluftar | Vapenstatus | Beskriver gas- eller tryckavlastning. |
| auto drive | autokörning | Fordon | Sammansättning i UI-status. |
| glide | glidning | Rörelse | Använd verbet `glida`/substantivet `glidning` efter satsens form. |
| resting position | viloläge | Autodoc | Naturlig svensk UI-term för maskinens vilande läge. |
| NPC placeholder | `<npcname>` | Spelmeddelanden | Bevaras exakt; svenskt possessiv skrivs `<npcname>:s`. |
| sound effect | oförändrad källa | `Glug`, `grnd` | Avsiktligt identisk med källtexten; kontrollvarningar är falska positiva. |
| wield | ta i handen | Föremålshantering och utrustningsmenyer | Beskriver spelhandlingen att hålla ett föremål aktivt, inte att bara bära det. |
| inventory | inventarium | Föremål som inte längre ryms | Följer tidigare etablerad formulering i projektet. |
| tile | ruta | Karta, odling och byggnation | Använd `mittrutan` när källan anger centre square. |
| disassemble | ta isär | Pågående isärtagning av föremål | Verbformen används i aktiviteter; `isärtagning` för det pågående arbetet. |
| outfit | klädsel | Byta sparad klädsel | Avser en samlad uppsättning kläder, inte en enskild dräkt. |
| reload (container) | fylla på | Vattentät behållare | Använd inte `ladda` när innehållet är vätska. |
| reload (weapon) | ladda | Vapen och ammunition | `ladda` är korrekt i vapen- och batterikontext. |
| field (overmap terrain) | fält | Övervärldsterräng | Inte åker eller område när termen är det synliga terrängnamnet. |
| pulp (corpses) | krossa lik | Hindrar lik från att återuppstå | Spelmekanik, inte lånordet `pulp`. |
| refit | anpassa passformen | Reparation av kläder och utrustning | Avser föremålets passform, inte ommontering av teknisk utrustning. |
| vehicle part | fordonsdel | Fordonsförvaring | Vid dynamiska namn: `%3$s på %2$s`, inte en engelsk genitivkedja. |
| source (sorting) | ursprungsplats | Automatisk föremålssortering | Platsen där föremålet hämtades. |

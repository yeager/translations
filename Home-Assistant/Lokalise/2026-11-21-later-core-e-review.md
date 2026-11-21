# Core — senare E-granskningar

Datum: 2026-11-21

Den här posten återställer spårbarheten för redan genomförda manuella Core-granskningar vars textändringar sparades i Lokalise med direkt läsåterkoppling. Varje här upptagen ändring är även upptagen i det verifierade Home Assistant-minnet i `yeager/swedish-tm`, releasecommit `10f4342`.

| Integration | Nycklar med sparad ändring | Resultat |
| --- | --- | --- |
| Dynalite | 3 | Gatewayadress och två servicebeskrivningar |
| E3/DC | 3 | Anslutningsfel och husets effekt |
| Ecoforest | 4 | Konvektorluftflöde, undertryck och larm |
| Edifier Infrared | 2 | Röst-EQ och linjeingång |
| Efergy | 1 | Effektförbrukning med `{sid}` |
| eMonitor | 1 | Genomsnitt med `{label}` |
| Electric Kiwi | 2 | Start- och sluttid för gratis el |
| EmonCMS | 2 | API-fel med `{details}` |
| Emulated Roku | 3 | Annonserings- och multicastterminologi |
| EnergyZero | 2 | Fältnamnet `Start` för el och gas |
| Engie BE | 1 | Anslutningsfel |

Övriga genomgångna integrationer i samma arbetsföljd utan textändring: Dyson Infrared, EAFM, Earn-e P1, ebusd, EcoNet, EcoSmart, Ecowitt, EDL21, Egardia, ElectraSmart, ElevenLabs, Elgato, Elmax, Elvia, Energenie Power Sockets, Energy och EnergyID. Ecobee, ekeybionyx, ELK M1 och Engie BE har påbörjade men ännu inte kompletta komponentgranskningar och ska inte räknas som avslutade.

Formatkontroll: den kanoniska TMX-filen validerades efter infogning: 2 196 enheter, 231 äldre källnycklar och 1 965 Lokalise-ID:n.

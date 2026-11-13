# Radgranskning – kampanj 3, NEXUS sista bas

**Datum:** 2026-11-13  
**Projekt:** Warzone 2100  
**Komponent:** huvudspel, `data/base/messages/strings/cam3strings.txt`  
**Omfattning:** 7 meddelanden

## Kontext och beslut

Slutsekvensen i kampanj 3 instruerar spelaren att angripa NEXUS sista bas. NEXUS behålls som fraktionsnamn. *Core systems* översätts konsekvent till *kärnsystem*, och den synliga förkortningen LZ behålls eftersom den används i spelbriefingarna.

| Källa | Svensk text |
| --- | --- |
| TRANSPORT MISSION: Attack NEXUS Final Base | TRANSPORTUPPDRAG: Anfall mot NEXUS sista bas |
| We have located NEXUS' base at this location. | Vi har lokaliserat NEXUS bas på den här platsen. |
| This area contains numerous NEXUS structures. | Det här området innehåller många NEXUS-byggnader. |
| We are certain that NEXUS's core systems are located here. | Vi är säkra på att NEXUS kärnsystem finns här. |
| Establish an LZ. | Upprätta en LZ. |
| Begin your attacks on NEXUS. You must destroy his core systems. | Inled dina angrepp mot NEXUS. Du måste förstöra dess kärnsystem. |
| Incoming intelligence report... Team Gamma | Inkommande underrättelserapport... Grupp Gamma |

## Kontroller

- `msgfmt --check --statistics`: 248 översatta och 3 699 oöversatta meddelanden i helkandidaten.
- Diffkontroll: godkänd.
- Gitleaks mot `po/sv.po`: godkänd, inga läckor.
- `svlang skrivregler`: godkänd.
- Hunspell: endast etablerade speltermer, egennamn och förkortningar återstår i ordlistningen.
- Kontroll av tre lika konsonanter i följd: inga svenska träffar; enda träffarna är engelska källreferenser.

## Status

Detta är lokal granskning och arkivering. Ingen uppladdning eller något upstream-inskick har skett; svenska saknas fortfarande i Warzone 2100:s Crowdin-projekt.

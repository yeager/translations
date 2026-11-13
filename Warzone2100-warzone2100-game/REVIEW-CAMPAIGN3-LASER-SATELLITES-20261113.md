# Radgranskning – kampanj 3, lasersatelliter och robotkoder

**Datum:** 2026-11-13  
**Projekt:** Warzone 2100  
**Komponent:** huvudspel, `data/base/messages/strings/cam3strings.txt`  
**Omfattning:** 31 unika meddelanden

## Kontext och beslut

Briefingarna är spelarens löpande uppdragsinformation i den norra sektorn av kampanj 3. NEXUS och NEXUS Intruder Program är projektnamn och behålls. *Missile* återges som *robot* och *silo* som *robotsilo*, medan *high orbit* återges som *hög omloppsbana*.

## Kontroller

- `msgfmt --check --statistics`: 279 översatta och 3 668 oöversatta meddelanden i helkandidaten.
- Diffkontroll: godkänd.
- Gitleaks mot `po/sv.po`: godkänd, inga läckor.
- `svlang skrivregler`: godkänd.
- Hunspell: endast etablerade speltermer, egennamn och förkortningar återstår i ordlistningen.
- Kontroll av tre lika konsonanter i följd: inga svenska träffar; enda träffarna är engelska källreferenser.

## Status

Detta är lokal granskning och arkivering. Ingen uppladdning eller något upstream-inskick har skett; svenska saknas fortfarande i Warzone 2100:s Crowdin-projekt.

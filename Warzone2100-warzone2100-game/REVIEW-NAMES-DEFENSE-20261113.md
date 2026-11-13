# Radgranskning – namn för försvar och byggnader

**Datum:** 2026-11-13  
**Projekt:** Warzone 2100  
**Komponent:** huvudspel och flerspelarkatalog, `names.txt`  
**Omfattning:** 16 unika namn

## Terminologi

Den projektspecifika [terminologilistan](TERMINOLOGY-20261113.md) är uppdaterad och användes för samtliga val: *ställning* för fasta vapenplatser, *torn* för roterande vapenenheter, *luftvärn* för AA/flak, samt *haubits* och *granatkastare* för respektive vapentyp. Produktnamnen Tornado, Ground Shaker, Hellstorm, Bombard och Pepperpot behålls.

## Kontroller

- `msgfmt --check --statistics`: 295 översatta och 3 652 oöversatta meddelanden.
- Diffkontroll: godkänd.
- Gitleaks mot `po/sv.po`: godkänd, inga läckor.
- `svlang skrivregler`: godkänd.
- Kontroll av tre lika konsonanter i följd: inga svenska träffar.

## Status

Lokal granskning och arkivering är klar för batchen. Ingen uppladdning eller något upstream-inskick har skett; svenska saknas fortfarande i Warzone 2100:s Crowdin-projekt.

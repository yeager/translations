# Warzone 2100 – svensk granskning: nätverk, repriser och systemdialoger

Datum: 2026-11-13

## Omfattning

54 användarvända strängar för nätverk, lobby, repriser, grafikstart och allmänna UI-kontroller. Protokollnamn, portnummer, platshållare och formatnamn har bevarats oförändrade.

## Terminologibeslut

- *lobby* → **lobby** och *lobby server* → **lobbyserver** i etablerad spelkontext.
- *port mapping* → **portmappning**.
- *replay* → **repris** i användargränssnitt och felmeddelanden.
- *graphics backend* → **grafikrutin**.
- UPnP, NAT-PMP, PCP, LAN, JSON, WZ, IP och platshållare behålls oförändrade.

## Lokal kontroll

- msgfmt --check --statistics: godkänd; huvudkatalogen hade 1 019 översatta och 2 928 oöversatta meddelanden.
- git diff --check: godkänd.
- gitleaks detect --no-git --source po/sv.po: godkänd, inga läckor.
- Trippelkonsonantkontroll: endast engelska källhänvisningar, inga svenska översättningar.

## Status

Arkiverad lokalt granskad kopia. Ingen uppladdning till Crowdin och inget upstream-inskick har gjorts.

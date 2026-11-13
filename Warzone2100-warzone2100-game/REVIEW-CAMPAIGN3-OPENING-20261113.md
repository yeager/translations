# Warzone 2100 – svensk granskning: kampanj 3, inledning

Datum: 2026-11-13

## Omfattning

42 strängar från kampanj 3:s inledande filmsekvenser, nödradio och NEXUS meddelanden. Översättningarna följer respektive roll: operativ rapportering, nödanrop och NEXUS egen hotfulla röst.

## Terminologibeslut

- *strike VTOL* → **VTOL-anfallsfarkost**.
- *command centre* → **ledningscentral**.
- *tactical nuclear warhead* → **taktisk kärnvapenstridsspets**.
- *synaptic link* → **synapslänk** och *core systems* → **kärnsystem**.
- NEXUS, Alpha-gruppen, Beta-basen och Gamma-gruppen skrivs konsekvent.

## Lokal kontroll

- msgfmt --check --statistics: godkänd; huvudkatalogen hade 818 översatta och 3 129 oöversatta meddelanden.
- git diff --check: godkänd.
- gitleaks detect --no-git --source po/sv.po: godkänd, inga läckor.
- Trippelkonsonantkontroll: endast engelska källhänvisningar, inga svenska översättningar.

## Status

Arkiverad lokalt granskad kopia. Ingen uppladdning till Crowdin och inget upstream-inskick har gjorts.

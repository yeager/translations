# Warzone 2100 – svensk granskning: försvar och ammunition

Datum: 2026-11-13

## Omfattning

50 namn för Hardcrete-försvar, värn och HE-, HEAP- och HEAT-ammunition.

## Terminologibeslut

- *Hardcrete* behålls som spelets materialnamn med svensk funktionsdel: **Hardcrete-mur** och **Hardcrete-port**.
- *hardpoint* → **värn**.
- HE, HEAP och HEAT behålls som etablerade tekniska ammunitionstyper; vapenslagen översätts till bland annat **haubitsgranater**, **miniroboter** och **robotstridsspetsar**.
- *rail dart* → **skenprojektil**.

## Lokal kontroll

- `msgfmt --check --statistics`: godkänd; huvudkatalogen har 1 526 översatta och 2 421 oöversatta meddelanden.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --source po/sv.po`: godkänd, inga läckor.
- Kontroll av trippelkonsonanter: inga svenska träffar; de enda träffarna är engelska källreferenser.

## Status

Arkiverad lokalt granskad kopia. Ingen uppladdning till Crowdin och inget upstream-inskick har gjorts.

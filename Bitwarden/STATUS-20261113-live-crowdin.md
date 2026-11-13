# Bitwarden: aktuell svensk Crowdin-status, 13 november 2026

Kontrollen är läsande och gjordes med projektens etablerade Crowdin-API-åtkomst. Projektens aktuella källfiler och svenska språkprogress kontrollerades separat. Inga röster, godkännanden eller översättningar ändrades.

| Komponent | Svenska filer | Översatt | Godkänd | QA-resultat |
| --- | --- | --- | --- | --- |
| Browser | `messages.json` och `copy.resx` | 2 481 av 2 481 | 21 % respektive 13 % | 1 649 godkända och 832 fallerande kontroller |
| Desktop | `messages.json` och `bitwarden-desktop.tbx` | 2 218 av 2 218 | 22 % respektive 98 % | 1 547 godkända och 671 fallerande kontroller |
| Mobile | iOS, iOS Watch, iOS-genvägar, Android UI och iOS-strängplural | 1 846 av 1 846 | 34 %, 100 %, 0 %, 3 % och 0 % | 1 781 godkända och 805 fallerande kontroller |

Samtliga räknade filer är alltså 100 % översatta. De fallerande QA-kontrollerna är inte automatiskt språkfel och har inte godkänts, avvisats eller massändrats här. Godkännandegrad är en separat projektrollsfråga och är inte samma sak som översättningsgrad eller upstream-release.

`msgfmt` är inte tillämpligt eftersom resurserna är JSON, RESX, TBX och Apple-/Android-strängfiler. Denna statuskontroll omfattar inga lokala översättningsändringar och har därför inte producerat någon importfil.

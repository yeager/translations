# Bitwarden Web — Crowdin-import 2026-10-29

Fem små XLIFF-deltan kontrollerades mot Crowdins aktuella svenska export innan import.
De innehåller 77 måltexter: 17 förbättringar från livegranskningen och 60 tidigare
oöversatta strängar för grupper, åtkomst och Privileged Access Management (PAM).

| Delta | API-import | Resultat |
| --- | ---: | --- |
| `Bitwarden-Web-live-reviewed-delta-20261029.xliff` | 16 importerade, 1 dubblettkontroll | Alla 17 måltexter bekräftade i ny export |
| `Bitwarden-Web-groups-access-delta-20261029.xliff` | 11 importerade | Alla 11 måltexter bekräftade i ny export |
| `Bitwarden-Web-pam-access-delta-20261029.xliff` | 22 importerade | Alla 22 måltexter bekräftade i ny export |
| `Bitwarden-Web-pam-request-dialog-delta-20261029.xliff` | 16 importerade | Alla 16 måltexter bekräftade i ny export |
| `Bitwarden-Web-pam-request-feedback-delta-20261029.xliff` | 10 importerade, 1 dubblettkontroll | Alla 11 måltexter bekräftade i ny export |

Crowdin importerade alltså 75 nya eller ändrade förslag. De två poster som flaggades som
dubbletter hade redan exakt samma svenska måltext i Crowdins aktuella export. Inga poster
godkändes automatiskt.

Efter import hämtades en ny XLIFF-export från Crowdin och alla 77 arkiverade måltexter
jämfördes maskinellt med den exporten.

# Foundation – bysträvanden: release, full radgranskning 2026-11-19

Samtliga 14 strängar i `village_aspirations.release.json` granskades via Crowdin API. Fem förbättringsförslag identifierades; övriga nio bedömdes korrekta.

| ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 23046 | Reach the top of the Clergy Progress Path | Gå hela vägen i Prästerskapets Riktning | Nå toppen av prästerskapets utvecklingsväg |
| 23048 | Reach the top of the Kingdom Progress Path | Gå hela vägen i Kungadömets Riktning | Nå toppen av kungadömets utvecklingsväg |
| 23050 | Reach the top of the Labour Progress Path | Gå hela vägen i Allmogens Riktning | Nå toppen av allmogens utvecklingsväg |
| 23052 | Village Aspiration Completed | Bysträvan lyckades | Bysträvan slutförd |
| 23062 | As the Clergy inaugurates your Abbatial Church … | När prästerskapet inviger din klosterkyrka … Ni uppfostrade … | När prästerskapet inviger din klosterkyrka … Du har uppfört ett troskloster och skapat en vördnadsfull klostergemenskap. … |

## Kontroller

- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` passerade utan anmärkningar.
- Förslagen har inte skickats till Crowdin.

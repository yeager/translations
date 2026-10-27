# GnuCash: utgåvekontroll, 27 oktober 2026

Senaste officiella GitHub-utgåva är [GnuCash 5.17](https://github.com/Gnucash/gnucash/releases/tag/5.17),
publicerad 27 september 2026. Projektet uppfyller därmed kravet på en
uppströmsutgåva som är högst 48 månader gammal.

## Lokal kontroll av väntande svensk deltafil

`gnucash-program-sv-reviewed-delta-20261027.po` innehåller 59 granskade
ändringar. Kontrollkedjan den 27 oktober gav:

| Kontroll | Resultat |
| --- | --- |
| `msgfmt --check` | 59 översatta poster, godkänd katalog |
| `l10n-lint` | 0 fel, 0 varningar |
| `svlang` | Inga anglicismer |
| Hunspell | Inga åtgärdskandidater efter manuell bedömning; den råa radbaserade utskriften delar sammansatta ord från flerradsposter och används inte som stavningsbevis |
| Gitleaks | Inga hemligheter |

Filen är lokalt kontrollerad men inte inskickad. Före uppladdning ska den
jämföras med den aktuella GnuCash-målfilen. De tre dokumenterade
`split`-posterna lämnas utanför tills projektet har fattat ett termbeslut.

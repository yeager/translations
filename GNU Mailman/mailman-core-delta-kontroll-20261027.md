# GNU Mailman Core: deltatranslationskontroll, 27 oktober 2026

`mailman-core-sv-20261026.delta.po` innehåller elva svenska rättningar för
Core, inklusive kommandohjälp och textmallnära meddelanden. Filen är en
separat deltakatalog och ersätter inte den fullständiga svenska katalogen.

En ny lokal kontroll hittade och rättade två formatbrister:

* kommandohjälpen för `mailman shell` saknade en av källans radbrytningar;
* `Note:` återges nu med svensk kolonmarkering som `Observera:`.

PO-huvudet har dessutom kompletterats så att den fristående importfilen
innehåller projekt-, språk- och överföringsmetadata.

## Kontrollresultat

| Kontroll | Resultat |
| --- | --- |
| `msgfmt --check --check-header --check-format` | 11 översatta poster, godkänd |
| `l10n-lint` | 0 fel, 0 varningar |
| `svlang` | Inga anglicismer |
| Gitleaks | Inga hemligheter |

Informationsraden om början på `--send` är förväntad: svensk meningsbyggnad
börjar med `Flaggorna`, medan källtexten börjar med ett kommandoargument.
Filen är lokal och ej uppladdad. Innan eventuell import ska aktuell svensk
måltext och Mailmans textmallar jämföras på nytt.

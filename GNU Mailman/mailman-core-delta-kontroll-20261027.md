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

## Jämförelse med aktuell Core-katalog

Core-katalogen på GitLabs `master` jämfördes 2026-10-27. Den hämtade filen
har SHA-256 `7fbeea7c77fc93aefd40a3094fd7fa6a89bb1ad3a1ec5a1706cf39b3d543f9e4`.
Av de ursprungliga elva deltaenheterna matchar tre redan uppströmstexten,
sju källtexter finns inte längre i katalogen och en sträng skiljer fortfarande.

Den återstående radbrytningsrättningen för `mailman shell` ligger därför i den
nya enpostersfilen `mailman-core-sv-live-jamford-20261027.delta.po`. Den var
den enda av de elva ursprungliga enheterna som kunde importeras utan att
försöka återinföra föråldrade källtexter. Den sparades i Hosted Weblate
2026-10-27 och kontrollvarningen för posten försvann.

Den separata kontrollen av enpostersfilen passerar `msgfmt`, `l10n-lint`,
`svlang` och Gitleaks. Hunspell träffar enbart de granskade fack- och
kommandotermerna `anropbart`, `modulsökvägen`, `listspec` och `details`.

## Avsiktligt tomma poster

Weblate visar fortfarande tre poster som oöversatta. De har dock tom
källtext och representerar endast kontexterna
`list:member:digest:header.txt`, `list:member:regular:header.txt` och
`list:user:notice:goodbye.txt`. Kommentarerna på samtliga tre uppmanar till
att ta bort tomma strängar. De ska lämnas tomma och får inte ersättas med
översatta filnamn eller importeras som deltakatalog.

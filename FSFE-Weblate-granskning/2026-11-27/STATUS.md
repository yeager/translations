# FSFE Weblate – svensk granskning (2026-11-27)

Källa: Hosted Weblate API, projekt `fsfe`, språk `sv`. Samtliga ursprungsfiler är exporterade 2026-11-27. Arbetet skickas komponentvis och varsamt. Ingen komponentinställning eller låsning har ändrats.

## Status

| Komponent | Översatt | Fuzzy | Saknas | Ändringar skickade | Status / blockerare |
|---|---:|---:|---:|---:|---|
| Ada & Zangemann | 299/299 | 0 | 0 | 2 korrigeringar | Uppladdad; 0 Weblate-kontroller med fel. |
| FSFE Website global text | 127/127 | 0 | 0 | 81 nya + 10 rättade | Uppladdad; 9 Weblate-kontroller flaggas fortfarande. |
| FSFE Website: What is Free Software | 67/67 | 0 | 0 | 67 fuzzy omarbetade | Uppladdad; 4 Weblate-kontroller flaggas fortfarande. |
| I Love Free Software Day – toolkit | 0/255 | 255 | 0 | 0 | Kvar att översätta och granska. |
| Refund 4 Freedom | 88/154 | 0 | 66 | 0 | 🔒 Hänglås i skärmbilden och API `locked=true`; 66 strängar saknas. |
| reuse-tool | 249/249 | 0 | 0 | 101 | Uppladdad; två Weblate-kontroller kvar, varav identiska svenska pluralformer är grammatisk korrekt undantag. `msgfmt --check --check-format` passerar med riktad flagga för Click-källans pluralformat. |
| REUSE Website Markdown | 193/559 | 24 | 342 | 0 | 🔒 Hänglås i skärmbilden och API `locked=true`; 366 strängar är fuzzy eller saknas. |
| REUSE Website Strings | 28/28 | 0 | 0 | 0 | 🔒 Hänglås i skärmbilden och API `locked=true`; uppladdning av 16 lokalt rättade strängar avvisades med HTTP 403 `permission_denied`. |

## Validering och anmärkningar

- `reuse-tool`: `msgfmt --check --check-format` godkänd. `l10n-lint`: 0 fel; tre varningar (emotikon och svensk pluralform utan grammatisk skillnad). Platshållare och pluralformsplatshållare jämfördes per form. Hunspell-resultat sparade; okända flaggor, identifierare, egennamn och tekniska termer ska inte behandlas som stavfel.
- `What is Free Software`: alla 67 enheter genomgångna, HTML-taggar och URL:er jämförda mot källan, inga oöversatta/fuzzy enheter kvar. `l10n-lint` saknar stöd för den här Weblate XHTML-exporten. Hunspell-markerade `Foundation`, `Initiative`, `Libre`, `Source` är egennamn; `upphovsrätts-` är ett korrekt sammansättningsled.
- `FSFE Website global text`: flat XML-parsning godkänd. `l10n-lint` tolkar inte Weblates flatxml-format (förväntar sig Android-resurser).
- `REUSE Website Strings`: JSON-parsning och käll-/målformatjämförelse godkända. Generisk `l10n-lint` tolkar Weblates `other`-fält felaktigt som CLDR-pluraler och ger därför falska fel. Hunspell hittade inga okända ord i målförslaget.
- De tre synliga hänglåsen gäller **Refund 4 Freedom**, **REUSE Website Markdown** och **REUSE Website Strings**. De har inte låsts upp eller fått inställningar ändrade.
- Filer med `reviewed.*` visar uppladdade resultat. `REUSE Website Strings/reviewed.json` är ett lokalt granskat förslag som inte kunde skickas in på grund av låset.

## Filer

Varje komponentkatalog innehåller API-exporten som original. Där granskning/ändring är klar finns en granskad fil och unified diff. För ODT och låsta kataloger finns originalfilen och aktuell status.

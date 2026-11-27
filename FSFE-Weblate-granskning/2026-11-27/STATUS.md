# FSFE Weblate – svensk granskning (2026-11-27)

Källa: Hosted Weblate API, projekt `fsfe`, språk `sv`. Ursprungsfilerna exporterades 2026-11-27. Ändringar har skickats via API i små batcher. Inga projektinställningar eller lås har ändrats.

## Status

| Komponent | Översatt | Fuzzy | Saknas | Ändringar skickade | Status / blockerare |
|---|---:|---:|---:|---:|---|
| Ada & Zangemann | 299/299 | 0 | 0 | 2 rättade | Uppladdad; API visar 0 felkontroller. |
| FSFE Website global text | 127/127 | 0 | 0 | 81 nya + 10 rättade | Uppladdad; senaste API-statistiken visar 7 Weblate-kontroller flaggade. |
| FSFE Website: What is Free Software | 67/67 | 0 | 0 | 67 fuzzy omarbetade | Uppladdad; 4 Weblate-kontroller flaggas ännu. |
| I Love Free Software Day – toolkit | 255/255 | 0 | 0 | 255 översatta/omarbetade | Uppladdad; 70 Weblate-kontroller flaggas ännu (se nedan). |
| Refund 4 Freedom | 88/154 | 0 | 66 | 0 | 🔒 Hänglås i skärmbilden och API `locked=true`; 66 strängar saknas. |
| reuse-tool | 249/249 | 0 | 0 | 101 | Uppladdad; 2 Weblate-kontroller kvar. `msgfmt --check --check-format` passerar med en riktad gettext-flagga för Click-källans pluralformat. |
| REUSE Website Markdown | 193/559 | 24 | 342 | 0 | 🔒 Hänglås i skärmbilden och API `locked=true`; 366 strängar är fuzzy eller saknas. |
| REUSE Website Strings | 28/28 | 0 | 0 | 0 | 🔒 Hänglås i skärmbilden och API `locked=true`; 16 lokala rättningar kunde inte laddas upp (HTTP 403 `permission_denied`). |

Oöversatta eller fuzzy strängar återstår på de två låsta komponenterna Refund 4 Freedom och REUSE Website Markdown: **432 totalt**. REUSE Website Strings är komplett i Weblate men dess granskade rättningsförslag ligger endast lokalt på grund av låset.

## Validering och anmärkningar

- **I Love Free Software Day – toolkit:** alla 255 poster jämförda mot källan; URL:er, e-postadresser, hashtags, licensidentifierare, kommandon, produktnamn och emoji kontrollerade. `msgfmt --check --check-format`: godkänd. `l10n-lint`: 0 fel och 0 varningar på den sammanslagna kontrollkatalogen. Hunspell-resultat och granskade undantag finns i katalogen. API visar 70 flaggade kontroller: 56 enheter vars mål korrekt är identiskt med källan (URL:er, hashtags, licens-/produktnamn, kommandon eller märkningar) och 14 enheter med den svenska etiketten ”Ett rätt svar”. Weblate API exponerar inte kontrollnamnen, så dessa flaggor är noterade och inte maskerade.
- **reuse-tool:** `msgfmt --check --check-format` godkänd. `l10n-lint`: 0 fel; varningar gäller emotikoner och svensk pluralform utan grammatisk skillnad. Platshållare granskades form för form.
- **What is Free Software:** alla 67 enheter genomgångna, HTML-taggar och URL:er jämförda mot källan, inga oöversatta/fuzzy enheter kvar. `l10n-lint` saknar stöd för Weblates XHTML-export; Hunspell-markerade egennamn/tekniska termer finns dokumenterade.
- **FSFE Website global text:** XML-parsning godkänd. `l10n-lint` tolkar inte Weblates flatxml-format som denna komponent använder.
- **REUSE Website Strings:** JSON-parsning och käll-/målformatjämförelse godkända. Den generiska linter tolkar Weblates `other`-form felaktigt som en CLDR-pluralform. Hunspell hittade inga okända ord i förslaget.
- Hänglåsikonen i den bifogade Weblate-skärmbilden markerar låsta komponenter: **Refund 4 Freedom**, **REUSE Website Markdown** och **REUSE Website Strings**. API bekräftar `locked=true` för alla tre. En uppladdning till REUSE Website Strings avvisades med HTTP 403 `permission_denied`. Låsen har inte ändrats; de två första komponenterna har 432 oöversatta/fuzzy strängar sammanlagt, och de 16 granskade REUSE Website Strings-rättningarna är bara lokala förslag.
- Filer med `reviewed.*` är uppladdade resultat. `reuse-website-strings/reviewed.json` är ett lokalt granskat förslag som inte gick att skicka in.

## Arkivinnehåll

Varje komponent har originalexporten. Färdiggranskade komponenter har även granskad fil och diff; ODT-komponenten har en granskad ODT och en per-sträng-diff. Låsta komponenter är markerade med blockeraren i statusen.

# Avogadro, svensk komplettering 2026-11-12

## Omfattning och upstreamstatus

Arbetet genomfördes i Hosted Weblate via API och varje uppladdad batch lästes
tillbaka från API:t med jämförelse mot den lokala deltafilen. Aktuell
komponentstatus efter sista återläsningen:

| Komponent | Översatt | Oöversatt | Luddiga | Aktuella Weblate-kontroller |
| --- | ---: | ---: | ---: | ---: |
| `avogadroapp` | 237 av 237 | 0 | 0 | 6 |
| `avogadrolibs` | 2 229 av 2 229 | 0 | 0 | 149 |

Upstreaminsändning: bekräftad i Hosted Weblate. Detta är inte ett påstående om
en framtida källsynk eller publicerad programutgåva.

## Arkiv

Färdiga deltafiler finns i `Weblate/avogadroapp-sv-batch-20261112.json` och
`Weblate/avogadrolibs-sv-batch-20261112-01.json` till och med
`Weblate/avogadrolibs-sv-batch-20261112-15.json` i
<https://github.com/yeager/translations/tree/main/Weblate>.

## Kontroller

- Alla nya batcher: JSON-struktur och enhets-id, platsvariabler, radbrytningar,
  tabbar och pluralformer kontrollerades före uppladdning.
- `l10n-lint` kördes med käll- och måltext i ett tillfälligt JSON-underlag för
  varje batch. Sista batchen gav inga fel eller varningar.
- `svlang`, Hunspell med svensk ordlista, `git diff --check` och Gitleaks
  passerade för varje batch. Hunspells återstående träffar är kodnamn,
  formatnamn och ämnesspecifika termer som `bondTo`, `ffmpeg` och `Å`.
- Full export kontrollerades med `msgfmt --check --statistics`. Kontrollens
  enda fatala fel är en befintlig källformatsdefekt i Navigator-texten
  `2% change`: katalogen har flaggan `c-format`, och gettext tolkar den
  bokstavliga procenten som en platshållare. Den svenska översättningen
  förfalskades inte för att kringgå detta.
- Full export med korrekt `.po`-ändelse gav 0 fel och 11 varningar i
  `l10n-lint`. Varningarna omfattar äldre inkonsekvenser, avsiktligt
  oförändrade produkt- och formatnamn samt två API-värdeintervall `1-3`.
  De 149 aktuella Weblate-kontrollerna är inte liktydiga med oöversatta
  strängar och omfattar redan befintliga katalogkontroller.

## Återstående arbete

Ingen oöversatt svensk sträng återstår i de två Avogadro-komponenterna. En
separat fullständig granskning av de 2 229 redan översatta libsträngarna och
upprättande av en uppströmsfråga om den felaktiga `c-format`-markeringen är
separata uppgifter.

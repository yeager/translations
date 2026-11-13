# Fossify Paint: svenska verktygsetiketter

Fossify Paint är en Android-app för enkel ritning och bildredigering.
Den svenska resursfilen täcker samtliga 12 aktuella engelska nycklar. Tre
synliga etiketter behövde justeras efter kontroll av ritverktygens konkreta
UI-kontext.

| Nyckel | Tidigare text | Granskad text |
| --- | --- | --- |
| `bucket_fill` | Färgpyts | Fyll med färg |
| `show_brush_size` | Visa penselstorleksverktyg | Visa verktyget för penselstorlek |
| `app_launcher_name` | Måla | Paint |

`Paint` är projektets produktnamn och ska därför inte översättas i
startetiketten.

## Kontroller och status

- Aktuell utgåva är från 2026-11-07 och uppfyller färskhetskravet.
- XML-syntax, täckning mot källkatalogen (12 av 12), `l10n-lint`, Hunspell-sv,
  svlang, diffkontroll och Gitleaks är godkända.
- `msgfmt` är inte tillämpligt på Android XML. Android-lint kunde inte köras
  lokalt eftersom Java Runtime saknas.
- Commit `60e689a` är pushad till `yeager/Paint` och inskickad som
  [FossifyOrg/Paint#255](https://github.com/FossifyOrg/Paint/pull/255).
  Pull-begäran är öppen och ännu inte upstreamgranskad, mergad eller släppt.

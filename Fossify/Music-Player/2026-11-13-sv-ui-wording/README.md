# Fossify Musikspelare: svensk UI-granskning

Fossify Musikspelare är en enkel Android-spelare för lokala ljudfiler. Den
svenska katalogen i aktuell `main` har 73 av 73 källnycklar, men ett antal
synliga reglage och hjälprader var oidiomatiska eller beskrev fel funktion.

## Rättade poster

| Nyckel | Tidigare text | Granskad text |
| --- | --- | --- |
| `repeat_off` | Repetera av | Upprepning av |
| `enable_shuffle` | Aktivera blanda | Aktivera blandning |
| `disable_shuffle` | Inaktivera blanda | Inaktivera blandning |
| `shuffle_enabled` | Blanda aktiverad | Blandning är aktiverad |
| `shuffle_disabled` | Blanda inaktiverad | Blandning är inaktiverad |
| `fetching_songs` | Hämtar låtar… | Läser in låtar… |
| `show_filename` | Ersätt låttitel med filnamn | Visa filnamn som låttitel |
| `swap_prev_next` | Växla hörlurars föregående- och nästaknappar | Byt plats på hörlurarnas knappar för föregående och nästa |
| `rescan_media` | Skanna media igen | Skanna medier igen |
| `faq_1_text` | Oidiomatisk klickinstruktion | Kortare instruktion med korrekt UI-kontext |

## Kontroller och upstreamstatus

- Aktuell release `1.8.5` publicerades 2026-10-24 och uppfyller
  färskhetskravet.
- XML-syntax och täckning mot engelska katalogen är godkända: 73 av 73
  strängnycklar.
- `l10n-lint`, Hunspell-sv, svlang, diffkontroll och Gitleaks är körda.
  Inga relevanta språk- eller syntaxfel rapporterades. `msgfmt` är inte
  tillämpligt på Android XML.
- Android-lint kunde inte köras lokalt eftersom Java Runtime saknas i
  miljön.
- Ändringen är pushad till forken `yeager/Music-Player` i commit `6324ae7`
  och inskickad som [FossifyOrg/Music-Player#529](https://github.com/FossifyOrg/Music-Player/pull/529).
  Pull-begäran är öppen; den är inte upstreamgranskad, mergad eller släppt.

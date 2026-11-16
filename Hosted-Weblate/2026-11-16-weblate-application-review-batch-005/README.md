# Hosted Weblate – Weblate Application – svenska – granskningsbatch 005

Datum: 2026-11-16

## Omfattning

Tio strängar har granskats rad för rad i sitt UI- och källkodssammanhang och sparats direkt i Hosted Weblate. Sökningen `state:needs-editing` minskade från 19 till 9 poster efter uppdatering av resultaten.

| Engelska | Svenska |
| --- | --- |
| The upload target or permissions changed. | Uppladdningsmålet eller behörigheterna har ändrats. |
| File upload has failed. Please try again later. | Filuppladdningen misslyckades. Försök igen senare. |
| Translation upload in progress. | Översättningsuppladdning pågår. |
| Template output exceeds its size limit. | Mallens utdata överskrider storleksgränsen. |
| Template rendering failed or exceeded its resource limits. | Mallrenderingen misslyckades eller överskred resursgränserna. |
| Invalid template rendering response. | Ogiltigt svar från mallrenderingen. |
| Template value exceeds its size limit. | Mallvärdet överskrider storleksgränsen. |
| Template context is nested too deeply. | Mallkontexten är nästlad för djupt. |
| Template context exceeds its size limit. | Mallkontexten överskrider storleksgränsen. |
| Unsupported template context key. | Mallkontextnyckeln stöds inte. |

## Terminologi och kontroller

- `template` har normaliserats till **mall** i felmeddelandenas tekniska UI-kontext.
- Direkt sparat upstream i Hosted Weblate; detta är inte en separat upstream-granskning eller merge.
- Weblate-resultat verifierat efter uppdatering: 19 → 9 `state:needs-editing`.
- Diffkontroll: godkänd (ny arkivpost).
- Gitleaks: godkänd.
- `msgfmt`: ej tillämpligt; Hosted Weblate gav ingen lokal gettext-export för denna batch.
- `l10n-lint`, `svlang` och `hunspell-sv`: ej körda, eftersom ingen lokal översättningsfil exporterades från Hosted Weblate.

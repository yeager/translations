# Hosted Weblate – Weblate Application – svenska – granskningsbatch 006

Datum: 2026-11-16

## Omfattning

De sista nio strängarna med tillståndet `needs-editing` har granskats rad för rad i sitt UI- och källkodssammanhang och sparats direkt i Hosted Weblate. Efter sparandet nådde kön slutet; komponenten har 5 966 av 5 966 översatta och granskade strängar.

| Engelska | Svenska |
| --- | --- |
| Unsupported template context value. | Mallkontextvärdet stöds inte. |
| Template rendering exceeded its time limit. | Mallrenderingen överskred tidsgränsen. |
| Template rendering exceeded its loop limit. | Mallrenderingen överskred gränsen för loopar. |
| Template intermediate value exceeds its size limit. | Mellanvärdet i mallen överskrider storleksgränsen. |
| Template replacement exceeds its size limit. | Mallen ersättning överskrider storleksgränsen. |
| Template padding exceeds its size limit. | Utfyllnaden i mallen överskrider storleksgränsen. |
| Template formatting exceeds its size limit. | Mallformateringen överskrider storleksgränsen. |
| Template join exceeds its size limit. | Sammanfogningen av mallen överskrider storleksgränsen. |
| Could not remove nested repository metadata. | Kunde inte ta bort kapslade förrådsmetadata. |

## Terminologi och kontroller

- `template` har konsekvent normaliserats till **mall** i den tekniska felmeddelandekontexten; `repository` följer projektets ordlista: **förråd**.
- Direkt sparat upstream i Hosted Weblate; detta är inte en separat upstream-granskning eller merge.
- Weblate-kö verifierad: 0 återstående `state:needs-editing`; 5 966/5 966 strängar översatta och granskade.
- En uppföljande språkjustering av raden om malleursättning samt tre separata Weblate-kontroller återstår att granska; de räknas inte som `needs-editing` och behandlas separat.
- Diffkontroll: godkänd (ny arkivpost).
- Gitleaks: godkänd.
- `msgfmt`: ej tillämpligt; Hosted Weblate gav ingen lokal gettext-export för denna batch.
- `l10n-lint`, `svlang` och `hunspell-sv`: ej körda, eftersom ingen lokal översättningsfil exporterades från Hosted Weblate.

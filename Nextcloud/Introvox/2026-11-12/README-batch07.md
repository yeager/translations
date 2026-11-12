# Nextcloud Introvox – svenska batch 7, 2026-11-12

- Komponent: `o:nextcloud:p:nextcloud:r:introvox`.
- Omfattning: 25 strängar, index 150–174 i den aktuella API-exporten. Batchen gäller administration av rundturer och synlighet.
- Terminologi: rundtur, Huvudspråk, Synlig för, rundturens aktivering, första inloggning och aktiverade konton.
- Kontroller: platshållaren `{example}` och all struktur bevarad; l10n-lint, diffkontroll och Gitleaks godkända; svlangs V2-träffar är falska positiva från UI-etiketter och brödtext i gemensam analys; Hunspell-träffar är `Nextcloud-installationen` och platshållaren `example`. `msgfmt` är inte tillämpligt för JSON-resursen.
- Upstream: inte uppladdat på grund av `locked`-taggar. Transifex API returnerar HTTP 409 för översättningsuppdatering.
- Status: lokalt granskat och arkiverat som väntande delta.

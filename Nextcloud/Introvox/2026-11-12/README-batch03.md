# Nextcloud Introvox – svenska batch 3, 2026-11-12

- Komponent: `o:nextcloud:p:nextcloud:r:introvox`.
- Omfattning: 25 strängar, index 50–74 i den aktuella API-exporten. Batchen omfattar Deck-rundturer och tillhörande UI-fragment.
- Terminologi kontrollerad mot Nextcloud Decks svenska katalog: tavla, kort, lista, Att göra, Klart, Kommande kort, Kan redigera, Markera som klart och Inget förfallodatum.
- Kontroller: HTML, platshållare och emoji bevarade för 25 av 25; l10n-lint utan fel eller varningar; ett frågetecken följde källans rubrikstil; svlangs V2-varningar bedöms som falska positiva för HTML och etikettfragment; Hunspell-träffar är Deck, em och emoji; diffkontroll och Gitleaks godkända. `msgfmt` är inte tillämpligt för JSON-resursen.
- Upstream: inte uppladdat. API-inventeringen visar taggen `locked` på Introvox strängar och Transifex avvisar översättningsuppdatering med HTTP 409.
- Status: lokalt granskat och arkiverat som väntande delta.

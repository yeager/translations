# Nextcloud Introvox – svenska batch 4, 2026-11-12

- Komponent: `o:nextcloud:p:nextcloud:r:introvox`.
- Omfattning: 25 strängar, index 75–99 i den aktuella API-exporten. Batchen omfattar Calendar-rundturer och UI-fragment.
- Terminologi kontrollerad mot Calendar-katalogen: Deltagare, Hitta en tid, Mer information, Spara, Idag, Kalenderinställningar, Papperskorg och Redigera och dela kalender.
- Kontroller: platshållare och HTML bevarade för 25 av 25; l10n-lint utan fel eller varningar; svlangs V2-varningar är falska positiva från HTML/etiketter; Hunspell-träffar är etablerade teknik- och produkttermer (`CalDAV`, `DAVx⁵`, `Deck`, `applösenord`, `veckovyn`); diffkontroll och Gitleaks godkända. `msgfmt` är inte tillämpligt för JSON-resursen.
- Upstream: inte uppladdat på grund av `locked`-taggar. Transifex API returnerar HTTP 409 för översättningsuppdatering.
- Status: lokalt granskat och arkiverat som väntande delta.

# Nextcloud Introvox – svenska batch 2, 2026-11-12

- Komponent: `o:nextcloud:p:nextcloud:r:introvox`.
- Omfattning: 25 ytterligare strängar, index 25–49 i den aktuella API-exporten. Texterna gäller Filer, Delningar, Borttagna filer och Call-rundturer.
- Terminologi: Delningar, Alla filer, Väntande delningar, Borttagna filer, rundtur, konversation, Deltagare och Notifieringar.
- Kontroller: platshållare och HTML bevarade; l10n-lint godkänd efter korrigering av ett kolon i en samtalssträng; svlangs fragmentvarningar bedöms i UI-/markup-kontext; Hunspell-träffar är etablerade Nextcloud-termer och emoji; diffkontroll och Gitleaks godkända. `msgfmt` är inte tillämpligt för JSON-resursen.
- Upstream: inte uppladdat. API-inventeringen visar att Introvox strängar har taggen `locked`; Transifex blockerar översättningsuppdatering med HTTP 409.
- Status: lokalt granskat och arkiverat som väntande delta.

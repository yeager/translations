# Nextcloud – svensk Transifex-status

Källa: Transifex-projektet `nextcloud/nextcloud`. Projektets serverrelease `v33.0.10` publicerades 2026-10-15 och uppfyller därför aktuellhetskravet.

Den 12 november 2026 granskades 297 tidigare oöversatta svenska resurssträngar i 32 komponenter och skickades med Transifex API. Varje komponent kontrollerades efter inskick med HTTP 200 och en separat API-läsning som visade 0 oöversatta strängar i den aktuella komponenten.

Memories är färdig: 75 strängar har granskats i fyra batcher och en separat API-läsning visar 0 oöversatta strängar.

LibreSign är färdig: 81 strängar granskades i tre batcher den 12 november 2026 (3 notifieringar, 8 e-postmallar och 70 UI- och inställningstexter). Alla batcher skickades med Transifex API, och en separat API-läsning efter den sista batchen visade 0 oöversatta svenska strängar i komponenten.

Souvenirs är färdig: 63 strängar med produktbeskrivning, guide och UI-gränssnitt granskades och skickades i en API-batch den 12 november 2026. En separat API-läsning efter inskicket visade 0 oöversatta svenska strängar i komponenten.

Vid den inledande inventeringen omfattade projektet 299 resurser. Den visade minst 821 oöversatta svenska strängar på första resultatenheten, fördelade på 36 komponenter. `introvox` och `pantry` var paginerade och har fler än de 150 strängar som första sidan visar. Efter de 297 verifierade ändringarna kunde en ny heltäckande inventering inte slutföras, eftersom Transifex svarade med HTTP 429. Därför anges inget osäkert totalantal återstående strängar här.

Arkivet innehåller oförändrade JSON-deltafiler, komponentvisa statusfiler och en projektterminologilista. För JSON-resurser är `msgfmt` inte tillämpligt. l10n-lint, svlang, Hunspell, `git diff --check` och Gitleaks kördes per batch; produktnamn, format och platshållare dokumenteras som förväntade Hunspell-träffar.

Status: de färdigmarkerade batcherna är lokalt granskade, arkiverade i `yeager/translations`, skickade och komponentvis verifierade i Transifex. Upstream-granskning eller publicering kan inte utläsas från Transifex API och anges inte som genomförd.

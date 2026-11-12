# Nextcloud Introvox – svenska batch 1, 2026-11-12

- Komponent: `o:nextcloud:p:nextcloud:r:introvox`.
- Versionskälla: IntroVox 1.7.8, aktuell utgåva i augusti 2026.
- Omfattning: 25 av 367 aktuella oöversatta svenska strängar granskades rad för rad. Strängarna är administratörsfel, rubriker och den inbyggda rundturen för Filer.
- Terminologi: rundtur, Filer, dela/delning, åtkomst och offentlig länk. Nextcloud, CalDAV och ID behålls.
- Kontroller: platshållare och HTML-markup bevarade för 25 av 25; l10n-lint godkänd; svlang gav endast falska positiva träffar från HTML och fristående etiketter; Hunspell endast `steguppgifter`, `Nextcloud` och emoji; diffkontroll och Gitleaks godkända. `msgfmt` är inte tillämpligt på Transifex JSON-resursen.
- Upstream: Transifex API-batch avvisades med HTTP 409. En efterföljande kontroll av alla 25 källsträngar visade taggen `locked`; Transifex tillåter inte API- eller filuppladdning för låsta strängar.
- Status: lokalt granskat och arkiverat som väntande delta. Inte uppladdat. Återstående i komponenten: 342 oöversatta strängar, samtliga 367 för närvarande låsta enligt API-inventeringen.

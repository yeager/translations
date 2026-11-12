# Souvenirs – svensk granskningsstatus 2026-11-12

Komponent: `o:nextcloud:p:nextcloud:r:souvenirs`.

Projekt- och kontextkontroll: Souvenirs 2.4.1 är den aktuella stabila versionen för Nextcloud 34 och appen uppdaterades i slutet av oktober 2026. Komponenten omfattar produktbeskrivning, användarguide och tillhörande UI-texter för album med foton, video och panoramor.

Deltafilen `souvenirs-sv-delta-20261112.jsonl` innehåller 63 strängar. Den granskades rad för rad med bevarade Markdown-markörer, länkar, filnamnet `album.json`, tangenter, specialtecken och den enda em dash som finns i källtexten.

Kontroller: l10n-lint, svlang, Hunspell, `git diff --check` och Gitleaks godkända. Hunspell-träffarna består av produktnamn, filnamn och sammansättningsdelar som `Nextcloud`, `Photo Sphere`, `album.json` och `360°-panorama`. `msgfmt` är inte tillämpligt eftersom Transifex-resursen är JSON-baserad.

Uppladdning: Transifex API returnerade HTTP 200 för 63 uppdateringar. En separat API-läsning efter inskicket visade 0 oöversatta svenska strängar i komponenten.

Status: lokalt granskat, arkiverat och uppladdat. Upstream-granskning eller publicering är inte verifierad.

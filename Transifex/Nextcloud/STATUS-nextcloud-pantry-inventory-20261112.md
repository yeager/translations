# Pantry – lagerbatch, svensk granskningsstatus 2026-11-12

Komponent: `o:nextcloud:p:nextcloud:r:pantry`.

Projekt- och kontextkontroll: Pantry 0.36.0 stöder Nextcloud 35 och har en aktuell utgåva från 2026. Batchen omfattar lagersaldon, checklistor, mallar, papperskorg och arkivering.

Deltafilen `pantry-inventory-sv-delta-20261112.jsonl` innehåller 100 strängar. Platshållarna `%n` och `{…}` samt tillåtna källtecken som `·`, `×` och em dash bevarades exakt. Em dash finns endast i översättningar där den också finns i källtexten.

Kontroller: l10n-lint, svlang, Hunspell, platshållar- och teckenparitetskontroll, `git diff --check` och Gitleaks godkända. Hunspell-träffar är enbart platshållarnamn. `msgfmt` är inte tillämpligt eftersom Transifex-resursen är JSON-baserad.

Uppladdning: Transifex API returnerade HTTP 200 för 100 uppdateringar. En separat API-läsning efter inskicket visade 138 oöversatta svenska strängar kvar i Pantry.

Status: batchen är lokalt granskad, arkiverad och uppladdad. Komponenten är inte färdig. Upstream-granskning eller publicering är inte verifierad.

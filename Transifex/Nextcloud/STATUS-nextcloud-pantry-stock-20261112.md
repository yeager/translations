# Pantry – lagerbatch 2, svensk granskningsstatus 2026-11-12

Komponent: `o:nextcloud:p:nextcloud:r:pantry`.

Deltafilen `pantry-stock-sv-delta-20261112.jsonl` innehåller 100 strängar för mallar, listor, lagersaldon, påfyllning och hållbarhet. Svenska termer följer den första Pantry-batchens terminologi, särskilt `lager`, `checklista`, `påfyllning`, `tillgänglig mängd` och `beställningspunkt`.

Kontroller: l10n-lint, svlang, Hunspell, platshållar- och teckenparitetskontroll, `git diff --check` och Gitleaks godkända. Hunspell-träffar är platshållarnamn och den projektspecifika termen `Förifyll`. `msgfmt` är inte tillämpligt eftersom Transifex-resursen är JSON-baserad.

Uppladdning: Transifex API returnerade HTTP 200 för 100 uppdateringar. En separat API-läsning efter inskicket visade 38 oöversatta svenska strängar kvar i Pantry.

Status: batchen är lokalt granskad, arkiverad och uppladdad. Komponenten är inte färdig. Upstream-granskning eller publicering är inte verifierad.

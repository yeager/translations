# Pantry – slutbatch, svensk granskningsstatus 2026-11-12

Komponent: `o:nextcloud:p:nextcloud:r:pantry`.

Deltafilen `pantry-final-sv-delta-20261112.jsonl` innehåller 38 strängar för sökning, länkning mellan lagervaror och checklistor, köpflöde, mallförslag och delade hem.

Kontroller: l10n-lint, svlang, Hunspell, platshållar- och specialteckenparitetskontroll, `git diff --check` och Gitleaks godkända. l10n-lint gav två informationsmeddelanden om att den svenska satsen börjar med `Det gick inte` i stället för `%n`; detta är avsiktligt idiomatisk svensk ordföljd och platshållaren är bevarad. Hunspell-träffar är platshållarnamn. `msgfmt` är inte tillämpligt eftersom Transifex-resursen är JSON-baserad.

Uppladdning: Transifex API returnerade HTTP 200 för 38 uppdateringar. En separat API-läsning efter inskicket visade 0 oöversatta svenska strängar i Pantry.

Status: samtliga 238 tidigare oöversatta strängar i Pantry är lokalt granskade, arkiverade och uppladdade i tre batcher. Upstream-granskning eller publicering är inte verifierad.

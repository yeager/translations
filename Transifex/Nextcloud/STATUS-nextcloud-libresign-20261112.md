# LibreSign – svensk granskningsstatus 2026-11-12

Komponent: `o:nextcloud:p:nextcloud:r:libresign`.

Projekt- och kontextkontroll: LibreSign har aktuell release 15.0.12, publicerad den 4 november 2026. De granskade strängarna är notifieringar och e-postmallar i dokumentflödet för elektroniska underskrifter.

## Färdiga batcher

| Deltafil | Strängar | Lokal kontroll | Transifex-inskick | Separat API-verifiering |
| --- | ---: | --- | --- | --- |
| `libresign-notifications-sv-delta-20261112.jsonl` | 3 | l10n-lint och Gitleaks godkända | HTTP 200, 3 uppdateringar | verifierad tillsammans med nästa läsning |
| `libresign-mail-sv-delta-20261112.jsonl` | 8 | l10n-lint, svlang, Hunspell, `git diff --check` och Gitleaks godkända | HTTP 200, 8 uppdateringar | 70 oöversatta strängar återstår i komponenten |
| `libresign-main-sv-delta-20261112.jsonl` | 70 | l10n-lint, svlang, Hunspell, `git diff --check` och Gitleaks godkända | HTTP 200, 70 uppdateringar | 0 oöversatta strängar återstår |

`msgfmt` är inte tillämpligt eftersom Transifex-resursen är JSON-baserad. Platshållarna `%1$s`, `%2$s` och `%3$s` samt radbrytningarna bevarades exakt i e-postmallarna. Hunspell gav inga träffar för den andra batchen.

Status: 81 strängar är lokalt granskade, arkiverade och uppladdade. En separat Transifex API-läsning efter den sista batchen visar 0 oöversatta strängar i LibreSign. Upstream-granskning eller publicering är inte verifierad.

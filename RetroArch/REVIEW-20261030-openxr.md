# RetroArch: svensk OpenXR-granskning 2026-10-30

- Projekt: RetroArch i Crowdin, svenska (`sv-SE`)
- Omfattning: 56 tidigare oöversatta OpenXR-strängar i `msg_hash_us.json` samt 5 Vita3K-strängar som Crowdin visade efter den första sparningen.
- Resultat: samtliga 61 strängar sparades direkt i Crowdin under `yeagersthlm`. OpenXR-delen visade inga återstående strängar efter sparning. Vita3K-tillägget omfattar borttagning av lokala data och troféer.
- Terminologi: `skärm`, `handkontroll`, `redigeringsläge`, `fästa mot skärmar`, `fästa mot vinklar` och `gångjärnsspalt` används konsekvent. Enhetsvärdena `15°`, `30°`, `45°` och centimeterstegen är medvetet oförändrade.

## Kontroller

- l10n-lint: godkänd efter normalisering till dess explicita JSON-postformat.
- svlang skrivregler med interpunktion: godkänd.
- Hunspell-sv: endast tekniska/sammansatta ord som `VR-headsetets`, `gångjärnsfäst` och `Rollning` markerades för manuell bedömning.
- kontroll för tre lika konsonanter: inga träffar.
- Gitleaks: inga hemligheter hittades.

Crowdins egna QA-markeringar om inledande versal och vissa sammansatta tekniska ord förhindrade inte sparningen. De är dokumenterade som granskningssignaler, inte som konstaterade språkfel.

## Arkiv

De exakta batcherna finns i `retroarch-sv-openxr-reviewed-20261030.json` och `retroarch-sv-vita3k-cleanup-20261030.json`.

SHA-256: `e3bd6bfb4ea4dcf1c30f79b96980a3927a1a1be6ea26295ba5cd0a64a6759a9e`

SHA-256: `a6a41e98ee48cac2fd4b872ee7331c473bd26c60351349a2e9a2b5a9638bfbe3`

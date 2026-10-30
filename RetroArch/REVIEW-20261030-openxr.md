# RetroArch: svensk OpenXR-granskning 2026-10-30

- Projekt: RetroArch i Crowdin, svenska (`sv-SE`)
- Omfattning: 56 tidigare oöversatta OpenXR-strängar i `msg_hash_us.json`.
- Resultat: samtliga 56 sparades direkt i Crowdin under `yeagersthlm`. Efter sparning visade filtret **Untranslated** inga strängar.
- Terminologi: `skärm`, `handkontroll`, `redigeringsläge`, `fästa mot skärmar`, `fästa mot vinklar` och `gångjärnsspalt` används konsekvent. Enhetsvärdena `15°`, `30°`, `45°` och centimeterstegen är medvetet oförändrade.

## Kontroller

- l10n-lint: godkänd efter normalisering till dess explicita JSON-postformat.
- svlang skrivregler med interpunktion: godkänd.
- Hunspell-sv: endast tekniska/sammansatta ord som `VR-headsetets`, `gångjärnsfäst` och `Rollning` markerades för manuell bedömning.
- kontroll för tre lika konsonanter: inga träffar.
- Gitleaks: inga hemligheter hittades.

Crowdins egna QA-markeringar om inledande versal och vissa sammansatta tekniska ord förhindrade inte sparningen. De är dokumenterade som granskningssignaler, inte som konstaterade språkfel.

## Arkiv

Den exakta batchen finns i `retroarch-sv-openxr-reviewed-20261030.json`.

SHA-256: `e3bd6bfb4ea4dcf1c30f79b96980a3927a1a1be6ea26295ba5cd0a64a6759a9e`

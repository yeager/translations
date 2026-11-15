# Music Assistant Server – Snapcast och Sonic, batch 83

Datum: 2026-11-15

Tjugo texter för Snapcast, SomaFM samt ljudanalys och likhetsfunktioner i
Sonic.

Terminologi: *stream quality* återges som *strömningskvalitet*, *window* som
*fönster*, *sampling* som *sampling*, *diversity* som *variation* och
*discover row* som *Upptäck-raden*. CLAP, MMR, Traits och Character bevaras
som modell- eller funktionsnamn.

Status: alla tjugo strängar uppdaterades via API och lästes tillbaka med samma
översättnings-ID. API-svaret bekräftade `is_untranslated: 0` för samtliga.
Denna arkivkopia har pushats till vårt arkiv; detta är inte en upstream-merge
eller ett upstream-godkännande.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är
inte tillämpligt på JSON-kataloger.

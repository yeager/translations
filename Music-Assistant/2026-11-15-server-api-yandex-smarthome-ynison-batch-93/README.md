# Music Assistant Server – Yandex Smart Home och Ynison, batch 93

Datum: 2026-11-15

Tjugo texter för Yandex Smart Homes molnregistrering och färdighet samt
Yandex Ynison-spelarval och QR-inloggning.

Terminologi: *one-time password* återges som *engångslösenord*, *skill* som
*färdighet*, *relay service* som *relätjänst*, *default player* som
*standardspelare* och *player switching* som *byte av spelare*. UUID,
OAuth-token, access_token, API och externa URL:er bevaras som tekniska
identifierare.

Status: alla tjugo strängar uppdaterades via API och lästes tillbaka med samma
översättnings-ID. API-svaret bekräftade `is_untranslated: 0` för samtliga.
Denna arkivkopia har pushats till vårt arkiv; detta är inte en upstream-merge
eller ett upstream-godkännande.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är
inte tillämpligt på JSON-kataloger.

# Music Assistant Server – Yandex Music, session och Wave-förval, batch 90

Datum: 2026-11-15

Tjugo texter för Yandex Musics sessioner, begränsning av begäranden och
Wave-förval.

Terminologi: *refresh token* återges som *uppdateringstoken*, *rate limits*
som *hastighetsbegränsningar*, *preset* som *förval*, *diversity* som
*variation* och *mood* som *stämning*. VPN, VPS, NAS, CAPTCHA och synliga
produktnamn bevaras.

Status: alla tjugo strängar uppdaterades via API och lästes tillbaka med samma
översättnings-ID. API-svaret bekräftade `is_untranslated: 0` för samtliga.
Denna arkivkopia har pushats till vårt arkiv; detta är inte en upstream-merge
eller ett upstream-godkännande.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är
inte tillämpligt på JSON-kataloger.

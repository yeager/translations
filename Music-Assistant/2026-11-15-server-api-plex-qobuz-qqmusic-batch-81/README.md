# Music Assistant Server – Plex Connect, Qobuz och QQ Music, batch 81

Datum: 2026-11-15

Tjugo strängar för Plex Connect, Qobuz kvalitetsval och QQ Musics
QR-inloggning och kvalitetsalternativ.

Terminologi: *network port* återges som *nätverksport*, *stream quality* som
*strömningskvalitet*, *fallback* som *reserv* och *preferred quality* som
*föredragen kvalitet*. Tekniska protokoll, format och produktnamn bevaras.

Status: alla tjugo strängar uppdaterades via API och lästes tillbaka med samma
översättnings-ID. API-svaret bekräftade `is_untranslated: 0` för samtliga.
Denna arkivkopia har pushats till vårt arkiv; detta är inte en upstream-merge
eller ett upstream-godkännande.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är
inte tillämpligt på JSON-kataloger.

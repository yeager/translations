# Music Assistant Server – OpenSubsonic och ORF Radiothek, batch 74

Datum: 2026-11-15

Tio texter för OpenSubsonic-strömmar och ORF Radiotheks uppspelning i
efterhand.

Terminologi: *transcoding* återges som *omkodning*, *starred* som
*stjärnmärkt*, *catch-up* som *lyssning i efterhand* och *stream type* som
*strömtyp*. Värdena `progressive`, `hls`, `mp3` och `m3u8` samt produktnamn
bevaras, eftersom de används som tekniska identifierare och formatnamn.

Status: alla tio strängar uppdaterades via API och lästes tillbaka med samma
översättnings-ID. API-svaret bekräftade `is_untranslated: 0` för samtliga.
Denna arkivkopia har pushats till vårt arkiv; detta är inte en upstream-merge
eller ett upstream-godkännande.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är
inte tillämpligt på JSON-kataloger.

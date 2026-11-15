# Music Assistant Server – OpenSubsonic-rekommendationer, batch 73

Datum: 2026-11-15

Tio inställningstexter för OpenSubsonic-serverns sökväg och port samt val av
rekommendationer från favoriter, nya album och mest spelade album.

Terminologi: *path* återges som *sökväg*, *port number* som *portnummer*,
*favorite/starred* som *favoritmarkerad/stjärnmärkt* och *recommendation* som
*rekommendation*.

Status: alla tio strängar uppdaterades via API och lästes tillbaka med samma
översättnings-ID. API-svaret bekräftade `is_untranslated: 0` för samtliga.
Denna arkivkopia har pushats till vårt arkiv; detta är inte en upstream-merge
eller ett upstream-godkännande.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är
inte tillämpligt på JSON-kataloger.

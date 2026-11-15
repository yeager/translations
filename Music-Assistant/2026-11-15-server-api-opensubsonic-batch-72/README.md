# Music Assistant Server – OpenSubsonic, batch 72

Datum: 2026-11-15

Tio inställningstexter för OpenSubsonic: äldre autentisering, poddar,
spolningskompatibilitet, sidindelning och anslutningsuppgifter.

Terminologi: *legacy authentication* återges som *äldre autentisering*,
*provider* som *leverantör*, *seeking* som *sökning* i API-kontext och *base
URL* som *bas-URL*. OpenSubsonic, Subsonic och API bevaras som tekniska namn.

Status: alla tio strängar uppdaterades via API och lästes tillbaka med samma
översättnings-ID. API-svaret bekräftade `is_untranslated: 0` för samtliga.
Denna arkivkopia har pushats till vårt arkiv; detta är inte en upstream-merge
eller ett upstream-godkännande.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är
inte tillämpligt på JSON-kataloger.

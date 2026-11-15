# Music Assistant Server – gPodder, Home Assistant och HEOS, batch 62

Datum: 2026-11-15

Tio inställningstexter för gPodder, Home Assistant och HEOS: SSL/TLS,
podcastprenumerationer, TTS-entiteter, spelarkontroll och kommandotidsgränser.

Terminologi: *text-to-speech* återges som *text till tal*, *timeout* som
*tidsgräns*, *hostname* som *värdnamn* och *main controller* som
*huvudstyrenhet*. Produkt- och protokollnamn bevaras. Det synliga interna
fältet `using_gpodder` lämnas oförändrat, eftersom det används som teknisk
konfigurationsidentifierare.

Status: alla tio strängar uppdaterades via API och lästes tillbaka med samma
översättnings-ID. API-svaret bekräftade `is_untranslated: 0` för samtliga.
Denna arkivkopia har pushats till vårt arkiv; detta är inte en upstream-merge
eller ett upstream-godkännande.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är
inte tillämpligt på JSON-kataloger.

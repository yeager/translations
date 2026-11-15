# Music Assistant Server – MPD och MSX Bridge, batch 67

Datum: 2026-11-15

Tio konfigurationstexter för MPD-upptäckt och MSX Bridge-gruppuppspelning.

Terminologi: *host* återges som *värd*, *port* som *port*, *stream* som
*ström* och *redirect* som *omdirigering*. Produkt- och protokollnamnen MPD,
MSX, URL, ffmpeg och Music Player Daemon behålls. De synliga strömlägena
`MA Streamserver` och `Independent` bevaras i förklaringen, medan det
användarorienterade alternativnamnet översätts.

Status: alla tio strängar uppdaterades via API och lästes tillbaka med samma
översättnings-ID. API-svaret bekräftade `is_untranslated: 0` för samtliga.
Denna arkivkopia har pushats till vårt arkiv; detta är inte en upstream-merge
eller ett upstream-godkännande.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är
inte tillämpligt på JSON-kataloger.

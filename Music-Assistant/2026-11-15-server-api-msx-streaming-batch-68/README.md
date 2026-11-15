# Music Assistant Server – MSX Bridge-strömning, batch 68

Datum: 2026-11-15

Tio MSX Bridge-inställningar för buffring, HTTP-server, ljudformat,
inaktivitetsmarkeringar, stoppmeddelanden och strömning till tv-apparater.

Terminologi: *shared buffer* återges som *delad buffert*, *reader* som
*läsare*, *idle timeout* som *tomgångstidsgräns* och *smart TV* som *smart
tv-apparat*. Tekniknamnen MSX, HTTP, ffmpeg, CPU, MA och Media Station X
bevaras.

Status: alla tio strängar uppdaterades via API och lästes tillbaka med samma
översättnings-ID. API-svaret bekräftade `is_untranslated: 0` för samtliga.
Denna arkivkopia har pushats till vårt arkiv; detta är inte en upstream-merge
eller ett upstream-godkännande.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är
inte tillämpligt på JSON-kataloger.

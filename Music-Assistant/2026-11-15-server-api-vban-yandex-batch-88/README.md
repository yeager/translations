# Music Assistant Server – VBAN och Yandex Music, batch 88

Datum: 2026-11-15

Tjugo konfigurations- och beskrivningstexter för VBAN-mottagaren samt Yandex
Musics inloggning med enhetskod.

Terminologi: *receiver* återges som *mottagare*, *sender* som *sändare*,
*sample rate* som *samplingsfrekvens*, *queue* som *kö* och *stream* som
*ström*. VBAN, PCM, UDP, IP, DEBUG, VERBOSE och ASCII bevaras som tekniska
namn.

Status: alla tjugo strängar uppdaterades via API och lästes tillbaka med samma
översättnings-ID. API-svaret bekräftade `is_untranslated: 0` för samtliga.
Denna arkivkopia har pushats till vårt arkiv; detta är inte en upstream-merge
eller ett upstream-godkännande.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är
inte tillämpligt på JSON-kataloger.

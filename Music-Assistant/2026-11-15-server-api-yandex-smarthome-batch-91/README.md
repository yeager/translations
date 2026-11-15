# Music Assistant Server – Yandex Music och Yandex Smart Home, batch 91

Datum: 2026-11-15

Tjugo texter för Yandex Music och Yandex Smart Home: molnanslutning,
autokonfiguration och direktanslutning.

Terminologi: *session token* återges som *sessionstoken*, *connection type*
som *anslutningstyp*, *device flow* som *enhetsflöde*, *cloud relay* som
*molnrelä* och *direct access token* som *direktåtkomsttoken*. OAuth, HTTPS,
URL, ID och fältnamn bevaras som tekniska identifierare.

Status: alla tjugo strängar uppdaterades via API och lästes tillbaka med samma
översättnings-ID. API-svaret bekräftade `is_untranslated: 0` för samtliga.
Denna arkivkopia har pushats till vårt arkiv; detta är inte en upstream-merge
eller ett upstream-godkännande.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är
inte tillämpligt på JSON-kataloger.

# Music Assistant Server – Tidal och VBAN, batch 87

Datum: 2026-11-15

Tjugo texter för Tidals PKCE-inloggning, session, token, kvalitetsval och en
VBAN-ljudinställning.

Terminologi: *authentication* återges som *autentisering*, *redirect URL* som
*omdirigerings-URL*, *refresh token* som *uppdateringstoken* och *streaming
quality* som *strömningskvalitet*. PKCE, Tidal.com, URL, FLAC och ”Page Not
Found” bevaras som tekniska eller synliga namn.

Status: alla tjugo strängar uppdaterades via API och lästes tillbaka med samma
översättnings-ID. API-svaret bekräftade `is_untranslated: 0` för samtliga.
Denna arkivkopia har pushats till vårt arkiv; detta är inte en upstream-merge
eller ett upstream-godkännande.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är
inte tillämpligt på JSON-kataloger.

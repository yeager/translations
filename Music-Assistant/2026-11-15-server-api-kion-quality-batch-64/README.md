# Music Assistant Server – KION Music, batch 64

Datum: 2026-11-15

Tio KION Music-inställningstexter för kodekval, spellistegränser,
ljudkvalitet och autentisering.

Terminologi: *codec* återges som *kodek*, *override* som *överstyrning* och
*virtual playlist* som *virtuell spellista*. Filformat, biträkning,
produktnamnet KION Music och spellistan My Mix behålls.

Status: alla tio strängar uppdaterades via API och lästes tillbaka med samma
översättnings-ID. API-svaret bekräftade `is_untranslated: 0` för samtliga.
Denna arkivkopia har pushats till vårt arkiv; detta är inte en upstream-merge
eller ett upstream-godkännande.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är
inte tillämpligt på JSON-kataloger.

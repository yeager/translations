# Music Assistant Server – NeteaseCloudMusic och leverantörer, batch 71

Datum: 2026-11-15

Tio texter om NeteaseCloudMusic-kvalitet och QR-inloggning samt
leverantörsbeskrivningar för NetEase Cloud Music, niconico, NTS Radio, nugs.net
och OpenSubsonic.

Terminologi: *lossless* återges som *förlustfri*, *QR login* som
*QR-inloggning* och *base URL* som *bas-URL*. Produkt- och tjänstenamn, även
NTS Radio, Infinite Mixtapes, JY Master och domänexemplet, bevaras.

Status: alla tio strängar uppdaterades via API och lästes tillbaka med samma
översättnings-ID. API-svaret bekräftade `is_untranslated: 0` för samtliga.
Denna arkivkopia har pushats till vårt arkiv; detta är inte en upstream-merge
eller ett upstream-godkännande.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är
inte tillämpligt på JSON-kataloger.

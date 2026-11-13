# elementary Settings Desktop, svensk avfuzzning

Datum: 13 november 2026

Den aktuella Weblate-katalogen har en enda svensk post som behöver redigeras.
Källtexten har bara fått ändrad versalisering, från `Accent Color` till
`accent color`. Den befintliga översättningen `Accentfärg` är rätt för
inställningsetiketten och överensstämmer med tidigare granskade elementary-
kataloger. Deltafilen tar därför bort fuzzy-markeringen utan att ändra
översättningens innebörd.

Kontroller: `msgfmt --check --check-format`, l10n-lint, svlang, Hunspell-SV,
diffkontroll och Gitleaks. `svlang` och Hunspell-SV godkänner själva
översättningen. Ingen import kunde göras eftersom Weblate-sessionen är
utloggad och den lokalt tillgängliga nyckelringen saknar en åtkomlig token för
`l10n.elementaryos.org`. Detta är lokal granskning och arkivering, inte ett
upstream-inskick eller en upstream-granskning.

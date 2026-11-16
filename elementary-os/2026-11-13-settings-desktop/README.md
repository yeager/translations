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
översättningen.

## Uppföljning 16 november 2026

En autentiserad Weblate-kontroll visar att Settings Desktop nu är 100 %
översatt (94 av 94 strängar) med 0 fuzzy-poster. Både den äldre och den nya
källtexten för accentfärg har den återlästa måltexten `Accentfärg`. Därmed
behövs ingen återuppladdning av den lokala enfilsdeltan. Detta bekräftar den
aktuella sparade Weblate-statusen, inte en separat programrelease.

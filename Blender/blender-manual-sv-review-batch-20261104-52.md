# Blender Manual: svensk granskningsbatch 52

Datum: 4 november 2026

Källa: `exports/2026-11-04/blender-manual-manual-sv.po` samt den officiella
manualen för Blender 5.3, *Asset Libraries*.

## Kontext och omfattning

Fjorton rubriker och hjälptexter för tillägg som gör fjärrresursbibliotek
tillgängliga i Blender. Manualen beskriver ett tillägg med ett manifest, ett
eventuellt åtkomsttokenflöde, byggning, publicering och drift av det externa
resursbiblioteket. Den lokala UI- och manualterminologin använder
**resursbibliotek**, **resursbläddrare** och **åtkomsttoken**; den följs
före den äldre, växlande formen *tillgångsbibliotek*.

`Library Access Token` och `Repository Access Token` avser två olika
autentiseringsflöden. De har därför fått tydliga sammansättningar i stället
för den ospecifika etiketten *Åtkomsttoken* på båda ställena.

*Remote asset library* skrivs **fjärranslutet resursbibliotek**, inte den
svårlästa sammansättningen *fjärrresursbibliotek* med tre `r` i följd.

## Kontroller

- `msgfmt --check --statistics`: 14 översatta meddelanden och godkänd syntax.
- Radvis jämförelse av `(msgctxt, msgid)` mot råexporten: 14/14 träffar.
- `l10n-lint --language sv`, `svlang skrivregler --enable-interpunktion`,
  `svlang svengelska` och Hunspell `sv_SE`: inga fel i måltexterna.
- `git diff --check` och Gitleaks: godkända, utan hemligheter.

Råexporten är orörd. Deltafilen är lokalt validerad men inte uppladdad till
Blender Translate.

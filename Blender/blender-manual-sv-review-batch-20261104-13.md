# Blender Manual: granskningsbatch 13 — USD-tillgänglighet per objekt

Datum: 2026-11-04  
Källa: `exports/2026-11-04/blender-manual-manual-sv.po`  
Omfattning: 7 ändrade poster i `files/import_export/usd.rst`.

Batchen kompletterar den föregående genomgången av USD-tillgänglighet med
information per objekt. Termerna *rotprim*, *datablock* och
*strängegenskap* följer samma tekniska register som den svenska Blender-UI:t.
Kodspecificerade egenskapsnamn, identifierare och tillåtna värden lämnas
oförändrade.

Validering före arkivering:

- `msgfmt --check`
- `l10n-lint` (inga fel eller varningar)
- `svlang skrivregler` (inga skrivregelfel)
- `hunspell-sv` (endast tekniska identifierare och RST-/USD-termer)
- `git diff --check`
- Gitleaks utan träffar

Status: lokalt granskad och arkiverad. Den räknas in i den framtida
manualbatchen om 500–1 000 strängar och är inte uppladdad separat.

# MihawkOS WebUI – svensk granskningsrapport

Granskad lokal ändring i `mihawk-99/PS5_MihawkOS`, arbetsgrenen
`l10n/swedish-setup`, 29 oktober 2026. Rapporten beskriver den lokalt
stagade WebUI-utökningen och ändrar inte dess källfiler.

## Omfattning

- `webui/i18n.js` lägger till `sv-SE` med Sveriges flagga och 307 svenska
  WebUI-strängar.
- `src/pw_webui.cpp` tillhandahåller flaggan som WebUI-resurs.
- `ps5/tools/link-title.sh` tar med flaggan i paketet för PS5.
- `src/pw_setup.c` innehåller den tillhörande språkregistreringen och den
  svenska installationsguiden.

## Verifiering

- `python3 tests/test_webui_i18n.py` godkänd: alla 11 språk innehåller exakt
  samtliga 307 aktuella WebUI-nycklar, med bevarade platshållare och
  tillgängliga flaggresurser.
- `node --check webui/i18n.js` godkänd.
- Riktat C++-test för WebUI godkänt: token, inställningar, bibliotek, väljare,
  maskerade loggar, sidfiler och avvisade vägar.
- Riktat `test_pw_setup` godkänt: 11 av 11 språk har komplett skrivbar text,
  platsmarkörer, sparad språkinställning och korrekta täckningssteg.
- `svlang skrivregler` är utan svenska skrivregelfel. Hunspell-SV:s återstående
  träffar är filformat, produktnamn och tekniska identifierare, exempelvis
  `PS5`, `DualSense`, `ShadowMountPlus` och `.zip`.
- `git diff --check` och Gitleaks för de stagade ändringarna är godkända.

## Begränsning

Den fullständiga värdtestsviten kan fortfarande inte startas i denna checkout,
eftersom den förväntar sig syskonkatalogen `PS5_Vulkan`. Den lokala
WebUI-kompileringen använder en tillåtande inställning enbart för två
deprecationsvarningar i tredjepartsfilen `external/tinygltf/json.hpp`; projektets
egen kod byggs fortsatt med `-Werror`.

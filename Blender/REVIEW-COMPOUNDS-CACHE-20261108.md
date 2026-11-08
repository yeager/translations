# Blender UI – sammansättningar och nedladdningscache

## Korrigeringar

- `Custom Shader Group Node` → `Anpassad shadergruppsnod`. `shader` är den
  etablerade formella Blender-termen; sammansättningen undviker samtidigt tre
  lika konsonanter.
- `Hit Color` → `Träffärg`, med svensk sammansättning utan tre f i följd.
- `Popover panel` → `Utfällbar panel`, en idiomatisk UI-beskrivning utan den
  svårlästa formen *poppupppanel*.
- `download cache directory of remote asset libraries` →
  `Cachekatalogen för nedladdning från fjärrbibliotek`; formuleringen följer
  den etablerade cachetermen och undviker *fjärrresursbibliotek* med tre r.
- `Remote Asset Library/Libraries` och `Remote Assets` →
  `fjärranslutet resursbibliotek`, `fjärranslutna resursbibliotek` respektive
  `fjärranslutna resurser`, enligt projektets terminologilista.
- `Clip Planes` → `Beskärningsplan`, och `wireframe mode` i löpande text →
  `läget trådmodell`; båda undviker trippelkonsonanter utan att förlora
  Blender-kontexten.

## Kontroller

`msgfmt --check`, l10n-lint, svlang, skrivregler och Gitleaks är godkända.
Den kompletterade batchen innehåller inga trippelkonsonanter.

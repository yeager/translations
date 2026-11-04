# Blender Manual: svensk granskningsbatch 38

Datum: 4 november 2026

Källa: `exports/2026-11-04/blender-manual-manual-sv.po`.

## Omfattning

Nio poster för Resursbiblioteks importmetoder har granskats:

- standardimportmetod och dess åsidosättning i Resursbläddraren;
- begränsningen för inbyggda respektive nätbaserade resursbibliotek;
- de faktiska Blender-operatörerna `Link` → *Länka* och `Append` →
  *Lägg till*;
- länkade resurser, skrivskydd och oberoende kopior.

API-målen `bpy.ops.wm.link`, `bpy.ops.wm.append` och
`bpy.types.FileAssetSelectParams.import_method` är bevarade bytekorrekt.

## Kontroller

- `msgfmt --check --statistics`: 9 översatta meddelanden, godkänd syntax.
- Radvis jämförelse av `(msgctxt, msgid)` mot råexporten: 9/9 träffar.
- Hunspell `sv_SE`: endast PO-huvudets fält och bevarade RST/API-identifierare.
- `git diff --check`: godkänd.
- Gitleaks: inga hemligheter hittades.

Råexporten är orörd. Deltafilen arkiveras för en senare samlad uppladdning.

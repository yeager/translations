# Blender Manual: svensk granskningsbatch 40

Datum: 4 november 2026

Källa: `exports/2026-11-04/blender-manual-manual-sv.po`.

## Omfattning

Tio poster för Resursbibliotek som följer med tillägg har granskats:

- kopplingen mellan tillägg, tilläggsförråd och fjärranslutna resursbibliotek;
- installation, avinstallation, aktivering och inaktivering;
- bibliotekets åtkomsttoken och den synliga Avancerad-inställningen.

Terminologin följer UI-katalogen: `Extensions` → *Tillägg*,
`Active Extension Repository` → *Aktivt tilläggsförråd*, `Access Token` →
*Åtkomsttoken* och `Advanced` → *Avancerad*. Alla RST-mål och
menymarkeringen är bevarade.

En efterkontroll den 5 november rättade två äldre avvikelser: *extension
repository* är genomgående *tilläggsförråd*, inte *tilläggsarkiv*, och
*remote asset library* är *fjärranslutet resursbibliotek*. Den senare formen
är både mer precis och undviker den svårlästa tre-r-kedjan i
*fjärrresursbibliotek*.

## Kontroller

- `msgfmt --check --statistics`: 10 översatta meddelanden, godkänd syntax.
- Radvis jämförelse av `(msgctxt, msgid)` mot råexporten: 10/10 träffar.
- Hunspell `sv_SE`: endast PO-huvudets fält och bevarade RST-identifierare.
- `git diff --check`: godkänd.
- Gitleaks: inga hemligheter hittades.

Råexporten är orörd. Deltafilen arkiveras för senare samlad uppladdning.

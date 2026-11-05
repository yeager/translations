# Blender Manual: svensk granskningsbatch 59

Datum: 5 november 2026

Källa: `exports/2026-11-04/blender-manual-manual-sv.po`, den aktuella
Node Wrangler-koden och Blenders svenska UI-katalog.

## Kontext och omfattning

Elva poster för Node Wranglers texturinställning och länkning av aktiva noder.
Operatornamnen följer den aktuella UI-katalogen: **Lägg till
texturinställning**, **Lägg till principiell texturinställning**, **Länka
aktiv till markerade**, **Använd nodnamn/etikett** och **Använd
utdata-namn**.

Nodnamnen är kontrollerade i UI-katalogen: `Texture Coordinate` →
**Texturkoordinater**, `Mapping` → **Kartläggning**, `Environment Texture` →
**Miljötextur**, `Principled BSDF` → **Principiell BSDF**, `Image Texture` →
**Bildtextur** och `Color Space` → **Färgrymd**. `Principled` behålls i den
synliga snabbmenyetiketten eftersom den är en etablerad Blender-beteckning,
men översätts till *principiell* när uttrycket beskriver inställningen i
löpande text.

## Kontroller

- `msgfmt --check --statistics`: 11 översatta meddelanden och godkänd syntax.
- Radvis jämförelse av `(msgctxt, msgid)` mot råexporten: 11/11 träffar.
- UI-katalogen och översättningsminnet har kontrollerats för samtliga
  operatörs- och nodnamn i batchen.
- l10n-lint, svlang, Hunspell, `git diff --check` och Gitleaks körs före
  arkivering.

Råexporten är orörd. Deltafilen är en lokal kandidat och är inte uppladdad
till Blender Translate.

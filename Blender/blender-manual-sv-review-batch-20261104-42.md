# Blender Manual: svensk granskningsbatch 42

Datum: 4 november 2026

Källa: `exports/2026-11-04/blender-manual-manual-sv.po`.

## Omfattning

Tjugotre poster från Curve Data, delade mellan den nya kurvmodelleringen och
Grease Pencil. Granskningen omfattar den synliga sidopanelens Kurvdata samt
NURBS-splinens cykliska läge, knutläge, ordning och upplösning.

UI-termerna har kontrollerats mot Blender-katalogen: `Curve Data` →
*Kurvdata*, `Cyclic` → *Cyklisk*, `Knot Mode` → *Knutläge*, `Endpoint` →
*Slutpunkt* och `Resolution` → *Upplösning*. Den matematiska facktermen
*ordning* används konsekvent för NURBS-kurvans *order*. `NURBS`, `Bézier`
och `Catmull Rom` bevaras som etablerade namn. RST-markeringar och
menystrukturen är oförändrade.

En efterkontroll mot UI-exporten den 5 november bekräftade `Cyklisk` som den
faktiska etiketten. I den löpande meningen skrivs därför *alternativet
Cyklisk* för att uttrycket ska bli grammatiskt korrekt på svenska.

NURBS-källans *endpoint clamping* kontrollerades även mot fackbeskrivningen:
inställningen gör att kurvan går genom den första och sista kontrollpunkten.
Den svenska förklaringen använder därför *slutpunktsinterpolation* i stället
för den missvisande allmänformen *begränsning vid slutpunkterna*.

Den tidigare svenska texten i råexporten innehåller flera felkopplade eller
ofullständiga måltexter för dessa nycklar. Detta är därför en kontextstyrd
ersättningsbatch, inte en mekanisk fyllning av tomma strängar.

## Kontroller

- `msgfmt --check --statistics`: 23 översatta meddelanden och godkänd syntax.
- Radvis jämförelse av `(msgctxt, msgid)` mot råexporten: 23/23 träffar.
- `l10n-lint --language sv`: inga träffar.
- `svlang skrivregler --enable-interpunktion` och `svlang svengelska`: inga
  träffar i de svenska måltexterna.
- Hunspell `sv_SE`: endast avsiktliga fack- och produkttermer samt
  RST-roller (`NURBS`, `Bézier`, `Catmull Rom`, `:guilabel:` och
  `:menuselection:`) träffade.
- `git diff --check`: godkänd.
- Gitleaks: inga hemligheter hittades.

Råexporten är orörd. Deltafilen arkiveras för senare samlad uppladdning till
den generiska Manual-komponenten.

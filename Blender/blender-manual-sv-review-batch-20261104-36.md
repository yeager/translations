# Blender Manual: svensk granskningsbatch 36

Datum: 4 november 2026

Källa: `exports/2026-11-04/blender-manual-manual-sv.po`.

## Omfattning

13 poster i Graph Editors kanalregion har granskats och korrigerats:

- kanalregionens beskrivning och färgkategorier;
- ikonetiketter för fästning, döljning, modifierare och låsning;
- nyckelrutor, NLA-redigeraren och skjutreglage.

Kontroll mot UI-katalogen bekräftar bland annat `Graph Editor` →
*Grafredigerare*, `Dope Sheet` → *Dopeblad*, `Pin` → *Fäst*, `Hide` →
*Dölj* och `Show Sliders` → *Visa skjutreglage*. RST-roller,
`bl-icon`-identifierare, tangentsekvenser och menystruktur är bevarade.

## Kontroller

- `msgfmt --check --statistics`: 13 översatta meddelanden, godkänd syntax.
- Radvis jämförelse av `(msgctxt, msgid)` mot råexporten: 13/13 träffar.
- Hunspell `sv_SE`: endast PO-huvudets fält, RST-roller, ikonidentifierare,
  `Ctrl-LMB`, `Tab` och projekttermer som *Dopebladet* och
  *NLA-redigeraren*.
- `git diff --check`: godkänd.
- Gitleaks: inga hemligheter hittades.

Råexporten har inte ändrats. Deltafilen är arkiverad för en senare samlad
uppladdning.

# Blender UI – Action-datatypens konsekvens, 2026-11-08

## Kontext

Blenders **Action** är namnet på en formell datatyp för animeringsdata, inte
det vanliga svenska substantivet *åtgärd*. I Action Editor, NLA, F-kurvor och
motionsbanor ska därför UI-texten behålla *Action* och böja det som ett svenskt
utrumord: *Actionen*, *Actioner* och *Action-slotten*.

Denna riktade uppföljning korrigerar en äldre granskningsbatch där ett fåtal
förekomster hade översatts som *åtgärd*. Termvalet följer
`TERMINOLOGY.md` och Blender-katalogens etablerade användning av
*Action-datablock*, *Action-slot* och *Actioner*.

## Ändrade poster

| Engelska | Svenska |
| --- | --- |
| The individual F-Curves that animate the slot | De enskilda F-kurvorna som animerar Action-slotten |
| A number that identifies which sub-set of the Action is considered to be for this data-block | Ett nummer som identifierar vilken delmängd av Actionen som anses vara för detta datablock |
| For bone motion paths, search whole Action for keyframes instead of in group with matching name only (is slower) | För rörelsebanor för ben söker du efter nyckelbildrutor i hela Actionen i stället för endast i en grupp med matchande namn (går långsammare) |
| Removed {:d} empty and/or fake-user only Actions | Tog bort {:d} tomma Actioner och/eller Actioner med endast falsk användare |

## Kontroller

- `msgfmt --check`: godkänd.
- `l10n-lint`: inga problem.
- `svlang consistency`, `svlang skrivregler` och `svlang svengelska`: godkända.
- `hunspell-sv`: *Actionen* och *Actioner* markeras eftersom de är böjningar
  av Blenders egennamn; de är medvetna katalogtermer enligt terminologin.
- `gitleaks`: inga hemligheter hittades.

## Avgränsning

Detta är en lokal deltafil för manuell import. Den styrker inte att ändringarna
har importerats eller granskats i Blender Translate.

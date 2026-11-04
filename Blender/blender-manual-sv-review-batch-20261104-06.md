# Blender Manual: svensk granskningsbatch 6

Datum: 2026-11-04  
Källa: aktuell export av `manual-sv.po`.  
Omfattning: 15 fuzzy-poster i glTF-import, export och animeringsalternativ.

Batchen rättar missvisande eller oidiomatisk svensk text i exportdialogens
dokumentation. Särskilt kontrollerade termer:

- *Sparse Accessor* → *gles accessor*, i enlighet med den aktuella svenska
  Blender UI-katalogen.
- *joint vertex influences* → *leders hörnpunktsinflytanden*, samma etablerade
  UI-term som `export_all_influences`.
- *Meshopt*, *Draco*, *TRS*, *LINEAR* och *STEP/CONSTANT* behålls som
  produkt-/formatnamn respektive enumvärden.
- *Shape Keys* → *formnycklar* och *Animation Pointer* → *animationspekare*,
  i enlighet med Blenders svenska UI.

Kontroller: `msgfmt`, `l10n-lint` (0 fel, 0 varningar), `svlang`
skrivregler, Hunspell, kontroll mot Blender UI och termbanken,
`git diff --check` samt Gitleaks. `svlang check` ger bara heuristiska
naturlighetsnotiser för tekniska UI-fragment; texten är manuellt granskad i
sin dokumentations- och gränssnittskontext.

Råexporten ändras inte. Deltafilen ingår i den kommande samlade
manualuppladdningen på 500–1 000 granskade strängar.

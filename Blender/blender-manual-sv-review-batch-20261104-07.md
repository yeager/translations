# Blender Manual: svensk granskningsbatch 7

Datum: 2026-11-04  
Källa: aktuell export av `manual-sv.po`.  
Omfattning: 6 återstående fuzzy- eller tomma poster i glTF-avsnittet.

Batchen avslutar den öppna glTF-del som inte redan täcks av batch 1–6:
menysökväg, punktljus, Meshopt och Animation Pointer. Blender UI:s aktuella
översättning används där den motsvarar dokumentationens etikett:
`Punctual Lights` → `Punktljus`, `Meshopt Extension` → `Meshopt-tillägg`
och `Animation Pointer` → `animationspekare`. De registrerade
komprimeringsidentifierarna behålls exakt.

Kontroller: `msgfmt`, `l10n-lint` (0 fel, 0 varningar), `svlang`
skrivregler, Hunspell, termbank/TM, `git diff --check` och Gitleaks.
`svlang check` noterar tekniska identifierare och korta UI-fragment men inga
språkliga fel efter manuell granskning.

Råexporten ändras inte. Deltafilen ingår i den kommande samlade
manualuppladdningen på 500–1 000 granskade strängar.

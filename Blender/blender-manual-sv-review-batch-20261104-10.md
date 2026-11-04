# Blender Manual: svensk granskningsbatch 10

Datum: 2026-11-04  
Källa: aktuell export av `manual-sv.po`.  
Omfattning: 12 fuzzy- eller tomma poster i den äldre FBX-importen/exporten.

Batchen rättar bland annat en direkt felaktig USD-hänvisning i en
FBX-sträng, trasiga menyer och saknade förklaringar av äldre exportval.
Kontroll mot Blender UI bekräftar `Importera FBX`, `Exportera FBX`,
`skinning` och formatnamnet FBX. RST-referenser, flaggor och filformat
bevaras.

Kontroller: `msgfmt`, `l10n-lint` (0 fel, 0 varningar), `svlang`
skrivregler, Hunspell, Blender UI/terminologi, `git diff --check` och
Gitleaks. Övriga `svlang check`-notiser gäller tekniska namn och korta
gränssnittstexter och är manuellt bedömda.

Råexporten ändras inte. Deltafilen ingår i den kommande samlade
manualuppladdningen på 500–1 000 granskade strängar.

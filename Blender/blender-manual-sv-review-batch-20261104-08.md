# Blender Manual: svensk granskningsbatch 8

Datum: 2026-11-04  
Källa: aktuell export av `manual-sv.po`.  
Omfattning: 17 poster i Blenders ordlista.

Satsen rättar och kompletterar begreppen kring åtgärder, tillgångsbibliotek,
färgrymder och armaturers vilopos. Särskilt viktiga beslut:

- `Primaries` → `Primärfärger`; den tidigare måltexten `Primärval` var
  semantiskt fel i färghanteringskontext.
- `Color Space`, `White Point`, `transfer function` och sRGB-texterna använder
  färgrymd, vitpunkt och överföringsfunktion konsekvent.
- Aktuella Blender UI-termer används för `formnycklar`, `åtgärder`,
  `tillgångsbibliotek` och `vilopos`.
- RST:s referensmål bevaras. Där linter inte kan tolka lokaliserad text i en
  `:term:`-roll står den svenska termen i löptexten och den tekniska
  referensen lämnas oförändrad.

Kontroller: `msgfmt`, `l10n-lint` (0 fel, 0 varningar), `svlang`
skrivregler, Hunspell, Blender UI/terminologi, `git diff --check` och
Gitleaks. Informationsnotiser från `svlang check` gäller tekniska
identifierare och RST-markup; varje text har granskats manuellt.

Råexporten ändras inte. Deltafilen ingår i den kommande samlade
manualuppladdningen på 500–1 000 granskade strängar.

# Dwarf Fortress 50.* `lua`: batch 1

15 november 2026. Materialorden `metal` och `silk` har granskats i den konkreta Lua-kontexten som väljer mellan materialen. De svenska måltexterna är `metall` respektive `siden`.

Båda strängarna sparades i Transifex och lästes sedan tillbaka genom omladdning. Räknaren för oöversatta strängar i resursen minskade från 1 774 till 1 772. Status: inskickat och verifierat i Transifex, men inte projektgranskat eller publicerat i en utgåva.

Kontroller: JSON-validering, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks. `msgfmt` är inte tillämpligt på Transifex JSON-deltat.

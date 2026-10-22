# Kontroll av Rust Coreutils, 2026-10-22

Kontrollen täcker de 100 komponenter som har svenska Fluent-kandidater i den här katalogen. För varje komponent har den aktuella engelska `en-US.ftl`-filen från uutils jämförts med den senaste svenska kandidatfilen med samma komponentnamn.

Resultat:

- `moz-fluent-lint`: godkänd för samtliga 100 komponenter
- Gitleaks: inga hemligheter hittades i `Rust-Coreutils`

Filer i kataloger med namnet `pending-*` är granskade och kontrollerade, men väntar fortfarande på uppladdning till Hosted Weblate. De får inte räknas som uppladdade innan Weblate har bekräftat importen.

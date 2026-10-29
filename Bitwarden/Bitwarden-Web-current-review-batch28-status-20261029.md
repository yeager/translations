# Bitwarden Web: häfte 28 är föråldrat

Kontrollerat den 29 oktober 2026 mot den lokala, nyare katalogen i
`bitwarden/clients` vid commit `6d2e3a182c257d8078e1bc1c1e99cd340ddc5a27`.

`Bitwarden-Web-current-review-batch28.xliff` innehåller bara tre poster:
`of`, `any` och `sendControls`. Filen är XML-giltig och passerar l10n-lint,
svlang-skrivregler, Hunspell-sv med en förväntad produktnamnsträff samt
Gitleaks.

Häftet ska ändå **inte** skickas till Crowdin:

- `sendControls` är redan `Send-kontroller` i den nyare katalogen. `Send` är
  Bitwardens produktnamn och ska inte översättas.
- `of` är redan `av`.
- `any` är i den nyare katalogen `Alla`. Det äldre förslaget `Valfri` saknar
  sammanhang och kan vara fel böjningsform i ett filter eller val.

Filen behålls som historiskt granskningsunderlag, men är inte ett
uppladdningsunderlag. En eventuell Crowdin-åtgärd ska utgå från den aktuella
valda måltexten, inte från detta häfte.

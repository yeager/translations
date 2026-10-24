# MATE, öppna komponenter, 24 oktober 2026

70 öppna komponenter exporterades från Fedora Weblate och kontrollerades lokalt.

- 23 949 aktiva strängar
- 23 949 översatta strängar
- 0 fuzzy-markeringar
- 0 `msgfmt`-fel
- 0 l10n-lint-fel
- 0 Gitleaks-fynd

26 konkreta svenska korrigeringar gjordes i 13 komponenter: kommatecken före `och` togs bort och den dubblerade frasen `antalet antalet` i Caja rättades.

De tre låsta komponenterna lämnades orörda: `mate-control-center`, `mate-control-center-help` och `mate-terminal`. Fedora Weblate gav HTTP 502 när en ny export skulle hämtas inför uppladdning, så dessa granskade filer har inte skickats upp i detta steg.

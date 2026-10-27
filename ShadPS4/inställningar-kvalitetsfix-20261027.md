# ShadPS4: lokala inställningsrättelser, 2026-10-27

`shadps4-qtlauncher-settings-kvalitetsfix-20261027.delta.ts` innehåller två
unika, manuellt granskade förbättringar för `SettingsDialog`:

* **Collect Shaders** får korrekt svensk meningsbyggnad, ett bevarat kortkommando
  och avslutande punkt.
* **Host Debug Markers** ersätter ordagrann och otydlig engelskpåverkad text med
  svensk fackprosa. Produktnamn, API-namn och funktionsnamn lämnas orörda.

Följande närliggande strängar fanns redan som separata Crowdin-förslag i
arkivet och dupliceras därför inte: *Add a folder to the list*, *Copy GPU
Buffers* och *Volume*.

## Lokal kontroll

XML-syntaxkontroll, `l10n-lint` (0 fel, 0 varningar), `svlang` och Gitleaks
passerar. Hunspell träffar endast `AMDGPU-kommandon`, `F10`, `RenderDoc`,
`emulatorinformation` och `shaders`; de är facktermer, produktnamn eller
accepterade sammansättningar i detta sammanhang. Detta är en lokal, ej
uppladdad deltafil; jämför alltid med aktuell målsträng i Crowdin innan den
skickas in.

Kontrollen kördes på nytt 2026-10-27 med samma resultat: XML är välformat,
`l10n-lint` rapporterar 0 fel och 0 varningar, `svlang` hittar inga
anglicismer och Gitleaks hittar inga hemligheter.

# Open Shaders: VR, slutsträngar, häfte 101

Detta delta omfattar de tio sista tidigare oarkiverade strängarna i
VR-funktionen. Källtexterna har jämförts med Open Shaders `dev` vid revision
`c1b1ef1` den 27 oktober 2026.

*Stereo blend* blir *stereoblandning* och *stereo reprojection* blir
*stereoomprojicering*. Förkortningarna SSGI, SSR, VR och GPU, numeriska värden
och radbrytningar bevaras. Deltafilen får importeras först efter upplåsning
och jämförelse med Hosted Weblates aktuella export.

## Kontroll

JSON-syntax, nyckeljämförelse, `l10n-lint`, svensk språkgranskning,
Hunspell-genomgång, Gitleaks och Git-whitespacekontroll har körts.
`svlang` ger en felaktig V2-varning för den tekniska satsen som beskriver
delning av skuggning mellan ögonen. Hunspell markerar endast förkortningar och
tekniska fackord. En arkivjämförelse bekräftar att samtliga 58
`feature.vr`-nycklar är täckta.

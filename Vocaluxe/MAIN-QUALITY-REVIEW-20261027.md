# Vocaluxe: lokal huvudfilsgranskning 2026-10-27

Den fullständiga svenska huvudfilen `sv-huvudfil-utkast-20261026.xml` har 403
nycklar och matchar den engelska utvecklingsfilens nyckelmängd. Den äldre
svenska upstreamfilen i arkivet har 304 nycklar, vilket förklarar varför den
tidigare kompletteringen innehöll 99 nya strängar.

Den lilla filen `sv-huvudfil-kvalitetsfix-20261027.delta.xml` innehåller sju
ytterligare språk- och kvalitetsrättningar:

- texturkvaliteternas `Lågt`, `Mellan` och `Högt` blir `Låg`, `Medel` och
  `Hög`;
- anglifieringen `Tagger` blir `Etiketter` i tre relevanta användartexter;
- `Tillagd datum` blir det etablerade `Datum tillagt`;
- förkortningen `t ex.` i sökhjälpen blir `t.ex.`.

Källnycklar och platshållare har jämförts per deltaenhet. `xmllint`,
l10n-lint, svlang och Gitleaks passerar utan fel eller varningar. Hunspell-sv
markerar endast sökprefixen `fi` och `fo` samt sammansättningen `mappnamn` i
hjälptexten; de behålls av funktionsskäl. Deltat är inte uppladdat till
Transifex och ingen visning i spelet har verifierats.

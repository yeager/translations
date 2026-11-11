# VirtualBox, svensk granskning 2026-11-11

## Källa och avgränsning

- Officiell källgren: `VirtualBox/virtualbox` `main`, revision
  `b6bea72111fcff48f31c57c9f66365b1d3301bb9` (20 oktober 2026).
- Granskningsunderlag: den öppna PR:n [#848](https://github.com/VirtualBox/virtualbox/pull/848),
  ursprunglig huvudrevision `7b2f494a0b0301f6f85423d1f4d4abc30222c5df`.
- Senaste stabila utgåva enligt projektets nedladdningssida är 7.2.22 och
  ligger väl inom 48 månader.

## Källkontroll

`lupdate` kördes mot hela `src/VBox/Frontends/VirtualBox` i PR-huvudet.
Den fann 3 589 källsträngar, exakt lika många som i PR:ns `VirtualBox_sv.ts`.
Den versionerade mallen `VirtualBox_xx_YY.ts` innehåller däremot 3 458
strängar och är alltså 131 strängar efter den aktuella koden. Det är en
källunderhållsbrist i mallen, inte ett bortfall i PR:ns svenska katalog.

PR #848 innehåller dessutom en separat rättning av macOS-paketeringen: även
`VirtualBoxVM.app` får `.lproj`-kataloger. Utan dem lokaliseras inte
hjälpprogrammets programmeny trots att TS- och QM-filerna finns.

## Status

- Batch 001–011 omfattar radvis granskning av angivna gränssnittsområden,
  bland annat start, maskinåtgärder, nätverk, lagring, media, loggar,
  guider och uppdateringsinställningar. De sammanlagda ändringarna är
  inskickade i PR #848.
- Den tekniska helkontrollen av katalogen är klar: 3 589 aktiva strängar,
  giltig XML och en kompilerbar QM-fil.
- **Den manuella radvisa granskningen av samtliga 3 589 strängar är inte
  klar.** Den fortsätter från den aktuella PR-katalogen i avgränsade,
  dokumenterade batcher. Tidigare formulering om en fullständig
  slutgranskning har korrigerats.
- 2026-11-11, batch 013: alla 281 aktiva meddelanden i `UICommon` har
  granskats radvis. Ändringarna är verifierade lokalt och ännu inte pushade
  till PR:n.
- 2026-11-11, batch 014: alla 102 aktiva meddelanden i `UIDetails` har
  granskats radvis. Ändringarna är verifierade lokalt och ännu inte pushade
  till PR:n.
- PR #848 uppdaterades 2026-11-11 till huvudrevision
  `f11f1d7cb7cd85ced4377bb8d3b329d68b30fa36` med samtliga tio
  granskningscommitar. GitHub har bekräftat mottagandet.
- Commithistoriken rättades därefter till `po@danielnylander.se` utan att
  kataloginnehållet ändrades. `oca/oracle` är godkänd för den aktuella
  huvudrevisionen.
- PR:n är öppen och ännu inte granskad eller mergad.
- Råfilerna i `../VirtualBox/` är historiska och har inte skrivits över.

## Kontroller för batch 001

- `lupdate`: 3 589 aktuella källsträngar.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `l10n-lint` med `lupdate`-mallen som referens: inga verkliga fel efter
  granskningen. Två tomma `--`-värden är avsiktliga språkmetadata.
- `git diff --check`: godkänd.
- `svlang consistency`: godkänd.
- `hunspell-sv`: granskad manuellt; återstående träffar är produktnamn,
  kommandon, format och tekniska identifierare.
- `gitleaks detect --no-git --redact`: inga läckta hemligheter.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är formatets motsvarande
  kompileringskontroll.

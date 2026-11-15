# Godot Editor, svensk granskningsstatus 2026-11-15

- Projekt: Godot Engine Editor, komponenten `godot`, språk `sv` på Hosted
  Weblate.
- Releasekontroll: Godot `4.7.2-stable`, publicerad 2026-08-18.
- Live-status före och efter den här ändringen: 6 577 översatta strängar,
  100 %, utan luddiga strängar.
- Senaste översättare i den nedladdade katalogens metadata före ändringen:
  Lasse Edsvik, 2026-11-05.

## Riktad kontroll

Den kompletta svenska PO-katalogen innehåller 6 255 översatta meddelanden.
`msgfmt` passerade. svlang och Gitleaks passerade utan träffar. Hunspell-sv
markerade endast produkt- och formatnamnen `Godot`, `glTF` och `FBX` i den
granskade texten.

l10n-lint hittade en verklig radbrytningsavvikelse i importdialogen för
3D-modeller: källtexten har explicita radbrytningar före `dialog` och före
slutraden, men den svenska måltexten hade slagit ihop dem. Övriga rapporterade
träffar i den riktade kontrollen var informations- eller stilvarningar och
utgjorde inte underlag för en säker massändring.

## Inskick

En enda översättning uppdaterades via Hosted Weblate API:

- enhet `174656555`, importdialogen för en 3D-modell.

Ändringen lästes tillbaka från API:t. Den är översatt men inte godkänd
(`state 20`) och väntar på projektets vanliga gransknings- och synkflöde.
Det är en upstream-inskickning, inte en merge eller en utgåva.

# Blender Manual: svensk granskningsbatch 49

Datum: 4 november 2026

Källa: `exports/2026-11-04/blender-manual-manual-sv.po`.

## Omfattning

Nio poster för menynavigering och cirkelmenyer i Inställningar › Gränssnitt.
Den svenska UI-exporten har använts som kontextkälla: `Pie Menus` →
*Cirkelmenyer*, `Animation Timeout` → *Animationstidsgräns*, `Tap Key
Timeout` → *Tidsgräns för tangenttryckning* och `Recenter Timeout` →
*Tidsgräns för återcentrering*.

Terminologin har uppdaterats med *cirkelmeny* och *tidsgräns*. Den mer
generella formen *pajmeny* förekommer i äldre, andra UI-kontexter men används
inte för just dessa inställningsetiketter, där den aktuella UI-katalogen är
den starkare källan.

## Kontroller

- `msgfmt --check --statistics`: 9 översatta meddelanden och godkänd syntax.
- Radvis jämförelse av `(msgctxt, msgid)` mot råexporten: 9/9 träffar.
- `l10n-lint --language sv`: 0 fel och varningar. Två informationsnotiser om
  `1/100ths` är falska positiva: den svenska formen *hundradels sekunder*
  återger samma mängd utan en sifferliteral.
- `svlang skrivregler --enable-interpunktion` och `svlang svengelska`: inga
  träffar i måltexterna.
- Hunspell `sv_SE` noterar endast *muspositionen*. Det är en korrekt svensk
  sammansättning men saknas i den lokala ordlistan.
- `git diff --check`: godkänd.
- Gitleaks: inga hemligheter hittades.

Råexporten är orörd. Deltafilen ingår i nästa körning av generatorn för
Weblate-batcher med högst 100 poster per fil.

## Terminologisk efterkontroll 5 november

UI-exporten bekräftar **Öppna vid hovring**, **Cirkelmenyer**,
**Animationstidsgräns**, **Tidsgräns för tangenttryckning** och
**Tidsgräns för återcentrering**. Måttenheten har rättats från den felaktiga
formen *hundradels sekunder* till **hundradelar av en sekund** i båda
hjälptexterna.

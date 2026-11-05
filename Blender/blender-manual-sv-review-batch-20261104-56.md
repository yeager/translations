# Blender Manual: svensk granskningsbatch 56

Datum: 5 november 2026

Källa: `exports/2026-11-04/blender-manual-manual-sv.po` och den aktuella
Node Wrangler-koden i Blender.

## Kontext och omfattning

Tolv poster i Node Wranglers meny för att sammanfoga noder och i dess
kortkommandon för blandningsfaktorn. Källkoden och den svenska UI-katalogen
visar att menyetiketterna är **Använd blandningsnoder** och **Använd
matematiska noder**. De formerna används därför även i manualens synliga
menyvägar, medan produktnamnet `Node Wrangler` lämnas oförändrat.

Den aritmetiska åtgärden `Divide` i Node Wranglers nodkontext heter
**Dividera** i UI-katalogen, inte det allmänna *Dela upp*. `Factor` är en
synlig inställning, inte en kodidentifierare, och återges konsekvent som
**faktor** eller **blandningsfaktor**. Tangentidentifierarna i RST-markeringen
är funktionella värden och behålls exakt som i källan.

## Kontroller

- `msgfmt --check --statistics`: 12 översatta meddelanden och godkänd syntax.
- Radvis jämförelse av `(msgctxt, msgid)` mot råexporten: 12/12 träffar.
- UI-katalogens rader för Node Wrangler har kontrollerats för `Use Mix Nodes`,
  `Use Math Nodes`, `Merge Selected Nodes` och nodoperationen `Divide`.
- l10n-lint, svlang, Hunspell, översättningsminne, `git diff --check` och
  Gitleaks körs före arkivering.

Råexporten är orörd. Deltafilen är en lokal kandidat och är inte uppladdad
till Blender Translate.

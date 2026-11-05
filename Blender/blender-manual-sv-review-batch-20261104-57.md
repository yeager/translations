# Blender Manual: svensk granskningsbatch 57

Datum: 5 november 2026

Källa: `exports/2026-11-04/blender-manual-manual-sv.po`, den aktuella
Node Wrangler-koden och Blenders svenska UI-katalog.

## Kontext och omfattning

Sju poster i Node Wranglers alternativ för att sammanfoga noder och
batchändra deras operationer. `Alpha Over` heter **Alfa över** som
Blender-nod och den konkreta nodtypen blir därför **Alfa över-nod**. I
Node Wranglers meny är den aktuella UI-etiketten **Använd alfa-över-noder**.

`Batch Change` används både som en menyetikett och som en åtgärd. Därför
används substantivet **Batchändring** i menyvägen och verbformen
**Batchändra** i rubriken som beskriver åtgärden. Matematikoperationen
`Divide` följer den UI-belägga formen **Dividera**.

## Kontroller

- `msgfmt --check --statistics`: 7 översatta meddelanden och godkänd syntax.
- Radvis jämförelse av `(msgctxt, msgid)` mot råexporten: 7/7 träffar.
- UI-katalogen har kontrollerats för `Alpha Over`, `Use Alpha Over Nodes`,
  `Batch Change`, `Batch Change Blend Type`, `Batch Change Math Operation`
  och nodoperationen `Divide`.
- l10n-lint, svlang, Hunspell, översättningsminne, `git diff --check` och
  Gitleaks körs före arkivering.

Råexporten är orörd. Deltafilen är en lokal kandidat och är inte uppladdad
till Blender Translate.

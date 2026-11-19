# Sparade ändringar – 2026-11-19 (granskning 12001–12120)

Tre förslag matchade fortfarande exakt både aktuell engelsk källtext och tidigare svensk översättning. De sparades via Lokalise API och lästes tillbaka. Åtta andra förslag hade redan en annan aktuell svensk text och lämnades därför orörda.

## `component::vizio::config::abort::unique_id_mismatch`

**Engelska:** Please ensure you reconfigure against the same device.

**Befintlig svenska:** Kontrollera att du konfigurerar om mot samma enhet.

**Sparad svenska:** Kontrollera att du konfigurerar om samma enhet.

**Motivering:** Tar bort den onödiga prepositionen och gör uppmaningen idiomatisk.

## `component::midea::entity::sensor::variable_mode::state::freeze_warm`

**Engelska:** Freeze / warm

**Befintlig svenska:** Frys varm

**Sparad svenska:** Frysning / uppvärmning

**Motivering:** Återger båda lägena som tydliga substantiv och behåller snedstrecket från källtexten.

## `component::midea::entity::sensor::mode::state::hot_spring_egg`

**Engelska:** Hot spring egg

**Befintlig svenska:** Varmt vårägg

**Sparad svenska:** Onsenägg

**Motivering:** Vedertagen svensk benämning på ägg som tillagas vid låg temperatur enligt onsenmetoden.

Kontroll: hunspell-sv hade endast produktnamn och *Onsenägg* som okända ord. sv-lang flaggade produktnamn samt falska positiva V2-varningar. Inga platshållare eller referenser förekommer i de sparade strängarna.

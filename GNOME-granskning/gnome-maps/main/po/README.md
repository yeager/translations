# GNOME Maps — main — svenska UI

- **GNOME-aktivitet:** <https://l10n.gnome.org/vertimus/gnome-maps/main/po/sv/>
- **Källunderlag:** senaste POT från Damned Lies, skapad 2026-11-24 08:49+0000; sha256 `3c32757ef658f156b0cbf089a9ba3802dd692d0dd4ea79b494d3602cf1b3ef31`.
- **Statistik före granskning:** 535 översatta, 7 fuzzy, 16 oöversatta av 558.
- **Slutlig lokal status:** 558/558 översatta, 0 fuzzy och 0 oöversatta.
- **Ändringar:** 16 nya översättningar, 7 fuzzy-strängar omarbetade och 89 befintliga översättningar rättade; 112 aktiva PO-poster ändrade totalt.
- **Validering:** `msgcmp` mot senaste POT och `msgfmt --check --check-format` godkända. Platshållare och acceleratorantal matchar; inga nordiska acceleratorer används. En radbrytningsskillnad i `translator-credits` är avsiktlig eftersom källan är specialmarkören och målet innehåller översättarlistan. `l10n-lint`: 0 fel och 2 varningar för korrekt svensk gemenform `fm`/`em`. Hunspell med `sv_SE` kördes på alla mål; okända egennamn, tekniska termer och acceleratorfragment dokumenteras i `hunspell-exceptions.md`.
- **TM-stöd:** GNOME TM användes för att kontrollera bland annat `Timezone` → `Tidszon`, `Current timezone` → `Aktuell tidszon`, `Map color scheme` → `Kartans färgschema` och `Plus Code` → `Plus Code`. Tidigare dåliga träffar rättades där sammanhanget visade att de var fel, exempelvis `Light` → `Ljust` (inte `Flyg`) och `Imperial` → `Brittiskt`.
- **Inskickning:** ingen. Den här granskningen är lokal; inget har skickats till Damned Lies.
- **Översättarmetadata:** Daniel Nylander <gnome@danielnylander.se>, 2026-11-27 12:00+0100.

## A11y-terminologi, 2026-11-28

`Accessibility` ändrades från *Åtkomlighet* till *Hjälpmedel*. Den aktuella POT-filen har 561 poster. Aktuell nedladdad PO: 527 översatta, 8 fuzzy och 26 tomma; aktivitetsidan visar 535/8/18. l10n-lint: 0 fel/varningar; Hunspell: inga anmärkningar. Katalogen är ofullständig mot senaste POT, därför kördes inte `msgfmt`. Ändringen skickades inte till GNOME. Se `gnome-maps-main-a11y-terminology-2026-11-28.diff`.

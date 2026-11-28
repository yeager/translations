# Swedish TM-kontroll

GNOME-delen av `swedish-tm` konsulterades med exakta källsträngar. Flera äldre träffar var användbara som termstöd; varje sträng kontrollerades mot terminalinställningarnas sammanhang. Exempel på använda eller bedömda träffar:

- `By default, when doing word-wise selection…` hade en TM-träff som användes efter kontextgranskning och omskrivning till naturlig svenska.
- `Enter new shortcut to change <b>%s</b>.` → `Ange en ny genväg för att ändra <b>%s</b>.` bevarar markup och `%s`.
- `Search Options` → `Sökalternativ`, `Show Open Tabs` → `Visa öppna flikar`, `Select Font` → `Välj typsnitt`.
- `Delete Key` → `Delete-tangent` och `Backspace Key` → `Backstegstangent` skiljer den namngivna Delete-tangenten från svensk tangentfunktion.
- De felaktiga fuzzy-URL:erna ersattes med respektive exakt käll-URL, inte med TM-förslag.

Den här granskade katalogen importeras till GNOME-TM efter validering, och exakta källpar skrivs över när tidigare svenska strängar har rättats.

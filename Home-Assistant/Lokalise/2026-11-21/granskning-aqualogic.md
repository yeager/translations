# Home Assistant Core – AquaLogic

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/aqualogic/strings.json`, tidigare rapport och Lokalise API med direkt återläsning.

Status: samtliga tio aktuella bladsträngar och referensmål är radgranskade. En korrigering är sparad och återläst.

| Nyckel | Sparad text | Motivering |
|---|---|---|
| `issues::deprecated_yaml_import_issue_cannot_connect::description` | `Konfiguration av {integration_title} via YAML är föråldrad och kommer att tas bort i en framtida version. När YAML-konfigurationen importerades kunde AquaLogic-enheten inte nås eller svarade inte som en AquaLogic-panel. Kontrollera att enheten kan nås och starta om Home Assistant för att försöka igen. Du kan också ta bort nyckeln {domain} från konfigurationen och konfigurera integrationen via användargränssnittet.` | Korrigerar nominalformen, förtydligar åtgärdsföljden och bevarar båda platshållarna. |

Värdnamn, TCP-port, panel, feltexter och YAML-rubrik är korrekta. Direkt API-återläsning bekräftade ändringen. TMX-ledgern är uppdaterad och validerad (1 720 poster).

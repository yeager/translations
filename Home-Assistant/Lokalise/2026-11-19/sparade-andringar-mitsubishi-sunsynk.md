# Home Assistant Core: Mitsubishi Comfort och Sunsynk

Kontrollerat mot aktuell Lokalise-källa och sparat/återläst via API 2026-11-19. Fem förslag från den [tidigare granskningsrapporten](../2026-11-19-granskning/granskning-10921-11040.md) matchade fortfarande den befintliga svenska texten och rättades. Övriga fem förslag i rapporten skrevs inte över eftersom den aktuella svenska texten inte längre var samma som den dokumenterade äldre texten.

## `component::mitsubishi_comfort::issues::missing_address::fix_flow::step::addresses::description`

**Engelska:** These devices have no known local IP address, so they have no entities yet. Enter the local IPv4 address for each device below; each field is labeled with the device's MAC address. Leave a field blank to keep waiting for DHCP discovery (which only works when the device is on the same network as Home Assistant). After you submit, the integration reloads and sets up every device that has an address. Devices: {devices}

**Tidigare svenska:** Dessa enheter saknar en känd lokal IP-adress och har därför ännu inga entiteter. Ange den lokala IPv4-adressen för varje enhet nedan; varje fält är märkt med enhetens MAC-adress. Lämna ett fält tomt om du vill fortsätta vänta på DHCP-identifiering (vilket endast fungerar när enheten är i samma nätverk som Home Assistant). När du skickar in laddas integrationen om och varje enhet med en adress konfigureras. Enheter: {devices}

**Sparad svenska:** Dessa enheter saknar en känd lokal IP-adress och har därför ännu inga entiteter. Ange den lokala IPv4-adressen för varje enhet nedan. Varje fält är märkt med enhetens MAC-adress. Lämna ett fält tomt om du vill fortsätta vänta på DHCP-upptäckt, som bara fungerar när enheten är i samma nätverk som Home Assistant. När du skickar in uppgifterna läses integreringen in på nytt och varje enhet med en adress konfigureras. Enheter: {devices}

## `component::sunsynk::entity::sensor::load_energy_today::name`

**Engelska:** Load energy today

**Tidigare svenska:** Förbrukningsenergi idag

**Sparad svenska:** Förbrukningsenergi i dag

## `component::sunsynk::entity::sensor::grid_import_today::name`

**Engelska:** Grid import today

**Tidigare svenska:** Import från nätet idag

**Sparad svenska:** Import från nätet i dag

## `component::sunsynk::entity::sensor::grid_export_today::name`

**Engelska:** Grid export today

**Tidigare svenska:** Export till nätet idag

**Sparad svenska:** Export till nätet i dag

## `component::sunsynk::entity::sensor::discharge_today::name`

**Engelska:** Discharge today

**Tidigare svenska:** Urladdning idag

**Sparad svenska:** Urladdning i dag


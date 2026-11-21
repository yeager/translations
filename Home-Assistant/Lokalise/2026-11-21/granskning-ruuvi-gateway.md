# Home Assistant Core – Ruuvi Gateway

Datum: 2026-11-21  
Källa: aktuell Core `2fdaa177`, `homeassistant/components/ruuvi_gateway/strings.json`  
Status: samtliga sex aktuella källsträngar är radgranskade mot Lokalise utan ändringsförslag.

De fyra `config::abort`- och `config::error`-värdena är oförändrade
`[%key:…%]`-referenser och stämmer exakt med källan. De två direkta värdena är
korrekta i Lokalise:

- `Host (IP address or DNS name)` → `Värd (IP-adress eller DNS-namn)`
- `Bearer token (configured during gateway setup)` → `Bearer-token (konfigureras när gatewayen installeras)`

`Bearer-token`, `IP-adress`, `DNS-namn` och `gatewayen` följer svensk teknisk
skrivpraxis i sammanhanget. Inga platshållare, produktnamnet `Home Assistant`
eller osparade förslag förekommer. Komponenten saknar sedan tidigare poster i
det kanoniska Home Assistant-minnet; inga nya TMX-enheter skapas för
oförändrade UI-värden när säkra översättnings-ID:n inte exponeras i läsvyn.

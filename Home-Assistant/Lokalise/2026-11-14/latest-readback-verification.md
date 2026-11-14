# Oberoende återläsning av senaste sparningar

Datum: 2026-11-14

De fyra senaste sparningarna lästes om var för sig i Lokalise efter att de
sparats. Källnyckel och sparad måltext verifierades separat:

- `high_temperature_early_warning` → `Tidigt varningsmeddelande om hög temperatur`
- `high_power` → `Hög strömförbrukning`
- `magnetic_interference` → `Magnetisk störning`
- Midea och delad humidifier-nyckel för `sleep` → `Sömnläge`

Midea-strängen använder en delad nyckelreferens. Den felaktiga mellanformen
`SovSömnläge` upptäcktes vid återläsningen och rättades genom att bevara
referensen i Midea-strängen och uppdatera den delade strängen. Den slutliga
visade måltexten är `Sömnläge`.

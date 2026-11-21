# Home Assistant Core – ASUSWRT

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/asuswrt/strings.json`, tidigare ASUSWRT-rapporter och Lokalise API med direkt återläsning.

Status: samtliga 59 aktuella bladsträngar och referensmål i Core-källan är radgranskade. En kvarvarande korrigering sparades och återlästes.

| Fullständig nyckel | Befintlig text | Sparad text | Motivering |
|---|---|---|---|
| `component::asuswrt::entity::sensor::cpu_core_usage::name` | `Processorkärna {core_id} användning` | `Användning av CPU-kärna {core_id}` | Korrekt svensk ordföljd och tydlig benämning av CPU-kärna; platshållaren är bevarad. |

Tidigare sparade förbättringar för anslutning, port, SSH-nyckel, router, IP-adress, tidsgräns, gränssnitt och enhetsspårning kontrollerades mot den aktuella källan. Alla referenser till användarsteget, inklusive port och SSH-nyckel vid omkonfiguration, har giltiga svenska referensmål. Tekniska identifierare och protokollnamn (`ASUSWRT`, `HTTP`, `HTTPS`, `SSH`, `Telnet`, `dnsmasq.leases`) är avsiktligt oförändrade.

`svlang` gav naturlighetspoäng 10/10 för den sparade texten; den enda signalen avsåg den avsiktliga platshållaren `{core_id}`. Hunspell och termbanken gav ingen relevant invändning. TMX-ledgern har uppdaterats med den återlästa Lokalise-posten.

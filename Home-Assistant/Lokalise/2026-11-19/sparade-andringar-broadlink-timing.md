# Sparad Broadlink-feltext

Sparad och återläst i Home Assistant Core i Lokalise 2026-11-19. Svenska fältet var tomt före ändringen. Platshållaren `{duration}` bevarades. Termen ”RF-timing” behöver jämföras med teknisk dokumentation och övrig terminologi.

| Fullständig nyckel | Engelska | Sparad svenska |
| --- | --- | --- |
| `component::broadlink::exceptions::timing_too_long::message` | Broadlink devices cannot transmit an RF timing of {duration} s; the maximum is about 2 s | Broadlink-enheter kan inte sända en RF-timing på {duration} s. Maxvärdet är ungefär 2 s |

## Teknisk uppföljning

[Home Assistants Broadlink-kod på dev-grenen](https://github.com/home-assistant/core/blob/dev/homeassistant/components/broadlink/radio_frequency.py) beskriver kodning av RF-tidsvärden som pulslängder och behandlar varje varaktighets absolutvärde. Den vid kontrollen tillgängliga dev-filen innehöll dock inte nyckeln `timing_too_long`; det går därför inte att enbart från den fastställa exakt vilka intervall felmeddelandet omfattar. ”RF-timing” behålls tills den version som genererar felet har identifierats. Ingen ytterligare Lokalise-ändring gjordes vid uppföljningen.

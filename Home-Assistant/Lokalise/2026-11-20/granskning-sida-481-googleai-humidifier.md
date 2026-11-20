# Home Assistant Core — granskning sida 481 (Google Generative AI Conversation och Luftfuktare)

Datum: 2026-11-20  
Status: granskad; **inga förslag och inget sparat i Lokalise**

Samtliga 20 nycklar på sidan granskades utan dokumenterat ändringsförslag.

## Uppföljning

`component::humidifier::entity_component::_::state_attributes::mode::state::baby` är översatt med `Bebis`. Som fristående lägesvärde kan `Babyläge` vara tydligare, men den engelska källan kan vara ett tillverkarspecifikt fast lägesnamn. Kontrollera enhetens faktiska gränssnitt innan ändring.

| Omfattning | Resultat |
|---|---|
| Google Generative AI Conversation | Tre fel är direkta referenser; `Instruktioner`, `Temperatur`, `Top-K` och `Top-P` är korrekta gränssnittstermer. |
| Luftfuktare | Fuktighetsattribut och gemensamma tillståndsreferenser är korrekta; `Tillgängliga lägen`, `Läge`, `Boost`, `Komfort` och `Eko` bevaras. |

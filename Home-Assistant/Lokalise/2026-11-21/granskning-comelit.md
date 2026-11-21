# Home Assistant Core – Comelit

Datum: 2026-11-21

Alla 73 aktuella strängar granskades mot Core `2fdaa177` och direkt återlästes från Lokalise. Tre säkra korrigeringar sparades: `config::abort::invalid_pin` och `config::error::invalid_pin` använder nu korrekt `PIN-koden`; `exceptions::device_storage_failure::message` beskriver korrekt misslyckad läsning av SD-kortet och rekommenderad ersättning. Platshållare och Comelit/VEDO-namn är intakta. TMX-minnet är validerat till 1 979 poster.

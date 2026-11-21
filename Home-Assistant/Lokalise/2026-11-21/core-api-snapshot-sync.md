# Home Assistant Core – Lokalise API-synkning

Datum: 2026-11-21

En avgränsad, fullständig Core-export hämtades från Lokalise API med den
säkra lokala tokenhanteringen. Den omfattar 75 090 översättningsenheter och
75 091 segment (42 534 unika engelsk-svenska par). Exportens PO- och
TMX-avbild validerades mot JSONL-snapshoten.

Kontroll av de nyligen sparade måltexterna bekräftar bland annat
`Högt pH-värde`, `Stöder Ethernet` och Redgtechs
`{integration_name}-API:et.`. Den live-exporterade TMX:en är en katalogbild;
det kanoniska granskningsminnet behåller separat status och proveniens för
individuellt återlästa korrigeringar.

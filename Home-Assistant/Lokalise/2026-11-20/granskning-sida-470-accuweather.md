# Home Assistant Core — granskning sida 470 (AccuWeather)

Datum: 2026-11-20  
Status: granskad; **inga förslag och inget sparat i Lokalise**

Samtliga 20 nycklar på sidan är direkta Lokalise-referenser till tidigare granskade tillstånd för luftkvalitet, gräspollen eller gemensamma tillstånd (`common::state`). De har kontrollerats för exakt referenssyntax i både engelska och svenska och behöver inte översättas lokalt.

| Omfattning | Resultat |
|---|---|
| Mögel-, ambrosia- och trädpollen: nivå och fem tillstånd vardera | Referenserna är identiska mellan käll- och svensktext och bevaras. |
| Referensmål | Följs via luftkvalitets- respektive gräspollennycklarna, inte genom lokala dubbletter. |

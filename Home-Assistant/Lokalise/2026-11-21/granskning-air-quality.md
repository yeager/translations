# Home Assistant Core – Air Quality

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/air_quality/strings.json`, aktuell Lokalise-API-läsning.

Status: pågående radgranskning. Komponenten omfattar 570 katalogposter med återanvända villkors- och triggerfält.

## Live-verifierad uppföljning

Den lokala katalogögonblicksbilden innehöll äldre måltexter som `I åtminstone` för `For at least`. Direktläsning i Lokalise bekräftar att de nu är sparade som `I minst` för både gemensamma och refererande nycklar, bland annat nyckel-ID `834982884`, `837648204`, `951645671` och `952245440`. Motsvarande verifierade poster finns redan i Home Assistant-TMX-minnet; inga dubblettändringar gjordes.

Gas-, partikel-, radon-, rök-, tröskel- och tidsuttrycken granskas vidare i grupper med särskild kontroll av kemiska beteckningar och återanvända referenser.

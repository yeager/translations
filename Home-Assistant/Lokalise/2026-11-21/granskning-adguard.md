# Home Assistant Core – AdGuard Home

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/adguard/strings.json`, aktuell Lokalise-export.

Status: samtliga 73 aktuella bladnycklar är radgranskade utan ändringsförslag.

## Verifiering

- Produktnamnet `AdGuard Home`, produktnamnet `Home Assistant` och förkortningarna DNS, SSL och URL är konsekventa.
- Konfigurations- och återautentiseringsflödena har korrekta svenska för värd, port, autentiseringsuppgifter, SSL-verifiering och instans.
- Sensorer och växlar använder etablerad nätverksterminologi: DNS-förfrågningar, filtrering, föräldrakontroll, säker surfning, säker sökning och förfrågningslogg.
- Tjänster för filterprenumerationer (lägga till, aktivera, inaktivera, uppdatera och ta bort URL) följer källans imperativ och bevarar referensfälten.
- Undantagstexterna har intakta `{error}`-platshållare och korrekt betydelse för anslutning, autentisering, åtgärd och uppdatering.

Den lokala källfilen och den aktuella Lokalise-exporten innehåller samma direkta och refererade omfång. Inga ändringar sparades.

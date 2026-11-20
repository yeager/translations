# Home Assistant Core – svensk granskning, sida 503

Datum: 2026-11-20  
Status: sparat och återläst i Lokalise

Granskade nycklar omfattar IntelliFire, PECO, Samsung TV, Threshold samt återanvända referenser för Home Assistant Sky Connect och Home Assistant Yellow. Referenserna kontrollerades som referenser och lämnades oförändrade. Thresholds `Input sensor` använder samma källa som Utility Meter och den befintliga svenska referensen är därför korrekt.

| Fullständig nyckel | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `component::samsungtv::config::error::invalid_pin` | `PIN-koden är ogiltig, försök igen.` | `PIN-koden är ogiltig. Försök igen.` | Två självständiga satser ska avgränsas med punkt; versal inleder den nya meningen. |

Källkontroll: Home Assistant Cores aktuella `threshold/strings.json` och `utility_meter/strings.json` på `dev` bekräftar att båda fälten heter `Input sensor` och ska dela svensk formulering.

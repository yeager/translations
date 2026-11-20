# Home Assistant Core – Evohome: varmvattenöverstyrning

Datum: 2026-11-20. Lokalise lästes i skrivskyddat läge. Källan har kontrollerats mot `homeassistant/components/evohome/strings.json` i Core-commit `3d340fb5fdf03e7db48b45aec10f9b8da3b31c12`.

## Tydliga ändringsförslag

| Fullständig nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
| --- | --- | --- | --- |
| `component::evohome::services::set_dhw_override::fields::duration::description` | Varmvattnet återgår till sitt normala schema efter denna tidpunkt. Om värdet är 0 gäller ändringen fram till nästa schemalagda inställningspunkt. | Varmvattnet återgår till sitt schema efter den här tiden. Om värdet är 0 gäller ändringen fram till nästa schemalagda börvärde. | Sparad och återläst i Lokalise. `duration` är en tidslängd, inte en tidpunkt; *setpoint* översätts här som *börvärde*. |
| `component::evohome::services::set_dhw_override::description` | Åsidosätter ett varmvattenberedares tillstånd, antingen på obestämd tid eller under en viss tid, varefter det återgår till att följa sitt schema. | Åsidosätter en varmvattenberedares tillstånd, antingen på obestämd tid eller under en viss tid. Därefter återgår varmvattenberedaren till att följa sitt schema. | `Varmvattenberedare` är utrum: *en*, inte *ett*. Den explicita satsen undanröjer också den oklara syftningen hos *det*. |

## Bedömda utan ändringsförslag

| Fullständig nyckel | Befintlig svenska | Bedömning |
| --- | --- | --- |
| `component::evohome::services::set_dhw_override::name` | Ställ in överstyrning av varmvatten | Korrekt tjänstenamn. |
| `component::evohome::services::set_dhw_override::fields::state::name` | Tillstånd | Korrekt. |
| `component::evohome::services::set_dhw_override::fields::state::description` | Varmvattentillstånd: Sant (på: värm vattnet upp till börvärdet) eller Falskt (av). | Korrekt boolesk förklaring; *börvärde* stämmer med TM-källorna. |
| `component::evohome::services::set_dhw_override::fields::duration::name` | Varaktighet | Korrekt. |

## Validering och minneshantering

- `svlang skrivregler` gav inga träffar för båda förslagen.
- `hunspell -d sv_SE -l` gav inga felstavningsträffar för förslagen.
- `swedish-tm` ger etablerat stöd för *börvärde* i Home Assistant, bland annat `component::plugwise::entity::sensor::domestic_hot_water_setpoint::name` → `Börvärde för varmvatten`.
- Varaktighetsbeskrivningen är sparad, återläst och införd i det kanoniska
  HA-TMX-minnet. Tjänstebeskrivningen är fortsatt ett lokalt förslag och förs
  inte in förrän den har sparats och återlästs.

## Närliggande zonöverstyrning

Den aktuella Core-källan innehåller även sex aktiva strängar för `set_zone_override`. Samtliga har lästs i Lokalise och kontrollerats mot samma `strings.json`; inga ändringsförslag behövs.

| Fullständig nyckel | Befintlig svenska | Bedömning |
| --- | --- | --- |
| `component::evohome::services::set_zone_override::name` | Ställ in zonens åsidosättning | Korrekt tjänstenamn. |
| `component::evohome::services::set_zone_override::fields::setpoint::name` | Målvärde | Etablerat inom Evohomes zonöverstyrning. |
| `component::evohome::services::set_zone_override::fields::setpoint::description` | Temperaturen som ska användas i stället för det schemalagda målvärdet. | Korrekt och idiomatisk. |
| `component::evohome::services::set_zone_override::fields::duration::name` | Varaktighet | Korrekt. |
| `component::evohome::services::set_zone_override::fields::duration::description` | Zonen återgår till sitt schema efter denna tid. Om 0 gäller ändringen fram till nästa schemalagda målvärde. | Korrekt; *målvärde* är konsekvent med de intilliggande zonfälten. |
| `component::evohome::services::set_zone_override::description` | Åsidosätter en zons målvärde, antingen på obestämd tid eller under en angiven tidsperiod, varefter den återgår till att följa sitt schema. | Korrekt. |

Lokalise visar dessutom två referenssträngar för den äldre tjänsten `clear_zone_override`. De saknas i aktuell Core-källa och pekar exakt på `set_zone_override`-fältens `entity_id`-nycklar. De behandlas som historiska och ändras inte.

## Systemläge

Åtta aktiva `set_system_mode`-strängar har kontrollerats mot aktuell Core-källa utan ändringsförslag. `Ställ in systemläge`, `Varaktighet` och referensen till den gemensamma `mode`-nyckeln är korrekta. De tre beskrivningarna bevarar kodvärdena `Auto`, `AutoWithEco`, `Away`, `DayOff` och `Custom` exakt och har korrekt svensk innebörd. De två äldre `entity_id`-raderna som Lokalise också visar saknas i aktuell Core-källa och behandlas som historiska, utan ändring.

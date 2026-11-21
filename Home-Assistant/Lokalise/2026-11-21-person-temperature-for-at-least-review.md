# Home Assistant Core – person och temperature: tidsvillkor

Granskad: 2026-11-21  
Omfattning: fem fullständiga nycklar med källtexten `For at least`.

| Nyckel | Resultat | Svensk text | Verifiering |
|---|---|---|---|
| `component::person::common::trigger_for_name` | Rättad | I minst | API PUT och efterföljande GET |
| `component::person::triggers::entered_home::fields::for::name` | Redan korrekt | I minst | API GET |
| `component::person::triggers::left_home::fields::for::name` | Redan korrekt | I minst | API GET |
| `component::temperature::common::trigger_for_name` | Rättad | I minst | API PUT och efterföljande GET |
| `component::temperature::triggers::crossed_threshold::fields::for::name` | Redan korrekt | I minst | API GET |

`I minst` är den idiomatiska etiketten för ett tidsvillkor; `I åtminstone` är
inte en fungerande svensk konstruktion här. Nyckelidentiteten kontrollerades
mot Lokalises live-nyckelresurs, inte bara den lokala exporten.

En äldre `update`-manifestfil återanvände av misstag de två
temperatur-ID:na. Den korrigerades samtidigt och de felmärkta TMX-raderna togs
bort innan temperaturposterna fördes in.

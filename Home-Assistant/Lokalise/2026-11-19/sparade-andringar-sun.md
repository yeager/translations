# Sparad ändring för solen

Sparad och återläst i Lokalise 2026-11-19 efter kontroll mot tidigare granskningsrapport.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::sun::triggers::golden_hour_started::description` | Triggers when golden hour starts, in the morning, the evening, or either. | Utlöses när gyllene timmen startar, på morgonen, kvällen eller endera. | Utlöses när gyllene timmen börjar, på morgonen, kvällen eller båda. |

”Båda” beskriver valet att reagera på morgon och kväll. Närliggande beskrivningar och periodväljaren återstår att kontrollera.

## Gyllene timmens slut och blå timmen

Sparade och återlästa i Lokalise efter kontroll mot tidigare granskningsrapport.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::sun::triggers::golden_hour_ended::description` | Triggers when golden hour ends, in the morning, the evening, or either. | Utlöses när gyllene timmen slutar, på morgonen, kvällen eller endera. | Utlöses när gyllene timmen slutar, på morgonen, kvällen eller båda. |
| `component::sun::triggers::blue_hour_started::description` | Triggers when blue hour starts, in the morning, the evening, or either. | Utlöses när blå timmen börjar, på morgonen, kvällen eller endera. | Utlöses när blå timmen börjar, på morgonen, kvällen eller båda. |
| `component::sun::triggers::blue_hour_ended::description` | Triggers when blue hour ends, in the morning, the evening, or either. | Utlöses när blå timmen slutar, på morgonen, kvällen eller endera. | Utlöses när blå timmen slutar, på morgonen, kvällen eller båda. |

Båda uttrycker att utlösaren kan användas för både morgon och kväll. Periodväljaren återstår att kontrollera.

## Periodväljare

Sparad och återläst i Lokalise efter kontroll av alternativen Morgon och Kväll.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::sun::selector::period::options::any` | Any | Något | Båda |

I denna väljare motsvarar alternativet båda tiderna på dagen.

## Villkor för gyllene och blå timmen

Sparade och återlästa i Lokalise efter kontroll mot tidigare granskningsrapport.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::sun::conditions::is_golden_hour::description` | Tests if it is golden hour, optionally for a specific period. | Testar om det är gyllene timmen, eventuellt för en viss tidsperiod. | Kontrollerar om det är gyllene timmen, vid behov för en viss tid på dagen. |
| `component::sun::conditions::is_blue_hour::description` | Tests if it is blue hour, optionally for a specific period. | Testar om det är blå timmen, eventuellt för en viss tidsperiod. | Kontrollerar om det är blå timmen, vid behov för en viss tid på dagen. |

Perioden avser morgon, kväll eller båda enligt periodväljaren.

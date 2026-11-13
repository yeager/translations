# PCSX2: värd-, förinläsnings- och VSync-granskning, 14 november 2026

Deltafilen `pcsx2-sv-host-cache-vsync-batch-95-20261114.xliff` innehåller
fyra kontextgranskade rättningar i Crowdin-fil `15`:

| Sträng-ID | Kontext | Svenskt val |
| --- | --- | --- |
| `4053` | DEV9-nätverksinställning | `Värdlista per spel` |
| `11512` | CDVD-inställning | `Aktivera förinläsning av CDVD` |
| `11472` | grafisk synkronisering | `Vertikal synkronisering (VSync)` |
| `10652` | grafikinställning | `Högsta målminnesbredd där CPU Sprite Renderer kan aktiveras.` |

`Host` avser nätverksvärdar i den första strängen, inte ett produktnamn.
`Precaching` är CDVD-förinläsning och följer projektets terminologi. VSync
behålls som etablerad teknikförkortning, medan det utskrivna ledet översätts.
`CPU Sprite Renderer` är namnet på den tekniska renderingsdelen och lämnas
oförändrat.

XML, l10n-lint, platshållarkontroll, Hunspell-sv på enbart batchens måltext,
svlang, diffkontroll och Gitleaks ska köras före arkivering och API-import.
`msgfmt` är inte tillämpligt på XLIFF.

## Verifierat inskick

Crowdins API importerade deltafilen till projekt `561203`, fil `15` och
språket `sv-SE`: 4 strängar och 25 ord importerades, 0 godkändes automatiskt
och 0 hoppades över. Direkt återläsning bekräftar de ogranskade kandidaterna
`450021` (`4053`), `450023` (`11512`), `450025` (`11472`) och `450027`
(`10652`). Upstreamgranskning, aktivt val och merge är fortfarande separata
och inte verifierade.

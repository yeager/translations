# Home Assistant Core – Ezviz: val och reglage

Datum: 2026-11-20. Lokalise lästes i skrivskyddat läge och 16 aktuella strängar kontrollerades mot `homeassistant/components/ezviz/strings.json` i Core-commit `3d340fb5fdf03e7db48b45aec10f9b8da3b31c12`.

## Val och binärsensorer

Alla tio valsträngar är korrekta: batterikamerans arbetsläge samt larmljudets nivåer (`Mjuk`, `Tyst`, `Intensiv`, `Varningsljud`). De två binärsensorerna `Kryptering` och `Larmscheman aktiverade` är också korrekta.

## PTZ-knappar

`PTZ uppåt`, `PTZ höger`, `PTZ vänster` och `PTZ nedåt` behålls. Home Assistant-minnet verifierar samma riktningstermer för motsvarande PTZ-knappar i Reolink och Imou; ingen ändring behövs.

Ingen Lokalise-skrivning har genomförts och inga TMX-poster har ändrats.

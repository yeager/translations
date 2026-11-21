# Home Assistant Core – Ambient Station

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/ambient_station/strings.json`, Lokalise API med direkt återläsning.

Status: pågående. Konfiguration, batterier och vindmått är granskade; återstående väder-, nederbörds-, luftkvalitets- och markmätvärden granskas rad för rad.

Sex vindmått har korrigerats till naturliga svenska mätbeteckningar: högsta vindby, genomsnittlig vindhastighet/riktning för två respektive tio minuter och vindbyarnas riktning. Lokalise-ID `362308835`, `362308877`, `362308878`, `362308880`, `362308881`, `362308883`.

Nederbördsmåtten använder nu `nederbörd` och tydliga tidsperioder i stället för engelsknära former. Lokalise-ID `362308813`, `362308815`, `362308832`, `362308836`, `362308876`, `362308884`.

Fyra AQIN-värden använder nu `24-timmarsmedelvärde`; PM2,5 har svenskt decimaltecken. Lokalise-ID `801824077`, `801824079`, `801824081`, `801824083`.

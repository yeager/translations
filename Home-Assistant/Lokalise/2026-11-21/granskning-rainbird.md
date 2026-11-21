# Home Assistant Core – Rain Bird

Datum: 2026-11-21  
Källa: aktuell Core `2fdaa177`, `homeassistant/components/rainbird/strings.json`  
Status: samtliga 28 aktuella strängar granskade; en korrigering är sparad och återläst.

Konfigurationsreferenser, lösenords- och värdadressbeskrivningar, Rain Bird-
namnet, `{program}`-platshållarna, enhetsnamn och servicetext är kontrollerade.
Lokalise innehåller även sju äldre nycklar för tjänsten `set_rain_delay`; de
ingår inte längre i aktuell Core-källa och har inte ändrats.

| Nyckel | Befintlig svensk text | Sparad svensk text | Motivering |
| --- | --- | --- | --- |
| `options::step::init::data_description::duration` | `Standardtiden som sprinklern kommer att köras när den slås på.` | `Standardtiden som sprinklern är igång när den slås på.` | Naturligt svenskt uttryck för hur länge sprinklern körs. Sparad och återläst i Lokalise 2026-11-21. |

Översättningen har API-verifierats med Lokalise-ID `4878200762` och är införd
i det kanoniska TMX-minnet med spårbar nyckel och återläsningsstatus.

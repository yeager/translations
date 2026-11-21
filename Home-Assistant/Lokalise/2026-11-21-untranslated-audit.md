# Home Assistant – kontroll av saknade svenska Lokalise-översättningar

Datum: 2026-11-21  
Omfattning: hela den svenska oöversattkön i Lokalise API

## Metod

API-frågan använde `filter_untranslated=1`, `filter_translation_lang_ids=754` och `include_translations=1`. Sida 1 med gränsen 50 returnerade 24 poster; sida 2 returnerade 0 poster. Varje post hämtades därefter på nytt med både engelsk och svensk översättning för att kontrollera om den engelska källan hade verkligt innehåll.

## Resultat

| Typ | Antal | Bedömning |
| --- | ---: | --- |
| Tomma pluralbehållare (`{"one":"","other":""}`) på både engelska och svenska | 16 | Strukturella nycklar; inte översättningsbara strängar. |
| Tomma beskrivningsnycklar på både engelska och svenska | 8 | Saknar källtext; inte översättningsbara strängar. |
| Svenska poster med faktisk engelsk källtext men tom svensk översättning | 0 | Inga luckor att fylla. |

De strukturella pluralbehållarna hör till Arcam FMJ, Firmata, RFXtrx, DSMR, Roku, Kraken, SwitchBot, Actron Air, GitHub, KlikAanKlikUit och Monzo. De tomma beskrivningsnycklarna hör till Sensor, Roborock och Vacuum.

## Slutsats

Den aktuella Lokalise-datan innehåller inga svenska oöversatta strängar med faktisk engelsk källtext. Inga översättningar skapades eller ändrades. Befintliga svenska översättningar har lämnats orörda enligt arbetsinriktningen att endast komplettera saknade texter.

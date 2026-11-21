# Home Assistant Core – saknade Lokalise-källnycklar

Datum: 2026-11-21  
Källrevision: `3d340fb5fdf03e7db48b45aec10f9b8da3b31c12`

## Metod och resultat

Core-skriptets officiella uppladdningsunderlag genererades lokalt med `script.hassfest.translation_data.generate_upload_data` och plattades ut med Core-skriptets egen funktion. Det gav 66 009 aktuella engelska källnycklar.

Hela Lokalise-projektets nyckeluppsättning hämtades skrivskyddat i 16 sidor om högst 5 000 nycklar utan översättningstexter. Projektet innehåller 75 142 nycklar. Jämförelsen gav 201 källnycklar som finns i aktuellt Home Assistant Core men saknas helt i Lokalise.

| Komponent | Saknade nycklar |
| --- | ---: |
| airgradient | 7 |
| denon_rs232 | 1 |
| hdfury | 16 |
| huawei_lte | 2 |
| lametric | 1 |
| light | 1 |
| music_assistant | 5 |
| my_pv | 20 |
| roborock | 2 |
| schlage | 10 |
| tuya | 13 |
| wled | 3 |
| zwave_js | 120 |

## Behörighetskontroll

Ett avgränsat försök att skapa en enda saknad Airgradient-nyckel via Lokalise API:s officiella `POST /keys`-operation returnerade HTTP 403 (Forbidden). Ingen nyckel skapades.

Den tillgängliga tokenen kan läsa nycklar och ändra befintliga översättningar, men saknar behörighet att skapa källnycklar. Core-skriptets officiella synkronisering använder `python3 -m script.translations upload` på grenen `dev` och skapar/uppdaterar dessa nycklar via Lokalise. Den lokala miljön saknar Docker, som skriptet kräver.

## Uppföljning

De 201 nycklarna kan fyllas med svenska översättningar först efter att en token med behörighet att skapa nycklar, eller den officiella Core-uppladdningsmiljön, har synkroniserat dem till Lokalise. Inga befintliga svenska översättningar ändrades under kontrollen.

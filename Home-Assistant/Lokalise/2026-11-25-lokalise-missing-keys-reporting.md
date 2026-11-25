# Felrapportering av saknade Home Assistant Core-nycklar i Lokalise

Datum: 2026-11-25  
Projekt: `130246255a974bd3b5e8a1.51616605`  
Core-revision: `86a2eabe7e43f526db5821ef068087ce8404ae07`

## Omfattning

Inventeringen jämför alla aktuella Home Assistant Core-källnycklar med Lokalise och identifierar **203 aktuella källnycklar som saknas helt**. Alla fullständiga nycklar och deras upplösta engelska källtexter finns i [`2026-11-25-full-core-missing-audit.md`](2026-11-25-full-core-missing-audit.md) och maskinläsbart i [`2026-11-25-full-core-missing-audit.json`](2026-11-25-full-core-missing-audit.json).

| Komponent | Saknade nycklar |
|---|---:|
| airgradient | 7 |
| denon_rs232 | 1 |
| hdfury | 16 |
| huawei_lte | 2 |
| lametric | 1 |
| light | 1 |
| music_assistant | 5 |
| my_pv | 20 |
| roborock | 2 |
| schlage | 12 |
| tuya | 13 |
| wled | 3 |
| zwave_js | 120 |
| **Totalt** | **203** |

## Försök att rapportera och åtgärda i Lokalise

Den 2026-11-25 provades de tillgängliga API-vägarna med den sparade Lokalise-tokenen:

- `POST /projects/{project_id}/keys` – HTTP 403 Forbidden; inga nycklar skapades.
- `POST /projects/{project_id}/files/upload` – HTTP 403 Forbidden; ingen import startade.
- `GET /projects/{project_id}/keys/{key_id}/comments` – HTTP 403 Forbidden.
- `POST /projects/{project_id}/keys/{key_id}/comments` – HTTP 403 Forbidden; ingen kommentar eller felrapport skapades i Lokalise.

Lokalise API-dokumentationen anger att nyckelskapande kräver `write_keys`/administratörsbehörigheten Manage keys och kommentarsskapande kräver `write_comments`. Den aktuella tokenen har inte de behörigheter som behövs. Försöken gav inga ändringar i Lokalise.

## Nästa åtgärd

Rapporten med samtliga 203 nycklar är sparad här och i GitHub-backupen `yeager/translations`. När tokenen har behörighet att skapa nycklar (eller ladda upp filer) kan dessa källposter importeras och därefter översättas och verifieras. Inga befintliga nycklar eller översättningar ska skrivas över som del av den saknade-nyckelimporten.

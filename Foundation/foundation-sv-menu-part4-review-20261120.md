# Foundation – menu.json, granskningsomgång 4

Datum: 2026-11-20  
Metod: Crowdin API; förslaget kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Förslag | Resultat | Lint/stavning |
|---|---|---|---|---|---|
| MENU_MODS_BROWSER → UPLOAD_MODS_URL | Upload your mods: {IMG1} | Skicka upp dina mods: {IMG1} | Ladda upp dina moddar: {IMG1} | Identisk översättning fanns redan i Crowdin; API:t rapporterade dubblett. | l10n-lint: inga fel. Hunspell: inga fel. |

Platshållaren `{IMG1}` bevarades. Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.
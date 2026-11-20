# Foundation – menu.json, granskningsomgång 12

Datum: 2026-11-20  
Metod: Crowdin API; förslagen kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Sparad svenska | Lint/stavning |
|---|---|---|---|---|
| MENU_CONTROL_REMAPPER_CONTROL_NAMES → CONTROL_RESIZE_BRUSH_HOLD | Brush Resize (Hold + Mouse Wheel) | Ändra penselstorlek (Håll + Mushjul) | Ändra penselstorlek (håll ned + mushjul) | l10n-lint: inga fel. Hunspell: inga fel. |
| MENU_CONTROL_REMAPPER_CONTROL_NAMES → CONTROL_WALL_REMOVE | Remove Node / Segment | Ta bort Nod / Segment | Ta bort nod / segment | l10n-lint: inga fel. Hunspell: inga fel. |

Båda ändringarna skickades direkt till Crowdin via API (HTTP 201). Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.
# Foundation – dlc_agriculture_general.json: färdig radgranskning

Granskad: 2026-11-20  
Omfattning: samtliga 424 svenska strängar hämtades och granskades radvis via Crowdin API.

Godkända förbättringar dokumenteras i del 1–3:
- Monastics → klosterfolket.
- Nobles → adeln.
- Shire → grevskap samt korrigerad titel med platshållare och Markdown.
- Svenskt mellanslag före procenttecken.

Alla ändringar validerades med l10n-lint --language sv och hunspell -d sv_SE utan anmärkningar samt sparades i Crowdin med HTTP 201. Slutkontroll: offset 424 returnerade 0 strängar.
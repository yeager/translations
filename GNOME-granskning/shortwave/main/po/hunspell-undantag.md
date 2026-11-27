# Hunspell-undantag — Shortwave — main/po

Validerat med systemets svenska Hunspell-ordlista (`hunspell -d sv_SE -l`) den 2026-11-28. Skriptet `hunspell-sv` finns inte installerat i denna miljö, men `sv_SE`-ordlistan är installerad och användes direkt.

Efter att XML-markup, URL:er, e-postadresser, gettext-acceleratorer och `{...}`-platshållare tagits bort flaggades följande sju unika ordformer. De har kontrollerats mot katalogens sammanhang:

- `Cast-enhet`, `Chromecast-enheter`: etablerat produkt-/protokollnamn Google Cast/Chromecast i svenska sammansättningar.
- `Gradio`: namn på stationskatalogen Gradio.
- `Häcker`: korrekt efternamn i krediteringen (Felix Häcker).
- `Stream`, `Wave`: stationskategorier/genreord i den semikolonseparerade listan; bevaras som källans kategorinamn.
- `kortkommandofönster`: korrekt svensk sammansättning för fönstret med kortkommandon.

Råa träffar: [hunspell-unknown.txt](hunspell-unknown.txt).

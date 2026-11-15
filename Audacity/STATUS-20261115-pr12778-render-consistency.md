# Audacity PR #12778: konsekvent ljudrendering, 15 november 2026

Efter CodeRabbits slutliga sammanfattning granskades samtliga närliggande svenska strängar för `Mix and Render` i sin källkodskontext. Fyra av dem beskrev ljudrendering och inte uppspelning. De använder därför nu konsekvent formen `rendera`:

* analysinstruktionen för mixning och rendering före frekvensanalys,
* statusraden för allt renderat ljud i ett spår,
* kommandot `Render`,
* statusraderna för mixning och rendering till nytt mono- eller stereospår.

Commit `8a7ab042016ab766ecaeef3b3eb30191a83da44c` är pushad till den öppna PR:n #12778. `msgfmt --check`, Hunspell-sv, svlang, diffkontroll och Gitleaks kördes. l10n-lint har inga fel; dess kvarvarande helkatalogvarningar är äldre och orelaterade. Hunspell markerar `monospår` som okänt, men ordet är korrekt facksvenska i denna kontext. svlang markerar en V2-varning när fraser sammanfogas artificiellt i kontrollinmatningen; den gäller inte katalogsträngarnas separata satser.

Upstream är ännu inte merged eller releasad. PR:n är öppen och väntar på projektgranskning.

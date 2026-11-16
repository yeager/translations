# Kontextgranskning av load, batch 123

Den avslutande granskningen av 84 träffar från hela katalogen omfattade 74 593
nycklar. Batch 122 tog tio säkra innehållsinläsningar. Av de återstående 74
träffarna behölls 55 oförändrade eftersom de avser laddning, elektrisk last
eller status för en integration som startat eller inte startat.

De 19 ändringarna här avser data- och bildinläsning, URL-navigering och ett
felaktigt översatt elektriskt *load state*. I den senare betyder `load` last,
inte laddning, därför är översättningen `Laststatus`.

Filen `l10n-lint-entries.json` är ett medvetet minimalt indataformat för
l10n-lint. Den skiljer sig från `changes.json`, som också behöver Lokalise-id:n
och före-bilder för spårbarhet.

## Resultat

Batchen sparades via Lokalise API den 16 november 2026. Återläsning från API:t
bekräftade 19 av 19 översättningar. `l10n-lint` gav inga fel eller varningar
för det explicita indataformatet. Platshållarpariteten kontrollerades separat
mot engelska källtexter utan avvikelser. Hunspell-SV markerade enbart
produktnamn och etablerade tekniska namn: All-Link, Fully och medie-URL.

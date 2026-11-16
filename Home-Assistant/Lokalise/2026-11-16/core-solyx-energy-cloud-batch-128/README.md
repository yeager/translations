# Home Assistant Core: Solyx Energy Cloud, batch 128

18 svenska konfigurations- och sensorsträngar. Terminologin följer energisensorns kontext, exempelvis `Panneffekt`, `Pannspänning` och `Näteffekt`.

`l10n-lint`, Hunspell-sv, diffkontroll och Gitleaks har körts. `msgfmt` är inte tillämpligt för Lokalise JSON/API-batcher.

Alla poster sparades med Lokalise API, med `is_unverified: false`, och återlästes efter varje sparning.

# Home Assistant – granskningskopia 19 november 2026

Kopian innehåller den pågående radgranskningen av Core (`ha-core/`, inklusive dess register) och iOS-underlagen. Den kompletterar tidigare arbete i Home-Assistant och är inte en uppgift om att samtliga Core-översättningar är färdiggranskade. Förslagen är inte införda i Lokalise.

Återskapa filerna i en tom katalog:

```sh
cat arkiv.tar.gz.b64.part-* | base64 -d > arkiv.tar.gz
sha256sum arkiv.tar.gz
tar -xzf arkiv.tar.gz
```

SHA-256: `7940ef65d2a3ffe2adee256675c2cb070aa2f13bf11d1a525d767e554662fb44`. Core-registret är `ha-core/README.md` och den senaste rapporten täcker nyckel 38 105–38 134 i den dokumenterade ögonblicksbildens ordning. Tidigare arkiverad granskning av oöversatta strängar finns i [projektets översikt](../../README.md).

## Senare rapporter

- [Nyckel 38 135–38 164](granskning-38135-38164.md)
- [Nyckel 38 165–38 194](granskning-38165-38194.md)
- [Nyckel 38 195–38 224](granskning-38195-38224.md)
- [Nyckel 38 225–38 254](granskning-38225-38254.md)

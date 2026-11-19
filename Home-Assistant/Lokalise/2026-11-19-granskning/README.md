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
- [Nyckel 38 255–38 284](granskning-38255-38284.md)
- [Nyckel 38 285–38 314](granskning-38285-38314.md)
- [Nyckel 38 315–38 344](granskning-38315-38344.md)
- [Nyckel 38 345–38 374](granskning-38345-38374.md)
- [Nyckel 38 375–38 404](granskning-38375-38404.md)
- [Nyckel 38 405–38 434](granskning-38405-38434.md)
- [Nyckel 38 435–38 464](granskning-38435-38464.md)
- [Nyckel 38 465–38 494](granskning-38465-38494.md)
- [Nyckel 38 495–38 524](granskning-38495-38524.md)

- [Nyckel 38 525–38 554](granskning-38525-38554.md)

Senast granskade nyckel i denna ordning: `component::matter::entity::sensor::esa_state::state::offline` (Lokalise-ID 653106087). De två referensmålen i den senaste rapporten har kontrollerats i Lokalise. Ordningen kan ha förändrats sedan ögonblicksbilden och måste verifieras vid fortsatt granskning.

- [Kompletterande Matter-kontroll](matter-uppfoljning-2026-11-19.md) – tio nycklar och referensmålen kontrollerade; fortsättningen finns i rapporten för nyckel 38 565–38 569.

- [Nyckel 38 565–38 569](granskning-38565-38569.md) – nästa ID i den äldre ordningen är 653058791. Två terminologifrågor kräver uppföljning.

- [Nyckel 38 570–38 573](granskning-38570-38573.md) – nästa ID i äldre ordning är 653058787; kodkontrollen visar att anslutningsfelets källreferens kan vara för specifik; uppströms uppföljning återstår.

- [Nyckel 38 574–38 585](granskning-38574-38585.md) – nästa ID i äldre ordning är 653058775.

- [Nyckel 38 586–38 590](granskning-38586-38590.md) – nästa ID i äldre ordning är 653058770.

- [Nyckel 38 591–38 595](granskning-38591-38595.md) – nästa ID i äldre ordning är 653058765.

- [Nyckel 38 596–38 600](granskning-38596-38600.md) – nästa ID i äldre ordning är 652595332.

- [Nyckel 38 601–38 604](granskning-38601-38604.md) – nästa ID i äldre ordning är 652591197.

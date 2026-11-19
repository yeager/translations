# RetroArch Xemu – Vulkan-profilerare, svensk granskningsbatch 2026-11-19

Två oöversatta svenska Xemu-beskrivningar i `xemu-libretro.json` har granskats via Crowdin API. Förslagen är inte sparade eller skickade till Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 6239303 | Vulkan: the profile file lists the textures that sit on memory the game renders into but are not taken from that render target (they go through RAM instead, which is slow), each case once with its count and the texture's and the render target's address, format, size and pitch. | — | Vulkan: profilfilen listar texturer som ligger i minne som spelet renderar till men inte hämtas från det renderingsmålet (de går i stället via RAM, vilket är långsamt), varje fall en gång med antal samt texturens och renderingsmålets adress, format, storlek och radsteg. |
| 6239319 | Vulkan: the profile file lists the render targets read back into RAM and written back to the GPU, by the part of the renderer that asked for it, with each render target's address, size and format. Also the render targets evicted, with why and the target that replaced them. | — | Vulkan: profilfilen listar renderingsmålen som läses tillbaka till RAM och skrivs tillbaka till grafikprocessorn efter vilken del av renderaren som begärde det, med varje renderingsmåls adress, storlek och format. Den listar även renderingsmål som kastats ut, varför och målet som ersatte dem. |

## Kontroller

- Projektets Crowdin-TM kontrollerades via concordance i API:t. Något separat verktyg med namnet `swedish-tm` finns inte installerat; projektets TM användes som tillgänglig motsvarighet.
- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` och Crowdins QA markerar profilfilen och renderaren som möjliga stavningsträffar. De är korrekta tekniska sammansättningar.
- QA:s felaktiga skiljeteckensträff för `GPU:n` undveks genom ”grafikprocessorn”; den slutliga QA-körningen innehåller bara stavningsträffarna ovan.
- Inga platshållare eller formateringsmarkörer finns i batchen.

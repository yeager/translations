# RetroArch Beetle PSX – VRAM-kopia på GPU-tråd, svensk granskningsbatch 2026-11-19

En oöversatt svensk Beetle PSX-beskrivning i `beetle-psx-libretro.json` har granskats via Crowdin API. Förslaget är inte sparat eller skickat till Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 6239353 | Keeps a native-resolution copy of VRAM drawn by the software renderer alongside the hardware renderer, on the GPU Thread where it can run. The game's reads of VRAM and savestates then come from that copy, exactly as the hardware would give them. Disabled, they are read back from the GPU, which stalls emulation and, at an upscaled internal resolution, gives the game downscaled pixels that can show as graphical errors. Disabling only saves time where the GPU Thread does not run: on a single fast core, with a light gun connected, or where the CPU's cores are not reported, unless a lane count is chosen. Leave enabled if unsure. | — | Behåller en kopia i ursprunglig upplösning av VRAM som programvarurenderaren ritar parallellt med hårdvarurenderaren, på GPU-tråden där den kan köras. Spelets läsningar av VRAM och sparade tillstånd kommer sedan från kopian, precis som maskinvaran skulle tillhandahålla dem. När den är inaktiverad läses de tillbaka från grafikprocessorn, vilket stoppar emuleringen och vid uppskalad intern upplösning ger spelet nedskalade bildpunkter som kan visa sig som grafikfel. Att inaktivera sparar endast tid där GPU-tråden inte körs: på en snabb enkelkärna, med en ljuspistol ansluten eller där processorns kärnor inte rapporteras, om inte ett trådantal väljs. Lämna den aktiverad om du är osäker. |

## Kontroller

- Projektets Crowdin-TM kontrollerades via concordance i API:t. Något separat verktyg med namnet `swedish-tm` finns inte installerat; projektets TM användes som tillgänglig motsvarighet.
- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` och Crowdins QA markerar programvarurenderaren, hårdvarurenderaren och GPU-tråden. De är korrekta tekniska sammansättningar.
- Inga platshållare eller formateringsmarkörer finns i posten.

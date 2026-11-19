# RetroArch Xemu – Vulkan-shaderkompilering, svensk granskningsbatch 2026-11-19

En oöversatt svensk Xemu-beskrivning i `xemu-libretro.json` har granskats via Crowdin API. Förslaget är inte sparat eller skickat till Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 6234801 | Currently only confirmed to work on Nvidia graphics cards, broken on AMD. Affects shader compilation speed on Vulkan. "All" is the fastest but can crash some games. "Auto" is None on AMD graphics cards and All on others. | — | Det är för närvarande bara bekräftat att fungera på Nvidia-grafikkort och fungerar inte på AMD. Påverkar hastigheten för shaderkompilering i Vulkan. ”Alla” är snabbast men kan krascha vissa spel. ”Automatiskt” är Ingen på AMD-grafikkort och Alla på övriga. |

## Kontroller

- Projektets Crowdin-TM kontrollerades via concordance i API:t. Något separat verktyg med namnet `swedish-tm` finns inte installerat; projektets TM användes som tillgänglig motsvarighet.
- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` och Crowdins QA markerar enbart shaderkompilering, en korrekt teknisk sammansättning.
- Inga platshållare eller formateringsmarkörer finns i posten.

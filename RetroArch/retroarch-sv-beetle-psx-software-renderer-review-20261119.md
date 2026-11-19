# RetroArch Beetle PSX – parallell programvarurendering, svensk granskningsbatch 2026-11-19

En oöversatt svensk Beetle PSX-beskrivning i `beetle-psx-libretro.json` har granskats via Crowdin API. Förslaget är inte sparat eller skickat till Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 6239355 | Draws the software renderer's picture, and the Software Framebuffer under the hardware renderers, on a thread of its own when the CPU has two or more fast cores. 'Enabled' also splits upscaled pictures across the fast cores left over, in bands of rows; a number of lanes splits every picture across that many threads. With a light gun connected, or where the CPU's cores are not reported, 'Enabled' keeps drawing on the emulation thread; a number of lanes starts the threads anyway. The picture and the emulated timing are the same either way. | — | Ritar programvarurenderarens bild och programvarubufferten under hårdvarurenderarna på en egen tråd när processorn har två eller fler snabba kärnor. ”Aktiverad” delar även uppskalade bilder mellan de återstående snabba kärnorna, i rader av band; ett antal trådar delar varje bild över så många trådar. Med en ljuspistol ansluten eller där processorns kärnor inte rapporteras fortsätter ”Aktiverad” att rita på emuleringstråden; ett antal trådar startar trådarna ändå. Bilden och den emulerade tidsinställningen är desamma oavsett. |

## Kontroller

- Projektets Crowdin-TM kontrollerades via concordance i API:t. Något separat verktyg med namnet `swedish-tm` finns inte installerat; projektets TM användes som tillgänglig motsvarighet.
- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` och Crowdins QA markerar programvarurenderarens, hårdvarurenderarna och emuleringstråden. De är korrekta tekniska sammansättningar.
- Inga platshållare eller formateringsmarkörer finns i posten.

# RetroArch Xemu – TLB-lägen, svensk granskningsbatch 2026-11-19

En oöversatt svensk Xemu-beskrivning i `xemu-libretro.json` har granskats via Crowdin API. Förslaget är inte sparat eller skickat till Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 6238673 | When the emulator resets the dirty state of guest memory in the CPU's address cache (the TLB), it looks only at the address-translation modes the Xbox actually uses (one or two of 22). Makes some games faster (Crimson Skies, Virtua Cop 3) and makes others micro-stutter (Burnout 3, Ollie King, Otogi, Ninja Gaiden Black, Conker). Takes effect right away. | — | När emulatorn återställer statusen för ändrat gästdataminne i processorns adresscache (TLB) tittar den bara på de adressöversättningslägen som Xbox faktiskt använder (ett eller två av 22). Det gör vissa spel snabbare (Crimson Skies, Virtua Cop 3) och får andra att mikrostamma (Burnout 3, Ollie King, Otogi, Ninja Gaiden Black, Conker). Träder i kraft omedelbart. |

## Kontroller

- Projektets Crowdin-TM kontrollerades via concordance i API:t. Något separat verktyg med namnet `swedish-tm` finns inte installerat; projektets TM användes som tillgänglig motsvarighet.
- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` och Crowdins QA markerar gästdataminne, TLB, Xbox och speltitlar. Det är korrekta sammansättningar, förkortningar eller egennamn.
- Inga platshållare eller formateringsmarkörer finns i posten.

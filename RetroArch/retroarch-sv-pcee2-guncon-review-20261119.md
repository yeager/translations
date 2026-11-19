# RetroArch PCE Engine CD/PC Engine – GunCon 2, svensk granskningsbatch 2026-11-19

En oöversatt svensk sträng i `pcee2-libretro.json` har granskats via Crowdin API. Förslaget är inte sparat eller skickat till Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 6234693 | Draw a crosshair where the GunCon 2 is aiming, in the chosen colour; in the Namco System 246/256 light gun games too. Off by default, as on the console. Requires restart. | — | Ritar ett hårkors där GunCon 2 riktas, i vald färg; även i ljuspistolspel för Namco System 246/256. Inaktiverad som standard, precis som på konsolen. Kräver omstart. |

## Kontroller

- Projektets Crowdin-TM kontrollerades via concordance i API:t. Något separat verktyg med namnet `swedish-tm` finns inte installerat; projektets TM användes som tillgänglig motsvarighet.
- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` och Crowdins QA markerar GunCon, ljuspistolspel och Namco. De är produktnamn eller korrekt svensk sammansättning.
- Inga platshållare eller formateringsmarkörer finns i posten.

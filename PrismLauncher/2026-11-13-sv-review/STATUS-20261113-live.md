# Prism Launcher: live-status för svenska, 13 november 2026

Prism Launcher är ett startprogram för Minecraft som hanterar flera separata
spelinstanser, moddar och konton. Den officiella svenska UI-komponenten
`prismlauncher/launcher/sv` kontrollerades direkt i Hosted Weblate den
13 november 2026.

## Aktuell status

- Release `11.1.1` publicerades 28 september 2026 och uppfyller
  48-månadersgränsen.
- Komponenten innehåller 2 581 strängar.
- 2 531 strängar är översatta.
- 47 strängar är tomma och tre behöver redigeras, alltså 50 ofärdiga
  strängar totalt.
- Weblate visar 61 felande kontroller. De hör till redan översatta poster och
  är en separat granskningskö från de 50 ofärdiga posterna.

Den tidigare lokala filen `prismlauncher-sv-20261113.delta.ts` täcker tre
tydliga poster, men kan inte täcka den nuvarande kön ensam. Den är därför ett
begränsat lokalt underlag, inte en fullständig importbatch.

## Upstream och blockerare

Webbläsarsessionen var inloggad, men Hosted Weblate meddelade att
översättningen är tillfälligt stängd för bidrag på grund av underhåll.
Projektet kan därmed inte ta emot en inskickning just nu. Ingen import,
granskning eller release påstås ha genomförts.

När komponenten låses upp ska en ny export hämtas, alla 50 ofärdiga poster
granskas i UI- och kodsammanhang, och sedan delas upp i validerade
deltafiler om det behövs innan uppladdning.

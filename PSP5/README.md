# PSP5 – svenska

Utgångspunkt: `tsuramatsu1/psp5` vid commit
`225c7d04c38231b794451cea0c5efc1cb929b3af` (2026-10-12).

PSP5 har PPSSPP:s befintliga översättningar samt en egen katalog för de
PS5-specifika gränssnittstexterna. Den svenska katalogen hade 60 av 78
översatta rader och var uttryckligen märkt som maskinöversatt och ogranskad.

## Resultat

- 78 av 78 PSP5-specifika strängar har svensk översättning.
- 18 saknade strängar har översatts, bland annat grafik-, prestanda-,
  textur- och kontrollhjälptexter.
- Tre äldre formuleringar har rättats för naturligare svenska.
- Generatorn är den kanoniska källan och märker den svenska katalogen som
  granskad, så att senare generering inte skriver över resultatet.

## Kontroller

- Generatorn ger exakt samma 78 nycklar i källan och den svenska INI-filen.
- Python-syntaxkontroll, `git diff --check` och Gitleaks för båda ändrade
  filer är godkända.
- Hunspell-SV rapporterar bara välkända produktnamn och teknikord.
- `l10n-lint` har ingen INI-parser och `svlang` analyserar käll- och måltext
  som en gemensam löptext; deras utslag är därför inte relevanta för denna
  katalogtyp.

Ingen konsolkörning har utförts. Ändringen är avgränsad till PSP5:s egen
språkresurs och dess generator.

# RetroArch, svenska, batch 1

Datum: 2026-11-12
Crowdin-projekt: RetroArch (`380544`)
Språk: svenska (`sv-SE`)
Komponent: `linuxloader-libretro.json`, första sidan i filtret Oöversatt

## Resultat

50 strängar har granskats i Crowdins aktuella strängkontext och skickats som vanliga ogranskade förslag. De gäller linuxloader-kärnans arkadkontroller, grafik, ljuspistol, styrning, ljud och interna felsökningsvärden.

Crowdin bekräftade samtliga 50 skapade förslag. Varje text har sedan lästs tillbaka från API:t med samma svenska mål och avsändaren `yeagersthlm`.

Internt exponerade konfigurationsvärden, bland annat `EMULATE_DRIVEBOARD`, `CPU_FREQ_GHZ` och `TEST_MODE`, behölls avsiktligt på källspråket. Det är inte oöversatta missar.

## Kontroller

- Kontextgranskning rad för rad mot Crowdins fil, identifierare och hjälptext.
- Kontroll av platshållare, em dash och tre identiska konsonanter: godkänd.
- `l10n-lint`: godkänd.
- `svlang` och Hunspell: signaler begränsade till produktnamn, spelnamn, interna nycklar och facktermer.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt`: inte tillämpligt för Crowdins strängförslag.

## Upstreamstatus

Inskickad och API-verifierad i Crowdin. Förslagen är inte automatiskt godkända och inväntar därför projektets vanliga granskningsflöde.

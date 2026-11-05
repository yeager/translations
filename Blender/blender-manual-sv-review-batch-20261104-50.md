# Blender Manual: svensk granskningsbatch 50

Datum: 4 november 2026

Källa: `exports/2026-11-04/blender-manual-manual-sv.po`.

## Kontext och omfattning

Nio korta hjälptexter till Blenders kommandoradsalternativ. De har lästs i
den aktuella engelska manualens grupper för fönsteralternativ, loggning,
felsökning och tilläggsförråd. Texterna beskriver respektive alternativs
verkan, därför använder översättningarna presensformen *Tvingar*, *Anger*,
*Visar*, *Verifierar*, *Fångar* och *Aktiverar* på samma sätt som övriga
kommandoradshjälptexter.

`--window-border` och `--log-level` har kontrollerats i den aktuella
uppströmsmanualen. `scope` i GPU-felsökningsalternativet är ett tekniskt
namn på fångstomfånget och behålls därför i sammansättningen *scope-namnet*.
`repository` avser ett tilläggsförråd, inte en kodbas i allmän mening.

## Kontroller

- `msgfmt --check --statistics`: 9 översatta meddelanden och godkänd syntax.
- Radvis jämförelse av `(msgctxt, msgid)` mot råexporten: 9/9 träffar.
- `l10n-lint --language sv` och `svlang skrivregler --enable-interpunktion`:
  inga fel i måltexterna.
- `svlang svengelska` noterar *scope*. Termen behålls i *scope-namnet*, eftersom
  den är Blenders etablerade tekniska namn för GPU-fångstomfånget i den här
  kommandoradsoptionen och inte den orelaterade bildanalysfunktionen *Scopes*.
- Hunspell `sv_SE` noterar `FFmpeg`, `videoindata` och det eliderade
  `-utdata`. Första formen är ett produktnamn och de två övriga är korrekta
  tekniska sammansättningar som saknas i ordlistan.
- `git diff --check` och Gitleaks: godkända, utan hemligheter.

Råexporten är orörd. Deltafilen är lokalt validerad men ännu inte uppladdad
till Blender Translate.

## Terminologisk efterkontroll 5 november

`--debug-gpu-scope-capture` lagrar det angivna scope-namnet i Blenders
GPU-felsökningskonfiguration; därför är **scope-namn** en avsiktlig teknisk
term här, inte en oöversatt UI-etikett. **ID-datablock**, **loggningsnivå**
och **förråd** stämmer med den svenska Blender-katalogen. Flaggor och andra
maskinläsbara värden lämnas exakt oförändrade.

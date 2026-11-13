# Eden Emulator – svenska Qt-översättningar

Datum: 2026-11-12  
Projekt: Eden Emulator / Qt Translations (`o:edenemu:p:eden-emulator:r:qt-translations`)  
Källa: Transifex API och projektets Git-förråd `https://git.eden-emu.dev/eden-emu/eden`  
Status: inskickat och verifierat i Transifex

## Omfattning

- 8 tidigare oöversatta strängar i `UpdateDialog` granskades och översattes.
- Alla berör uppdaterarens nedladdning, uppackning, mellanlagring och felmeddelanden.
- Resursen hade 2 134 strängar; efter uppladdningen returnerar Transifex 0 oöversatta svenska strängar.

## Kvalitetskontroller

- `l10n-lint --language sv --json-format entries`: godkänd.
- `svlang skrivregler --enable-interpunktion`: godkänd.
- `hunspell -d sv_SE`: inga träffar.
- `git diff --no-index --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga läckor.
- `msgfmt`: ej tillämpligt; resursen är Qt (`i18n_type: QT`), inte PO. Format- och platshållarkontrollen gjordes med l10n-lint och Transifex accepterade batchen.

## Upstream

En Transifex API-batch med 8 översättningar skickades den 2026-11-12 och fick HTTP 200. En efterföljande API-kontroll med filtret `translated=false` bekräftade 0 återstående strängar i den svenska Qt-resursen.

### Livekontroll 13 november 2026

En ny API-kontroll bekräftar att `qt-translations` har **2 134 av 2 134**
svenska strängar och **0 oöversatta** (10 709 av 10 709 ord). Resursens
senaste översättningsuppdatering är 12 november 2026 09:21:31 UTC.

Androidresursen har **1 084 av 1 084** svenska strängar och **0 oöversatta**
(5 079 av 5 079 ord). Dess senaste översättningsuppdatering är 13 november
2026 12:59:48 UTC.

Transifex rapporterar samtidigt **0 granskade** och **0 korrekturlästa**
strängar för båda resurserna. Översättningarna är alltså inskickade och
synliga, men de är inte verifierat upstreamgranskade eller släppta.

## Versionskontroll

Senaste stabila tagg som kontrollerades var `v0.2.1`, daterad 2026-06-01. Projektet uppfyller därför 48-månaderskravet.


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

## Versionskontroll

Senaste stabila tagg som kontrollerades var `v0.2.1`, daterad 2026-06-01. Projektet uppfyller därför 48-månaderskravet.


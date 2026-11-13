# OpenCloud web-pkg – svenska översättningar

Datum: 2026-11-12
Projekt och komponent: OpenCloud / `web-pkg`
Status: inskickat och verifierat i Transifex

## Omfattning

- 12 tidigare oöversatta strängar för filvisning och redigering granskades och översattes.
- Omfattar UTF-8-varning, skrivskydd, beskärning, krypterade mappar, delningsinläsning, ogiltiga tecken i arbetsytenamn samt HTML-block.
- `HTML` och `UTF-8` behölls som etablerade formatnamn.

## Kvalitetskontroller

- `l10n-lint --language sv --json-format entries`: godkänd.
- Platshållarkontroll: godkänd.
- `svlang skrivregler --enable-interpunktion`: två falska positiva i en avsiktligt ordagrann lista med ogiltiga tecken (`/ \\ . : ? * " > < |`).
- Hunspell: inga träffar.
- `git diff --no-index --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga läckor.
- `msgfmt`: ej tillämpligt för JSON-resursen.

## Upstream

En Transifex API-batch med 12 uppdateringar skickades 2026-11-12 och fick HTTP 200. En efterföljande ny API-läsning med `translated=false` returnerade 0 oöversatta svenska strängar för komponenten.

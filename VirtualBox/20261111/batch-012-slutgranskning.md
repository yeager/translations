# Batch 012: slutgranskning och inskick

Datum: 2026-11-11
Komponent: `VirtualBox_sv.ts`, hela Qt-katalogen för VirtualBox Manager.

## Slutlig korrigering

Startsidan angav tidigare att VirtualBox Manager skulle konfigureras för att
använda datorn. Texten rättades till att konfigurationen får programmet att
fungera med datorn. Ändringen bygger på strängens faktiska användning i
startsidan och bevarar HTML-markeringen.

## Slutkontroll

- `lupdate`: 3 589 aktiva källsträngar, inga nya strängar jämfört med den
  svenska katalogen.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `l10n-lint`: endast två avsiktliga `--`-värden i språkmetadata rapporteras
  som oavslutade. Inga verkliga översättningsfel.
- `hunspell-sv`: träffarna granskades i sammanhang. Produktnamn, kommandon,
  filformat och tekniska identifierare behölls avsiktligt.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga läckta hemligheter.
- `msgfmt`: inte tillämpligt på Qt TS; `lrelease` är formatets validering.

## Upstream

Den befintliga [PR #848](https://github.com/VirtualBox/virtualbox/pull/848)
uppdaterades först med ett force-with-lease-push efter kontroll att
fjärrgrenen fortfarande stod på PR:ns ursprungliga huvudrevision. Därefter
skrevs de tio granskningscommitarnas identitet om till
`po@danielnylander.se`, utan innehållsändring i katalogen. Den aktuella
huvudrevisionen är `f11f1d7cb7cd85ced4377bb8d3b329d68b30fa36`.

GitHub bekräftade mottagandet och `oca/oracle` är godkänd för den aktuella
huvudrevisionen. PR:n är öppen, har inga granskningskommentarer och är inte
mergad.

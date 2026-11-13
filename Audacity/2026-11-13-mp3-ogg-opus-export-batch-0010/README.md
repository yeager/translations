# Audacity: MP3-, Ogg- och Opus-export, batch 0010

Den här radvisa granskningsbatchen omfattar 40 aktiva poster i
`au3/locale/sv.po` vid Audacity-huvudet `4596ccf`.

Den rättar MP3-kodning, bithastigheter och LAME, Ogg Vorbis-diagnostik samt
Opus-kodarens inställningar, felmeddelanden och filformatbenämningar.

Kontroller som passerade: `msgfmt --check --statistics` (4 443 aktiva
översättningar), avgränsad Hunspell-sv-kontroll med formatnamn och
platshållare som undantag, `git diff --check` samt Gitleaks.

`l10n-lint` och `svlang` har också körts. De rapporterar befintliga, globala
katalogvarningar utanför denna diff, bland annat tekniska identifierare och
avsiktligt oförändrade produktnamn.

Upstream: [Audacity PR #12759](https://github.com/audacity/audacity/pull/12759)
uppdaterades 2026-11-13. PR:en är öppen och inväntar upstreamgranskning.

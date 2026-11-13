# Audacity: Molnsynkronisering och MIDI, batch 0013

Den här radvisa granskningsbatchen omfattar 23 aktiva poster i
`au3/locale/sv.po` vid Audacity-huvudet `528ac23`.

Den rättar audio.com-projektens versionskonflikter, synkronisering och
delning samt MIDI- och Allegro-filernas importer- och exportdialoger.

Kontroller som passerade: `msgfmt --check --statistics` (4 443 aktiva
översättningar), `git diff --check` samt Gitleaks. Den lokala
Hunspell-sv-kontrollen för denna batch körs vid nästa sammanhållna
exportkontroll.

Upstream: [Audacity PR #12759](https://github.com/audacity/audacity/pull/12759)
uppdaterades 2026-11-13 och inväntar upstreamgranskning.

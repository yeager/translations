# Audacity: hjälp och äldre projektimport, batch 0006

Den här radvisa granskningsbatchen omfattar 18 aktiva poster i
`au3/locale/sv.po` vid Audacity-huvudet `4d23a4d`.

Hjälpämnenas rubriker har gjorts grammatiskt konsekventa. Länkar och deras
måladresser är återställda till källtextens aktuella adresser, och de äldre
AUP-projektens diagnostik har fått korrekt svenska.

Kontroller som passerade: `msgfmt --check --statistics` (4 443 aktiva
översättningar), avgränsad Hunspell-sv-kontroll med endast formatnamn och
markup som undantag, `git diff --check` samt Gitleaks.

Upstream: [Audacity PR #12759](https://github.com/audacity/audacity/pull/12759)
uppdaterades 2026-11-13. Den är öppen och mergebar, men inväntar
upstreamgranskning. Inga CI-resultat eller upstream-merge fanns vid kontrollen.

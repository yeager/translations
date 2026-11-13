# Audacity: teman och VST, batch 0005

Den här radvisa granskningsbatchen omfattar 23 aktiva poster i
`au3/locale/sv.po` vid Audacity-huvudet `c88e38b`.

Den korrigerar temafilers statusmeddelanden, VST- och VST3-diagnostik,
vågformsspår, integritetspolicy och återgivning av klipp. Protokollnamnen
VST och VST3 behålls, medan svensk grammatik och sammansättning har rättats.

Kontroller som passerade för patchen:

- `msgfmt --check --statistics` (4 443 aktiva översättningar)
- avgränsad Hunspell-sv-kontroll; VST och VST3 är produktnamn/förkortningar
- `git diff --check`
- Gitleaks

Upstream: [Audacity PR #12759](https://github.com/audacity/audacity/pull/12759)
uppdaterades 2026-11-13. Den är öppen och mergebar, men inväntar
upstreamgranskning. Inga CI-resultat eller upstream-merge fanns vid kontrollen.

# Audacity: moduler och MIDI-enheter, batch 0003

Den här radvisa granskningsbatchen omfattar 22 aktiva poster i
`au3/locale/sv.po` vid Audacity-huvudet `87742bd`.

Den rättar modulhanteringens svenska arbetsflöde, inklusive konsekvent
`läs in` i stället för `ladda`, samt felaktiga MIDI-enhetsdiagnoser,
pluralformer och en trasig platshållare i uppladdningsfelet.

Kontroller som passerade för patchen:

- `msgfmt --check --statistics` (4 443 aktiva översättningar)
- avgränsad Hunspell-sv-kontroll; endast produkt- och API-namnen LADSPA,
  LV2 och Audacity behövde undantas
- `git diff --check`
- Gitleaks

Upstream: [Audacity PR #12759](https://github.com/audacity/audacity/pull/12759)
uppdaterades 2026-11-13. Den är öppen och mergebar, men inväntar
upstreamgranskning. Inga CI-resultat eller upstream-merge fanns vid kontrollen.

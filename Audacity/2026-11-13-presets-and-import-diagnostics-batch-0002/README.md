# Audacity: effektförinställningar och importdiagnostik, batch 0002

Den här radvisa granskningsbatchen omfattar 32 aktiva poster i
`au3/locale/sv.po` vid Audacity-huvudet `3c8b9fe`.

Granskningen rättar svenska namn på instrument- och begränsarförinställningar,
felaktig stavning och oklar filhantering. Importmeddelandena beskriver nu
ljud-CD:er, krypterade filer och filformat med samma innebörd som källtexten.
`ladda ned` ersattes av `hämta` i den relevanta instruktionen.

Kontroller som passerade för patchen:

- `msgfmt --check --statistics` (4 443 aktiva översättningar)
- `git diff --check`
- Gitleaks

Upstream: [Audacity PR #12759](https://github.com/audacity/audacity/pull/12759)
uppdaterades 2026-11-13. Den är öppen och mergebar, men inväntar
upstreamgranskning. Inga CI-resultat eller upstream-merge fanns vid kontrollen.

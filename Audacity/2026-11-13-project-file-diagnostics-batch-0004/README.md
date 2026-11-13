# Audacity: projektfilsdiagnostik, batch 0004

Den här radvisa granskningsbatchen omfattar 50 aktiva poster i
`au3/locale/sv.po` vid Audacity-huvudet `e2831b3`.

Den rättar tidsformat, projektfilernas databasdiagnostik,
säkerhetskopiering, insticksmodulregistret, bildruteformat och SQLite-fel.
Flera oöversatta eller sakligt felaktiga feltexter har fått korrekt svensk
innebörd.

Kontroller som passerade för patchen:

- `msgfmt --check --statistics` (4 443 aktiva översättningar)
- avgränsad Hunspell-sv-kontroll; tekniska identifierare och förkortningar
  som `sqlite3`, `BLOB`, `NTSC` och `fps` behövde undantas
- `git diff --check`
- Gitleaks

Upstream: [Audacity PR #12759](https://github.com/audacity/audacity/pull/12759)
uppdaterades 2026-11-13. Den är öppen och mergebar, men inväntar
upstreamgranskning. Inga CI-resultat eller upstream-merge fanns vid kontrollen.

# Kodi services and metadata, Swedish refresh

Four small components were refreshed from current Kodi Weblate exports and
updated as individual API units on 2026-11-02.

| Component | Updated units | Archive SHA-256 |
| --- | ---: | --- |
| `service-scrobbler-lastfm` | 2 | `622246b6b6a6d4a75d472e2215b89b50a576f38791a7d20ccce2dbabc1b554c0` |
| `service-libreelec-settings` | 5 | `8652bb6a585f9c3d32d0312b3bb62c27f3c8e0ce99d1a86df38ef7aee380e46a` |
| `metadata-generic-albums` | 2 | `2056f4d56ef6d8358372d96eabe89afb7dc065beae9662be510de9d4445c7c2d` |
| `metadata-generic-artists` | 2 | `46af5499846d3fdbd9ce2f3c1023fb4c84ad76ca929daa76111ca69d4c6bfbfc` |

The refreshed whole-file exports pass `msgfmt --check`, `l10n-lint`, `svlang
skrivregler` and Gitleaks. API write responses were read back for each unit.

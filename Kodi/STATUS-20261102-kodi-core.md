# Kodi core – svenska

| Fält | Status |
| --- | --- |
| Plattform | Kodi Weblate (`kodi-core/kodi-main/sv_se`) |
| Häfte | `kodi-core-kodi-main-sv-reviewed-20261102-delta.po` |
| Omfattning | 67 nya eller kompletterade strängar; 4 688 av 4 688 strängar är översatta i den lokala arbetskopian |
| Filformat | GNU gettext PO |
| Katalogkontroll | `msgfmt --check`: godkänd |
| l10n-lint | 0 fel, 0 varningar; en avsiktlig informationsnotis för den etablerade termen `Slow motion` |
| svlang skrivregler | godkänd utan träffar |
| Hunspell | tekniska/projektspecifika träffar manuellt granskade: Kodi, OSD, EXIF-metadata, NFO-fil, Blu-ray-bitmappar, PGS-undertexter, SDR-visning och `extras` |
| Uppladdning | Klar för import i Weblate via webbläsaren; inte uppladdad från denna lokala arbetskörning |
| SHA-256 | `e4e8a003209eabdf930974c937e47ac6eb0a8b63f771e320e6b92660150451cd` |

Den fullständiga nedladdade katalogen finns lokalt under arbetskatalogen. Arkivet
innehåller endast ändringshäftet så att Weblate-importen är liten och spårbar.

## Informationsleverantörer

| Komponent | Omfattning | Arkivfil | Status |
| --- | --- | --- | --- |
| `metadata.generic.albums` | 2 kompletterade strängar, 21 av 21 översatta | `kodi-add-ons-information-providers-metadata-generic-albums-sv-reviewed-20261102.po` | Klar för Weblate-import |
| `metadata.generic.artists` | 2 kompletterade strängar, 26 av 26 översatta | `kodi-add-ons-information-providers-metadata-generic-artists-sv-reviewed-20261102.po` | Klar för Weblate-import |
| `metadata.universal` | 1 språklig korrigering, 87 av 87 översatta | `kodi-add-ons-information-providers-metadata-universal-sv-reviewed-20261102.po` | Klar för Weblate-import |

Båda katalogerna klarar `msgfmt --check`, l10n-lint och svlangs skrivregler.
Hunspellträffarna är granskade projektnamn och tekniska termer, bland annat
Discogs, MusicBrainz, AllMusic och `discogs.com`.

I `metadata.universal` rättades den befintliga varningen med tre utropstecken
och felaktig sammansättning: `Om alla filmkategorier inkluderas minskar
sökträffsäkerheten avsevärt!`

## PVR-klienter

| Komponent | Omfattning | Arkivfil | Status |
| --- | --- | --- | --- |
| `pvr.waipu` | 3 kompletterade strängar, 62 av 62 översatta | `kodi-add-ons-pvr-clients-pvr-waipu-sv-reviewed-20261102.po` | Klar för Weblate-import |

`pvr.waipu` har en uppströmsgenererad PO-huvudvarning om saknat
`Project-Id-Version`; katalogen är i övrigt syntaktiskt korrekt. l10n-lint,
svlangs skrivregler och den manuella Hunspell-granskningen är godkända.

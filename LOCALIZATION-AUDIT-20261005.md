# Lokal granskningsstatus — 5 oktober 2026

Kontrollen bygger på de aktuella lokala exporterna och arbetskopiorna. En tom källsträng räknas inte som en oöversatt post.

| Projekt | Underlag | Kontroll | Resultat |
|---|---|---|---|
| CUPS | `cups_sv.po` | gettext, l10n-lint | Inga aktiva tomma eller fuzzy-poster. |
| libcups | `libcups-sv-reviewed-20261005.strings` | full nyckeltäckning, l10n-lint, Gitleaks | 2 495 innehållssträngar granskade. |
| cpdb-libs | `cpdb-libs-sv-full-review-20261005.po` | gettext, l10n-lint, Gitleaks | Komplett granskad katalog. |
| Blender UI | `sv.po` | gettext | 39 835 aktiva strängar; 0 tomma, 0 fuzzy. |
| FreeCAD | svenska XLIFF- och TS-exporter | XML-kontroll | 38 501 segment med källtext; 0 tomma/ofärdiga målsegment. |
| Cacti | `cacti-sv-reviewed-20261005.po` | msgfmt, gettext, l10n-lint, Gitleaks | 0 tomma, 0 fuzzy, inga lintfel eller varningar. |
| Kodi core | `kodi-core-kodi-main-sv_se.po` | gettext | 0 tomma, 0 fuzzy. |
| Codeberg/Forgejo | `forgejo-locale_sv-SE-reviewed-20261005.json` | JSON-kontroll | 1 169 textvärden; 0 tomma. |
| RPCS3 | `rpcs3_sv.ts` | XML-kontroll | 3 618 meddelanden; 0 ofärdiga. |
| PCSX2 | `pcsx2-qt_sv-SE.ts` | XML-kontroll | 5 049 meddelanden; 0 ofärdiga. |
| PostGIS manual | aktuell PO-arbetskopia | gettext | 0 tomma, 0 fuzzy. |
| pgRouting | aktuell PO-arbetskopia | gettext | 0 tomma, 0 fuzzy. |
| DigiAgriapp | aktuell ARB-export | JSON-kontroll | 392 svenska nycklar; 0 tomma. |

PostGIS och pgRouting har fortfarande historiska lintobservationer som måste granskas semantiskt innan de kan kallas fullständigt kvalitetsgranskade. PCSX2 har egna bidragsregler som kräver mänsklig avstämning innan nytt bidragsinnehåll kan skapas eller publiceras.

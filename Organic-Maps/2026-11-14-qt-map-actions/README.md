# Organic Maps – svenska Qt-kartåtgärder

Datum: 2026-11-14  
Komponent: `data/strings/strings.txt` och den genererade `qt/translations/sv/organicmaps.ts`  
Källversion: `2026.11.11-39-android`, publicerad 2026-11-11

## Granskad batch

Sjutton tidigare engelska Qt-strängar har fått svenska översättningar i kartprogrammets datorgränssnitt:

- hämtningsknapp, köstatus, omförsök och förlopp för kartområden
- rutt längs spår samt kopiering av länk och text
- val av kollektivtrafiklinje och koordinatformat
- bokmärkesfärg, kulturarvslänk, Wikipedia-rubrik och avslutning
- uppladdning av kartändringar, välkomsttext, positionssökning och kollektivtrafik

Projektets källfil är Twine-liknande `strings.txt`; Qt-katalogen återskapades med projektets eget skript. Android- och Apple-resurser påverkas inte eftersom samtliga strängar är märkta `qt`.

## Terminologi

| Engelska | Svenska | Kontext |
| --- | --- | --- |
| Download / Downloading | Hämta / Hämtar | Hämtning av offlinekartor |
| Route Along Track | Rutt längs spår | Åtgärd för valt GPS-spår |
| Public transport | Kollektivtrafik | Ruttprofil för tåg, tunnelbana och kollektivtrafik |
| Bookmark color | Bokmärkesfärg | Fältetikett i bokmärkesredigeraren |
| Upload Edits | Skicka ändringar | Överföring av användarens kartändringar |

## Kontroller

- `tools/unix/strings_validate_keys.sh`: godkänd, 897 definierade och 897 använda nycklar.
- `tools/unix/strings_validate_format.sh`: godkänd för `strings.txt`, `types_strings.txt` och `sound.txt`.
- `lrelease`: 277 färdiga och 0 oavslutade svenska Qt-översättningar.
- svlang: godkänd för den avgränsade batchen.
- Hunspell-SV: körd endast för batchens 17 strängar med låg CPU-prioritet; inga stavfel.
- l10n-lint: 0 fel; 16 befintliga varningar i den genererade Qt-filen utanför batchen.
- `git diff --check` och Gitleaks: godkända.
- `msgfmt`: ej tillämpligt, eftersom resurserna inte är PO-filer.

## Upstream

PR [organicmaps/organicmaps#14218](https://github.com/organicmaps/organicmaps/pull/14218) är öppnad från `yeager:sv-qt-map-actions-20261114`.

Status: lokalt granskat, arkiverat och inskickat som PR. Upstreamgranskning och merge återstår.

# Music Assistant – Lokalise API-kontroll av svenska

Datum: 2026-11-16  
Kanal: Lokalise API v2  
Språk: `sv_SE`

Kontrollen gjordes med `filter_lang_ids=756`, `filter_untranslated=1` och
`include_translations=1` för respektive projekt. Inga API-skrivningar gjordes
eftersom kontrollen inte fann någon verkligt oöversatt svensk sträng.

| Projekt | API-resultat |
| --- | --- |
| MA Desktop App | Inga oöversatta svenska nycklar. |
| MA Frontend | Inga oöversatta svenska nycklar. |
| MA Mobile App | Inga oöversatta svenska nycklar. |
| MA Server | En träff på en nyckel med tom engelsk källtext. Svensk måltext är redan `Plex.tv`; detta är en API-falsk positiv, inte en lucka i översättningen. |

Den här kontrollen bekräftar sparat innehåll som API:t exponerar vid
kontrolltillfället. Den bekräftar inte upstream-granskning, merge eller
utgivning.

`msgfmt` är inte tillämpligt eftersom detta är en API-kontroll och ingen
PO-katalog.

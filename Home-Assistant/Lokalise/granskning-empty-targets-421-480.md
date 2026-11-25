# Home Assistant Core: tidigare tomma svenska mål 421–480

- Granskade och sparade: **60/60**. Fullständiga nycklar och engelska källor kontrollerades mot live Lokalise; svenska mål sparades via API och varje ändring lästes tillbaka. Källrevision: `86a2eabe7e43f526db5821ef068087ce8404ae07`.
- Batchen innehåller inga referensnycklar och inga platshållare. Azure Speech-språk, regioner och skrivsystem kontrollerades radvis.
- `svlang skrivregler`: inga fel. Separat `svlang check` per sträng: inga fel. Hunspell efter uppdaterad svensk ordlista: inga flaggade ord. Ordlistans 19 regressionstester passerar.
- NE användes för svenska språkbenämningar där formen inte är självklar: [Iriska](https://www.ne.se/uppslagsverk/skola/standard/iriska), [galiciska](https://www.ne.se/uppslagsverk/encyklopedi/lang/galiciska), [Kannada](https://www.ne.se/uppslagsverk/skola/avancerad/kannada), [Malayalam](https://www.ne.se/uppslagsverk/skola/avancerad/malayalam), [Marathi](https://www.ne.se/uppslagsverk/skola/avancerad/marathi), [Gujarati](https://www.ne.se/uppslagsverk/skola/avancerad/gujarati), [Odia/Oriya](https://www.ne.se/uppslagsverk/skola/avancerad/oriya), [Panjabi/Punjabi](https://www.ne.se/uppslagsverk/skola/avancerad/panjabi), [singalesiska](https://www.ne.se/uppslagsverk/skola/avancerad/singalesiska), [sundanesiska](https://www.ne.se/uppslagsverk/skola/avancerad/sundanesiska) och [kiswahili](https://www.ne.se/uppslagsverk/encyklopedi/lang/kiswahili).
- Manifest: `2026-11-25-reviewed-empty-targets-421-480.json`; TM-underlag: `2026-11-25-reviewed-empty-targets-421-480-tm.json`.

## Radgranskning

### `component::microsoft::selector::language::options::fr-fr`
**Källa:** French (France)
**Svenska:** Franska (Frankrike)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::ga-ie`
**Källa:** Irish (Ireland)
**Svenska:** Iriska (Irland)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::gl-es`
**Källa:** Galician
**Svenska:** Galiciska
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::gu-in`
**Källa:** Gujarati (India)
**Svenska:** Gujarati (Indien)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::he-il`
**Källa:** Hebrew (Israel)
**Svenska:** Hebreiska (Israel)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::hi-in`
**Källa:** Hindi (India)
**Svenska:** Hindi (Indien)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::hr-hr`
**Källa:** Croatian (Croatia)
**Svenska:** Kroatiska (Kroatien)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::hu-hu`
**Källa:** Hungarian (Hungary)
**Svenska:** Ungerska (Ungern)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::hy-am`
**Källa:** Armenian (Armenia)
**Svenska:** Armeniska (Armenien)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::id-id`
**Källa:** Indonesian (Indonesia)
**Svenska:** Indonesiska (Indonesien)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::is-is`
**Källa:** Icelandic (Iceland)
**Svenska:** Isländska (Island)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::it-it`
**Källa:** Italian (Italy)
**Svenska:** Italienska (Italien)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::iu-cans-ca`
**Källa:** Inuktitut (Syllabics, Canada)
**Svenska:** Inuktitut (stavelseskrift, Kanada)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::iu-latn-ca`
**Källa:** Inuktitut (Latin, Canada)
**Svenska:** Inuktitut (latinsk skrift, Kanada)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::ja-jp`
**Källa:** Japanese (Japan)
**Svenska:** Japanska (Japan)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::jv-id`
**Källa:** Javanese (Latin, Indonesia)
**Svenska:** Javanesiska (latinsk skrift, Indonesien)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::ka-ge`
**Källa:** Georgian (Georgia)
**Svenska:** Georgiska (Georgien)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::kk-kz`
**Källa:** Kazakh (Kazakhstan)
**Svenska:** Kazakiska (Kazakstan)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::km-kh`
**Källa:** Khmer (Cambodia)
**Svenska:** Khmer (Kambodja)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::kn-in`
**Källa:** Kannada (India)
**Svenska:** Kannada (Indien)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::ko-kr`
**Källa:** Korean (Korea)
**Svenska:** Koreanska (Korea)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::lo-la`
**Källa:** Lao (Laos)
**Svenska:** Laotiska (Laos)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::lt-lt`
**Källa:** Lithuanian (Lithuania)
**Svenska:** Litauiska (Litauen)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::lv-lv`
**Källa:** Latvian (Latvia)
**Svenska:** Lettiska (Lettland)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::mk-mk`
**Källa:** Macedonian (North Macedonia)
**Svenska:** Makedonska (Nordmakedonien)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::ml-in`
**Källa:** Malayalam (India)
**Svenska:** Malayalam (Indien)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::mn-mn`
**Källa:** Mongolian (Mongolia)
**Svenska:** Mongoliska (Mongoliet)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::mr-in`
**Källa:** Marathi (India)
**Svenska:** Marathi (Indien)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::ms-my`
**Källa:** Malay (Malaysia)
**Svenska:** Malajiska (Malaysia)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::mt-mt`
**Källa:** Maltese (Malta)
**Svenska:** Maltesiska (Malta)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::my-mm`
**Källa:** Burmese (Myanmar)
**Svenska:** Burmesiska (Myanmar)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::nb-no`
**Källa:** Norwegian Bokmål (Norway)
**Svenska:** Norskt bokmål (Norge)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::ne-np`
**Källa:** Nepali (Nepal)
**Svenska:** Nepalesiska (Nepal)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::nl-be`
**Källa:** Dutch (Belgium)
**Svenska:** Nederländska (Belgien)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::nl-nl`
**Källa:** Dutch (Netherlands)
**Svenska:** Nederländska (Nederländerna)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::or-in`
**Källa:** Odia (India)
**Svenska:** Odia (Indien)
**Motivering:** Odia är källans moderna språkbenämning; NE listar odia som alternativ benämning till oriya.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::pa-in`
**Källa:** Punjabi (India)
**Svenska:** Punjabi (Indien)
**Motivering:** Punjabi/panjabi är språkets internationella namn; NE redovisar även den svenska formen punjabiska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::pl-pl`
**Källa:** Polish (Poland)
**Svenska:** Polska (Polen)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::ps-af`
**Källa:** Pashto (Afghanistan)
**Svenska:** Pashto (Afghanistan)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::pt-br`
**Källa:** Portuguese (Brazil)
**Svenska:** Portugisiska (Brasilien)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::pt-pt`
**Källa:** Portuguese (Portugal)
**Svenska:** Portugisiska (Portugal)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::ro-ro`
**Källa:** Romanian (Romania)
**Svenska:** Rumänska (Rumänien)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::ru-ru`
**Källa:** Russian (Russia)
**Svenska:** Ryska (Ryssland)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::si-lk`
**Källa:** Sinhala (Sri Lanka)
**Svenska:** Singalesiska (Sri Lanka)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::sk-sk`
**Källa:** Slovak (Slovakia)
**Svenska:** Slovakiska (Slovakien)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::sl-si`
**Källa:** Slovenian (Slovenia)
**Svenska:** Slovenska (Slovenien)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::so-so`
**Källa:** Somali (Somalia)
**Svenska:** Somaliska (Somalia)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::sq-al`
**Källa:** Albanian (Albania)
**Svenska:** Albanska (Albanien)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::sr-latn-rs`
**Källa:** Serbian (Latin, Serbia)
**Svenska:** Serbiska (latinsk skrift, Serbien)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::sr-rs`
**Källa:** Serbian (Cyrillic, Serbia)
**Svenska:** Serbiska (kyrillisk skrift, Serbien)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::su-id`
**Källa:** Sundanese (Indonesia)
**Svenska:** Sundanesiska (Indonesien)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::sv-se`
**Källa:** Swedish (Sweden)
**Svenska:** Svenska (Sverige)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::sw-ke`
**Källa:** Kiswahili (Kenya)
**Svenska:** Swahili (Kenya)
**Motivering:** Kiswahili är NE:s huvuduppslagsform och anges där som en annan benämning på swahili.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::sw-tz`
**Källa:** Kiswahili (Tanzania)
**Svenska:** Swahili (Tanzania)
**Motivering:** Kiswahili är NE:s huvuduppslagsform och anges där som en annan benämning på swahili.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::ta-in`
**Källa:** Tamil (India)
**Svenska:** Tamil (Indien)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::ta-lk`
**Källa:** Tamil (Sri Lanka)
**Svenska:** Tamil (Sri Lanka)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::ta-my`
**Källa:** Tamil (Malaysia)
**Svenska:** Tamil (Malaysia)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::ta-sg`
**Källa:** Tamil (Singapore)
**Svenska:** Tamil (Singapore)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::te-in`
**Källa:** Telugu (India)
**Svenska:** Telugu (Indien)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::th-th`
**Källa:** Thai (Thailand)
**Svenska:** Thailändska (Thailand)
**Motivering:** Azure Speech-localeetikett; språk, region och eventuell skriftvariant återges tydligt på svenska.
**Status:** sparad och återläst i Lokalise.

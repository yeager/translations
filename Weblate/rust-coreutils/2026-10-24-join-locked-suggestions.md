# Rust Coreutils: låsta svenska join-strängar

Kontrollerad 2026-10-24 via Hosted Weblates API.

Komponenten `join` är låst. Sex befintliga svenska förslag kunde därför inte accepteras: API:t svarade `403` med `This translation is currently locked.` Förslagen ligger kvar i Weblate och kan accepteras när komponenten låses upp.

| Kontext | Svenskt förslag |
| --- | --- |
| `join-error-multi-character-tab` | `tabulator med flera tecken '{ $value }'` |
| `join-diag-help-format` | `ett utmatningsfält är FILNUMMER.FÄLT, som i -o 1.2,2.1; 0 står för sammanfogningsfältet` |
| `join-error-missing-operand` | `operand saknas` |
| `join-error-missing-operand-after` | `operand saknas efter { $file }` |
| `join-error-extra-operand` | `extra operand { $operand }` |
| `join-error-conflicting-empty-field` | `motstridiga ersättningssträngar för tomma fält` |

Övriga rust-coreutils-komponenter var fullständiga efter att `chmod`, `mkdir` och `sort` accepterats.

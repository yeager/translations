# Rust Coreutils: Weblate-granskning 2026-10-28

Den svenska Weblate-översikten visade 11 ofärdiga poster. Fem av dem saknade
förslag och granskades i den aktuella webbredigeraren. Följande texter är
redo att sparas, men har inte publicerats ännu.

| Komponent | Nyckel | Engelska | Föreslagen svenska |
| --- | --- | --- | --- |
| `cp` | `cp-error-cannot-open-for-reading` | `cannot open { $source } for reading: permission denied` | `kan inte öppna { $source } för läsning: behörighet saknas` |
| `cut` | `cut-help-whitespace-delimited` | `use any run of blanks (Space/Tab, plus Unicode spaces in a UTF-8 locale) as delimiter; ignore leading and trailing blanks with 'trimmed'` | `använd en följd av blanktecken (mellanslag, tabb och Unicode-blanksteg i en UTF-8-lokal) som avgränsare; ignorera inledande och avslutande blanktecken med ”trimmed”` |
| `numfmt` | `numfmt-error-multiple-field-specifications` | `multiple field specifications` | `flera fältspecifikationer` |
| `rm` | `rm-error-dangerous-recursive-operation-same-as-root` | `it is dangerous to operate recursively on { $path } (same as '/')` | `det är farligt att utföra rekursiva åtgärder på ”{ $path }” (samma som ”/”)` |
| `sort` | `sort-incompatible-tabs` | `incompatible tabs` | `inkompatibla tabbar` |

Kontroll före publicering: jämför varje post med den då aktuella Weblate-raden
och bevara Fluent-variablerna exakt. Spara därefter komponentvis och kontrollera
att filtreringen inte längre visar posterna som ofärdiga.

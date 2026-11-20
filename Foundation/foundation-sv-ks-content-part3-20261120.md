# Foundation – svenska granskning: ks_content.json, del 3

Datum: 2026-11-20  
Metod: Crowdin API; `l10n-lint --language sv`; `hunspell -d sv_SE`.

| Sträng-ID | Engelsk källa | Tidigare svenska | Föreslagen svenska | Resultat |
|---|---|---|---|---|
| 26504 | The Tax Collector will seek your attention again later. | Skatteindrivaren kommer att söka din uppmärksamhet igen senare. | Skatteindrivaren kommer att kontakta dig igen senare. | Sparad i Crowdin (201) |
| 26506 | Tax Collector… (flerradig händelsetext) | Skatteindrivaren skyndar till dig … De har hittat den! … | Skatteindrivaren skyndar till dig … Hen har hittat den! … | Sparad i Crowdin (201) |
| 26520 | Dragon's Treasure Found! | Drakens skatt hittad! | Drakens skatt har hittats! | Sparad i Crowdin (201) |

## Validering

- `l10n-lint`: inga problem.
- `hunspell-sv`: inga stavningsanmärkningar.
- Styckeindelning och skiljetecken bevarades.
- Lint rapporterade endast en informationsvarning om typografiska icke-ASCII-apostrofer i den engelska källan.

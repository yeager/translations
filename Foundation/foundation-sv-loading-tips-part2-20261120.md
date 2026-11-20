# Foundation – svenska granskning: loading_tips.json, del 2

Datum: 2026-11-20  
Metod: Crowdin API; `l10n-lint --language sv`; `hunspell -d sv_SE`.

| Sträng-ID | Engelsk källa | Tidigare svenska | Föreslagen svenska | Resultat |
|---|---|---|---|---|
| 23325 | Right-click on resources displayed on the HUD to toggle their {1} Tracker. | …växla mellan deras {1} spårare. | …växla deras {1}-spårning. | Sparad i Crowdin (201) |
| 23327 | Promoting villagers is key to prosperity … | Att främja byborna är nyckeln … | Att befordra byborna är nyckeln … | Sparad i Crowdin (201) |

## Validering

- `l10n-lint`: inga problem.
- `hunspell-sv`: inga stavningsanmärkningar.
- Platshållaren `{1}` bevarades.

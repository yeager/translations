# Foundation – svenska granskning: achievements.release.json, del 1

Datum: 2026-11-20  
Metod: Crowdin API; `l10n-lint --language sv`; `hunspell -d sv_SE`.

| Sträng-ID | Engelsk källa | Tidigare svenska | Föreslagen svenska | Resultat |
|---|---|---|---|---|
| 13670 | Expansion | Expansion | Utvidgning | Sparad i Crowdin (201) |
| 13676 | Own 30 Territories | Äg 30 territorium | Äg 30 territorier | Dubblettöversättning finns redan i Crowdin; API avvisade ny identisk proposal (400). |

## Validering

- `l10n-lint`: inga problem.
- `hunspell-sv`: inga stavningsanmärkningar.
- För sträng 13676 visar Crowdin fortfarande den äldre godkända texten; den identiska befintliga översättningen måste röstas på eller godkännas i Crowdin.

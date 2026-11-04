# Slutgranskning: Blender Manual batch 28

Granskad fil: `blender-manual-sv-review-batch-20261104-28.po`

Underlag: råexportens `animation/actions.rst:201–263`,
`agent-animation-next-candidates-20261104.md`,
`agent-animation-next-review-20261104.md`, Blender UI-exporten och
`TERMINOLOGY.md`.

| Referens | Bedömning | Kontroll |
| --- | --- | --- |
| `actions.rst:201` | Godkänd | `datablock`, `åtgärd` och `slot` följer termlistan. |
| `actions.rst:207` | Godkänd | Synlig RST-text använder den belagda formen `egenskapsredigeraren`; målet är intakt. |
| `actions.rst:210` | Godkänd | `åtgärdsredigerarens rubrik` återger UI-kontexten. |
| `actions.rst:220` | Godkänd | RST-referensen och dess mål är bevarade. |
| `actions.rst:223` | Godkänd | RST-referensen och dess mål är bevarade. |
| `actions.rst:243` | Godkänd | Rubriken är idiomatisk och använder `datablock`. |
| `actions.rst:245` | Godkänd | De två motgranskade följdrättelserna `ersätta den med en annan åtgärd` och `Gör det samtidigt` är införda. |
| `actions.rst:250` | Godkänd | `Ersätt åtgärd` är den belagda UI-etiketten. |
| `actions.rst:251` | Godkänd | `NLA-remsor`, `åtgärdsbegränsningar` och den synliga RST-texten stämmer med terminologin. |
| `actions.rst:255` | Godkänd | `Omdirigera användare` är den belagda UI-etiketten. |
| `actions.rst:256` | Godkänd | Följdrättelsen `för *alla* användare` är införd; RST-målet är intakt. |
| `actions.rst:263` | Godkänd | `NLA-redigeraren` och `NLA-system` följer UI och teknisk kontext. |

## Verktygsresultat

- `msgfmt --check`: godkänd.
- `l10n-lint`: 0 fel och 0 varningar.
- `svlang skrivregler`: inga skrivregelfel i de svenska måltexterna.
- Hunspell-rester är RST-roller, källreferenser, API-mål, engelska `msgid`
  och Blenderidentiteter; inga svenska stavfel återstår.
- Gitleaks: inga träffar.
- `git diff --check`: inga fel i Blender-scope.

Alla tolv poster godkänns för den samlade, ännu ej uppladdade
manualbatchen.

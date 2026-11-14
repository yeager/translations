# PrismLauncher Swedish review — 2026-11-14

The official contribution route is Hosted Weblate, not a pull request to the
translation repository.

## Reviewed entries

| Source | Swedish | Result |
| --- | --- | --- |
| `Blocked path traversal in %1` | `Blockerade sökvägstraversering i %1` | Submitted through Weblate and read back as translated. |
| `On Windows, symbolic links may require admin permission to create.` | `I Windows kan skapande av symboliska länkar kräva administratörsrättigheter.` | Verified already translated upstream; no duplicate edit submitted. |
| `Version` (TexturePackFolderModel) | `Version` | Submitted through Weblate and read back as translated. Source equality is intentional in this UI context. |

## Checks

- `lrelease`: 2,534 finished translations and 47 untranslated source strings.
- `git diff --check`: passed.
- `Gitleaks`: passed.
- Targeted Hunspell-sv was run at low CPU priority. It flagged only the
  deliberate technical compound `sökvägstraversering`.

## Upstream readback

Hosted Weblate readback after submission reported 2,533 translated strings,
48 unfinished strings, 47 empty strings, and one remaining needs-editing
string. The remaining needs-editing string is not one of the three entries
above.

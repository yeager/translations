# Dwarf Fortress 50.* — Lua batch 05

- **Project/resource/language:** `dwarf-fortress-steam` / `lua` / Swedish (`sv`)
- **Reviewed:** 2026-11-15
- **Scope:** three procedural sickness interactions and their player-facing verb forms.
- **Changes saved upstream:** 6
  - `Sicken` → `Gör sjuk` (contexts `COUGH_BLOOD`, `VOMIT_BLOOD`, `NAUSEA`)
  - `feel sick:looks sick` → `känner mig sjuk:ser sjuk ut` (same contexts)
- **Context checked:** `data/vanilla/vanilla_procedural/scripts/init.lua:136–153`.
- **Validation:** JSON parse, l10n-lint automatic JSON detection, svlang, Hunspell-sv, whitespace diff check and Gitleaks passed.
- **Read-back:** all six targets were visible in the authenticated Transifex editor immediately after saving.

Upstream project review/merge and release inclusion remain outside this save operation.

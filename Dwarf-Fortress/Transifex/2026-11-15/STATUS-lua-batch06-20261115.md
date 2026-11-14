# Dwarf Fortress 50.* — Lua batch 06

- **Project/resource/language:** `dwarf-fortress-steam` / `lua` / Swedish (`sv`)
- **Reviewed:** 2026-11-15
- **Scope:** procedural suffocation interaction label and player-facing verb form.
- **Changes saved upstream:** 2
  - `Suffocate` → `Kväv`
  - `feel breath leaving you:pauses` → `känner hur andningen upphör:stannar upp`
- **Context checked:** `SUFFOCATE`, `data/vanilla/vanilla_procedural/scripts/init.lua:184–185`.
- **Validation:** JSON parse, l10n-lint automatic JSON detection, svlang, Hunspell-sv, whitespace diff check and Gitleaks passed.
- **Read-back:** both targets were visible in the authenticated Transifex editor immediately after saving.

Upstream project review/merge and release inclusion remain outside this save operation.

# Dwarf Fortress 50.* — Lua batch 03

- **Project/resource/language:** `dwarf-fortress-steam` / `lua` / Swedish (`sv`)
- **Reviewed:** 2026-11-15
- **Scope:** procedural pain interaction labels and player-facing verb forms.
- **Changes saved upstream:** 2
  - `Cause pain` → `Orsaka smärta`
  - `feel intense pain:grimaces` → `känner intensiv smärta:grimaserar`
- **Context checked:** `PAIN`, `data/vanilla/vanilla_procedural/scripts/init.lua:104–105`.
- **Validation:** JSON parse, `l10n-lint`, `svlang`, Hunspell-sv, whitespace diff check and Gitleaks passed.
- **Read-back:** both targets were visible in the authenticated Transifex editor immediately after saving.

Upstream project review/merge and release inclusion remain outside this save operation.

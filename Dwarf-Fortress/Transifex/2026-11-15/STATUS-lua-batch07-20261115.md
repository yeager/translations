# Dwarf Fortress 50.* — Lua batch 07

- **Project/resource/language:** `dwarf-fortress-steam` / `lua` / Swedish (`sv`)
- **Reviewed:** 2026-11-15
- **Scope:** procedural blindness interaction label and player-facing verb form.
- **Changes saved upstream:** 2
  - `Blind` → `Förblinda`
  - `see your sight is fading:pauses` → `ser hur synen avtar:stannar upp`
- **Context checked:** `BLIND`, `data/vanilla/vanilla_procedural/scripts/init.lua:192–193`.
- **Validation:** JSON parse, l10n-lint automatic JSON detection, svlang, Hunspell-sv, whitespace diff check and Gitleaks passed.
- **Read-back:** both targets were visible in the authenticated Transifex editor immediately after saving.

Upstream project review/merge and release inclusion remain outside this save operation.

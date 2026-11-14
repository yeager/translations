# Audit: Dwarf Fortress Steam `hardcoded_steam`, batches 58–80

- **Date:** 2026-11-14
- **Scope:** 23 archived JSON delta batches, containing 526 translation-ID entries.
- **JSON validation:** All 23 batch files parse successfully.
- **Duplicate-ID audit:** Three duplicate IDs were found. Each is an intentional batch 66 correction of a prior translation that had localised a direction code:
  - `Ice Upward Track (NE)`: corrected from `NO` to `NE`.
  - `Track/Ramp (W)`: corrected from `V` to `W`.
  - `Ice Downward Track (NE)`: corrected from `NO` to `NE`.
- **Upstream verification:** Direct Transifex API readback confirms the current values retain `NE` and `W` exactly.
- **Security:** `gitleaks detect --no-git --source …/2026-11-14 --redact` passed with no leaks.
- **Conclusion:** There are no unintended duplicate translation IDs in this archive range. The three retained duplicates document necessary game-code corrections.

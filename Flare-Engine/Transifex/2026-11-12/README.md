# Flare Engine, svenska på Transifex

- Projekt/resurs: `o:flareorg:p:flare-engine:r:engine-pot`
- Versionskälla: Flare Engine `v1.15`, taggad 2026-05-23.
- Omfattning: 68 tidigare oöversatta svenska UI-strängar.
- Status: uppladdade i ett Transifex API-anrop och återlästa. Resursen har 0 oöversatta svenska strängar efter uppladdningen. Formell upstream-granskning är inte verifierad.

## Terminologi

| Engelska | Svenska | Kontext |
| --- | --- | --- |
| stat | egenskap | Rollspelsattribut och uppgraderingspoäng. |
| loot | byte | Föremål som kan plockas upp. |
| action bar | åtgärdsrad | Konfigurerbar rad med handlingar. |
| resist | motstånd mot | Skydd mot skada eller negativ effekt. |
| shortcut | genväg | Sparat konsolkommando eller tangentbindning. |
| procedural | procedurell | Genererad karta eller segmentkarta. |

## Kontroller

- Källkod och befintlig svensk PO-katalog granskade för sammanhang och befintliga termer.
- `msgfmt --check` godkänd för projektets svenska PO-katalog.
- C-format (`%s`, `%d`), markup och radbrytningar kontrollerade och bevarade.
- `l10n-lint` och `svlang svengelska`: inga fel.
- `hunspell-sv`: facktermer och produktterminologi bedömda i sammanhang.
- `git diff --check` och `gitleaks detect --no-git --redact`: godkända.

Råexporten bevaras oförändrad. Kandidatfilerna utgör granskningsdeltat.

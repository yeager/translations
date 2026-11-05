# Blender Manual: svensk granskningsbatch 58

Datum: 5 november 2026

Källa: `exports/2026-11-04/blender-manual-manual-sv.po` och den aktuella
svenska Blender-UI-katalogen.

## Kontext och omfattning

Tio poster i Node Wranglers flöde för omdirigeringar, länkning och
bildsekvenser. `Reroute` heter **Omdirigering** i Blender, inte *omväg*,
och operatören `Detach Outputs` heter **Koppla bort utgångar**. Därför följer
både rubriker, menyvägar och beskrivningar samma kontextberoende UI-termer.

De delade UI-etiketterna `Relative Path` och `Start Frame` används på flera
ställen i manualen. De rättas till **Relativ sökväg** respektive
**Startbildruta**, vilket överensstämmer med den aktuella UI-katalogen och
fungerar i såväl bildsekvenser som animation och filhantering. Den längre
hjälptexten använder därför *startbildruta*, inte den felaktiga formen
*starta ram*.

## Kontroller

- `msgfmt --check --statistics`: 10 översatta meddelanden och godkänd syntax.
- Radvis jämförelse av `(msgctxt, msgid)` mot råexporten: 10/10 träffar.
- UI-katalogen har kontrollerats för `Reroute`, `Add Reroutes`,
  `Detach Outputs`, `Link Active to Selected`, `Relative Path` och
  `Start Frame`.
- l10n-lint, svlang, Hunspell, översättningsminne, `git diff --check` och
  Gitleaks körs före arkivering.

Råexporten är orörd. Deltafilen är en lokal kandidat och är inte uppladdad
till Blender Translate.

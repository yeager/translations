# Ymir: svenska gemensamma inställningsreglage

Den lokala Ymir-patchen ansluter centrala videoinställningar till det svenska översättningsskiktet, inklusive grafikmotor, adapter, VDP-rendering och deinterlace.

- Kontroll: `git diff --check` utan fel, svlang utan skrivregelfel och Gitleaks utan träffar.
- Hunspell markerade endast tekniktermerna SH-2, SDL och VDP.
- CMake-konfigureringen saknar fortfarande `spirv-cross`; någon kompileringskontroll kan därför inte köras ännu.
- Patchen är en full, lokal Ymir-diff och är inte skickad uppströms.

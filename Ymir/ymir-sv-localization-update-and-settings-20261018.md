# Ymir: svenska uppdateringsdialoger och inställningsflikar

Den lokala Ymir-patchen utökar svenska texter för uppdateringsdialogen och alla inställningsflikar.

- Kontroll av källändringarna: `git diff --check` utan fel och Gitleaks utan träffar.
- Översättningskatalogen innehåller 239 unika svenska nycklar.
- CMake-konfigureringen når projektets shadersteg men stoppar eftersom `spirv-cross` saknas lokalt.
- Patchen är en full, lokal Ymir-diff och är inte skickad uppströms.

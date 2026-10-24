# ComfyUI svensk ombasning, manuell batch 1

Källan har ombasats lokalt mot ComfyUI_frontends huvudgren den 24 oktober 2026.

Batchen omfattar:

- 79 nya eller ändrade texter i agentpanelen
- 4 nya kortkommandon
- 6 nya inställningsetiketter och verktygstips
- uppdatering av svensk översättningsväg i i18n-konfigurationen

Kontroller: JSON-parsning, platshållarjämförelse för ändrade kataloger,
svlang, l10n-lint 1.23.27, TypeScript-typkontroll och avgränsad Gitleaks.

Grenen är inte pushad efter ombasningen. Återstående källnycklar måste
översättas manuellt innan PR:n kan uppdateras utan att försämra kvaliteten.

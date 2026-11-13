# Obsidian, svensk UI-verifiering, 13 november 2026

Granskningen av inventeringsposten för Obsidian är klar. Den tidigare uppgiften
om att svensk resurs saknades i `obsidian-releases` var missvisande: Obsidian
förvaltar appens svenska strängar i det separata officiella arkivet
`obsidianmd/obsidian-translations`.

Kontrollerat mot revision `db6a392c3a378ebcc98033cf3d9fe6c8a150b98f`:

- `translations/sv.txt` har samma uppsättning nycklar som den engelska
  källfilen, utan saknade, extra eller tomma översättningar.
- Projektets webbkontroll rapporterar `sv: OK (1246 keys)`.
- Projektets språkregister markerar svenska som komplett för app, webb och
  hjälpdokumentation.
- Den senaste appuppdateringen med svenska strängar gjordes av `lishid` den
  3 november 2026. Senaste uttryckliga svenska bidraget är `ReineW`, 15 juli
  2026.

Ingen ändring behövde göras och ingen upstream-åtgärd är därför aktuell.

Källor:

- https://github.com/obsidianmd/obsidian-translations
- https://obsidian.md/help/translations

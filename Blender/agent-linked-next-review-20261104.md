# Motgranskning: Blender Manual — `linked_libraries/proxy.rst`

## Kontrollunderlag

Jag kontrollerade kandidatrapportens påstående mot samtliga lokala
manualexporter från 2026-11-04:

- `blender-manual-manual-sv.po`
- `blender-manual-manual-4-5-sv.po`
- `blender-manual-manual-5-2-sv.po`
- `blender-manual-manual-5-3-sv.po`

En exakt sökning efter `files/linked_libraries/proxy.rst` gav noll träffar i
varje fil. Det finns visserligen UI-strängar för proxyer i
`blender-ui-ui-sv.po`, men de är inte dokumentationssidan som uppgiften
avsåg och är därför inte grund för en manuell kandidat.

## Slutsats

Kandidatrapportens slutsats godkänns: proxysidan saknas i den lokala
exportuppsättningen, och det finns inga säkra nya `msgid`/`msgstr`-ändringar
att föreslå från denna avgränsning. `library_overrides.rst` och
`link_append.rst` ska fortsatt hanteras i sina separata granskningsspår för
att undvika dubbla eller motstridiga ändringar.

Inga PO-filer har ändrats.

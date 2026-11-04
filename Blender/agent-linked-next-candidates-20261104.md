# Granskning: Blender Manual — `linked_libraries/proxy.rst`

Källa: `exports/2026-11-04/blender-manual-manual-sv.po`
Avgränsning: `files/linked_libraries/proxy.rst` samt direkt efterföljande
filer i samma del av manualen.

## Resultat

Råexporten innehåller ingen post med referensen
`files/linked_libraries/proxy.rst`. Sökning gjordes även i de lokalt
nedladdade versionerna 4.5, 5.2, 5.3 och den versionslösa manualexporten;
ingen innehåller den referensen. Det tyder på att proxysidan har tagits bort
eller flyttats uppströms, och därför finns ingen säker `msgid`/`msgstr`-ändring
att föreslå för just den sidan.

De efterföljande aktuella filerna i exporten är
`library_overrides.rst` och `link_append.rst`. De är redan behandlade i de
separata, parallella kandidatunderlagen
`agent-linked-candidates-20261104.md`,
`agent-linked-deep-candidates-20261104.md` och
`agent-linkappend-deep-candidates-20261104.md`. För att inte duplicera eller
konkurrera med deras föreslagna ändringar lämnar denna avgränsade granskning
inga ytterligare kandidater.

Status: ingen råfil, deltafil eller befintlig kandidatfil har ändrats av denna
granskning. När en aktuell upstream-export åter har en `proxy.rst`-referens
bör sidan granskas på nytt i den exporten.

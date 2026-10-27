# Zammad: kontroll av aktuell release

Kontrollerad 2026-10-27 mot Zammads officiella Git-taggar på GitHub.

GitHub har inga särskilda releaseobjekt för projektet, men den stabila taggen
`7.2.2` pekar på en commit från 2026-10-08 med meddelandet "Release Zammad
7.2.2.". Det är en aktuell officiell release och uppfyller
48-månadersregeln. Det finns dessutom en senare förhandsversion,
`7.3.0-alpha`.

De två lokala deltafilerna för stable och development har validerats med
`msgfmt`, `l10n-lint`, `svlang` och Gitleaks. `l10n-lint` ger två varningar
per fil för "redaktör". De är granskade felträffar: i rollen
"Kunskapsbasredaktör" är ordet redaktör en avsiktlig och mer precis svensk
benämning än redigerare.

# elementary Settings Desktop, svensk statusverifiering

Datum: 14 november 2026

Den officiella Weblate-API:n visar att komponenten **Settings/Desktop Plug**
har 94 strängar på svenska: 93 översatta, en fuzzy och inga fallerande
kontroller. Den enda fuzzy-posten är den tidigare granskade
`accent color` (en ändring av källans versalisering från `Accent Color`).
Måltexten är fortfarande `Accentfärg`, vilket är korrekt som etikett i
inställningsgränssnittet.

Den redan arkiverade deltafilen
`../2026-11-13-settings-desktop/elementary-settings-desktop-sv-accent-color.delta.po`
kan därför importeras utan språklig ändring när skrivåtkomst till elementarys
Weblate finns. Ingen upstream-import gjordes i denna uppföljning: servern
saknar en åtkomlig inloggning eller API-token i den aktuella miljön.

Projektets senaste GitHub-release är `8.1.0-rc3`, publicerad 11 december
2025, och ligger inom projektets aktualitetsgräns.

Kontroller: officiellt Weblate-API, publicerad GitHub-release, kontroll av
den befintliga deltafilens måltext samt diffkontroll och Gitleaks före
arkivering. `msgfmt`, l10n-lint, svlang och Hunspell-SV har redan passerat
för deltafilen den 13 november; inga översättningstextändringar har gjorts
i denna verifiering.

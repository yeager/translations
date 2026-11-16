# Audacity – svensk kataloggranskning

Senast uppdaterad: 2026-11-16

Audacitys svenska UI-kataloger är granskade rad för rad och den samlade
ändringen är inskickad som [PR #12778](https://github.com/audacity/audacity/pull/12778).
Den ersätter den stängda, äldre PR #12759.

PR:en ändrar endast svenska kataloger:

- `au3/locale/sv.po`
- `share/locale/audacity_sv.ts`

Den omfattar bland annat konsekvent terminologi för ljudrendering,
markörintervall, menyalternativ och översättarattributering.

## Verifierad upstreamstatus

Kontrollerad 16 november 2026: PR #12778 är öppen, inte ett utkast och har en
godkänd CodeRabbit-kontroll. Det finns inga språkrelaterade kommentarer att
åtgärda. GitHub rapporterar ändå `REVIEW_REQUIRED` och `BLOCKED`, alltså krävs
mänsklig upstreamgranskning innan merge.

PR-mallen har dessutom en omarkerad CLA-ruta. Commitsen använder
`github@danielnylander.se`, men en CLA är en juridisk bekräftelse och måste
göras av Daniel själv enligt Audacitys etablerade flöde. Ingen sådan bekräftelse
har påståtts eller gjorts automatiskt.

## Kontroller

PR-beskrivningen redovisar `msgfmt --check`, l10n-lint, svlang, Hunspell,
git-diffkontroll och Gitleaks. Dessa kontroller avser katalogändringarna; de
utgör inte bevis på upstream-merge.

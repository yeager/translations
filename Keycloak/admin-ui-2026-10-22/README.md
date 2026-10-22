# Keycloak Admin UI, 22 oktober 2026

Den här kopian utgår från den aktuella svenska exporten från Hosted Weblate.

Ändringarna kompletterar de sex saknade SSF-strängarna och rättar två befintliga fel i exporten:

- `inviteSentError` hade en korrekt översättning, men också en extra nyckellös rad längre ned i filen. Den felaktiga raden är borttagen.
- `authenticatorRefConfig.maxAge.help` innehöll dubbelprepositionen `i i`.

Kontroller före uppladdning:

- `l10n-lint --language sv`: utan fel och varningar.
- `svlang skrivregler`: utan skrivregelfel för de ändrade strängarna.
- Platshållare: kontrollerade mot engelsk källfil.
- Hunspell: återstående träffar är produktnamn, protokollnamn och etablerade tekniska termer.
- Gitleaks: inga hemligheter hittades.

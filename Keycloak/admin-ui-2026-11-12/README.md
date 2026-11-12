# Keycloak Admin UI, svenska, 2026-11-12

- Plattform: Hosted Weblate, projekt `keycloak`, komponent `admin-ui`, språk `sv`.
- Källa: aktuella enheter i Weblate och Keycloaks engelska `.properties`-källor.
- Batch: 7 tidigare tomma strängar granskade och sparade via den inloggade Weblate-redigeraren.
- Upstream-resultat: samtliga sju sparades som **väntar på granskning**. Weblate visade efter sparningen 2 återstående ofärdiga strängar; de är befintliga strängar som behöver redigeras, inte denna batch.
- Kontroller: JSON-/format-/markupkontroll, em dash-policy, l10n-lint, `git diff --check` och Gitleaks godkända. `svlang` och Hunspell flaggade endast etablerade Keycloak-termer såsom `Realm`, `SAML-assertioner`, `protokollmappare` och `ämnestoken`.
- Begränsning: `msgfmt` är inte tillämpligt eftersom underlaget är en Weblate-deltafil i JSONL och ingen PO-fil har ändrats.

Status: inskickat till Weblate och väntar på upstream-granskning.

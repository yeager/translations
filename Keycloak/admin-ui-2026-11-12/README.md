# Keycloak Admin UI, svenska, 2026-11-12

- Plattform: Hosted Weblate, projekt `keycloak`, komponent `admin-ui`, språk `sv`.
- Källa: aktuella enheter i Weblate och Keycloaks engelska `.properties`-källor.
- Batch: 9 strängar granskade och sparade via den inloggade Weblate-redigeraren: 7 tidigare tomma samt 2 som behövde redigeras efter utökade källsträngar.
- Upstream-resultat: samtliga nio sparades som **väntar på granskning**. Weblate visade därefter 4 286 av 4 286 strängar som översatta, 12 väntar på granskning, 0 oöversatta och 0 som behöver redigeras.
- Kontroller: JSON-/format-/markupkontroll, em dash-policy, l10n-lint, `git diff --check` och Gitleaks godkända. `svlang` och Hunspell flaggade endast etablerade Keycloak-termer såsom `Realm`, `SAML-assertioner`, `protokollmappare` och `ämnestoken`.
- Begränsning: `msgfmt` är inte tillämpligt eftersom underlaget är en Weblate-deltafil i JSONL och ingen PO-fil har ändrats.

Status: komponenten är komplett översatt; batchen är inskickad till Weblate och väntar på upstream-granskning.

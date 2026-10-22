# Keycloak Account backend, 22 oktober 2026

Den svenska Account backend-komponenten kontrollerades lokalt med källfilen från Hosted Weblate och därefter rad för rad i Weblate.

## Genomförd granskning

- 34 strängar som väntade på granskning genomlästes mot engelsk källa och godkändes en i taget.
- `filterByName` rättades från tre punkter till svenskt ellipstecken: `Filtrera efter namn…`.
- Alla 385 strängar visas därefter som godkända i Hosted Weblate.

## Kontroller

- `l10n-lint --language sv`: utan fel.
- `svlang skrivregler --enable-interpunktion`: utan skrivregelfel efter rättelsen.
- Platshållare och nycklar stämde mot den engelska källfilen.
- Gitleaks: inga hemligheter hittades.

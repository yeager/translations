# Keycloak Account UI, 22 oktober 2026

Account UI granskades rad för rad i Hosted Weblate.

## Ändringar

- De fyra väntande strängarna för programsessioner kontrollerades mot engelsk källa och godkändes.
- `endApplicationSessionMessage` använder `offlinesessioner` utan bindestreck.
- Sex befintliga fel rättades: utloggning, delning, inloggningsstatus och konsekvent terminologi för klientomfång.
- Tre UI-etiketter använder nu svenskt ellipstecken.

## Kontroller

- `l10n-lint --language sv`: utan fel.
- `svlang skrivregler --enable-interpunktion`: utan skrivregelfel.
- Gitleaks: inga hemligheter hittades.
- Hosted Weblate visar 242 av 242 godkända strängar.

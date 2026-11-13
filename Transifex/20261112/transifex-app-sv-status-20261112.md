# Transifex App, svenska, 2026-11-12

- Plattform och upstreamkanal: Transifex API.
- Projekt: `o:transifex:p:transifex-app`; resurs: `transifex-app`.
- Projektstatus före batchen: 8 271 strängar, 8 267 översatta och 4 oöversatta.
- Batch: 4 svenska HubSpot- och Jira-texter granskade med integrationskontext och uppladdade i en API-batch.
- Upstream-resultat: HTTP 200. Direkt API-återläsning bekräftade 4 av 4 sparade måltexter.
- Kontroller: l10n-lint utan fel, svlang 10/10, JSON-/struktur-, em dash- och trippelkonsonantkontroll, diffkontroll och Gitleaks godkända. Hunspell träffade endast produktnamnen Transifex, HubSpot och Jira samt det avsiktliga sammansättningsbindestrecket i `webb- och målsidor`.
- Begränsning: `msgfmt` är inte tillämpligt eftersom källan och deltat är Transifex JSON, inte PO.

Status: uppladdat och verifierat upstream.

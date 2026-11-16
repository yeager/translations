# Weblate Application — svensk granskningsbatch 059

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Application  
Språk: svenska

## Omfattning

En UI-sträng för slutförd registrering har omformulerats för naturligare svenska:

> Du kan nu slutföra registreringen och skapa ett Weblate-konto.

## Lokal granskning

Texten har granskats i registreringsflödets UI-kontext. Den är direkt och handlingsinriktad, undviker den stela formuleringen ”står i begrepp att” och behåller Weblate som produktnamn.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk applikations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

Ändringen sparades i Hosted Weblate via REST API och lästes tillbaka som översatt, med statusen **väntar på granskning**. Den är inte verifierad som upstream-granskad eller mergad.

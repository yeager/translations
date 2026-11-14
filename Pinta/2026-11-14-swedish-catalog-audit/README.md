# Pinta – svensk katalogkontroll

Datum: 2026-11-14

Komponent: `po/sv.po`
Källversion: Pinta 3.1.2, publicerad 2026-04-02

## Resultat

Pinta är ett bildredigeringsprogram med arbetsflöden för bland annat ritning,
lager, markering, beskärning och justeringar. Den svenska PO-katalogen i den
aktuella huvudgrenen innehåller 644 översatta poster. Inga poster är oöversatta
eller markerade som osäkra.

Projektets README hänvisar översättare till Hosted Weblate. Därför gjordes ingen
Git-ändring eller upstreaminsändning: den lokala källkatalogen saknar saknade
eller osäkra svenska strängar. Den publika Weblate-statusen gick inte att läsa
utan behörig API-session (HTTP 403), så den verifierar inte en separat aktuell
Weblate-procent.

## Kontroller

- `msgattrib --untranslated`: 0 poster.
- `msgattrib --only-fuzzy`: 0 poster.
- `msgfmt --check --statistics`: 644 översatta poster.
- Gitleaks: godkänd.

## Status

Lokalt kontrollerat och arkiverat. Ingen ändring behövde skickas upstream.

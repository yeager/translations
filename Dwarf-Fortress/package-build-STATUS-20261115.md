# DFint package-build – svenska

Datum: 2026-11-15  
Projekt: `dwarf-fortress-translation/package-build`  
Resurs: `messages`  
Kanal: Transifex REST API

## Resultat

Den svenska språkförfrågan var godkänd i Transifex. Alla 32 strängar i
`messages` översattes och skrevs via API, inklusive den svenska pluralformen
för `%(num)d hour ago`.

API-återläsningen efter inskick visade:

| Mått | Antal |
| --- | ---: |
| Strängar totalt | 32 |
| Översatta | 32 |
| Oöversatta | 0 |
| Ogranskade i Transifex | 32 |

## Terminologiska beslut

- `package` är *paket* och `package builder` är *paketbyggare*.
- `DF variant` är *DF-variant* och `DF version` är *DF-version*.
- `dfint-installer` och `dfhooks` är produkt- respektive biblioteksnamn och
  är därför oförändrade.
- `%(num)d` och de svenska pluralformerna bevarades i tidsangivelsen.

## Verifiering

API-återläsning bekräftade att ingen sträng saknas. Transifex-granskning är
en separat upstreamstatus och är ännu inte genomförd.

## Kompletterande radgranskning

Den 15 november 2026 hämtades den aktuella svenska `messages`-resursen igen
från Transifex och samtliga 32 strängar kontrollerades mot källtexten,
applikationens paketbyggarkontext och terminologin ovan. Ingen ändring behövdes:
alla översättningar är kompletta och kontextkorrekta.

`l10n-lint`, `svlang`, Hunspell-granskning och Gitleaks passerade. Hunspell
rapporterar endast avsiktliga produkt- och platshållarnamn: `DF-lokalisering`,
`DF-variant`, `DF-version`, `dfhooks`, `dfint-installer` och `num`. `msgfmt`
är inte tillämpligt på resursens JSON-format.

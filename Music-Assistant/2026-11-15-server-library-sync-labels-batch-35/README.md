# Music Assistant Server – bibliotekssynkronisering, batch 35

Datum: 2026-11-15

## Omfattning

11 svenska etiketter för val av import och synkronisering mellan en
musikkällas bibliotek och Music Assistant.

## Terminologi och kontext

- *Synkronisera*, *källans bibliotek*, *spellistespår* och
  *tvåvägssynkronisering* används genomgående för samma riktning och funktion.
- Music Assistant bevaras som produktnamn.

## Kontroller

- Källtext och nycklar kontrollerade mot aktuell `en.json`.
- `l10n-lint --language sv`: godkänd.
- `svlang skrivregler`: godkänd.
- Hunspell-svenska: kvarvarande träff är produktnamnet Music Assistant.
- JSON-syntax, diffkontroll och Gitleaks: godkända.
- `msgfmt` är inte tillämpligt eftersom resursformatet är JSON.

## Status

En tidigare snabbkontroll var inte tillräcklig för att intyga radvis
verifiering. Två rader är nu verifierade och tre är manuellt sparade i Lokalise;
sex återstår.
Arkivering och push sker efter varje ändring:
Lokalise-tokenen saknar rättigheten `Upload files`.

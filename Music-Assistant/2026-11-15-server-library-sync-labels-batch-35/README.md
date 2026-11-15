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

Den radvisa granskningen är klar: tre rader är verifierade och åtta är
manuellt sparade i Lokalise. Batchen är arkiverad och pushad till
`yeager/translations`; detta är inte ett merge-besked för Music Assistant.
Lokalise-tokenen saknar rättigheten `Upload files`.

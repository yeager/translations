# Music Assistant Server – vanliga fel, batch 12

Datum: 2026-11-15

## Omfattning

13 svenska felmeddelanden från `common.errors` för användare, otillgängliga
funktioner, fjärranslutningar och hårdvarukrav för lokal ljudanalys.

## Terminologi och kontext

- AVX2, CPU, RAM, Intel Haswell, AMD Zen, Proxmox, TrueNAS och CPU-inställningen
  `host` är tekniska namn och kodvärden och behålls.
- *Ljudanalys på enheten* är användargränssnittets lokala analys, inte
  molnbearbetning.
- Platshållarna `{0}`, `{1}` och `{2}` har bevarats exakt från engelsk källa.

## Kontroller

- Källtext, nycklar och platshållare kontrollerade mot aktuell `en.json`.
- `l10n-lint --language sv`: godkänd.
- `svlang skrivregler`: godkänd.
- Hunspell-svenska: kontrollerad; tekniska produkt- och formatnamn är
  avsiktligt bevarade.
- JSON-syntax och diffkontroll: godkända.
- Gitleaks: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt eftersom resursformatet är JSON.

## Status

Lokalt granskad och arkiverad. Inte uppladdad, inskickad, granskad eller
integrerad upstream. Tillsammans med batch 09–11 täcker den återstående
lokala granskningen av `common.errors`.

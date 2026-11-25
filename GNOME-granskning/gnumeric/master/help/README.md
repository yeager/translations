# Gnumeric — hjälp (`master`)

- GNOME-katalog: [Gnumeric manual, svenska](https://l10n.gnome.org/vertimus/gnumeric/master/help/sv/)
- Senaste POT SHA-256: `346f58c8dc45cf0fb6eeba59354aaa80c8811472bc94bbd11d97a1b31b89ad8e`
- Ursprunglig svensk PO SHA-256: `29bed38f66595d234c63b6b98901a9ff13dba75b820dad3443a1c8e834bf4fee`
- Granskad fil SHA-256: `47126d9c58d2e28cf88d1458869b7a38a97bcc1fa790c5c5c3921e6a0134e2c6`
- Granskningsdatum: 2026-11-25
- Last-Translator i granskad PO: Daniel Nylander <gnome@danielnylander.se>

## Statistik mot senaste POT (8955 aktiva poster)

| | Översatta | Fuzzy | Oöversatta |
|---|---:|---:|---:|
| Före granskning | 3963 | 97 | 4895 |
| Efter granskning | 8556 | 0 | 399 |

Nya godkända översättningar: 4593 (varav 4 tidigare fuzzy-poster fick statusen klar utan ändrad text). Rättade befintliga översättningar: 158. Diffen omfattar 4747 ändrade aktiva poster: 4589 från tom till ifylld och 158 rättade.

Samtliga 399 kvarvarande tomma poster är externa bildreferenser (`external ref=...`) som källkatalogen uttryckligen anger inte används som översättningstext. De är därför avsiktligt tomma. Övriga poster har svensk text; kod, formler, formatsträngar och numeriska exempel har bevarats där de inte ska översättas. Inga fuzzy-poster återstår.

## Validering

- `msgfmt --check`: godkänd.
- `l10n-lint --language sv --reference <senaste POT>`: 399 `missing-translation`-träffar gäller enbart de dokumenterade externa bildreferenserna. Kvarvarande varningar gäller svenska gemener i datumexempel, bokstavliga datum-/formelkoder, formatliterals, markup-skyddade metavariabler och markörer i tabell-/kodsampel; deras kategorier och undantag är radgranskade.
- Funktionsnamn jämförda mot POT: 0 avvikelser. Pluralposter: 0. Platshållare, DocBook-taggar och acceleratorer kontrollerade.
- `hunspell-sv`: hela filen kontrollerad. Okända ord består huvudsakligen av produkt-/funktionsnamn, API- och kodidentifierare, matematik, datum-/talexempel och svenska tekniska sammansättningar. Se [Hunspell-undantag](hunspell-exceptions.md).

## Filer

- [Originalfil](gnumeric.master.help.sv.original.po)
- [Granskad fil](gnumeric.master.help.sv.reviewed.po)
- [Unified diff](gnumeric.master.help.sv.diff)
- [Hunspell-undantag](hunspell-exceptions.md)

Damned Lies-inskick: 2026-11-25 via API. Kommentaren var `Granskad och klar. Argumentnamnen i hjälptexterna är översatta; funktionsidentifierarna är bevarade.` Aktivitetssidan visar den inskickade filen och 8 556/0/399. De 399 tomma posterna är källmarkerade externa bildreferenser.

För att klara Damned Lies gräns på 3 MiB skickades en separat uppladdningskopia med endast aktuella POT-poster och utan källradreferenser. Den har exakt samma nycklar, pluralformer och översättningar som den arkiverade granskade filen (`msgfmt --check` godkänd).

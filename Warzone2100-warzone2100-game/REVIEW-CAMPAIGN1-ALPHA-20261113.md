# Warzone 2100 – kampanj 1, svensk granskningsbatch

**Datum:** 2026-11-13

**Projekt och komponent:** Warzone 2100, huvudspel, kampanj 1 – `data/base/messages/strings/cam1strings.txt`

**Omfattning:** 82 översatta meddelanden i den lokala svenska PO-kandidaten. Batchen täcker de sammanhängande uppdrags- och underrättelsetexterna med källreferenser till rad 3–142. Den är inte en komplett svensk spelöversättning.

## Kontext och beslut

Warzone 2100 är ett fritt strategispel i realtid. Texterna visas som mål, uppdragsrubriker, landningsbriefingar och underrättelser. Tonen är kort, militär och direkt.

Följande namn eller förkortningar behålls när de fungerar som synliga spelnamn: **New Paradigm**, **NEXUS** och **LZ**. Återkommande speltermer är konsekvent översatta enligt terminologilistan i samma mapp.

## Lokala kontroller

- `msgfmt --check --statistics`: godkänd, **82 översatta** och 3 865 ännu oöversatta meddelanden i hela katalogen.
- Diffkontroll: `git diff --check` och whitespacekontroll av den otrackade PO-filen är godkända.
- Gitleaks: godkänd utan träffar för `po/sv.po`.
- Kontroll av tre lika konsonanter i följd: inga träffar i batchens svenska måltexter. Träffar i hela PO-filen är engelska källreferenser.
- Hunspell: träffar gäller sammansättningar och speltermer som `synapslänksteknik`, `alfabasuppdrag` och `LZ`; samtliga är granskade.
- svlang: `skrivregler` godkänd. Naturlighetskontrollen flaggar rubrikfragment och korrekta V2-satser som falska positiva.
- l10n-lint: verktyget kan läsa PO-filen, men ger förväntade `missing-translation`-diagnoser för den ofullständiga helkatalogen. Det är därför inte ett godkänt helkatalogtest i detta skede.
- Projektets svenska TM/TBX saknas tills svenska aktiveras i Crowdin.

## Status

- Lokal radgranskning: färdig för denna batch.
- Arkivering och push till detta arkiv: färdig när denna fil och deltakatalogen finns i `main`.
- Crowdin-uppladdning: inte genomförd.
- Upstream-inskick, upstream-granskning och merge: har inte skett.

Crowdin-projektet är projektets etablerade översättningskanal. Svenska saknas fortfarande; kandidaterna hålls därför lokalt och i detta arkiv tills språket har aktiverats och en aktuell export, TM och ordlista kan jämföras.
# Warzone 2100 – kampanj 2, svensk granskningsbatch

**Datum:** 2026-11-13

**Projekt och komponent:** Warzone 2100, huvudspel, övergången till kampanj 2 – `cam1strings.txt:145–157` och `cam2strings.txt:4–107`

**Omfattning:** 61 nya översatta meddelanden. Tillsammans med den föregående batchen omfattar den lokala kandidaten 143 av 3 947 meddelanden. Detta är inte en komplett svensk spelöversättning.

## Kontext och beslut

Källtexterna är uppdragsrubriker, landningsbriefingar och underrättelser som introducerar Bas Beta, The Collective, VTOL-teknik och NASDA. Namnen **The Collective**, **NEXUS**, **NASDA**, **VTOL** och **LZ** behålls. Speltermerna följer den projektspecifika terminologilistan.

## Lokala kontroller

- `msgfmt --check --statistics`: godkänd, **143 översatta** och 3 804 oöversatta meddelanden i hela katalogen.
- Diffkontroll: `git diff --check` samt whitespacekontroll av den otrackade PO-filen är godkända.
- Gitleaks: godkänd utan träffar för `po/sv.po`.
- Kontroll av tre lika konsonanter i följd: inga träffar i batchens svenska måltexter.
- Hunspell: träffar gäller egennamn, förkortningar och granskade sammansättningar, bland annat `bitströmsignaler`, `VTOL-farkoster` och `BETABASUPPDRAG`.
- svlang: `skrivregler` godkänd. Naturlighetskontrollen ger endast falska positiva för rubrikfragment och korrekta V2-satser.
- l10n-lint: kan läsa PO-filen men rapporterar väntade `missing-translation`-diagnoser för resten av helkatalogen; det är inte ett godkänt helkatalogtest medan katalogen är ofullständig.
- Projektets svenska TM/TBX saknas tills svenska aktiveras i Crowdin.

## Status

- Lokal radgranskning: färdig för denna batch.
- Arkivering och push till detta arkiv: färdig och verifierad genom GitHubs API-svar.
- Crowdin-uppladdning, upstream-inskick, upstream-granskning och merge: har inte skett.
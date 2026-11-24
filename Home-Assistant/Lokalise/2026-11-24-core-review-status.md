# Home Assistant Core – aktuell granskningsstatus

Datum: 2026-11-24

## Lokalise-omfattning och export

- Aktiva, synliga Lokalise-nycklar i den exporterade nyckelordningen: **75 660**. Efter snapshoten tillkom 17 nya, synliga nycklar; de bekräftades via API och finns i senaste Core-källan, vilket ger **75 677** synliga nycklar i aktuell omfattning.
- Fullständig Core-API-export: **75 628** strängar med användbara engelska och svenska värden.
- Exporten sparar nu också nycklar som inte kan ingå i TMX i `2026-11-24-core-export-exclusions.jsonl`: **49** unika poster. Av dem är **32 synliga** nycklar utan användbart käll-/målpar (24 tomma på båda språken och 8 utan engelsk källtext, med platshållartext på svenska) och **17 nya synliga** nycklar med tom svensk måltext som saknades i den äldre nyckelordningssnapshoten. De är översättningsbara och ska inte undantas; de har verifierats mot aktuell Core-källa och förs in i granskningskön. Den äldre texten om att de skulle vara dolda var fel.
- Lokalise-API:et kan uppdatera måltext men nekar statusflaggan `is_reviewed` med HTTP 403, `No permission to update translation status`. Lokalise-granskningsflaggan är därför inte satt; ändrade texter är däremot lästa tillbaka via API.

## Radgranskningsunderlag

Tidigare positionsrapporter täcker **38 378** rader i intervallen 331–38 554 och 38 565–38 718. Följande positioner saknar ännu motsvarande rapport: 1–330 och 38 555–38 564. Det återstår dessutom nyare Lokalise-nycklar som tillkommit efter de daterade rapporterna. Dessa antal är inventering av rapportfiler, inte ett påstående om att Core är färdiggranskat.

Intervallet 22 441–22 560 hade en äldre granskningsrapport. Live-värdena jämfördes på nytt mot Lokalise-exporten 2026-11-24; **22 rättningar** sparades och lästes tillbaka. Hela intervallet med 120 poster skrevs eller uppdaterades i Home Assistant-TMX. Rapporten flaggar **24 lokala källvägar** som saknas i den utcheckade Core-versionen; de granskades mot aktuell Lokalise-källtext, men behöver följas upp mot en nyare/upstream Core-källa.

## Home Assistant-TM

- Kanonisk TMX: **16 372** poster, validerad 2026-11-24.
- Status i TMX: 2 705 `saved-and-read-back`, 13 643 `verified-existing` och 24 `source-path-follow-up`.
- Rättningar i intervallet omfattar att-göra-villkor, Yamaha MusicCast-lägen och SmartThings-stickdammsugarvärden. Den fullständiga nyckellistan, befintlig text, slutlig text, motivering och uppföljningar finns i `2026-11-24-core-review-22441-22560.md` och manifestet `2026-11-24-reviewed-core-22441-22560.json`.
- Exportverktyget ändrades så att tomma och felaktiga pluralposter inte längre faller bort tyst; de sparas med orsak i en separat JSONL-inventering.

## Nästa steg

1. Fyll de saknade positionsintervallen och gå igenom rapporterade förslag i ordning utan dubbelarbete.
2. Hämta en uppdaterad HA Core-källcheckout för de 24 saknade strängvägarna.
3. Reconcile:a nya/ändrade Lokalise-nycklar mot snapshoten och fortsätt uppdatera TMX efter varje sparad korrigering.

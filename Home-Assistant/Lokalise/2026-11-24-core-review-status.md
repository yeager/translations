# Home Assistant Core – aktuell granskningsstatus

Datum: 2026-11-24

## Lokalise-omfattning och export

- Aktiva, synliga Lokalise-nycklar i den exporterade nyckelordningen: **75 660**. Efter snapshoten tillkom 17 nya, synliga nycklar; de bekräftades via API och finns i senaste Core-källan, vilket ger **75 677** synliga nycklar i aktuell omfattning.
- Fullständig Core-API-export: **75 645** strängar med användbara engelska och svenska värden efter att 17 nytillkomna strängar översatts och lästs tillbaka via API.
- Exporten sparar nu också nycklar som inte kan ingå i TMX i `2026-11-24-core-export-exclusions.jsonl`: **32** unika poster utan användbart käll-/målpar: 24 tomma på båda språken och 8 utan engelsk källtext men med svensk platshållartext. Alla är synliga; 17 nya synliga strängar som tidigare låg i exkluderingslistan har översatts, lästs tillbaka och flyttats till snapshoten. Den äldre uppgiften om 17 dolda poster var fel.
- Lokalise-API:et kan uppdatera måltext men nekar statusflaggan `is_reviewed` med HTTP 403, `No permission to update translation status`. Lokalise-granskningsflaggan är därför inte satt; ändrade texter är däremot lästa tillbaka via API.

## Radgranskningsunderlag

Tidigare positionsrapporter täcker **38 378** rader i intervallen 331–38 554 och 38 565–38 718. Följande positioner saknar ännu motsvarande rapport: 1–330 och 38 555–38 564. Det återstår dessutom nyare Lokalise-nycklar som tillkommit efter de daterade rapporterna. Dessa antal är inventering av rapportfiler, inte ett påstående om att Core är färdiggranskat.

Intervallet 22 441–22 560 hade en äldre granskningsrapport. Live-värdena jämfördes på nytt mot Lokalise-exporten 2026-11-24; **22 rättningar** sparades och lästes tillbaka. Hela intervallet med 120 poster skrevs eller uppdaterades i Home Assistant-TMX. De **24** tidigare källvägsuppföljningarna kontrollerades mot senaste utcheckade Core (`27d3675a294`); dessa källvägar finns inte längre i aktuell `strings.json`, så posterna står kvar som uppföljningar av föråldrade/utgångna Lokalise-nycklar.

## Home Assistant-TM

Retroaktiv jämförelse av verifierade HA-Core-manifest mot kanonisk TMX hittade ytterligare **11 tidigare sparade** Lokalise-översättningar som saknades i minnet. De återkontrollerades live och lades till. En Datadog-rad rättades mot aktuell källtext och sparades i Lokalise. Se `2026-11-24-core-tmx-gap-reconciliation.md`.

Intervallet 22 561–22 680 har också stämts av mot livevärden och aktuell Core-källa. **9 rättningar** sparades och lästes tillbaka; 11 aktuella översättningar behölls. Se `2026-11-24-core-review-22561-22680.md` och JSONL-manifestet.

- Kanonisk TMX: **16 407** poster, validerad 2026-11-24.
- Status i TMX: 2 729 `saved-and-read-back`, 13 654 `verified-existing` och 24 `source-path-follow-up`.
- Rättningar i intervallet omfattar att-göra-villkor, Yamaha MusicCast-lägen och SmartThings-stickdammsugarvärden. Den fullständiga nyckellistan, befintlig text, slutlig text, motivering och uppföljningar finns i `2026-11-24-core-review-22441-22560.md` och manifestet `2026-11-24-reviewed-core-22441-22560.json`.
- Exportverktyget ändrades så att tomma och felaktiga pluralposter inte längre faller bort tyst; de sparas med orsak i en separat JSONL-inventering.

## Nästa steg

1. Fyll de saknade positionsintervallen och gå igenom rapporterade förslag i ordning utan dubbelarbete.
2. Följ upp de 24 Lokalise-nycklar som saknar motsvarande sträng i senaste Core-källan; avgör om de är utgångna katalogposter eller har flyttats/ersatts.
3. Reconcile:a nya/ändrade Lokalise-nycklar mot snapshoten och fortsätt uppdatera TMX efter varje sparad korrigering.

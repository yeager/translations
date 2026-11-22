# Mopeka, SensorPush Cloud och Sensoterra: komponentgranskning

Samtliga 36 svenska strängar lästes från Lokalise API och granskades rad för
rad den 22 november 2026: Mopeka (12), SensorPush Cloud (12) och Sensoterra
(12). Mopekas två felaktiga livevärden `Medium typ` rättades till `Medietyp`;
det tredje motsvarande fältet var redan korrekt i Lokalise. Samtliga tre
fälten lästes tillbaka efter kontroll. Övriga 33 strängar var korrekta.

Kontrollen omfattar Bluetooth-flöden, API-åtkomst, länken `{dashboard_url}`,
plattformarna iOS och Android, sensorenheter samt djupplatshållaren `{depth}`.

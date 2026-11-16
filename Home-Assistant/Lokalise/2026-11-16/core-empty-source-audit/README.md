# Home Assistant Lokalise: tomma källposter

Granskning genomförd 2026-11-16 efter att samtliga strängar med faktisk källtext hade översatts, sparats genom Lokalise API och lästs tillbaka.

Lokalises filter för oöversatta poster returnerar därefter 33 poster. Av dem är 24 aktiva nycklar som innehåller antingen en tom sträng eller pluralobjektet `{"one":"","other":""}` som både källa och mål. De räknas ändå som oöversatta, eftersom en tom målsträng är semantiskt identisk med den tomma källan. De ska inte fyllas med platshållartext eller mellanslag, eftersom det skulle ändra funktionella tomma beskrivningar och strukturfält.

De återstående 9 posterna är föräldralösa översättningsposter: deras nycklar returnerar HTTP 404 från Lokalise API. De kan alltså inte granskas eller ändras från språksidan och behöver städas av projektadministrationen om räknaren ska bli noll.

Slutsats: inga översättningsbara svenska strängar återstår i den aktuella API-kön. Detta är en API-statusavvikelse, inte återstående svensk lokalisering.

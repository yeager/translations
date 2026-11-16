# Home Assistant Lokalise: tomma källposter

Granskning genomförd 2026-11-16 efter att samtliga strängar med faktisk källtext hade översatts, sparats genom Lokalise API och lästs tillbaka.

Lokalises filter för oöversatta poster returnerar därefter 24 poster. De innehåller antingen en tom sträng eller pluralobjektet `{"one":"","other":""}` som både källa och mål. De är redan verifierade (`is_unverified: false`) men räknas ändå som oöversatta, eftersom en tom målsträng är semantiskt identisk med den tomma källan. De ska inte fyllas med platshållartext eller mellanslag, eftersom det skulle ändra funktionella tomma beskrivningar och strukturfält.

Slutsats: inga översättningsbara svenska strängar återstår i den aktuella API-kön. Detta är en API-statusavvikelse, inte återstående svensk lokalisering.

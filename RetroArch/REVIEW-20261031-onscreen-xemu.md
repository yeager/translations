# RetroArch – svensk komplettering 2026-10-31

## Omfattning

En färsk Crowdin-kontroll av svenska hittade fyra oöversatta strängar:

- en menybeskrivning i `msg_hash_us.json` för Skärmvisning;
- tre Xemu-strängar om anisotropisk filtrering och ljuspistolens analoga spak.

De fyra posterna är arkiverade i
`retroarch-sv-20261031-onscreen-xemu.json` och sparades som Crowdin-förslag
under användaren `yeagersthlm`. Crowdins API svarade med HTTP 201 för varje
post: 2982245, 2982247, 2982249 och 2982251.

## Språkval och kontroller

- Befintliga namn i samma katalog följs: *Skärmvisning*, *Skärmmeddelanden*,
  *Skärmöverlägg*, *Sikta med ljuspistol* och *Anisotropisk filtrering*.
- Kandidaten täcker exakt de fyra aktuella, oöversatta sträng-id:na och inga
  andra poster.
- Platshållarjämförelsen är ren; de fyra källtexterna saknar formatvariabler.
- De sparade måltexterna återlästes från API-svaret.

## Verifierad plattformsstatus

Efter sparningen visar Crowdin 4 737 av 4 737 översatta fraser i
`msg_hash_us.json` och 130 av 130 i `xemu-libretro.json`. Förslagen är ännu
inte godkända. Crowdins befintliga QA-kö visar 476 respektive 28 varningar för
dessa filer och måste granskas i kontext, komponent för komponent.

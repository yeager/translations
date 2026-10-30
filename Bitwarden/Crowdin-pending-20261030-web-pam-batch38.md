# Bitwarden Web – PAM-häfte 38

Den 30 oktober 2026 hämtades `bitwarden/clients` huvudgren vid
`41f307c001f55f8aa65cae80b7d2de193e762f6d`. Den senaste klientreleasen är
`desktop-v2026.10.2`, publicerad den 29 oktober 2026, och uppfyller därmed
färskhetskravet.

`bitwarden-web-pam-connectors-target-systems-batch38-20261030.json` innehåller
100 svenska förslag för nya PAM-gränssnitt: åtkomstanslutningar,
granskningshändelser och de första åtgärderna för målsystem. De valdes genom
att först avräkna 263 nycklar i den tidigare lokala Web-grenen och 204
nycklar med exakta svenska måltexter i de redan arkiverade Crowdin-häftena.
Kvar efter avräkningen var 156 nya nycklar; detta är det första av två häften.
Det avslutande häftet finns i
`bitwarden-web-pam-target-systems-batch39-20261030.json`.

Kontroller:

- JSON parsar med `jq`.
- 100 av 100 poster har oförändrade platshållare.
- `l10n-lint` passerar utan anmärkning.
- `svlang skrivregler` passerar för samtliga svenska måltexter.
- Hunspell träffar bara Bitwarden och platshållarnamnen `COUNT`, `DATETIME`,
  `DAYS` och `NAME`.
- Gitleaks passerar utan fynd.

Crowdin CLI 5.5.0 finns lokalt, men projektets konfiguration kräver
`CROWDIN_API_TOKEN` och `CROWDIN_PROJECT_ID`; de är inte tillgängliga i den
aktuella säkra CLI-sessionen. Häftet är därför **inte uppladdat**, och ingen
uppgift om aktuell Crowdin-status eller dubbletter görs utan en färsk export.
Importera det som oautogodkända förslag efter att en aktuell export har
jämförts; använd aldrig automatisk godkänning.

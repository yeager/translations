# Keycloak: revisionsunderlag för väntande svenska strängar

Datum: 2026-11-04  
Komponent: `theme-baseadmin`  
Underlag: `WEBLATE-QUICK-REVIEW-20261104.md` samt den lokala, granskade
Keycloak-katalogen.

## Rekommendation per sträng

| Nyckel | Källtext | Nuvarande svenska | Rekommenderad svensk text | Åtgärd |
| --- | --- | --- | --- | --- |
| `webOriginsInvalid` | A web origin is not a valid URI | Ett webbursprung är inte en giltig URI | Ett webbursprung är inte en giltig URI | Godkänn utan ändring. |
| `webOriginsIllegalSchemeError` | A web origin uses an illegal scheme | Ett webbursprung använder ett olagligt schema | Ett webbursprung använder ett otillåtet schema | Ersätt och godkänn. |
| `sectorIdentifierUriInvalid` | Sector identifier URI is not a valid URL | Sektoridentifierarens URI är inte en giltig URL | Sektoridentifierarens URI är inte en giltig URL | Godkänn utan ändring. |
| `sectorIdentifierUriIllegalSchemeError` | Sector identifier URI uses an illegal scheme | Sektoridentifierarens URI använder ett olagligt schema | Sektoridentifierarens URI använder ett otillåtet schema | Ersätt och godkänn. |

## Terminologisk kontroll

`otillåtet schema` är etablerad form i den granskade Keycloak-katalogen för
valideringsfelet *illegal scheme*. Samma term används bland annat i
`clientRootURLIllegalSchemeError`, `clientBaseURLIllegalSchemeError`,
`backchannelLogoutUrlIllegalSchemeError`,
`clientRedirectURIsIllegalSchemeError` och
`clientPostLogoutRedirectURIsIllegalSchemeError`. `Olagligt schema` antyder i
stället att användningen är rättsligt förbjuden; här avses att schemat inte är
tillåtet av valideringen.

`webbursprung` är lämpligt för *web origin* och ligger i linje med den lokala
formen `addWebOrigins=Lägg till webbursprung`. `URI` respektive `URL` ska
behållas oförändrade: källsträngarna skiljer uttryckligen på begreppen.
`Sektoridentifierarens URI` är en grammatisk och begriplig genitivform i ett
felmeddelande och behöver inte ändras för att överensstämma med den kortare
fältrubrikens `Sektoridentifierare URI`.

## Genomförande

Genomförd i Hosted Weblate den 4 november 2026:

- `webOriginsInvalid` och `sectorIdentifierUriInvalid` godkändes utan
  textändring.
- `webOriginsIllegalSchemeError` och
  `sectorIdentifierUriIllegalSchemeError` ändrades till `otillåtet schema`
  och godkändes.
- En tillfälligt tillagd slutpunkt togs bort från den första av de två
  ändrade posterna, eftersom källsträngen saknar slutpunkt och Weblate
  korrekt rapporterade kontrollavvikelsen.

Efter sparning gav Weblates sökning `state:translated` inga träffar. Det
verifierar att de fyra poster som låg till grund för denna granskning inte
längre väntar på granskning. Ingen råexport har skrivits över lokalt.

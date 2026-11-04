# Keycloak: snabbgranskning i Weblate

Datum: 2026-11-04
Källa: Keycloaks svenska projekt på Hosted Weblate, komponenten
`theme-baseadmin`.

## Observerad status

Weblate visade 5 671 av 5 671 strängar översatta, varav 5 653 godkända och
fyra väntade på granskning. De fyra posterna gäller URI- och
ursprungsvalidering i administrationsgränssnittet.

## Lokal språkbedömning

| Nyckel | Källtext | Nuvarande svenska | Bedömning |
| --- | --- | --- | --- |
| `webOriginsInvalid` | A web origin is not a valid URI | Ett webbursprung är inte en giltig URI | Godkänn. |
| `webOriginsIllegalSchemeError` | A web origin uses an illegal scheme | Ett webbursprung använder ett olagligt schema | Ändra till `Ett webbursprung använder ett otillåtet schema.` |
| `sectorIdentifierUriInvalid` | Sector identifier URI is not a valid URL | Sektoridentifierarens URI är inte en giltig URL | Godkänn. |
| `sectorIdentifierUriIllegalSchemeError` | Sector identifier URI uses an illegal scheme | Sektoridentifierarens URI använder ett olagligt schema | Ändra till `Sektoridentifierarens URI använder ett otillåtet schema.` |

`otillåtet schema` följer den redan godkända, närliggande Keycloak-terminologin
för samma tekniska betydelse. URI, URL och produktnamn behålls.

## Inskickningsstatus

Ändringarna är ännu inte sparade eller godkända i Weblate. För Weblate-
gränssnittet krävs en explicit åtgärd i den inloggade sessionen för att
markera de fyra posterna som godkända och spara de två språkjusteringarna.

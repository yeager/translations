# QGIS: autentisering och certifikat 077

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen följer QGIS fastställda termer **autentisering** och
**autentiseringsmetod**. Den skiljer mellan ett certifikat som är *ogiltigt*
och ett som inte är *betrott*, eftersom dessa är separata säkerhetstillstånd.
`SSL`, `VSI`, `GDAL`, `QGIS` och versionsnumret bevaras.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Authentication` | `Verifiering` | `Autentisering` |
| `No Authentication Methods` | `Inga verifieringsmetoder` | `Inga autentiseringsmetoder` |
| `Certificate is not trusted.` | `Certifikatet är ogiltigt.` | `Certifikatet är inte betrott.` |
| `Certificate Authority is invalid or not found.` | `Certifikat Auktoritet är ogiltig eller kan inte hittas` | `Certifikatutfärdaren är ogiltig eller hittades inte.` |
| `Certificate Authority has expired.` | `Certifikat Auktoritet har gått ut.` | `Certifikatutfärdaren har upphört att gälla.` |
| `Server Authentication` | `Serververifiering` | `Serverautentisering` |
| `Client Authentication` | `Klientverifiering` | `Klientautentisering` |
| `Certificate Authority` | `Certifikat Auktoritet` | `Certifikatutfärdare` |
| `Authentication method` | `Verifieringsmetod` | `Autentiseringsmetod` |
| `Authentication required` | `Autenticering krävs` | `Autentisering krävs` |
| `Authentication SSL Configs` | `Autentiserings SSL Konfiguration` | `SSL-konfigurationer för autentisering` |
| `An existing QGIS authentication ID string` | `En existerande autentiserings-ID för QGIS som textsträng` | `En befintlig QGIS-autentiserings-ID-sträng` |
| `Cannot use VSI credential options on GDAL versions earlier than 3.5` | `Kan inte använda VSI referensalternativ på GDAL versioner tidigare än 3.5` | `Det går inte att använda VSI-inloggningsalternativ i GDAL-versioner före 3.5` |
| `QGIS Authentication` | `QGIS Autentisering` | `QGIS-autentisering` |

Ingen extern ändring har gjorts. Aktuella Transifex-enhetsidentifierare måste
hämtas innan en separat deltafil kan skapas.

# Home Assistant Core – objektlagringsslutpunkt

Fem anslutningsfel för Cloudflare R2 och IDrive E2 använde den inkonsekventa
formen `ändpunkt`. De är nu `slutpunkten`, samma etablerade term som för
övriga Core- och S3-strängar. Samtliga sparades och återlästes via Lokalise
API samt fördes in i den kanoniska TMX-filen.

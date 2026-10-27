# Routerconfigs: basreparationer 2026-10-27

Den lokala exporten med 304 aktiva poster har granskats radvis i avsnittet med anslutnings-, överförings- och säkerhetskopieringsinställningar, säkerhetskopieringslistor, tidsval samt komponentens avslutande menytexter. Den separata PO-filen innehåller 90 säkra rättelser och är avsedd som en liten komponentvis uppladdning. Den har inte skickats till Cacti Translate.

Rättningarna tar bort engelska *Backup* och *timeout* i måltext, förtydligar behörighetsinställningar, gör rubrikerna idiomatiska och rättar kvarvarande engelska produktord i svensk text. De behåller tekniska protokollnamn som TFTP och loggnivåerna `FATAL`, `ERROR` och `STATS` från källsträngarna.

Begränsning: exportens ålder och serverns aktuella tillstånd måste kontrolleras i Cacti Translate före uppladdning. Inga påståenden om aktuell fjärrstatus eller upstreamsynkronisering följer av denna lokala granskning.

## Uppströmsjämförelse

Den aktuella svenska katalogen på `Cacti/plugin_routerconfigs`-grenen
`develop` jämfördes 2026-10-27. Den har SHA-256
`47c8fe7102e4ff938d917d66079875e4f7450054fb28e9798d341a01b39b2646`.
Av deltafilens 90 rättningar matchar redan `From Address`, `Last Change` och
`Utilities`. Övriga 87 källsträngar finns kvar men har fortfarande annan svensk
måltext uppströms.

Behåll den befintliga komponentfilen vid en eventuell import: Cacti Translate
kan hoppa över de tre redan matchande posterna och behandla de 87 återstående.
Senaste stabila Routerconfigs-release är `v1.7`, publicerad 2026-02-03, och
uppfyller 48-månadersregeln.

# AlmaLinux HPC-sida, svensk komplettering

Datum: 15 november 2026.

Den aktuella Hosted Weblate-katalogen hade 67 oöversatta strängar i
`website-backend`. De gäller AlmaLinux webbplats om vetenskapliga beräkningar,
HPC, AI, kluster, ELevate och RHEL-kompatibilitet. Alla 67 översättningar
finns i den separata JSON-deltan `2026-11-15-hpc-sv-batch.json`.

Tekniska namn, versionsnummer, arkitekturer, sökvägen `/series/book.epub`,
produktnamn och kodnamn bevaras. Terminologi som används konsekvent i batchen
är bland annat *vetenskapliga beräkningar*, *beräkningsnoder*,
*säkerhetskorrigeringar*, *verktygskedjor*, *behållare* och *uppgradering på
plats*.

## Kontroller

JSON-validering, l10n-lint, `svlang skrivregler`, `git diff --check` och
Gitleaks är godkända. `msgfmt` och Hunspell är inte tillämpliga på JSON;
Hunspell kördes dessutom inte enligt användarens CPU-begränsning.

## Upstreamstatus

En direktimport och ett förslagsimportförsök gjordes 15 november 2026. Båda
returnerade HTTP 403 med beskedet att den svenska översättningen är låst.
Ingen av de 67 ändringarna har därför uppladdats eller mottagits upstream.

# Nextcloud Server, svensk lokaliseringsinventering 2026-11-15

- Releasekontroll: Nextcloud Server `v33.0.11`, publicerad 2026-11-12.
- Etablerad översättningskanal: Transifex-projektet `nextcloud`.
- Källkodens genererade `l10n/sv.*`-filer ska inte redigeras direkt; svenska
  ändringar skickas genom Transifex.

## Serverresurser

Transifex API bekräftar att de centrala Server-resurserna saknar oöversatta
svenska strängar:

- `core`: 577 av 577 översatta, senast ändrad 2026-11-10.
- `settings-1`: 1 097 av 1 097 översatta, senast ändrad 2026-11-12.
- `files`: 434 av 434 översatta.
- `files_sharing`: 424 av 424 översatta.
- `dav`: 388 av 388 översatta.
- `lib`: 548 av 548 översatta.
- `user_ldap`: 204 av 204 översatta.

Ingen serveröversättning har skickats i denna omgång eftersom en ny översättning
skulle vara en dubblett eller försämra den kompletta täckningen.

## Avgränsning

Transifex-projektet rymmer även fristående produkter och appar, till exempel
Nextcloud Talk, Android, iOS, Mail och LibreSign. De är egna komponenter med
skilda utgåvor och ska granskas separat. Inventeringen visar bland annat
oöversatta strängar i LibreSign (6), Mail (1), Talk för Android (3), iOS (12)
och Nextcloud Analytics (2); de räknas inte som olösta Server-strängar.

## Verifiering

Statusen hämtades genom Transifex REST API med projekt-, resurs- och
språkfilter för `sv`. Ingen merge eller utgåva påstås för detta
inventeringsarbete.

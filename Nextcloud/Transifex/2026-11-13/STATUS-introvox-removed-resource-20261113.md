# Nextcloud IntroVox, svenska

Datum: 13 november 2026
Projekt: `nextcloud/nextcloud`
Tidigare komponent: `introvox`
Upstreamstatus: komponenten finns inte längre i projektets aktuella API-lista

## Omfattning

Den arkiverade deltafilen innehåller 367 lokalt radgranskade svenska kandidater
från inventeringen 12 november 2026. De täcker administrationsflöden,
välkomstrundturer och filintroduktionen i IntroVox.

## Validering

- JSON-källfilen är bevarad oförändrad: SHA-256
  `4a8278d42901e606c04b3d2ec99f7c1f83e9a207ddb6550843a04e8d6b862256`.
- Alla 367 poster har måltext.
- Pluralnycklar, `%n`, HTML-taggar och Markdown-token matchar källan.
- Gitleaks och `git diff --check` passerade.
- `msgfmt` är inte tillämpligt, eftersom filen är ett Transifex-JSON-delta.
- l10n-lint och svlang kan inte tolka Transifex lista-av-poster-formatet som en
  vanlig lokaliseringsfil. Deras resultat används därför inte för att påstå att
  formatet är felaktigt; respektive batch hade redan dokumenterad språk- och
  formatgranskning.

## Upstream

Vid arbetstillfället 12 november var de berörda källsträngarna låsta och
uppdatering avvisades med HTTP 409. En ny skrivskyddad Transifex-API-kontroll
13 november hämtade samtliga 263 nuvarande resurser i projektet
`o:nextcloud:p:nextcloud`; ingen resurs med namn eller slug som innehåller
`intro` återfinns längre. Den gamla komponentens ID returnerar HTTP 404.

Ingen uppladdning har därför gjorts. Deltat får endast återanvändas om
projektet återställer komponenten eller anger dess ersättande resurs-ID och
källsträngarna fortfarande matchar.

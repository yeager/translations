# Nextcloud Enterprise IntroVox, svenska

Datum: 13 november 2026
Projekt: `nextcloud/enterprise-4`
Komponent: `introvox`
Källa: Transifex API-inventering 12 november 2026
Upstreamstatus: låst, inte inskickad

## Omfattning

Deltafilen innehåller 367 svenska kandidater för tidigare oöversatta strängar.
325 har en identisk källsträng i den redan radgranskade komponenten
`nextcloud/nextcloud/introvox` och återanvänder därför dess svenska måltext.
De återstående 42 Enterprise-specifika strängarna har granskats rad för rad.

## Validering

- JSON-källfilen är oförändrad vid arkivering: SHA-256
  `d1c89612bc7b74322b57ddd161e492683e5af332044a9d5655379c1c9719485e`.
- 367 av 367 poster har en måltext och Transifex tagg `locked`.
- Pluralnycklar, `%n` och Markdown-token matchar källan.
- Ingen ny em dash och inga otillåtna tredubbla konsonanter hittades.
- Hunspell-sv träffade bara produktnamn, formatnamn, kodfragment och
  projekttermer, exempelvis `IntroVox`, `Nextcloud`, `Shepherd.js` och `Vue`.
- Gitleaks för deltafilen passerade utan läckor.
- `git diff --check` passerade.
- `msgfmt` är inte tillämpligt eftersom Transifex-deltat är JSON, inte en
  GNU gettext-katalog.
- `l10n-lint` saknar stöd för Transifex egna lista-av-poster-JSON och ger
  därför 359 falska CLDR-fel på entalsfält som lagras som `other`; resultatet
  används inte som formatvalidering.
- `svlang` tar endast en igenkänd lokaliseringsfil, inte den här
  Transifex-listan. Svensk text kontrollerades därför med radgranskning,
  Hunspell och den formatmedvetna paritetskontrollen ovan.

## Upstream

Vid inventeringen var samtliga 367 poster märkta `locked`. Transifex avvisade
den etablerade uppdateringen med HTTP 409, så ingen API-skrivning eller
webbläsaruppladdning har gjorts för denna batch. Ladda upp exakt denna
deltafil först när komponenten har låsts upp och kontrollera därefter både
importkvittens och återläst komponentstatus.

# Batch 119: offentliga nycklar

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 6 aktiva meddelanden i `UIAcquirePublicKeyDialog` har granskats
radvis mot dialogens kod för molnkonsolanslutningar.

## Resultat

`publik nyckel` har konsekvent ersatts med den etablerade tekniska termen
`offentlig nyckel`. Dialogen gör tydligt att filen med `id_rsa[.pub]` kan
väljas eller att nyckelinnehållet kan klistras in. HTML-markering,
platsmarkörer, filnamn och kommandon är bevarade.

## Kontroller

- XPath-räkning: 6 aktiva meddelanden i `UIAcquirePublicKeyDialog`.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- Hunspell med användarens svenska ordlista: inga språkfel i ändrad text;
  `rsa` är en avsiktlig del av filnamnet `id_rsa`.
- `l10n-lint --language sv --check`: kunde inte slutföra för denna Qt
  TS-katalog och avslutade med kod 2 utan diagnostik. Det är inte ett godkänt
  resultat och påverkar inte de övriga formatkontrollerna.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga aktuella `UIAcquirePublicKeyDialog`-granskningen är lokalt
slutförd i commit `633f115` och ännu inte pushad till PR #848.

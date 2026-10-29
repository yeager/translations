# Bitwarden Web: granskningshäfte 27

Datum: 29 oktober 2026

Häftet `Bitwarden-Web-current-review-batch27.xliff` omfattar 37 svenska
måltexter: importanvisningar för lösenordshanterare och händelser för
automatisk användarbekräftelse samt inbjudningslänkar.

Fyra händelsetexter justerades efter radvis granskning så att
attributfrasen uttrycks med `för automatisk användarbekräftelse`. Två
händelsetexter ändrades från imperativ form till det avsedda
substantiviska `Kravet på administratörsgodkännande`.

## Kontroller

- XML: `xmllint --noout` passerade.
- l10n-lint 1.23.30: 0 fel och 0 varningar. En informativ
  gränsteckenträff för `User $ID$ left $ORGNAME$ vault` är förväntad eftersom
  svensk ordföljd placerar `$ORGNAME$` sist.
- svlang skrivregler: inga träffar.
- Platshållarkontroll: `$ID$` och `$ORGNAME$` matchar källtexterna.
- Kontroll för tre identiska konsonanter i följd: inga träffar.
- Hunspell-sv: återstående ord är produktnamn, filformat, platshållare eller
  engelska etiketter som avsiktligt bevaras för att instruktionerna ska
  motsvara respektive programs gränssnitt.
- Swedish FOSS Terminology: `vault`/`valv`, `master password`/`huvudlösenord`
  och `export`/`exportera` följs där kontexten är en svensk funktionsterm.
  Faktiska engelska menyetiketter lämnas oförändrade.
- Gitleaks: inga hemligheter.

## Upstreamstatus

Häftet är klart för inskick som ett separat Crowdin-häfte om 37 strängar.
Det var inte möjligt att öppna Crowdins redigerare vid denna kontroll eftersom
värddatorn var låst. Inga externa översättningar påstås därför vara sparade av
den här granskningen.

## Jämförelse med lokal klientkatalog

Mot den lokala svenska webbkatalogen vid commit
`6d2e3a182c257d8078e1bc1c1e99cd340ddc5a27` är en post identisk
(`importNetwrixInstructions`) och 36 poster avviker. Det är väntat eftersom
häftet bevarar exakta produktnamn och menyetiketter samt har en jämnare svensk
meningsbyggnad. Jämförelsen bevisar inte vad som är valt i Crowdin; innan
inskick ska varje föreslagen måltext fortfarande jämföras mot Crowdins aktuella
måltext.

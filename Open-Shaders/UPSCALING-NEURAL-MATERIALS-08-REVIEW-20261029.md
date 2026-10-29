# Open Shaders: neural rendering och material, granskning 8

Det åttonde uppskalningshäftet innehåller 25 nycklar för materialkartan,
modellskala och begränsning till den spårade aktören.

`Follow Foveation` behålls som inställningsnamn. `Unlabelled pixels` är
översatt med `bildpunkter utan etikett`, vilket är tydligare än den onaturliga
formen `oetiketterade`. Procenttal har svensk typografi med mellanrum före
procenttecknet; de är inte formatmarkörer.

Kontroller den 29 oktober 2026:

- JSON-syntax, 25 källnycklar och verkliga formatmarkörer är kontrollerade mot
  den lokala engelska katalogen.
- `l10n-lint` och `svlang skrivregler` godkänner filen utan anmärkning.
- Hunspell markerar endast avsiktliga facktermer, inklusive `Foveation` och
  `foveerad`.
- Häftet kräver en ny Weblate-export före import till den låsta komponenten.

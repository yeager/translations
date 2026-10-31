# Wireshark Qt 5.0 – svensk sats 1

## Omfattning

Den aktuella Transifex-resursen `qt-50` hade 45 tomma svenska UI-strängar.
De är samma gränssnittsområde som tidigare kontrollerats i `qt-master`, men
har egna resurs-ID:n och behövde därför skickas separat.

Satsen finns i
[`wireshark-qt-50-sv-batch-01-20261031.json`](wireshark-qt-50-sv-batch-01-20261031.json).
Den omfattar fångst, kolumner, teckensnitt, färgläggningsregler,
välkomstsidans layout och produktnamnen Tips och Discord.

## Kontrollkedja

- Alla 45 aktuella sträng-ID:n och källtexter jämfördes med Transifex.
- 34 måltexter är källmatchande återanvändning från den arkiverade,
  granskade `qt-master`-satsen.
- De återstående elva kontexterna granskades manuellt.
- `msgfmt --check`, `l10n-lint` och `svlang skrivregler` passerade.
- Hunspellträffarna begränsades till tekniska förkortningar, produktnamn och
  kortkommandomarkörer, exempelvis EWMA, SMA, Discord och `&`.
- Gitleaks fann inga hemligheter.

## Inskick och efterkontroll

Varje måltext skickades som en ogranskad Transifex-översättning med
`resource_translations`-API:t. Alla 45 anrop returnerade HTTP 200 och varje
måltext lästes tillbaka exakt. Den slutliga Transifex-statistiken är 4 488 av
4 488 strängar översatta och 0 oöversatta.

Senaste Wireshark 4.6-serie är aktuell enligt projektets officiella
releaseinformation och uppfyller kravet på en release inom 48 månader.

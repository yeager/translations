# Tenacity: svensk översättning och granskning

Samtliga 3830 aktiva strängar har översättning och har gåtts igenom mot den engelska källtexten.

- 865 tidigare tomma strängar har fått översättning.
- 469 tidigare osäkra strängar har bearbetats; ingen fuzzy-markering kvarstår.
- Totalt 1527 strängar är nya eller ändrade, inklusive ändrad status.
- Lokal Hunspell med /usr/share/hunspell/sv_SE användes. Rårapport finns i hunspell-sv-report.txt. Ordlistan flaggar även egennamn, programtermer och sammansättningar; rapporten är inte en lista över bekräftade stavfel.
- msgfmt --check --check-format godkänner filen och rapporterar 3830 översatta meddelanden.
- URL:er, wiki-länkmål och Nyquist-formatdirektiv stämmer med källtexten.
- Radbrytningar samt inledande/avslutande blanktecken kontrollerades. Det enda kvarvarande &-antalavsteget är ”Click & move …”, där & betyder ”och” i löptext och inte är ett kortkommando.

## Underlag

Original: https://hosted.weblate.org/download/tenacity/tenacity/sv/
Källtext: https://hosted.weblate.org/download/tenacity/tenacity/en/
Översättningsminne: https://raw.githubusercontent.com/audacity/audacity/release-3.7.8/locale/sv.po

1 184 ursprungligen ofärdiga strängar hade matchningar i Audacity-underlaget; dessa granskades och fel rättades. Övriga 150 översattes separat. Originalfilens upphovspersoner finns kvar i filhuvudet.

## Weblate

Uppladdningen är inte genomförd: webbläsarens filväljare returnerade utan fel men filfältet förblev tomt. Inga översättningar har skickats in. Formuläret är förberett för ”Lägg till som översättning” och ”Ändra översatta strängar”.

Kontot visar inga kontroller för formellt granskningsgodkännande. Den lokala språkgranskningen ska därför inte förväxlas med Weblates status ”Godkänd”.

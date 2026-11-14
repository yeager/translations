# Xournal++ – UI-verktyg och navigering (svenska)

Datum: 2026-11-14

## Omfattning

En avgränsad, radvis granskad deltafil med 304 poster för verktyg, textjustering, navigering, PDF-val, export, penntryck, filformat, XML-tolkning, felmeddelanden, inmatningsenheter, LaTeX, textverktyg, mallar, ljud, filtyper, metadata och visning i Xournal++. Merparten var tidigare oöversatt; flera poster rättar dessutom befintliga felöversättningar, bland annat exportens `Backend` från `Backend` till `Exportmotor`, pennans `Tip` från `Tips` till `Spets`, den fysikaliska parametern `Drag` från `Dra` till `Dämpning`, men även felaktig svensk böjning i beskrivningen av omfärgning. Ändringen `Drawing Type - don't change` från `Ritläge - ändra inte` till `Ritläge - ändra inte` finns i den lokala katalogen för att följa källtextens skiljetecken, men ingår inte i deltafilen eftersom den redan har en svensk översättning.

## Kontroller

- `msgfmt --check --statistics`: godkänd, 1 107 översatta och 0 oöversatta meddelanden i den lokala katalogen efter batchen.
- `l10n-lint`: körd; inga oöversatta poster återstår. Två datumformatsträffar gäller beskrivningar av `%`-koder, inte datumformat som används direkt. Informationsvarningar om acceleratorer är granskade.
- `svlang`: godkänd för representativa formuleringar.
- `hunspell-sv`: körd med låg prioritet på batchens svenska ord. De accepterade tekniska sammansättningarna `Kommandoutdata`, `indatatrycket`, `MIME-typ`, `dokumenttagg`, `bakgrundstaggen`, `rithastigheten`, `indatastabilisering`, `Dödzonsradie`, `ritspetsen`, `bifogningsläge`, `handflatsavkänning`, `nypgester`, `tvåfingergester`, `namnlisten`, `DPI-kalibrering` och `omrendering`, samt kodnamnet `ElementRange` och produktnamnet `Cairo`, finns inte i ordlistan; inga oavsedda stavningsfel återstår.
- `git diff --check`: godkänd.
- `Gitleaks`: godkänd.

## Status

Lokalt granskat och arkiverat. Den lokala katalogen är komplett översatt. Xournal++ hänvisar till Crowdin för översättningar. Crowdin-CLI:n saknar i denna arbetskopia både projekt-id och auktorisering, så batchen är **inte uppladdad eller inskickad upstream**. En inloggad webbsession öppnar den svenska Xournal++-redigeraren, men inga strängar har ändrats i den här batchen via webben.

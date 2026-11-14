# Scribus svenska UI - granskningsbatch 006

Datum: 2026-11-14
Komponent: Scribus UI (`o:scribus:p:scribus:r:scribus`)
Språk: svenska (`sv`)

Den här batchen omfattar 20 radgranskade strängar inom färghantering,
färgscheman, ramlänkning, länkdialoger och teckenpaletter.

Ändringarna sparades via Transifex REST API och varje sparad måltext
lästes tillbaka och jämfördes med den lokala granskade texten.

Kontroller:

- `lrelease`: godkänd, 8 126 färdiga översättningar
- diffkontroll: genomförd för den lokala arbetsfilen
- Hunspell-SV: endast projektnamn och namn i projektets URL
- svlang: granskad; dess V2-varningar är falska positiva för sammanfogade UI-fragment och bisatser
- Gitleaks: körs på den arkiverade batchen före push

Transifex-token saknar behörighet att sätta formell granskningsstatus.
Ändringarna är därför sparade och återlästa, men inte massmarkerade som granskade.

# HP Printer: patronuppgifter, batch 48

Datum: 2026-11-14

Trettiotalet entydiga patronfält kontrollerades mot komponentens aktuella
sensorimplementation och sparades i Lokalise. Varje måltext återlästes
separat efter sparning.

Fälten för svart, cyan, magenta, trefärg och gul patron följer samma
betydelse: installationsdatum, nivå, tillverkningsdatum, utskrivna sidor,
återstående sidor och garantins utgångsdatum. Formuleringarna använder
"patron" för att fungera för både bläck och toner.

Påfyllningsräknarna ingår inte i batchen. Komponentkoden visar att de är
diagnostiska, ackumulerande räknare, men deras underliggande HP-betydelse
behöver kontrolleras ytterligare innan "counterfeit" och "genuine" får en
svensk formulering.

Kontroller före sparning: l10n-lint, individuell svlang-kontroll,
Hunspell-sv, diffkontroll och Gitleaks. Hunspell-sv saknar sammansättningen
"trefärgspatron"; svlang bedömer den till 10/10 och den är accepterad som
normal svensk sammansättning i denna konkreta UI-kontext. `msgfmt` är inte
tillämpligt eftersom Lokalise hanterar JSON-nycklar, inte en PO-fil.

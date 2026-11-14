# Amaze File Manager – svensk lokalisering, status 2026-11-14

## Projekt och aktuell status

- Projekt: [TeamAmaze/AmazeFileManager](https://github.com/TeamAmaze/AmazeFileManager)
- Senaste utgåva: `v3.11.4`, 2026-10-15.
- Auktoritativ översättningskanal: [Amaze File Manager i Transifex](https://explore.transifex.com/amaze/amaze-file-manager/).
- Den publika projektsidan visar svenska (Sverige) som 72 % klar, totalt 9,77 tusen ord, med aktivitet 2026-11-09.

## Lokal jämförelse

Repositoryt innehåller `app/src/main/res/values-sv/strings.xml`, men den filen omfattar 507 av 723 aktuella engelska nycklar. Det saknas alltså 216 nycklar i Git-kopian. Eftersom projektets dokumentation hänvisar översättningarna till Transifex är Git-filen en inaktuell ögonblicksbild, inte en säker importkälla.

`xmllint --noout` godkände både engelska och svenska XML-filen.

## Transifex-integration

Två lokalt lagrade API-autentiseringsuppgifter verifierades enbart mot den publika språkresursen; båda gav HTTP 200. Uppslag av projektet `o:amaze:p:amaze-file-manager` via Transifex v3-API gav däremot HTTP 404 med båda. Den publika projektsidan visar dessutom en oinloggad webbsession.

Ingen fil har därför laddats upp och ingen översättning har ändrats upstream. Nästa steg är att få korrekt v3-projektidentifierare eller en inloggad Transifex-session, och därefter hämta den aktuella svenska resursen före granskning.

## Kontrollstatus

- XML-syntax: godkänd (`xmllint`).
- `msgfmt`: ej tillämpligt (Android XML).
- l10n-lint, svlang och Hunspell-SV: avvaktar en aktuell Transifex-export, så att granskningen sker mot rätt källa.
- Gitleaks: körs före arkivering och eventuellt inskick.

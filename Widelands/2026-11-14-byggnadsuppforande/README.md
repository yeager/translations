# Widelands Add-Ons: byggnadsuppförande

Fyra strängar för byggnaders uppförande och rivning har granskats lokalt och
sparats i Transifex.

Projekt: Widelands Add-Ons
Resurs: rotresursen
Språk: svenska (\`sv\`)

## Strängar

- 612431492: direkt uppförande eller förbättring
- 612431493: kostnad för direkt bygge
- 612431499: återfått material vid rivning av direkt uppförd byggnad
- 612431500: återfått material vid rivning av förbättrad byggnad

\`enhancing\` följer projektets etablerade term \`förbättra\`.

## Verifiering

- \`msgfmt --check --statistics\`
- \`l10n-lint --language sv --check\`
- Hunspell-sv och svlang, med manuell kontextgranskning
- \`git diff --check\`
- Gitleaks
- Transifex: varje sträng sparad och återläst utan QA-varning

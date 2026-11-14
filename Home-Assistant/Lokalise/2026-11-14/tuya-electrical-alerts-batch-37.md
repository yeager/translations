# Tuya – elektriska varningar, batch 37

Datum: 2026-11-14

Sju Tuya-sensorer med elektriska fel och varningar har granskats i
komponentkontext, sparats i Lokalise och lästs tillbaka i redigeraren:

| Källa | Svenska |
| --- | --- |
| Surge | Överspänning |
| Overpower early warning | Tidigt varningsmeddelande om övereffekt |
| Overcurrent early warning | Tidigt varningsmeddelande om överström |
| Leakage current early warning | Tidigt varningsmeddelande om läckström |
| Leakage current alarm | Läckströmslarm |
| Current imbalance | Strömobalans |
| Test alarm | Testlarm |

Termerna följer elkraftssvenska: `överström`, `övereffekt`, `läckström` och
`strömobalans`. Varningarna är binära sensorer, därför används korta
namnfraser i stället för imperativ.

## Kontroller

- l10n-lint: godkänd
- svlang: 10/10 naturliga formuleringar
- Hunspell-sv: endast `Läckströmslarm`, en sammansatt fackterm som saknas i
  ordlistan
- diffkontroll och Gitleaks: godkända
- msgfmt: ej tillämpligt; Lokalise arbetar här med JSON-strängdata, inte PO

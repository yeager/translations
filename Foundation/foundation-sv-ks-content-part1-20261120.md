# Foundation – svenska granskning: ks_content.json, del 1

Datum: 2026-11-20  
Metod: Crowdin API; `l10n-lint --language sv`; `hunspell -d sv_SE`.

| Sträng-ID | Engelsk källa | Tidigare svenska | Föreslagen svenska | Resultat |
|---|---|---|---|---|
| 26470 | You assured the Tax Collector that a Company would be sent in the woods to find a long-lost treasure, the legendary Dragon’s hoard. But does it even exist? | Du försäkrade skatteindrivaren om att ett kompani skulle skickas ut i skogen för att hitta en sedan länge försvunnen skatt, den legendariska drakens gömma. Men finns den ens? | Du försäkrade skatteindrivaren om att ett kompani skulle skickas in i skogen för att hitta en sedan länge försvunnen skatt, den legendariska drakens gömma. Men finns den ens? | Sparad i Crowdin (201) |
| 26478 | Your monastics share the lore they discovered. | Dina munkar delar med sig av vad de har upptäckt. | Dina munkar delar med sig av den kunskap de har upptäckt. | Sparad i Crowdin (201) |

## Validering

- `l10n-lint`: inga problem.
- `hunspell-sv`: inga stavningsanmärkningar.
- Lint rapporterade endast en informationsvarning om icke-ASCII-tecknet i engelsk källtext (typografisk apostrof); den är källrelaterad.
- Interpunktion och Foundation-terminologi bevarades.

# PCSX2: svensk rättning av spelkorrigeringspanelen

- Datum: 2026-11-13
- Underlag: `pcsx2-qt_en_sv-SE.xliff`, hämtad 2026-11-11
- Deltakatalog: `pcsx2-sv-game-fixes-grammar-batch-96-20261113.xliff`
- Crowdin: projekt `561203`, källfil `15`, målspråk `sv-SE`

Sträng `7321` är informationstexten i PCSX2:s panel för *Game Fixes*.
Den aktiva svenska texten hade kongruensfelet *Spelfixar är inte aktiverat*.
Den granskade måltexten är:

> Spelfixar är inte aktiverade. Kompatibiliteten med vissa spel kan påverkas.

`Spelfixar` behålls eftersom det är panelens etablerade svenska UI-namn.
Hunspell-sv saknar sammansättningen, men svlang bedömer hela formuleringen
som naturlig svenska. `xmllint --noout` och `l10n-lint` godkände deltafilen.

Den projektspecifika terminologin skiljer nu mellan panelnamnet `Game Fixes`,
som blir *spelfixar*, och tekniska spelpatchar eller patchfiler, som behåller
*patch* efter sin konkreta kontext. Den tidigare generella regeln att alltid
översätta *patch* till *korrigering* var för grov för PCSX2 och ersattes.

Förslag `450001` skickades via Crowdin API den 13 november och återlästes
direkt med identisk text. Det är ett ogranskat förslag; ingen
upstreamgranskning, godkännande eller aktivering av den befintliga
översättningen är verifierad.

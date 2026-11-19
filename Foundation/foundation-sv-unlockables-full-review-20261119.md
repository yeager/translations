# Foundation – upplåsningar: full radgranskning 2026-11-19

Samtliga 73 strängar i `unlockables.json` granskades via Crowdin API. Tio förbättringsförslag identifierades; övriga 63 bedömdes korrekta.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 712 | A tier of unlockables has been locked. | En nivå av upplåsningsbara saker har låsts. | En nivå med upplåsningar har låsts. |
| 22732 | Unlocks Fish production, a Rustic Food resource. | Låser upp Fiskproduktion, en Rustik matresurs. | Låser upp fiskproduktion, en rustik matresurs. |
| 22740 | Unlocks Meat production, a Refined Food resource. | Låser upp Köttproduktion, en Förädlad matresurs. | Låser upp köttproduktion, en förädlad matresurs. |
| 22742 | Unlocks Bread production, a Refined Food resource. | Låser upp Brödproduktion, en Förädlad matresurs. | Låser upp brödproduktion, en förädlad matresurs. |
| 22754 | {1} Improvement | {1} Förbättring | {1} förbättring |
| 22758 | Manor House Village Architecture | Arkitektur för byns Herrgård | Byarkitektur för herrgården |
| 22782 | Your land is an example of beauty and prosperity. | Ert land är ett exempel på skönhet och välstånd. | Ditt land är ett exempel på skönhet och välstånd. |
| 22784 | Commonfolk have heard of your land. | Folk i allmänhet har hört talas om ert land. | Vanligt folk har hört talas om ditt land. |
| 22794 | The Splendour of your village has opened a new tier of unlockables. | Din bys prakt har låst upp en ny nivå av saker. | Din bys prakt har låst upp en ny nivå med upplåsningar. |
| 26018 | Woodcutting | Träskärning | Trädfällning |

## Kontroller

- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` passerade utan anmärkningar.
- Platshållaren `{1}` har bevarats.
- Förslagen har inte skickats till Crowdin.

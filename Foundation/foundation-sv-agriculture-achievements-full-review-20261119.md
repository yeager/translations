# Foundation – jordbruks-DLC: prestationer, full radgranskning 2026-11-19

Samtliga 22 strängar i `dlc_agriculture_achievements.json` granskades via Crowdin API. Fem förbättringsförslag identifierades; övriga 17 bedömdes korrekta.

| ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 23964 | Complete the Aspiration: "A Granary of the Realm" | Slutför ambitionen ”Ett spannmålsmagasin för riket” | Slutför strävan: "Ett spannmålsmagasin för riket" |
| 23984 | Complete a Harvest Festival | Slutför en skördefest | Slutför en skördefestival |
| 23992 | Invite the Elders to a Harvest Festival | Bjud in de äldste till en skördefest | Bjud in de äldste till en skördefestival |
| 23998 | I 'ave 'un! | Jag har roligt! | Jag har kul! |
| 26404 | Produce Cabbages at a Cabbage Farm | — | Producera kål på en kålodling |

## Kontroller

- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` passerade utan anmärkningar.
- Terminologin *Aspiration* → *strävan* och *Harvest Festival* → *skördefestival* är konsekvent med övriga Foundation-batcher.
- Förslagen har inte skickats till Crowdin.

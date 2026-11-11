# Radgranskning av Proxmox svenska katalog

## Källa och omfattning

- Projekt: `proxmox-i18n`, samlad svensk UI-katalog.
- Källa: `https://git.proxmox.com/git/proxmox-i18n.git`, commit
  `e34b1d1af19b0c62aa6bf69e88be68c305a2075f`.
- Källfil: `sv.po`, POT-datum 2026-11-02 08:08+0000.
- Projektstatus: aktivt. Proxmox VE 9.2 publicerades 2026-05-21, alltså inom
  fyrtioåttamånadersgränsen.
- Granskning: samtliga 4 059 aktiva poster, rad för rad.
- Ändrade poster: 312.

`sv.po.raw` är den oförändrade råexporten. `sv.po` är den granskade filen och
`sv-review.patch` innehåller endast skillnaden mellan dem.

## Kontroller

| Kontroll | Resultat |
| --- | --- |
| `msgfmt --check --statistics` | Godkänd, 4 059 översatta meddelanden. |
| `l10n-lint --language sv` | 0 fel, 0 varningar. Informationsnotiserna gäller medvetet bevarade produktnamn, tekniska identifierare, formatsträngar och normaliserade pluraluttryck. |
| `svlang consistency` | Godkänd. |
| Utökad Yeager `hunspell-sv` | Manuell genomgång av 771 okända token. De återstående träffarna är kod, protokoll, konfigurationsnycklar, produktnamn, format och tekniska sammansättningar. |
| `git diff --check` | Godkänd. |
| `gitleaks detect --no-git --redact` | Godkänd, inga hemligheter hittades. |

`svterm` och en fristående CLI för `swedish-foss-terminology` saknas som
installerbara verktyg. Termbasens lokala TBX- och CSV-data användes ändå för
att kontrollera generella tekniska termer; den projektspecifika kontexten har
företräde när den är mer precis.

## Status

- Lokal radgranskning: klar och verifierad.
- Arkivering i `yeager/translations`: klar.
- Push av arkiv: verifierad på `main` i commit
  `1efb01510a8b48dd2adcd8c9a72d40bf90766a42`.
- Upstream-inskick: inte gjort av Codex. Beställaren uppgav att hen skickar in
  katalogen själv.
- Upstream-granskning, merge och publicering: okända.

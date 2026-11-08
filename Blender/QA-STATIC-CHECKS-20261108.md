# Blender UI – statiska kvalitetskontroller (2026-11-08)

Kontrollernas underlag är den lokala exporten
`blender-ui-ui-sv (5).po`, med 40 427 översatta meddelanden.

| Kontroll | Resultat | Bedömning |
| --- | --- | --- |
| `msgfmt --check --statistics` | 40 427 översatta meddelanden | Godkänd. |
| `l10n-lint` | 0 fel, 26 varningar | Godkänd efter kontextgranskning. Varningarna gäller främst format-, färgrymds- och produktidentifierare som ACES, ProRes, WebM, Open Shading Language och Visual Studio Code samt medvetna svenska skiljeteckensskillnader. |
| `svlang consistency` | Alla översättningar konsekventa | Godkänd. |
| `svlang skrivregler` | 7 träffar | Inte språkfel: källkodens ternäroperator `? A : -A` och formatsträngar som `%s : %s` måste behålla mellanslag och tecken exakt. |
| `svlang svengelska` | 3 kandidater | Granskade: *taggar/tagga* är Blenders metadata- och meshterm i denna kontext; `startup` är ett bokstavligt katalognamn. |
| `hunspell-sv` | Använt för ändrade svenska ord | Godkänd för batchernas vanliga svenska ord. Namn som *Actionen* och *Actioner* hanteras som avsiktliga böjningar av Blenders formella datatyp. |
| Tre lika konsonanter | Inga träffar i måltexterna | Godkänd. |

Kontrollerna är kvalitetssignaler, inte automatiska översättningsbeslut.
Källkontext, Blender-specifik terminologi och bevarade kod-/formatnamn går
före generella träffar.

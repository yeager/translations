# 0 A.D. – svensk Transifex-status 7 november 2026

0 A.D. är ett fritt realtidsstrategispel om antik krigföring. Den aktuella
utgåvan är Release 28: Boiorix, publicerad 18 februari 2026. Projektet är
alltså aktivt och ligger klart inom 48-månadersgränsen.

78 oöversatta svenska strängar hämtades från Transifex REST-API och
granskades mot respektive spelresurs. Två längre civilisationstexter fick
svenska saköversättningar. Benämningar som är antikgrekiska eller historiska
egennamn behölls avsiktligt för att följa spelets egen namngivning; engelska
rollord översattes där de förekom.

Underlagen är:

- `0ad-sv-20261107-civilizations-and-historic-names-batch-01.json` (10)
- `0ad-sv-20261107-unit-names-batch-02.json` (20)
- `0ad-sv-20261107-unit-names-batch-03.json` (24)
- `0ad-sv-20261107-unit-names-batch-04.json` (24)

`l10n-lint` gav inga fel för batcherna. Hunspell-SV markerade förväntat
antikgrekiska och historiska namn; de är inte svenska stavningsfel. `svlang`
är inte ett tillförlitligt heltest för dessa JSON-underlag eftersom verktyget
även analyserar engelska källtexter och tekniska id:n. `msgfmt` är inte
tillämpligt på JSON-batcher.

Alla 78 poster skickades med Transifex REST-API och varje måltext återlästes
exakt. Slutlig API-statistik omfattar 18 resurser, 7 470 av 7 470 översatta
svenska strängar och 0 oöversatta. Detta bekräftar översättningsstatus, inte
en eventuell separat granskningsstatus i Transifex.

## play0ad.com-webbplatsen

Det separata projektet `play0ad-website` är uppdaterat i november 2026 och
har tydliga anvisningar om att behålla Markdown-länkar och formatering.
Svenska är dock inte aktiverat som projektspråk. Ett försök att lägga till
`l:sv` via projektets normala Transifex-ändpunkt fick HTTP 403
`permission_denied`; Wildfire Games behöver därför aktivera svenska eller ge
behörighet innan webbplatsens svenska översättning kan påbörjas.

### Statusuppdatering 14 november 2026

Transifex bekräftar nu att svenska är ett aktivt projektspråk för
`play0ad-website`: 474 källsträngar, 0 % översatta och 0 % granskade.
Projektets teamanslutning krävs fortfarande, men dialogens lista över
tillgängliga språk innehåller ännu inte svenska. Någon svensk webbplatsdeltafil
finns inte i detta arkiv och därför har ingen översättning laddats upp eller
skickats in. Väntar på att Transifex synkroniserar svenska till teamets
anslutningslista.

Senare samma dag verifierades direktredigering i Transifex och den första
webbplatssträngen skickades och återlästes: `release_line` →
`{{ .Name }}, släppt {{ .Date }}.`. Efter återläsning visar Transifex 14
ogranskade svenska strängar och 460 oöversatta. Arkivbatch:
`website-2026-11-14-batch-01`.

Fortsatt radgranskning och direkt sparande i Transifex har slutfört
komponenterna About – Concept art, About – Development activity, About – The
story, Community – Tips och Community – Mods. Varje komponent har arkiverats
som egen deltafil med granskningslogg. I Community – Mods är båda strängarna
nu översatta och återlästa (2/2), med bevarad Markdown-länk till `mod.io`.
Projektgranskning, källsynkronisering och webbpublicering är fortfarande inte
verifierade.

Community – Donate har därefter granskats rad för rad: 14 av 14 svenska
strängar är sparade och återlästa i Transifex. Länkar, den escapade
dollarsymbolen och Hugo-kortkoden har bevarats. Arkivbatch:
`website-2026-11-14-community-donate`. Projektgranskning,
källsynkronisering och publicering är inte verifierade.

Community – Get support har därefter granskats rad för rad: 19 av 19 svenska
strängar är sparade och återlästa i Transifex. Markdown-länkar, URL-parametrar,
IRC-markeringen och avdelarna har bevarats. Arkivbatch:
`website-2026-11-14-community-support`. Projektgranskning,
källsynkronisering och publicering är inte verifierade.

About – Contact us har därefter granskats rad för rad: 12 av 12 svenska
strängar är sparade och återlästa i Transifex. Markdown, interna länkar och
avdelare har bevarats; en felaktig radbrytning rättades efter Transifex QA.
Arkivbatch: `website-2026-11-14-about-contact-us`. Projektgranskning,
källsynkronisering och publicering är inte verifierade.

About – Official logos har därefter granskats rad för rad: 7 av 7 svenska
strängar är sparade och återlästa i Transifex. Hugo-kortkoder,
typsnittsnamn, licenslänkar och filformat har bevarats. Arkivbatch:
`website-2026-11-14-about-official-logos`. Projektgranskning,
källsynkronisering och publicering är inte verifierade.

About – Organization har därefter granskats rad för rad: 6 av 6 svenska
strängar är sparade och återlästa i Transifex. Namn, användarnamn,
organisationsnamn och datum har bevarats. Arkivbatch:
`website-2026-11-14-about-organization`. Projektgranskning,
källsynkronisering och publicering är inte verifierade.

About – Contributors har därefter granskats rad för rad: 4 av 4 svenska
strängar är sparade och återlästa i Transifex. Produktnamn, UI-namn och
Gitea- och forumlänkar har bevarats. Arkivbatch:
`website-2026-11-14-about-contributors`. Projektgranskning,
källsynkronisering och publicering är inte verifierade.

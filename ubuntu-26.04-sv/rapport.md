# Granskning av installerade svenska gettext-kataloger

Granskad 19 september 2026. **57 individuellt verifierade fyndgrupper, 65 förekomster:** 2 med prioritet P1, 32 P2 och 23 P3. Hela materialet har kontrollerats automatiskt; språkgranskningen är en riktad granskning av utvalda kandidater, inte en genomläsning av alla 230 304 poster.

Jämförelsen gäller översatta meddelanden, utan metadatahuvudet. Gettext kan normalisera det kompilerade huvudets teckenkodning och skapandedatum; före/efter finns i metadata. PO-filerna och diffarna behåller ursprunglig teckenkodning (OpenSP: ISO-8859-1).

De viktigaste fynden är en felaktig Python-nyckel i Cinder som ger `KeyError`, två trunkerade tidsformat i GDB, felaktig formatering i Glance, trasiga länkar/taggar samt omkastade vinkelvärden i libmypaint. Översättningsförslagen har inte lagts in i systemets MO-filer. SHA-256-kontroll efter arbetet visar att samtliga 479 inlästa sökvägar är oförändrade.

## Publicerade rättningar

Samtliga 57 fyndförslag är införda i **31 PO-filer, 61 ändrade översättningsposter**. De 65 ursprungliga förekomsterna inkluderar fyra ISO-alias. [Filindex med upstream](README.md), [metadata för alla rättade filer](metadata.json) och [validering](validation-summary.json). Originalfilerna bevaras i `original/`; rättade filer ligger i `po/`. Git har dessutom två dokumenterade sysdep-normaliseringar. Systemets MO-filer är oförändrade.

## Omfattning och metod

| Mapp | Sökvägar | Poster före deduplicering | Unika binärkataloger | Poster efter deduplicering |
|---|---:|---:|---:|---:|
| `/usr/share/locale-langpack/sv/LC_MESSAGES` | 432 | 204 087 | 432 | 204 087 |
| `/usr/share/locale/sv/LC_MESSAGES` | 47 | 40 536 | 41 | 26 217 |
| Totalt | 479 | 244 623 | 473 | 230 304 |

Fem sökvägar är symboliska länkar till ISO-kataloger. `WebKitGTK-4.1.mo` och `WebKitGTK-6.0.mo` är byteidentiska. Deduplicering sker med SHA-256; olika filer för samma domän i de två mapparna behålls. Den kanoniska filen och alla alias framgår av [manifestet](manifest.json). Fyndens 65 förekomster inkluderar fyra ISO-alias.

Alla 479 sökvägar har dekompilerats med **GNU `msgunfmt --no-wrap` 0.23.2**. Radnummer i rapporten avser de medföljande dekompilerade PO-filerna, inte en upstream-PO-fil eller en binär MO-offset. Originalets MO-sökväg, hash, metadata, PO-hash och kommandoutfall finns i manifestet.

`l10n-lint` har körts med samtliga standardregler och språk `sv`. `svlang` har kört skrivregler och svengelska på samtliga 231 636 målformer, samt kontext- och pluralmedveten konsekvenskontroll mellan katalogerna. Kontrollerna anropas via verktygens installerade Python-API för att bevara kopplingen till varje PO-post; [körskripten](scripts/scan.py) redovisar exakt anrop. Svlangs heuristiska naturlighetspoäng och full ordlistekontroll ingår inte.

Samtliga 15 PO-exporter i Swedish TM och termbankens CSV har jämförts mot exakt källtext. Referensexporterna saknar ursprunglig kontext och pluralidentitet. Avvikelser är därför granskningskandidater. Ingen automatisk ersättning har gjorts utifrån majoritetsval eller konfidensvärden.

## Råresultat efter verktygsfixarna

| Kontroll | Resultat | Tolkning |
|---|---:|---|
| msgunfmt | 479/479 lyckades | Samtliga sökvägar extraherade |
| msgfmt --check --check-format | 478/479 godkända | Git ger reproducerbar sysdep-dubblett efter dekompilering, se nedan |
| Återkompilering/jämförelse | 478/478 jämförbara filer har samma meddelandetabell | Git exkluderad på grund av dubbletterna; metadata och binär layout jämförs inte |
| l10n-lint | 16 297 träffar | 1 733 error, 8 707 warning, 5 857 info; verktygsnivå, inte verifierad allvarlighetsgrad |
| svlang skrivregler/svengelska | 426 träffar | Språkkandidater |
| svlang konsekvens | 3 927 grupper | Samma källtext/kontext/pluralform har olika måltexter |
| Swedish TM: exakt parträff | 138 550 målformer | Överensstämmelse är ingen kvalitetsgaranti |
| Swedish TM: annan måltext | 13 328 målformer | Förslag finns; kontext måste bedömas |
| Swedish TM: källtext saknas | 79 758 målformer | Ingen exakt referensträff |
| Termbank: kanonisk träff | 67 454 målformer | Exakt överensstämmelse |
| Termbank: annan måltext | 9 017 målformer | Terminologikandidater |
| Termbank: källtext saknas | 155 165 målformer | Ingen exakt referensträff |

Träffarna från olika kontroller överlappar och får inte summeras till ett antal fel. [Lint-kandidater CSV](lint-kandidater.csv), [TM-avvikelser JSON](raw/tm-differences.json), [termavvikelser JSON](raw/terminology-differences.json), [konsekvensgrupper JSON](raw/svlang-consistency.json) och [statistik per katalog](scan-summary.json) innehåller hela resultatet. En fyndreferens i kandidat-CSV betyder att samma post har ett verifierat fynd; den bekräftar inte varje regel som träffat posten.

## Prioritering och verifiering

P1: trasigt format med högre funktionsrisk. P2: förlorad information, felaktig betydelse, markup eller övriga formatavvikelser. P3: stavning och språk. Prioriteringen beskriver fyndet i katalogen; berörda program har inte körts igenom i sina respektive felvägar.

23 utvalda formatförslag kontrollerades separat med syntetiska formatflaggor: 22 original underkändes och samtliga 23 förslag godkändes av `msgfmt --check-format`. Glances original godkänns av gettext men Python konsumerar `s` i ordet `som`: resultatet blir `image-1om`. Det är verifierat med en ofarlig formateringsreproduktion. Cinders original ger `KeyError: ret.statuss`; originalets engelska text och det svenska förslaget fungerar med samma exempeldictionary. Fulla kontrollutdata finns i [findings.json](findings.json).

## Bekräftade fynd

Tabellen är ett prioriterat urval ur de automatiska träffarna. Full källtext, nuvarande översättning, komplett förslag, samtliga förekomster och verifieringsdata finns längre ned samt i [findings.csv](findings.csv) och [findings.json](findings.json).

| ID | Prioritet | Katalog och PO-rad | Fynd |
|---|---|---|---|
| F001 | P1 | [locale-langpack/cinder:1695](original/locale-langpack/cinder.po) | Fel nyckel i Python-formatfält |
| F003 | P1 | [locale-langpack/gdb:14147](original/locale-langpack/gdb.po) | Två trasiga tidsformat |
| F002 | P2 | [locale-langpack/glance:1473](original/locale-langpack/glance.po) | Typbokstaven saknas efter image_id |
| F004 | P2 | [locale/OpenSP:799](original/locale/OpenSP.po) | Fel argument för den saknade starttaggen |
| F005 | P2 | [locale/OpenSP:874](original/locale/OpenSP.po) | HTTP-adressen har tappat sin platshållare |
| F006 | P2 | [locale/OpenSP:1120](original/locale/OpenSP.po) | Identifieraren saknas i felmeddelandet |
| F007 | P2 | [locale/OpenSP:1126](original/locale/OpenSP.po) | Värdnumret saknas i felmeddelandet |
| F008 | P2 | [locale/OpenSP:1390](original/locale/OpenSP.po) | Numrerad platshållare har blivit printf-format |
| F009 | P2 | [locale/OpenSP:1537](original/locale/OpenSP.po) | Entitetens namn saknas |
| F010 | P2 | [locale/OpenSP:1546](original/locale/OpenSP.po) | Entitetens namn saknas |
| F011 | P2 | [locale/OpenSP:1567](original/locale/OpenSP.po) | Entitetens namn saknas |
| F012 | P2 | [locale-langpack/dpkg:3433](original/locale-langpack/dpkg.po) | Översättningen lägger till ett obefintligt argument |
| F013 | P2 | [locale-langpack/binutils:9133](original/locale-langpack/binutils.po) | Extra %s i meddelandet om felsökningssektion |
| F014 | P2 | [locale-langpack/binutils:9601](original/locale-langpack/binutils.po) | Extra %s i meddelandet om BFD-data |
| F015 | P2 | [locale-langpack/cryptsetup:2486](original/locale-langpack/cryptsetup.po) | Rothash har blivit begärd hash och ett extra argument |
| F016 | P2 | [locale-langpack/cryptsetup:2717](original/locale-langpack/cryptsetup.po) | Extra %u i meddelandet om metadata |
| F017 | P2 | [locale-langpack/fetchmail:2123](original/locale-langpack/fetchmail.po) | Extra %s i meddelandet om --moveto |
| F018 | P2 | [locale-langpack/gas:11177](original/locale-langpack/gas.po) | Ett dollartecken har blivit %s |
| F019 | P2 | [locale-langpack/gdb:3188](original/locale-langpack/gdb.po) | Skiftlägesinställningen ersätts med ett fast påstående |
| F020 | P2 | [locale-langpack/gdb:9950](original/locale-langpack/gdb.po) | &s används i stället för %s |
| F021 | P2 | [locale-langpack/git:8271](original/locale-langpack/git.po) | Extra %s i meddelandet om incheckningsgraf |
| F022 | P2 | [locale-langpack/ld:1712](original/locale-langpack/ld.po) | Duplicerat instick får ett extra argument |
| F023 | P2 | [locale-langpack/libgphoto2-2:6856](original/locale-langpack/libgphoto2-2.po) | Antalet återförsök har ersatts med %i |
| F024 | P2 | [locale-langpack/libgphoto2-2:6161](original/locale-langpack/libgphoto2-2.po) | Adressen till utvecklarlistan ersätts med %s |
| F025 | P2 | [locale-langpack/simple-scan:278](original/locale-langpack/simple-scan.po) | Trasiga länktaggar i hjälptexten |
| F026 | P2 | [locale-langpack/synaptic:281](original/locale-langpack/synaptic.po) | Fel avslutning av big-taggen |
| F027 | P2 | [locale-langpack/slideshow-oem-config-ubuntu-mate:164](original/locale-langpack/slideshow-oem-config-ubuntu-mate.po) | Netflix får fel avslutningstagg |
| F028 | P2 | [locale-langpack/snappy:2305](original/locale-langpack/snappy.po) | Trasig länk till felsökningshjälp |
| F029 | P2 | [locale/libmypaint:287](original/locale/libmypaint.po) | Pennans vinkelvärden är omkastade (x-led) |
| F030 | P2 | [locale/libmypaint:290](original/locale/libmypaint.po) | Pennans vinkelvärden är omkastade (y-led) |
| F031 | P2 | [locale/iso_639-3:15064](original/locale/iso_639-3.po) | Medelfranskans tidsintervall avviker |
| F032 | P2 | [locale/iso_639-3:15073](original/locale/iso_639-3.po) | Medeliriskans tidsintervall avviker |
| F033 | P2 | [locale/iso_639-3:18205](original/locale/iso_639-3.po) | Fornfranskans slutår avviker |
| F034 | P2 | [locale/iso_639-3:18223](original/locale/iso_639-3.po) | Forniriskans slutår avviker |
| F035 | P3 | [locale-langpack/NetworkManager:87](original/locale-langpack/NetworkManager.po) | Stavfel: rutttyp |
| F036 | P3 | [locale-langpack/NetworkManager:7022](original/locale-langpack/NetworkManager.po) | Stavfel: huvudrutttabellen |
| F037 | P3 | [locale-langpack/app-install-data:4845](original/locale-langpack/app-install-data.po) | Stavfel: nätverksanslutnngar |
| F038 | P3 | [locale-langpack/app-install-data:15555](original/locale-langpack/app-install-data.po) | Stavfel: Allmänn |
| F039 | P3 | [locale-langpack/ubiquity-debconf:810](original/locale-langpack/ubiquity-debconf.po) | Stavfel: tidspunkt |
| F040 | P3 | [locale-langpack/dpkg-dev:949](original/locale-langpack/dpkg-dev.po) | Stavfel: körnng |
| F041 | P3 | [locale-langpack/dpkg-dev:1649](original/locale-langpack/dpkg-dev.po) | Stavfel: klasss |
| F042 | P3 | [locale-langpack/glance:1398](original/locale-langpack/glance.po) | Stavfel: tilllåter |
| F043 | P3 | [locale-langpack/mutt:1298](original/locale-langpack/mutt.po) | Stavfel: öpppna |
| F044 | P3 | [locale-langpack/unity-control-center:343](original/locale-langpack/unity-control-center.po) | Stavfel: Tilllåt |
| F045 | P3 | [locale-langpack/unity-control-center:349](original/locale-langpack/unity-control-center.po) | Stavfel: Tilllåt |
| F046 | P3 | [locale-langpack/unity:81](original/locale-langpack/unity.po) | Stavfel: Tilllåter |
| F047 | P3 | [locale-langpack/unity:814](original/locale-langpack/unity.po) | Stavfel: Skugggfärg |
| F048 | P3 | [locale-langpack/xz-man:1120](original/locale-langpack/xz-man.po) | Stavfel: kommmer |
| F049 | P3 | [locale/OpenSP:646](original/locale/OpenSP.po) | Felaktig upprepning: därför därför |
| F050 | P3 | [locale/dpkg:133](original/locale/dpkg.po) | Felaktig upprepning: men men |
| F051 | P3 | [locale/dpkg:2424](original/locale/dpkg.po) | Felaktig upprepning: för för |
| F052 | P3 | [locale/gnome-builder:2868](original/locale/gnome-builder.po) | Felaktig upprepning: dina dina |
| F053 | P3 | [locale-langpack/snappy:2749](original/locale-langpack/snappy.po) | Felaktig upprepning: relative tider till till |
| F054 | P3 | [locale-langpack/xfsprogs:5717](original/locale-langpack/xfsprogs.po) | Felaktig upprepning: ignoreras ignoreras |
| F055 | P3 | [locale-langpack/xfsprogs:6391](original/locale-langpack/xfsprogs.po) | Felaktig upprepning: filsystemet filsystemet |
| F056 | P3 | [locale-langpack/xz-man:1651](original/locale-langpack/xz-man.po) | Felaktig upprepning: 1 beta beta |
| F057 | P3 | [locale-langpack/xz-man:1837](original/locale-langpack/xz-man.po) | Felaktig upprepning: med med |

## Begränsningar och avvisade falska larm

MO-formatet bevarar inte de flesta ursprungliga formatflaggor, källkodsreferenser, kommentarer, fuzzy-markeringar eller oöversatta poster. Granskningen kan därför inte mäta projektens fullständiga översättningstäckning. Ett godkänt `msgfmt --check-format` på dekompilerad PO innebär inte att alla runtime-formatsträngar är korrekta.

Git-katalogens dubbla pluralposter beror på samspelet mellan GNU gettexts förutvidgade `<PRI…>`-format och portabla systemberoende poster. Samma fel återskapades från en minimal giltig PO-fil genom `msgfmt → msgunfmt → msgfmt`. Detta är **en verktygs-/extraktionsavvikelse**, inte ett belagt svenskt översättningsfel. [Reproduktion](raw/gettext-sysdep-reproducer.json), [giltigt testoriginal](raw/sysdep-original.po), [dekompilerat test](raw/sysdep-unformatted.po).

Följande kvarvarande regelträffar behöver särskild bedömning: `<FILE>` i kommandodokumentation kan översättas utan att vara XML; datumformat får lokaliseras; svenska decimaltecken och utskrivna tal skiljer sig legitimt från originalet; radbrytningar och indrag kan anpassas; e2fsprogs använder egen @-expansion; portabla PRI-format kan visas som expanderade format av msgunfmt. `man man`, språknamn med upprepade ord och korrekta svenska konstruktioner med `till till` är inte automatiskt fel. Oförändrad käll- och måltext kan vara ett produktnamn eller en kod. Rårapportens `nordic-accelerator`-nivå säger inte i sig att en svensk tangentkombination är trasig.

Referensbankernas matchningar är sekundärt stöd. Stavningsfelen och formatfynden ovan har bedömts mot de faktiska meddelandena, inte godkänts för att en referensbank föredrar en annan text.

## Installerade verktyg och genomförda förbättringar

Kommandona finns i `/usr/local/bin` och körs från `/opt/yeager-l10n/2026-09-19/venv`. Swedish TM är installerat i `/usr/local/share/swedish-tm` och termbanken i `/usr/local/share/swedish-foss-terminology`. Datasamlingarna är referensdata, inte egna körbara granskningsprogram. Installationen ändrar inte systemets Python-paket.

Installerade lokala versioner: **l10n-lint 1.21.2+localeaudit1** och **svlang 0.2.1+localeaudit1**. De bygger på de angivna GitHub-revisionerna nedan. Ändringarna är implementerade och installerade lokalt; de är inte införda i verktygens upstream-repon. Patchar med regressionstester medföljer.

| Förbättring | Före → efter i denna körning |
|---|---:|
| Pluralhuvud krävs endast när filen faktiskt har pluralposter; felaktiga befintliga huvuden kontrolleras fortfarande | 200 → 0 felaktiga plural-header-missing |
| Identiska printf-kontrakt känns igen även med suffix som `%iHz`, `%uth` och `%ss`; verkliga typ-/antalsskillnader kontrolleras fortsatt | 268 → 188 placeholder-mismatch |
| Sammansatta ord och talintervall tolkas inte som kommandoflaggor | 16 → 2 option-value-missing |
| Oförändrade källtoken som IEEE, PPP, pppd, III och www ger inte svenska trippelbokstavslarm; uttryckliga stavfelsregler behålls | 296 → 45 typo |
| Både iväg och i väg accepteras av svlang | 2 felaktiga stavfelsträffar borttagna |

Totalt **547 verktygsorsakade träffar borttagna**. Stödet för båda stavningarna av iväg finns i [Svensk ordbok via Språkbanken](https://spraakbanken.gu.se/resurser/data/karp/so-2009-webbversion/iv%C3%A4g.html). L10n-lints tester: **274 godkända**; svlangs tester: **83 godkända**. Nya tester täcker både de falska larmen och kontrollfall där verkliga fel ska fortsätta upptäckas. Alla 473 unika kataloger har körts om med de installerade rättade versionerna.

[l10n-lint-patch](tool-fixes/l10n-lint.patch) · [svlang-patch](tool-fixes/svlang.patch) · [ändringsmetadata](tool-fixes/changes.json) · [råresultat före rättning](raw/fore-verktygsfix/scan-summary.json).

## Verktygsrevisioner och reproducerbarhet

- [l10n-lint](https://github.com/yeager/l10n-lint), commit `1377624eae52703510d0c8f25010009edfdfee02`.
- [svlang](https://github.com/yeager/svlang), commit `41e5bc0afdf428e2ecf8f2379f2b2bfa4214d66c`.
- [swedish-tm](https://github.com/yeager/swedish-tm), commit `96972a8aa49d364e078f34ee9322fa4e377ff363`.
- [swedish-foss-terminology](https://github.com/yeager/swedish-foss-terminology), commit `063c2d9bcb8581ca26ace192e72730950218d143`.

Exakt installerad proveniens och lokala patchhashar finns i [tools.json](tools.json). De två ursprungligen angivna adresserna `yeager/lswedish-tm` och `yeager/lsvlang` fanns inte; de verifierade arkiven `yeager/swedish-tm` och `yeager/svlang` användes.

Körningen använder i grunden följande kommandon för varje fil; utdata lagras utanför systemets översättningsmappar:

```sh
msgunfmt --no-wrap -o dekompilerad.po /sökväg/katalog.mo
msgfmt --check --check-format -o /dev/null dekompilerad.po
l10n-lint --language sv --format json --output resultat.json dekompilerad.po
```

[extract.py](scripts/extract.py), [scan.py](scripts/scan.py), [references.py](scripts/references.py) och [curate.py](scripts/curate.py) dokumenterar extraktion, full automatisk kontroll, exakta referensjämförelser och explicit urval/verifiering. Skripten använder arbetsmappens `work/` och `outputs/` samt de installerade verktygssökvägarna. [source-integrity.json](source-integrity.json) redovisar slutlig integritetskontroll.

## Fullständiga fynd och förslag

### F001 · P1 · Fel nyckel i Python-formatfält

ret.status har blivit ret.statuss. Formatering med originalets nycklar ger KeyError.

Förekomster: [locale-langpack/cinder:1695](original/locale-langpack/cinder.po).

Källtext:

```text
Error getting replication source details. Return code: %(ret.status)d Message: %(ret.data)s .
```

Nuvarande svenska:

```text
Fel vid hämtning av replikationskällans detaljer. Returkod: %(ret.statuss)d Meddelande: %(ret.data)s .
```

Förslag:

```text
Fel vid hämtning av replikationskällans detaljer. Returkod: %(ret.status)d Meddelande: %(ret.data)s .
```

### F002 · P2 · Typbokstaven saknas efter image_id

%(image_id) saknar s. Python konsumerar mellanslaget och s i ordet som som formatsyntax: exempelvärdet image-1 följs av om i stället för som.

Förekomster: [locale-langpack/glance:1473](original/locale-langpack/glance.po).

Källtext:

```text
The Image %(image_id)s object being created by this task %(task_id)s, is no longer in valid status for further processing.
```

Nuvarande svenska:

```text
Avbildobjektet %(image_id) som skapas av den här uppgiften %(task_id)s, är inte längre i en giltig status för vidare behandling.
```

Förslag:

```text
Avbildobjektet %(image_id)s som skapas av den här uppgiften %(task_id)s, är inte längre i en giltig status för vidare behandling.
```

### F003 · P1 · Två trasiga tidsformat

Båda %06ld har trunkerats till %06. Formatkontraktet och återgivningen av tidsvärden går förlorade.

Förekomster: [locale-langpack/gdb:14147](original/locale-langpack/gdb.po).

Källtext:

```text
Trace started at %ld.%06ld secs, stopped %ld.%06ld secs later.

```

Nuvarande svenska:

```text
Spårningen startade vid %ld.%06 sekunder och avslutades %ld.%06 sekunder senare

```

Förslag:

```text
Spårningen startade vid %ld.%06ld sekunder och avslutades %ld.%06ld sekunder senare

```

### F004 · P2 · Fel argument för den saknade starttaggen

Den andra platshållaren ska vara %2; nu visas argument %1 två gånger.

Förekomster: [locale/OpenSP:799](original/locale/OpenSP.po).

Källtext:

```text
document type does not allow element %1 here; assuming missing %2 start-tag
```

Nuvarande svenska:

```text
dokumenttypen tillåter ej elementet %1 här; antar att starttaggen %1 saknas
```

Förslag:

```text
dokumenttypen tillåter ej elementet %1 här; antar att starttaggen %2 saknas
```

### F005 · P2 · HTTP-adressen har tappat sin platshållare

%1 har ersatts med (%), så den berörda URL-adressen kan inte återges korrekt.

Förekomster: [locale/OpenSP:874](original/locale/OpenSP.po).

Källtext:

```text
empty host in HTTP URL %1
```

Nuvarande svenska:

```text
tom värd i HTTP-URL:en(%)
```

Förslag:

```text
tom värd i HTTP-URL:en %1
```

### F006 · P2 · Identifieraren saknas i felmeddelandet

Originalets %1 saknas i översättningen.

Förekomster: [locale/OpenSP:1120](original/locale/OpenSP.po).

Källtext:

```text
invalid formal public identifier %1: no SPACE after public text class
```

Nuvarande svenska:

```text
ogiltig formell publik identifierare: inget SPACE efter publik textklass
```

Förslag:

```text
ogiltig formell publik identifierare %1: inget SPACE efter publik textklass
```

### F007 · P2 · Värdnumret saknas i felmeddelandet

Originalets %1 saknas i översättningen.

Förekomster: [locale/OpenSP:1126](original/locale/OpenSP.po).

Källtext:

```text
invalid host number %1
```

Nuvarande svenska:

```text
ogiltigt värdnummer
```

Förslag:

```text
ogiltigt värdnummer %1
```

### F008 · P2 · Numrerad platshållare har blivit printf-format

%1 har ändrats till %d, vilket är en annan formatsyntax.

Förekomster: [locale/OpenSP:1390](original/locale/OpenSP.po).

Källtext:

```text
normalized length of attribute value literal must not exceed LITLEN (%1); length was %2
```

Nuvarande svenska:

```text
längden av normaliserad attributvärdesliteral får ej överskrida LITLEN (%d); längden var %2
```

Förslag:

```text
längden av normaliserad attributvärdesliteral får ej överskrida LITLEN (%1); längden var %2
```

### F009 · P2 · Entitetens namn saknas

Originalets %1 saknas; felmeddelandet tappar uppgiften om vilken entitet som avses.

Förekomster: [locale/OpenSP:1537](original/locale/OpenSP.po).

Källtext:

```text
reference to external data entity %1 not allowed in XML
```

Nuvarande svenska:

```text
referens till extern dataentitet ej tillåtet i XML
```

Förslag:

```text
referens till extern dataentitet %1 ej tillåtet i XML
```

### F010 · P2 · Entitetens namn saknas

Originalets %1 saknas; felmeddelandet tappar uppgiften om vilken entitet som avses.

Förekomster: [locale/OpenSP:1546](original/locale/OpenSP.po).

Källtext:

```text
reference to internal SDATA entity %1 not allowed in XML
```

Nuvarande svenska:

```text
referens till intern SDATA-entitet ej tillåtet i XML
```

Förslag:

```text
referens till intern SDATA-entitet %1 ej tillåtet i XML
```

### F011 · P2 · Entitetens namn saknas

Originalets %1 saknas; felmeddelandet tappar uppgiften om vilken entitet som avses.

Förekomster: [locale/OpenSP:1567](original/locale/OpenSP.po).

Källtext:

```text
reference to subdocument entity %1 not allowed in XML
```

Nuvarande svenska:

```text
referens till subdokumententitet ej tillåtet i XML
```

Förslag:

```text
referens till subdokumententitet %1 ej tillåtet i XML
```

### F012 · P2 · Översättningen lägger till ett obefintligt argument

Originalet innehåller ingen %s. Översättningen har kvar en platshållare och ett prefix som saknar motsvarighet i källtexten.

Förekomster: [locale-langpack/dpkg:3433](original/locale-langpack/dpkg.po), [locale/dpkg:3412](original/locale/dpkg.po).

Källtext:

```text
need a pathname argument
```

Nuvarande svenska:

```text
--%s behöver ett sökvägsnamnargument
```

Förslag:

```text
behöver ett sökvägsargument
```

### F013 · P2 · Extra %s i meddelandet om felsökningssektion

Källtexten har ingen formateringsparameter; den svenska texten lägger till : %s.

Förekomster: [locale-langpack/binutils:9133](original/locale-langpack/binutils.po).

Källtext:

```text
can't create debugging section
```

Nuvarande svenska:

```text
kan inte skapa felsökningssektionen: %s
```

Förslag:

```text
kan inte skapa felsökningssektionen
```

### F014 · P2 · Extra %s i meddelandet om BFD-data

Källtexten har ingen formateringsparameter; den svenska texten lägger till : %s.

Förekomster: [locale-langpack/binutils:9601](original/locale-langpack/binutils.po).

Källtext:

```text
error copying private BFD data
```

Nuvarande svenska:

```text
fel vid kopiering av privat BFD-data: %s
```

Förslag:

```text
fel vid kopiering av privat BFD-data
```

### F015 · P2 · Rothash har blivit begärd hash och ett extra argument

Root hash har fått annan innebörd och översättningen innehåller en %s som originalet saknar.

Förekomster: [locale-langpack/cryptsetup:2486](original/locale-langpack/cryptsetup.po).

Källtext:

```text
Root hash signature verification is not supported.
```

Nuvarande svenska:

```text
Begärd hashsignaturverifiering %s stöds inte.
```

Förslag:

```text
Verifiering av rothashsignaturer stöds inte.
```

### F016 · P2 · Extra %u i meddelandet om metadata

Originalet anger inte någon numerisk posttyp men översättningen kräver ett sådant argument.

Förekomster: [locale-langpack/cryptsetup:2717](original/locale-langpack/cryptsetup.po).

Källtext:

```text
Unexpected metadata entry found when parsing startup key.
```

Nuvarande svenska:

```text
Oväntad metadatapost av typ ”%u” funnen vid tolkning av uppstartsnyckel.
```

Förslag:

```text
Oväntad metadatapost funnen vid tolkning av uppstartsnyckel.
```

### F017 · P2 · Extra %s i meddelandet om --moveto

Översättningen har ett formatargument som inte finns i originalet.

Förekomster: [locale-langpack/fetchmail:2123](original/locale-langpack/fetchmail.po).

Källtext:

```text
fetchmail: configuration invalid, --moveto is only valid for IMAP servers

```

Nuvarande svenska:

```text
fetchmail: %s-konfigurationen är ogiltig, --moveto är endast giltigt för IMAP-servrar

```

Förslag:

```text
fetchmail: konfigurationen är ogiltig, --moveto är endast giltigt för IMAP-servrar

```

### F018 · P2 · Ett dollartecken har blivit %s

Originalets bokstavliga $ får inte ersättas med ett nytt formatargument.

Förekomster: [locale-langpack/gas:11177](original/locale-langpack/gas.po).

Källtext:

```text
instruction requires label sans '$'
```

Nuvarande svenska:

```text
instruktion kräver etikett utan ”%s”
```

Förslag:

```text
instruktion kräver etikett utan ”$”
```

### F019 · P2 · Skiftlägesinställningen ersätts med ett fast påstående

Originalet återger inställningen via %s. Översättningen säger alltid att sökningen inte är skiftlägeskänslig.

Förekomster: [locale-langpack/gdb:3188](original/locale-langpack/gdb.po).

Källtext:

```text
Case sensitivity in name search is "%s".

```

Nuvarande svenska:

```text
Namnsökningen är inte skiftlägeskänslig

```

Förslag:

```text
Namnsökningens skiftlägeskänslighet är ”%s”.

```

### F020 · P2 · &s används i stället för %s

Sektionens namn försvinner eftersom procenttecknet har blivit &.

Förekomster: [locale-langpack/gdb:9950](original/locale-langpack/gdb.po).

Källtext:

```text
Section %s not found
```

Nuvarande svenska:

```text
Kapitel &s hittades inte
```

Förslag:

```text
Sektionen %s hittades inte
```

### F021 · P2 · Extra %s i meddelandet om incheckningsgraf

Källtexten har ingen platshållare för filnamn men översättningen har %s.

Förekomster: [locale-langpack/git:8271](original/locale-langpack/git.po).

Källtext:

```text
commit-graph file is too small
```

Nuvarande svenska:

```text
incheckningsgraffilen %s är för liten
```

Förslag:

```text
incheckningsgraffilen är för liten
```

### F022 · P2 · Duplicerat instick får ett extra argument

Översättningen innehåller två %s medan originalet bara innehåller en. %P är länkarens egna direktiv och ska bevaras.

Förekomster: [locale-langpack/ld:1712](original/locale-langpack/ld.po).

Källtext:

```text
%P: %s: duplicated plugin

```

Nuvarande svenska:

```text
%P: %s: duplicerat instick: %s

```

Förslag:

```text
%P: %s: duplicerat instick

```

### F023 · P2 · Antalet återförsök har ersatts med %i

Originalets fasta två återförsök har blivit ett formatargument som inte finns i originalet.

Förekomster: [locale-langpack/libgphoto2-2:6856](original/locale-langpack/libgphoto2-2.po), [locale-langpack/libgphoto2-6:9598](original/locale-langpack/libgphoto2-6.po).

Källtext:

```text
Transmission timed out even after 2 retries. Giving up...
```

Nuvarande svenska:

```text
Överföringen tog för lång tid och avbröts efter %i försök. Ger upp…
```

Förslag:

```text
Överföringen överskred tidsgränsen även efter två nya försök. Ger upp…
```

### F024 · P2 · Adressen till utvecklarlistan ersätts med %s

Originalet hänvisar till gphotos utvecklarlista utan formatargument. Översättningen kräver en extra %s.

Förekomster: [locale-langpack/libgphoto2-2:6161](original/locale-langpack/libgphoto2-2.po), [locale-langpack/libgphoto2-6:8692](original/locale-langpack/libgphoto2-6.po).

Källtext:

```text
Some notes about Epson cameras:
- Some parameters are not controllable remotely:
  * zoom
  * focus
  * custom white balance setup
- Configuration has been reverse-engineered with
  a PhotoPC 3000z, if your camera acts differently
  please send a mail to the gphoto developer mailing list (in English)

```

Nuvarande svenska:

```text
Några anteckningar om Epson-kameror:
- Vissa parametrar går inte att fjärrstyra:
  * zoom
  * fokus
  * anpassad vitbalansinställning
- Konfigurationen har blivit avkodad med
  en PhotoPC 3000z, om din kamera beter sig annorlunda
  skriv ett brev till %s (på Engelska)

```

Förslag:

```text
Några anteckningar om Epson-kameror:
- Vissa parametrar går inte att fjärrstyra:
  * zoom
  * fokus
  * anpassad vitbalansinställning
- Konfigurationen har blivit avkodad med
  en PhotoPC 3000z, om din kamera beter sig annorlunda
  skriv ett brev till gphotos utvecklarsändlista (på engelska)

```

### F025 · P2 · Trasiga länktaggar i hjälptexten

Den första länken har felaktig escapning och saknar avslutande attributcitat och >. Den andra saknar även inledande <. Länktexten hamnar i attributen.

Förekomster: [locale-langpack/simple-scan:278](original/locale-langpack/simple-scan.po).

Källtext:

```text
Please check if your <a href="http://www.sane-project.org/sane-supported-devices.html">scanner is supported by SANE</a>, otherwise report the issue to the <a href="https://alioth-lists.debian.net/cgi-bin/mailman/listinfo/sane-devel">SANE mailing list</a>.
```

Nuvarande svenska:

```text
Se om din <a href=\"http://www.sane-project.org/sane-supported-devices.html bildläsare stöds av SANE</a>, annars kan du rapportera problemet till a href="https://alioth-lists.debian.net/cgi-bin/mailman/listinfo/sane-devel sändlistan för SANE</a>."
```

Förslag:

```text
Kontrollera om din <a href="http://www.sane-project.org/sane-supported-devices.html">bildläsare stöds av SANE</a>, annars kan du rapportera problemet till <a href="https://alioth-lists.debian.net/cgi-bin/mailman/listinfo/sane-devel">sändlistan för SANE</a>.
```

### F026 · P2 · Fel avslutning av big-taggen

<b><big> avslutas med </b></b>. Den inre taggen ska avslutas med </big>.

Förekomster: [locale-langpack/synaptic:281](original/locale-langpack/synaptic.po).

Källtext:

```text
<b><big>Mark upgrades in a smart way?</big></b>

The default upgrade method skips upgrades that would introduce conflicts or require installation of additional packages.

The smart upgrade (dist-upgrade) attempts to resolve conflicts and to fulfil all dependencies of upgrades in a smart way.

<b>Note:</b> The upgrades will be marked only. You still have to apply them afterwards.
```

Nuvarande svenska:

```text
<b><big>Markera uppgraderingar på ett smart sätt?</b></b>

Standardmetoden för uppgradering hoppar över de uppgraderingar som skulle introducera konflikter eller kräva installation av ytterligare paket.

Den smarta uppgraderingen (dist-upgrade) försöker att lösa konflikter och uppfylla alla beroenden för uppgraderingen på ett smart sätt.

<b>Observera:</b> Uppgraderingarna kommer endast markeras. Du behöver fortfarande verkställa dem efteråt.
```

Förslag:

```text
<b><big>Markera uppgraderingar på ett smart sätt?</big></b>

Standardmetoden för uppgradering hoppar över de uppgraderingar som skulle introducera konflikter eller kräva installation av ytterligare paket.

Den smarta uppgraderingen (dist-upgrade) försöker att lösa konflikter och uppfylla alla beroenden för uppgraderingen på ett smart sätt.

<b>Observera:</b> Uppgraderingarna kommer endast markeras. Du behöver fortfarande verkställa dem efteråt.
```

### F027 · P2 · Netflix får fel avslutningstagg

</string> ska vara </strong>. Samma fel finns i OEM-bildspelet.

Förekomster: [locale-langpack/slideshow-oem-config-ubuntu-mate:164](original/locale-langpack/slideshow-oem-config-ubuntu-mate.po), [locale-langpack/slideshow-ubuntu-mate:164](original/locale-langpack/slideshow-ubuntu-mate.po).

Källtext:

```text
Ubuntu MATE comes with <strong>Firefox</strong> pre-installed and <strong>Google Chrome</strong> is in the Software Boutique so you can watch content from your favourite streaming services such as <strong>Netflix</strong> and <strong>YouTube</strong>.
```

Nuvarande svenska:

```text
Ubuntu MATE har <strong>Firefox</strong> förinstallerat, och <strong>Google Chrome</strong> finns i Programbutiken så att du kan titta på innehåll från dina favorit-streaming-tjänster, såsom <strong>Netflix</string> och <strong>YouTube</strong>.
```

Förslag:

```text
Ubuntu MATE har <strong>Firefox</strong> förinstallerat, och <strong>Google Chrome</strong> finns i Programbutiken så att du kan titta på innehåll från dina favorit-streaming-tjänster, såsom <strong>Netflix</strong> och <strong>YouTube</strong>.
```

### F028 · P2 · Trasig länk till felsökningshjälp

https: har blivit https; så länken är inte längre korrekt.

Förekomster: [locale-langpack/snappy:2305](original/locale-langpack/snappy.po).

Källtext:

```text
%s was not found in your $PATH. If you've not restarted your session since you installed snapd, try doing that. Please see https://forum.snapcraft.io/t/9469 for more details.
```

Nuvarande svenska:

```text
%s hittades inte i din $PATH. Om du inte har startat om din session sedan du installerade snapd, testa att göra det. Se https;//forum.snapcraft.io/t/9469 för fler detaljer.
```

Förslag:

```text
%s hittades inte i din $PATH. Om du inte har startat om din session sedan du installerade snapd, testa att göra det. Se https://forum.snapcraft.io/t/9469 för fler detaljer.
```

### F029 · P2 · Pennans vinkelvärden är omkastade (x-led)

Originalet anger ±90 vid parallell penna och 0 vid vinkelrät penna. Översättningen anger motsatsen.

Förekomster: [locale/libmypaint:287](original/locale/libmypaint.po).

Källtext:

```text
Declination of stylus tilt on X-Axis. 90/-90 when stylus is parallel to tablet and 0 when it's perpendicular to tablet.
```

Nuvarande svenska:

```text
Pennans lutning i x-led relativt ritbrädans yta. Är 0 när pennan är parallell och 90.0 när den hålls vinkelrät.
```

Förslag:

```text
Pennans lutning i x-led. Värdet är 90 eller −90 när pennan är parallell med ritplattan och 0 när den är vinkelrät mot ritplattan.
```

### F030 · P2 · Pennans vinkelvärden är omkastade (y-led)

Originalet anger ±90 vid parallell penna och 0 vid vinkelrät penna. Översättningen anger motsatsen.

Förekomster: [locale/libmypaint:290](original/locale/libmypaint.po).

Källtext:

```text
Declination of stylus tilt on Y-Axis. 90/-90 when stylus is parallel to tablet and 0 when it's perpendicular to tablet.
```

Nuvarande svenska:

```text
Pennans lutning i y-led relativt ritbrädans yta. Är 0 när pennan är parallell och 90.0 när den hålls vinkelrät.
```

Förslag:

```text
Pennans lutning i y-led. Värdet är 90 eller −90 när pennan är parallell med ritplattan och 0 när den är vinkelrät mot ritplattan.
```

### F031 · P2 · Medelfranskans tidsintervall avviker

Årtalen överensstämmer inte med katalogens engelska källtext. Förslaget återställer källtextens intervall.

Förekomster: [locale/iso_639-3:15064](original/locale/iso_639-3.po), [locale/iso_639_3:15064](original/locale/iso_639-3.po).

Källtext:

```text
Middle French (ca. 1400-1600)
```

Nuvarande svenska:

```text
Medelfranska (ca 1300-1600)
```

Förslag:

```text
Medelfranska (ca 1400-1600)
```

### F032 · P2 · Medeliriskans tidsintervall avviker

Årtalen överensstämmer inte med katalogens engelska källtext. Förslaget återställer källtextens intervall.

Förekomster: [locale/iso_639-3:15073](original/locale/iso_639-3.po), [locale/iso_639_3:15073](original/locale/iso_639-3.po).

Källtext:

```text
Middle Irish (900-1200)
```

Nuvarande svenska:

```text
Medeliriska (ca 1100-1550)
```

Förslag:

```text
Medeliriska (ca 900-1200)
```

### F033 · P2 · Fornfranskans slutår avviker

Årtalen överensstämmer inte med katalogens engelska källtext. Förslaget återställer källtextens intervall.

Förekomster: [locale/iso_639-3:18205](original/locale/iso_639-3.po), [locale/iso_639_3:18205](original/locale/iso_639-3.po).

Källtext:

```text
Old French (842-ca. 1400)
```

Nuvarande svenska:

```text
Fornfranska (ca 842-1300)
```

Förslag:

```text
Fornfranska (ca 842-1400)
```

### F034 · P2 · Forniriskans slutår avviker

Årtalen överensstämmer inte med katalogens engelska källtext. Förslaget återställer källtextens intervall.

Förekomster: [locale/iso_639-3:18223](original/locale/iso_639-3.po), [locale/iso_639_3:18223](original/locale/iso_639-3.po).

Källtext:

```text
Old Irish (to 900)
```

Nuvarande svenska:

```text
Forniriska (-1100)
```

Förslag:

```text
Forniriska (-900)
```

### F035 · P3 · Stavfel: rutttyp

Ett överflödigt eller saknat tecken ger ett felstavat svenskt ord.

Förekomster: [locale-langpack/NetworkManager:87](original/locale-langpack/NetworkManager.po).

Källtext:

```text
%s is not a valid route type
```

Nuvarande svenska:

```text
%s är inte en giltig rutttyp
```

Förslag:

```text
%s är inte en giltig ruttyp
```

### F036 · P3 · Stavfel: huvudrutttabellen

Ett överflödigt eller saknat tecken ger ett felstavat svenskt ord.

Förekomster: [locale-langpack/NetworkManager:7022](original/locale-langpack/NetworkManager.po).

Källtext:

```text
Whether to configure MPTCP endpoints and the address flags. If MPTCP is enabled in NetworkManager, it will configure the addresses of the interface as MPTCP endpoints. Note that IPv4 loopback addresses (127.0.0.0/8), IPv4 link local addresses (169.254.0.0/16), the IPv6 loopback address (::1), IPv6 link local addresses (fe80::/10), IPv6 unique local addresses (ULA, fc00::/7) and IPv6 privacy extension addresses (rfc3041, ipv6.ip6-privacy) will be excluded from being configured as endpoints. If "disabled" (0x1), MPTCP handling for the interface is disabled and no endpoints are registered. The "enabled" (0x2) flag means that MPTCP handling is enabled. This flag can also be implied from the presence of other flags. Even when enabled, MPTCP handling will by default still be disabled unless "/proc/sys/net/mptcp/enabled" sysctl is on. NetworkManager does not change the sysctl and this is up to the administrator or distribution. To configure endpoints even if the sysctl is disabled, "also-without-sysctl" (0x4) flag can be used. In that case, NetworkManager doesn't look at the sysctl and configures endpoints regardless. Even when enabled, NetworkManager will only configure MPTCP endpoints for a certain address family, if there is a unicast default route (0.0.0.0/0 or ::/0) in the main routing table. The flag "also-without-default-route" (0x8) can override that. When MPTCP handling is enabled then endpoints are configured with the specified address flags "signal" (0x10), "subflow" (0x20), "backup" (0x40), "fullmesh" (0x80). See ip-mptcp(8) manual for additional information about the flags. If the flags are zero (0x0), the global connection default from NetworkManager.conf is honored. If still unspecified, the fallback is "enabled,subflow". Note that this means that MPTCP is by default done depending on the "/proc/sys/net/mptcp/enabled" sysctl. NetworkManager does not change the MPTCP limits nor enable MPTCP via "/proc/sys/net/mptcp/enabled". That is a host configuration which the admin can change via sysctl and ip-mptcp. Strict reverse path filtering (rp_filter) breaks many MPTCP use cases, so when MPTCP handling for IPv4 addresses on the interface is enabled, NetworkManager would loosen the strict reverse path filtering (1) to the loose setting (2).
```

Nuvarande svenska:

```text
Huruvida MPTCP-ändpunkter och adressflaggor ska konfigureras. Om MPTCP är aktiverat i NetworkManager kommer den att konfigurera gränssnittets adresser som MPTCP-slutpunkter. Observera att IPv4 loopback-adresser (127.0.0.0/8), IPv4-länk lokala adresser (169.254.0.0/16), IPv6 loopback-adress (::1), IPv6-länk lokala adresser (fe80::/10), IPv6 unik lokal adresser (ULA, fc00::/7) och IPv6 integritetstilläggsadresser (rfc3041, ipv6.ip6-privacy) kommer att uteslutas från att konfigureras som slutpunkter. Om "inaktiverad" (0x1) är MTCP-hantering för gränssnittet inaktiverad och inga slutpunkter registreras. Flaggan "enabled" (0x2) betyder att MPTCP-hantering är aktiverad. Denna flagga kan också antydas från närvaron av andra flaggor. Även när den är aktiverad, kommer MPTCP-hantering som standard fortfarande att vara inaktiverad om inte "/proc/sys/net/mptcp/enabled" sysctl är på. NetworkManager ändrar inte sysctl och detta är upp till administratören eller distributionen. För att konfigurera slutpunkter även om sysctl är inaktiverat kan flaggan "also-without-sysctl" (0x4) användas. I så fall tittar NetworkManager inte på sysctl och konfigurerar slutpunkter oavsett. Även när den är aktiverad kommer NetworkManager endast att konfigurera MPTCP-slutpunkter för en viss adressfamilj, om det finns en unicast-standardrutt (0.0.0.0/0 eller ::/0) i huvudrutttabellen. Flaggan "även-utan-default-route" (0x8) kan åsidosätta det. När MPTCP-hantering är aktiverad konfigureras slutpunkter med de angivna adressflaggorna "signal" (0x10), "subflow" (0x20), "backup" (0x40), "fullmesh" (0x80). Se ip-mptcp(8) manual för ytterligare information om flaggorna. Om flaggorna är noll (0x0), uppfylls den globala anslutningsstandarden från NetworkManager.conf. Om den fortfarande är ospecificerad är reservfunktionen "enabled,subflow". Observera att detta betyder att MPTCP görs som standard beroende på "/proc/sys/net/mptcp/enabled" sysctl. NetworkManager ändrar inte MPTCP-gränserna eller aktiverar MPTCP via "/proc/sys/net/mptcp/enabled". Det är en värdkonfiguration som administratören kan ändra via sysctl och ip-mptcp. Strikt omvänd sökvägsfiltrering (rp_filter) bryter många MPTCP-användningsfall, så när MPTCP-hantering för IPv4-adresser på gränssnittet är aktiverad, skulle NetworkManager lossa den strikta omvända sökvägsfiltreringen (1) till den lösa inställningen (2).
```

Förslag:

```text
Huruvida MPTCP-ändpunkter och adressflaggor ska konfigureras. Om MPTCP är aktiverat i NetworkManager kommer den att konfigurera gränssnittets adresser som MPTCP-slutpunkter. Observera att IPv4 loopback-adresser (127.0.0.0/8), IPv4-länk lokala adresser (169.254.0.0/16), IPv6 loopback-adress (::1), IPv6-länk lokala adresser (fe80::/10), IPv6 unik lokal adresser (ULA, fc00::/7) och IPv6 integritetstilläggsadresser (rfc3041, ipv6.ip6-privacy) kommer att uteslutas från att konfigureras som slutpunkter. Om "inaktiverad" (0x1) är MTCP-hantering för gränssnittet inaktiverad och inga slutpunkter registreras. Flaggan "enabled" (0x2) betyder att MPTCP-hantering är aktiverad. Denna flagga kan också antydas från närvaron av andra flaggor. Även när den är aktiverad, kommer MPTCP-hantering som standard fortfarande att vara inaktiverad om inte "/proc/sys/net/mptcp/enabled" sysctl är på. NetworkManager ändrar inte sysctl och detta är upp till administratören eller distributionen. För att konfigurera slutpunkter även om sysctl är inaktiverat kan flaggan "also-without-sysctl" (0x4) användas. I så fall tittar NetworkManager inte på sysctl och konfigurerar slutpunkter oavsett. Även när den är aktiverad kommer NetworkManager endast att konfigurera MPTCP-slutpunkter för en viss adressfamilj, om det finns en unicast-standardrutt (0.0.0.0/0 eller ::/0) i huvudruttabellen. Flaggan "även-utan-default-route" (0x8) kan åsidosätta det. När MPTCP-hantering är aktiverad konfigureras slutpunkter med de angivna adressflaggorna "signal" (0x10), "subflow" (0x20), "backup" (0x40), "fullmesh" (0x80). Se ip-mptcp(8) manual för ytterligare information om flaggorna. Om flaggorna är noll (0x0), uppfylls den globala anslutningsstandarden från NetworkManager.conf. Om den fortfarande är ospecificerad är reservfunktionen "enabled,subflow". Observera att detta betyder att MPTCP görs som standard beroende på "/proc/sys/net/mptcp/enabled" sysctl. NetworkManager ändrar inte MPTCP-gränserna eller aktiverar MPTCP via "/proc/sys/net/mptcp/enabled". Det är en värdkonfiguration som administratören kan ändra via sysctl och ip-mptcp. Strikt omvänd sökvägsfiltrering (rp_filter) bryter många MPTCP-användningsfall, så när MPTCP-hantering för IPv4-adresser på gränssnittet är aktiverad, skulle NetworkManager lossa den strikta omvända sökvägsfiltreringen (1) till den lösa inställningen (2).
```

### F037 · P3 · Stavfel: nätverksanslutnngar

Ett överflödigt eller saknat tecken ger ett felstavat svenskt ord.

Förekomster: [locale-langpack/app-install-data:4845](original/locale-langpack/app-install-data.po).

Källtext:

```text
Edit your network connections
```

Nuvarande svenska:

```text
Redigera dina nätverksanslutnngar
```

Förslag:

```text
Redigera dina nätverksanslutningar
```

### F038 · P3 · Stavfel: Allmänn

Ett överflödigt eller saknat tecken ger ett felstavat svenskt ord.

Förekomster: [locale-langpack/app-install-data:15555](original/locale-langpack/app-install-data.po).

Källtext:

```text
Universal karaoke songs and movies player
```

Nuvarande svenska:

```text
Allmänn uppspelare av karaokelåtar och -filmer
```

Förslag:

```text
Allmän uppspelare av karaokelåtar och -filmer
```

### F039 · P3 · Stavfel: tidspunkt

Ett överflödigt eller saknat tecken ger ett felstavat svenskt ord.

Förekomster: [locale-langpack/ubiquity-debconf:810](original/locale-langpack/ubiquity-debconf.po).

Källtext:

```text
This may be due to using an old installer image, or it may be due to a bug in some of the packages listed above. More details may be found in /var/log/syslog. The installer will try to continue anyway, but may fail at a later point, and will not be able to install or remove other packages (possibly including itself) from the installed system. You should first look for newer versions of your installer image, or failing that report the problem to your distributor.
```

Nuvarande svenska:

```text
Det här kan bero på användningen av en gammal installationsavbild, eller det kan bero på ett fel i några av de paket som listas ovan. Mer information kan hittas i filen /var/log/syslog. Installationsprogrammet kommer att försöka fortsätta ändå men kan misslyckas vid en senare tidspunkt, och kommer inte kunna installera eller ta bort andra paket (kanske även sig själv) från det installerade systemet. Du bör först leta efter nyare versioner av din installationsavbild, eller rapportera misslyckandet till din leverantör.
```

Förslag:

```text
Det här kan bero på användningen av en gammal installationsavbild, eller det kan bero på ett fel i några av de paket som listas ovan. Mer information kan hittas i filen /var/log/syslog. Installationsprogrammet kommer att försöka fortsätta ändå men kan misslyckas vid en senare tidpunkt, och kommer inte kunna installera eller ta bort andra paket (kanske även sig själv) från det installerade systemet. Du bör först leta efter nyare versioner av din installationsavbild, eller rapportera misslyckandet till din leverantör.
```

### F040 · P3 · Stavfel: körnng

Ett överflödigt eller saknat tecken ger ett felstavat svenskt ord.

Förekomster: [locale-langpack/dpkg-dev:949](original/locale-langpack/dpkg-dev.po).

Källtext:

```text
Options:
  -l<library-path>         add directory to private shared library search list.
  -p<package>              generate symbols file for package.
  -P<package-build-dir>    temporary build directory instead of debian/tmp.
  -e<library>              explicitly list libraries to scan.
  -v<version>              version of the packages (defaults to
                           version extracted from debian/changelog).
  -c<level>                compare generated symbols file with the reference
                           template in the debian directory and fail if
                           difference is too important; level goes from 0 for
                           no check, to 4 for all checks (default level is 1).
  -q                       keep quiet and never emit any warnings or
                           generate a diff between generated symbols
                           file and the reference template.
  -I<file>                 force usage of <file> as reference symbols
                           file instead of the default file.
  -O[<file>]               write to stdout (or <file>), not .../DEBIAN/symbols.
  -t                       write in template mode (tags are not
                           processed and included in output).
  -V                       verbose output; write deprecated symbols and pattern
                           matching symbols as comments (in template mode only).
  -a<arch>                 assume <arch> as host architecture when processing
                           symbol files.
  -d                       display debug information during work.
  -?, --help               show this help message.
      --version            show the version.

```

Nuvarande svenska:

```text
Flaggor:
  -l<bibliotekssökväg>     lägg till katalog till privat söklista för delade bibliotek.
  -p<paket>                skapar symbolfil för paket.
  -P<paketbyggkatalog>     temporär byggkatalog istället för debian/tmp.
  -e<bibliotek>            explicit lista över bibliotek att söka i.
  -v<version>              version på paketet (förval är versionen
                           som utläses ur debian/changelog).
  -c<nivå>                 jämför genererade symbolfiler med referensfilen
                           i katalogen ”debian” och misslyckas om skillnaderna
                           är för stora; nivå går från 0 för ingen test, till
                           4 för alla tester (förvald nivå är 1).
  -q                       var tyst och skriv aldrig ut några varningar eller
                           generera en diff mellan genererad symbolfil och
                           referensfilen.
  -I<fil>                  tvinga användning av <fil> som symbolreferensfil
                           istället för standardfilen.
  -O[<fil>]                skriv till standard ut/<fil>, inte .../DEBIAN/symbols.
  -t                       skriv i malläge (taggar behandlas inte och
                           tas med i utdata).
  -V                       pratsam utdata; skriv föråldrade symboler och
                           mönster som motsvarar symboler som kommentarer
                           (endast i mall-läget).
  -a<ark>                  förutsätt <ark> som värdarkitektur vid behandling
                           av symbofilen.
  -d                       visa felsökningsinformation under körnng.
  -?, --help               visa detta hjälpmeddelande.
      --version            visa versionsnummer.

```

Förslag:

```text
Flaggor:
  -l<bibliotekssökväg>     lägg till katalog till privat söklista för delade bibliotek.
  -p<paket>                skapar symbolfil för paket.
  -P<paketbyggkatalog>     temporär byggkatalog istället för debian/tmp.
  -e<bibliotek>            explicit lista över bibliotek att söka i.
  -v<version>              version på paketet (förval är versionen
                           som utläses ur debian/changelog).
  -c<nivå>                 jämför genererade symbolfiler med referensfilen
                           i katalogen ”debian” och misslyckas om skillnaderna
                           är för stora; nivå går från 0 för ingen test, till
                           4 för alla tester (förvald nivå är 1).
  -q                       var tyst och skriv aldrig ut några varningar eller
                           generera en diff mellan genererad symbolfil och
                           referensfilen.
  -I<fil>                  tvinga användning av <fil> som symbolreferensfil
                           istället för standardfilen.
  -O[<fil>]                skriv till standard ut/<fil>, inte .../DEBIAN/symbols.
  -t                       skriv i malläge (taggar behandlas inte och
                           tas med i utdata).
  -V                       pratsam utdata; skriv föråldrade symboler och
                           mönster som motsvarar symboler som kommentarer
                           (endast i mall-läget).
  -a<ark>                  förutsätt <ark> som värdarkitektur vid behandling
                           av symbofilen.
  -d                       visa felsökningsinformation under körning.
  -?, --help               visa detta hjälpmeddelande.
      --version            visa versionsnummer.

```

### F041 · P3 · Stavfel: klasss

Ett överflödigt eller saknat tecken ger ett felstavat svenskt ord.

Förekomster: [locale-langpack/dpkg-dev:1649](original/locale-langpack/dpkg-dev.po).

Källtext:

```text
changelog format %s is not a Dpkg::Changelog class
```

Nuvarande svenska:

```text
ändringsloggformatet %s är inte en Dpkg::Changelog-klasss
```

Förslag:

```text
ändringsloggformatet %s är inte en Dpkg::Changelog-klass
```

### F042 · P3 · Stavfel: tilllåter

Ett överflödigt eller saknat tecken ger ett felstavat svenskt ord.

Förekomster: [locale-langpack/glance:1398](original/locale-langpack/glance.po).

Källtext:

```text
Some resource types allow more than one key / value pair per instance.  For example, Cinder allows user and image metadata on volumes. Only the image properties metadata is evaluated by Nova (scheduling or drivers). This property allows a namespace target to remove the ambiguity.
```

Nuvarande svenska:

```text
Vissa resurstyper tillåter fler än ett nyckel-/värdepar per instans. Till exempel Cinder tilllåter användar- och bildmetadata på volymer. Bara bildegenskapers metadata utvärderas av Nova (schemaläggning eller drivrutiner). Denna egenskap tillåter en namnrymd att ta bort tvetydigheten.
```

Förslag:

```text
Vissa resurstyper tillåter fler än ett nyckel-/värdepar per instans. Till exempel Cinder tillåter användar- och bildmetadata på volymer. Bara bildegenskapers metadata utvärderas av Nova (schemaläggning eller drivrutiner). Denna egenskap tillåter en namnrymd att ta bort tvetydigheten.
```

### F043 · P3 · Stavfel: öpppna

Ett överflödigt eller saknat tecken ger ett felstavat svenskt ord.

Förekomster: [locale-langpack/mutt:1298](original/locale-langpack/mutt.po).

Källtext:

```text
Failure to open file to parse headers.
```

Nuvarande svenska:

```text
Misslyckades med att öpppna fil för att tolka huvuden.
```

Förslag:

```text
Misslyckades med att öppna fil för att tolka huvuden.
```

### F044 · P3 · Stavfel: Tilllåt

Ett överflödigt eller saknat tecken ger ett felstavat svenskt ord.

Förekomster: [locale-langpack/unity-control-center:343](original/locale-langpack/unity-control-center.po).

Källtext:

```text
Allow different sources for each window
```

Nuvarande svenska:

```text
Tilllåt olika källor för var fönster
```

Förslag:

```text
Tillåt olika källor för var fönster
```

### F045 · P3 · Stavfel: Tilllåt

Ett överflödigt eller saknat tecken ger ett felstavat svenskt ord.

Förekomster: [locale-langpack/unity-control-center:349](original/locale-langpack/unity-control-center.po).

Källtext:

```text
Allow louder than 100% (may distort sound)
```

Nuvarande svenska:

```text
Tilllåt högre än 100% (kan förvränga ljudet)
```

Förslag:

```text
Tillåt högre än 100% (kan förvränga ljudet)
```

### F046 · P3 · Stavfel: Tilllåter

Ett överflödigt eller saknat tecken ger ett felstavat svenskt ord.

Förekomster: [locale-langpack/unity:81](original/locale-langpack/unity.po).

Källtext:

```text
Allows using the mouse scrollwheel to focus an application if the icon is inactive.
```

Nuvarande svenska:

```text
Tilllåter musens rullhjul att sätta ett program i fokus om ikonen är inaktiv.
```

Förslag:

```text
Tillåter musens rullhjul att sätta ett program i fokus om ikonen är inaktiv.
```

### F047 · P3 · Stavfel: Skugggfärg

Ett överflödigt eller saknat tecken ger ett felstavat svenskt ord.

Förekomster: [locale-langpack/unity:814](original/locale-langpack/unity.po).

Källtext:

```text
The color of the shadows for the inactive windows.
```

Nuvarande svenska:

```text
Skugggfärg på de inaktiva fönstren.
```

Förslag:

```text
Skuggfärg på de inaktiva fönstren.
```

### F048 · P3 · Stavfel: kommmer

Ett överflödigt eller saknat tecken ger ett felstavat svenskt ord.

Förekomster: [locale-langpack/xz-man:1120](original/locale-langpack/xz-man.po).

Källtext:

```text
Future versions may add new line types and new columns can be added to the existing line types, but the existing columns won't be changed.
```

Nuvarande svenska:

```text
Framtida versioner kan lägga till fler radtyper och fler kolumner kan läggas til på de befintliga radtyperna, men de befintliga kolumnerna kommmer inte ändras.
```

Förslag:

```text
Framtida versioner kan lägga till fler radtyper och fler kolumner kan läggas til på de befintliga radtyperna, men de befintliga kolumnerna kommer inte ändras.
```

### F049 · P3 · Felaktig upprepning: därför därför

Upprepningen är ett skrivfel i denna mening och har inte stöd i källtexten.

Förekomster: [locale/OpenSP:646](original/locale/OpenSP.po).

Källtext:

```text
character %1 is not significant in the reference concrete syntax and so cannot occur in a comment in the SGML declaration
```

Nuvarande svenska:

```text
tecknet %1 är ej signifikant i den konkreta referenssyntaxen och får därför därför ej förekomma i en kommentar i SGML-deklarationen
```

Förslag:

```text
tecknet %1 är ej signifikant i den konkreta referenssyntaxen och får därför ej förekomma i en kommentar i SGML-deklarationen
```

### F050 · P3 · Felaktig upprepning: men men

Upprepningen är ett skrivfel i denna mening och har inte stöd i källtexten.

Förekomster: [locale/dpkg:133](original/locale/dpkg.po).

Källtext:

```text
  %s provides %s but is %s.

```

Nuvarande svenska:

```text
%s tillhandahåller %s men men är %s.

```

Förslag:

```text
%s tillhandahåller %s men är %s.

```

### F051 · P3 · Felaktig upprepning: för för

Upprepningen är ett skrivfel i denna mening och har inte stöd i källtexten.

Förekomster: [locale/dpkg:2424](original/locale/dpkg.po).

Källtext:

```text
cannot set security execution context for maintainer script
```

Nuvarande svenska:

```text
kan inte sätta säkerhetsexekveringssammanhang för för utvecklarskript
```

Förslag:

```text
kan inte sätta säkerhetsexekveringssammanhang för utvecklarskript
```

### F052 · P3 · Felaktig upprepning: dina dina

Upprepningen är ett skrivfel i denna mening och har inte stöd i källtexten.

Förekomster: [locale/gnome-builder:2868](original/locale/gnome-builder.po).

Källtext:

```text
Quickly access your projects
```

Nuvarande svenska:

```text
Kom snabbt åt dina dina projekt
```

Förslag:

```text
Kom snabbt åt dina projekt
```

### F053 · P3 · Felaktig upprepning: relative tider till till

Upprepningen är ett skrivfel i denna mening och har inte stöd i källtexten.

Förekomster: [locale-langpack/snappy:2749](original/locale-langpack/snappy.po).

Källtext:

```text
Display absolute times (in RFC 3339 format). Otherwise, display relative times up to 60 days, then YYYY-MM-DD.
```

Nuvarande svenska:

```text
Visa absoluta tider (i formatet RFC 3339). Visa annars relative tider till till 60 dagar, sedan ÅÅÅÅ-MM-DD.
```

Förslag:

```text
Visa absoluta tider (i formatet RFC 3339). Visa annars relativa tider upp till 60 dagar, sedan ÅÅÅÅ-MM-DD.
```

### F054 · P3 · Felaktig upprepning: ignoreras ignoreras

Upprepningen är ett skrivfel i denna mening och har inte stöd i källtexten.

Förekomster: [locale-langpack/xfsprogs:5717](original/locale-langpack/xfsprogs.po).

Källtext:

```text
ALERT: The filesystem has valuable metadata changes in a log which is being
ignored because the -n option was used.  Expect spurious inconsistencies
which may be resolved by first mounting the filesystem to replay the log.

```

Nuvarande svenska:

```text
VARNING: Filsystemet har värdefulla metadataändringar i en logg som ignoreras
ignoreras eftersom flaggan -n användes.  Förvänta dig falska inkonsekvenser
som kan lösas genom att först montera filsystemet för att spela upp loggen igen.

```

Förslag:

```text
VARNING: Filsystemet har värdefulla metadataändringar i en logg som ignoreras eftersom flaggan -n användes.  Förvänta dig falska inkonsekvenser
som kan lösas genom att först montera filsystemet för att spela upp loggen igen.

```

### F055 · P3 · Felaktig upprepning: filsystemet filsystemet

Upprepningen är ett skrivfel i denna mening och har inte stöd i källtexten.

Förekomster: [locale-langpack/xfsprogs:6391](original/locale-langpack/xfsprogs.po).

Källtext:

```text
ERROR: The log head and/or tail cannot be discovered. Attempt to mount the
filesystem to replay the log or use the -L option to destroy the log and
attempt a repair.

```

Nuvarande svenska:

```text
FEL: Loggens huvud och/eller svans kan inte hittas. Försök att montera filsystemet
filsystemet för att spela upp loggen igen eller använd flaggan -L för att förstöra loggen och
försöka reparera den.

```

Förslag:

```text
FEL: Loggens huvud och/eller svans kan inte hittas. Försök att montera filsystemet för att spela upp loggen igen eller använd flaggan -L för att förstöra loggen och
försöka reparera den.

```

### F056 · P3 · Felaktig upprepning: 1 beta beta

Upprepningen är ett skrivfel i denna mening och har inte stöd i källtexten.

Förekomster: [locale-langpack/xz-man:1651](original/locale-langpack/xz-man.po).

Källtext:

```text
Stability.  0 is alpha, 1 is beta, and 2 is stable.  I<S> should be always 2 when I<YYY> is even.
```

Nuvarande svenska:

```text
Stabilitet.  0 är alfa, 1 beta beta och 2 är stabil. I<S> skall alltid vara 2 när I<YYY> är jämnt.
```

Förslag:

```text
Stabilitet.  0 är alfa, 1 är beta och 2 är stabil. I<S> skall alltid vara 2 när I<YYY> är jämnt.
```

### F057 · P3 · Felaktig upprepning: med med

Upprepningen är ett skrivfel i denna mening och har inte stöd i källtexten.

Förekomster: [locale-langpack/xz-man:1837](original/locale-langpack/xz-man.po).

Källtext:

```text
These are like B<-6> but with higher compressor and decompressor memory requirements.  These are useful only when compressing files bigger than 8\ MiB, 16\ MiB, and 32\ MiB, respectively.
```

Nuvarande svenska:

```text
Dessa liknar B<-6> med med högre krav på minne till komprimerare och dekomprimerare. Dessa är bara användbara vid komprimering av filer större än 8\ MiB, 16\ MiB respektive 32\ MiB.
```

Förslag:

```text
Dessa liknar B<-6> men med högre krav på minne till komprimerare och dekomprimerare. Dessa är bara användbara vid komprimering av filer större än 8\ MiB, 16\ MiB respektive 32\ MiB.
```

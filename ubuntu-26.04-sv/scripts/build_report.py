import bisect,collections,csv,datetime,hashlib,html,json,shutil,subprocess,zipfile
from pathlib import Path

OUT=Path('outputs/locale-granskning')
def read(name):return json.loads((OUT/name).read_text())
def save(name,data):
    p=OUT/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def num(n):return f'{n:,}'.replace(',',' ')
def esc(s):return html.escape(str(s))
manifest=read('manifest.json');summary=read('scan-summary.json');before=read('raw/fore-verktygsfix/scan-summary.json');refs=read('references-summary.json');findings=read('findings.json');tools=read('tools.json')
entries=json.loads(Path('work/entries.json').read_text());bycat=collections.defaultdict(list)
for e in entries:bycat[e['catalog']].append(e)
counts=collections.Counter(f['severity'] for f in findings)
unique=[r for r in manifest if r['id']==r['canonical_id']]
current_total=sum(summary['lint_rules'].values());old_total=sum(before['lint_rules'].values())
svtotal=sum(r['svlang_issues'] for r in summary['catalogs']);svold=sum(r['svlang_issues'] for r in before['catalogs'])
consistency=len(read('raw/svlang-consistency.json'))
severities=collections.Counter();candidates=[]
finding_by_loc=collections.defaultdict(list)
for f in findings:
    for o in f['occurrences']:finding_by_loc[(o['catalog'],o['line'])].append(f['id'])
for r in unique:
    es=bycat[r['id']];lines=[e['line'] for e in es]
    for issue in read('raw/l10n-lint/'+r['id']+'.json')['issues']:
        i=bisect.bisect_right(lines,issue['line'])-1
        e=es[i] if i>=0 else None
        candidates.append({'catalog':r['id'],'po':r['po'],'line':issue['line'],'severity':issue['severity'],'rule':issue['rule'],'message':issue['message'],'source':e['msgid'] if e else '', 'plural_source':e['msgid_plural'] if e else '', 'translations':json.dumps({str(x['plural_index']):x['msgstr'] for x in es if e and x['ordinal']==e['ordinal']},ensure_ascii=False),'findings_in_same_entry':','.join(finding_by_loc[(r['id'],e['line'])]) if e else ''})
        severities[issue['severity']]+=1
with (OUT/'lint-kandidater.csv').open('w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(candidates[0]));w.writeheader();w.writerows(candidates)
with (OUT/'findings.csv').open('w',newline='',encoding='utf-8-sig') as f:
    fields=['id','priority','category','catalog','po','line','source','translation','proposal','reason']
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
    for x in findings:
        for o in x['occurrences']:
            w.writerow(dict(id=x['id'],priority=x['severity'],category=x['category'],catalog=o['catalog'],po=o['po'],line=o['line'],source=x['entry']['msgid'],translation=x['entry']['msgstr'],proposal=x['proposal'],reason=x['reason']))

(OUT/'tool-fixes').mkdir(exist_ok=True)
for name in ['l10n-lint.patch','svlang.patch','changes.json']:
    shutil.copy2(Path('outputs/installation/uppdatering')/name,OUT/'tool-fixes'/name)
shutil.copy2('work/l10n-tests.txt',OUT/'tool-fixes/l10n-tests.txt')
(OUT/'tool-fixes/svlang-tests.txt').write_text('PYTHONPATH=src python3 -m pytest -q\n83 passed in 2.16s\n')
(OUT/'scripts').mkdir(exist_ok=True)
for name in ['extract.py','scan.py','references.py','curate.py','build_report.py']:
    shutil.copy2(Path('work')/name,OUT/'scripts'/name)
for name in ['sysdep-original.po','sysdep-unformatted.po']:
    shutil.copy2(Path('work')/name,OUT/'raw'/name)

intro=f'''# Granskning av installerade svenska gettext-kataloger

Granskad 19 september 2026. **{len(findings)} individuellt verifierade fyndgrupper, {sum(len(f['occurrences']) for f in findings)} förekomster:** {counts['P1']} med prioritet P1, {counts['P2']} P2 och {counts['P3']} P3. Hela materialet har kontrollerats automatiskt; språkgranskningen är en riktad granskning av utvalda kandidater, inte en genomläsning av alla {num(summary['entries'])} poster.

De viktigaste fynden är en felaktig Python-nyckel i Cinder som ger `KeyError`, två trunkerade tidsformat i GDB, felaktig formatering i Glance, trasiga länkar/taggar samt omkastade vinkelvärden i libmypaint. Översättningsförslagen har inte lagts in i systemets MO-filer. SHA-256-kontroll efter arbetet visar att samtliga 479 inlästa sökvägar är oförändrade.

## Omfattning och metod

| Mapp | Sökvägar | Poster före deduplicering | Unika binärkataloger | Poster efter deduplicering |
|---|---:|---:|---:|---:|
| `/usr/share/locale-langpack/sv/LC_MESSAGES` | 432 | 204 087 | 432 | 204 087 |
| `/usr/share/locale/sv/LC_MESSAGES` | 47 | 40 536 | 41 | 26 217 |
| Totalt | 479 | 244 623 | 473 | 230 304 |

Fem sökvägar är symboliska länkar till ISO-kataloger. `WebKitGTK-4.1.mo` och `WebKitGTK-6.0.mo` är byteidentiska. Deduplicering sker med SHA-256; olika filer för samma domän i de två mapparna behålls. Den kanoniska filen och alla alias framgår av [manifestet](manifest.json). Fyndens 65 förekomster inkluderar fyra ISO-alias.

Alla 479 sökvägar har dekompilerats med **GNU `msgunfmt --no-wrap` 0.23.2**. Radnummer i rapporten avser de medföljande dekompilerade PO-filerna, inte en upstream-PO-fil eller en binär MO-offset. Originalets MO-sökväg, hash, metadata, PO-hash och kommandoutfall finns i manifestet.

`l10n-lint` har körts med samtliga standardregler och språk `sv`. `svlang` har kört skrivregler och svengelska på samtliga {num(summary['target_forms'])} målformer, samt kontext- och pluralmedveten konsekvenskontroll mellan katalogerna. Kontrollerna anropas via verktygens installerade Python-API för att bevara kopplingen till varje PO-post; [körskripten](scripts/scan.py) redovisar exakt anrop. Svlangs heuristiska naturlighetspoäng och full ordlistekontroll ingår inte.

Samtliga 15 PO-exporter i Swedish TM och termbankens CSV har jämförts mot exakt källtext. Referensexporterna saknar ursprunglig kontext och pluralidentitet. Avvikelser är därför granskningskandidater. Ingen automatisk ersättning har gjorts utifrån majoritetsval eller konfidensvärden.

## Råresultat efter verktygsfixarna

| Kontroll | Resultat | Tolkning |
|---|---:|---|
| msgunfmt | 479/479 lyckades | Samtliga sökvägar extraherade |
| msgfmt --check --check-format | 478/479 godkända | Git ger reproducerbar sysdep-dubblett efter dekompilering, se nedan |
| Återkompilering/jämförelse | 478/478 jämförbara filer har samma meddelandetabell | Git exkluderad på grund av dubbletterna; metadata och binär layout jämförs inte |
| l10n-lint | {num(current_total)} träffar | {num(severities['error'])} error, {num(severities['warning'])} warning, {num(severities['info'])} info; verktygsnivå, inte verifierad allvarlighetsgrad |
| svlang skrivregler/svengelska | {num(svtotal)} träffar | Språkkandidater |
| svlang konsekvens | {num(consistency)} grupper | Samma källtext/kontext/pluralform har olika måltexter |
| Swedish TM: exakt parträff | {num(refs['tm']['exact_pair_match'])} målformer | Överensstämmelse är ingen kvalitetsgaranti |
| Swedish TM: annan måltext | {num(refs['tm']['different_target'])} målformer | Förslag finns; kontext måste bedömas |
| Swedish TM: källtext saknas | {num(refs['tm']['source_absent'])} målformer | Ingen exakt referensträff |
| Termbank: kanonisk träff | {num(refs['terminology']['canonical_match'])} målformer | Exakt överensstämmelse |
| Termbank: annan måltext | {num(refs['terminology']['different_target'])} målformer | Terminologikandidater |
| Termbank: källtext saknas | {num(refs['terminology']['source_absent'])} målformer | Ingen exakt referensträff |

Träffarna från olika kontroller överlappar och får inte summeras till ett antal fel. [Lint-kandidater CSV](lint-kandidater.csv), [TM-avvikelser JSON](raw/tm-differences.json), [termavvikelser JSON](raw/terminology-differences.json), [konsekvensgrupper JSON](raw/svlang-consistency.json) och [statistik per katalog](scan-summary.json) innehåller hela resultatet. En fyndreferens i kandidat-CSV betyder att samma post har ett verifierat fynd; den bekräftar inte varje regel som träffat posten.

## Prioritering och verifiering

P1: trasigt format med högre funktionsrisk. P2: förlorad information, felaktig betydelse, markup eller övriga formatavvikelser. P3: stavning och språk. Prioriteringen beskriver fyndet i katalogen; berörda program har inte körts igenom i sina respektive felvägar.

23 utvalda formatförslag kontrollerades separat med syntetiska formatflaggor: 22 original underkändes och samtliga 23 förslag godkändes av `msgfmt --check-format`. Glances original godkänns av gettext men Python konsumerar `s` i ordet `som`: resultatet blir `image-1om`. Det är verifierat med en ofarlig formateringsreproduktion. Cinders original ger `KeyError: ret.statuss`; originalets engelska text och det svenska förslaget fungerar med samma exempeldictionary. Fulla kontrollutdata finns i [findings.json](findings.json).

## Bekräftade fynd

Tabellen är ett prioriterat urval ur de automatiska träffarna. Full källtext, nuvarande översättning, komplett förslag, samtliga förekomster och verifieringsdata finns längre ned samt i [findings.csv](findings.csv) och [findings.json](findings.json).

| ID | Prioritet | Katalog och PO-rad | Fynd |
|---|---|---|---|
'''
for f in sorted(findings,key=lambda f:(f['severity'],f['id'])):
    o=f['occurrences'][0]
    intro+=f"| {f['id']} | {f['severity']} | [{o['catalog']}:{o['line']}]({o['po']}) | {f['title'].replace('|','&#124;')} |\n"

method='''
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

'''
for name,r in tools['repositories'].items():method+=f"- [{name}]({r['url']}), commit `{r['commit']}`.\n"
method+='''
Exakt installerad proveniens och lokala patchhashar finns i [tools.json](tools.json). De två ursprungligen angivna adresserna `yeager/lswedish-tm` och `yeager/lsvlang` fanns inte; de verifierade arkiven `yeager/swedish-tm` och `yeager/svlang` användes.

Körningen använder i grunden följande kommandon för varje fil; utdata lagras utanför systemets översättningsmappar:

```sh
msgunfmt --no-wrap -o dekompilerad.po /sökväg/katalog.mo
msgfmt --check --check-format -o /dev/null dekompilerad.po
l10n-lint --language sv --format json --output resultat.json dekompilerad.po
```

[extract.py](scripts/extract.py), [scan.py](scripts/scan.py), [references.py](scripts/references.py) och [curate.py](scripts/curate.py) dokumenterar extraktion, full automatisk kontroll, exakta referensjämförelser och explicit urval/verifiering. Skripten använder arbetsmappens `work/` och `outputs/` samt de installerade verktygssökvägarna. [source-integrity.json](source-integrity.json) redovisar slutlig integritetskontroll.

## Fullständiga fynd och förslag

'''
md=intro+method
for f in findings:
    e=f['entry'];md+=f"### {f['id']} · {f['severity']} · {f['title']}\n\n{f['reason']}\n\n"
    md+='Förekomster: '+', '.join(f"[{o['catalog']}:{o['line']}]({o['po']})" for o in f['occurrences'])+'.\n\n'
    for title,value in [('Källtext',e['msgid']),('Nuvarande svenska',e['msgstr']),('Förslag',f['proposal'])]:md+=title+':\n\n```text\n'+value+'\n```\n\n'
(OUT/'rapport.md').write_text(md)

css='''body{font:16px/1.55 system-ui,sans-serif;margin:0;color:#172431;background:#f2f5f7}main{max-width:1120px;margin:auto;padding:40px 24px 80px}h1{font-size:36px;line-height:1.2;max-width:850px}h2{margin-top:42px}a{color:#125d92}header{border-bottom:3px solid #16788e;padding-bottom:22px}.lead{font-size:19px;max-width:950px}.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:12px;margin:24px 0}.card,details{background:white;padding:18px;border:1px solid #d5e0e4;border-radius:8px}.card strong{display:block;font-size:29px;color:#11697b}table{width:100%;border-collapse:collapse;background:white;font-size:14px}th,td{text-align:left;padding:10px;border-bottom:1px solid #d9e1e5;vertical-align:top}th{background:#e5eef2;position:sticky;top:0}.tablewrap{overflow:auto;max-height:650px}pre{white-space:pre-wrap;overflow-wrap:anywhere;font-size:14px;background:#f0f4f6;padding:12px}code{font-size:.9em}summary{cursor:pointer;font-weight:650}details{margin:12px 0}input{font:inherit;padding:10px;width:min(600px,90%);border:1px solid #94aab4;border-radius:6px}.muted{color:#496170}.badge{padding:2px 8px;border-radius:4px;background:#e6eff3;margin-right:8px}.P1{background:#ffe0de;color:#891e17}.P2{background:#fff0ce;color:#785412}.P3{background:#e3eef7;color:#215579}nav{display:flex;gap:18px;flex-wrap:wrap}.notice{border-left:4px solid #16788e;padding:12px 18px;background:#e6f0f3}.hidden{display:none}@media print{input,nav{display:none}.tablewrap{max-height:none}details{break-inside:avoid}body{background:white}main{max-width:none;padding:0}}'''
body=f'''<!doctype html><html lang="sv"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Svenska lokalkataloger – granskningsrapport</title><style>{css}</style><main><header><p class="muted">19 september 2026 · msgunfmt / l10n-lint / svlang / Swedish TM / FOSS-termbanken</p><h1>Granskning av installerade svenska översättningar</h1><p class="lead">{len(findings)} verifierade fyndgrupper med {sum(len(f['occurrences']) for f in findings)} förekomster. Systemets översättningsfiler är oförändrade.</p><nav><a href="#findings">Verifierade fynd</a><a href="#catalogs">Alla kataloger</a><a href="#method">Metod och begränsningar</a><a href="#fixes">Verktygsfixar</a><a href="rapport.md">Full rapport Markdown</a><a href="findings.csv">Fynd CSV</a><a href="findings.json">Fynd JSON</a></nav></header><div class="cards"><div class="card"><strong>473</strong>unika kataloger / 479 sökvägar</div><div class="card"><strong>230 304</strong>automatiskt kontrollerade poster</div><div class="card"><strong>2 / 32 / 23</strong>fynd med P1 / P2 / P3</div><div class="card"><strong>547</strong>verktygsorsakade träffar borttagna</div></div><p class="notice">Hela materialet är automatiskt kontrollerat. Den individuella granskningen är riktad mot utvalda kandidater. {num(current_total)} lint-träffar är inte {num(current_total)} verifierade fel. Radnummer avser de medföljande PO-filerna efter msgunfmt.</p><h2 id="findings">Verifierade fynd</h2><p>P1: högre funktionsrisk · P2: betydelse, information, markup eller format · P3: språk och stavning. Öppna ett fynd för full källtext och rättningsförslag.</p><label for="filter">Sök bland fynd och kataloger</label><br><input id="filter" type="search" placeholder="Exempel: cinder, OpenSP, P1, stavfel"><p id="shown" class="muted"></p>'''
for f in sorted(findings,key=lambda f:(f['severity'],f['id'])):
    e=f['entry'];search=' '.join([f['id'],f['severity'],f['title'],f['reason'],e['msgid'],e['msgstr'],*[o['catalog'] for o in f['occurrences']]])
    body+=f'<details class="finding" data-search="{esc(search.lower())}" id="{f["id"]}"><summary><span class="badge {f["severity"]}">{f["severity"]}</span>{f["id"]} · {esc(f["title"])} <span class="muted">— {esc(e["catalog"])}</span></summary><p>{esc(f["reason"])}</p><p>'
    body+=', '.join(f'<a href="{esc(o["po"])}">{esc(o["catalog"])}:{o["line"]}</a>' for o in f['occurrences'])+'</p>'
    for title,value in [('Källtext',e['msgid']),('Nuvarande svenska',e['msgstr']),('Förslag',f['proposal'])]:body+=f'<strong>{title}</strong><pre>{esc(value)}</pre>'
    if 'runtime_reproducer' in f:body+='<strong>Python-reproduktion</strong><pre>'+esc(json.dumps(f['runtime_reproducer'],ensure_ascii=False,indent=2))+'</pre>'
    if 'format_validation' in f:
        v=f['format_validation'];body+=f'<p class="muted">msgfmt med syntetisk {v["synthetic_flag"]}: original status {v["before"]["exit_code"]}, förslag status {v["proposed"]["exit_code"]}. Programmens kompletta felvägar är inte körda.</p>'
    body+='</details>'
body+=f'''<h2 id="catalogs">Alla kataloger och råresultat</h2><p>{num(current_total)} lint-träffar ({num(severities['error'])} error / {num(severities['warning'])} warning / {num(severities['info'])} info), {svtotal} svlang-träffar och {num(consistency)} konsekvensgrupper. Verktygsnivåerna återges oförändrade.</p><p><a href="lint-kandidater.csv">Alla lint-kandidater, CSV</a> · <a href="raw/tm-differences.json">13 328 TM-avvikelser</a> · <a href="raw/terminology-differences.json">9 017 termbanksavvikelser</a> · <a href="raw/svlang-consistency.json">Konsekvensgrupper</a> · <a href="manifest.json">Manifest och hashvärden</a></p><div class="tablewrap"><table><thead><tr><th>Katalog</th><th>Poster</th><th>Lint</th><th>Svlang</th><th>Filer</th></tr></thead><tbody>'''
for r in sorted(summary['catalogs'],key=lambda r:(-r['lint_issues'],r['catalog'])):
    cat=r['catalog'];body+=f'<tr class="catalog" data-search="{esc(cat.lower())}"><td>{esc(cat)}</td><td>{num(r["entries"])}</td><td>{num(r["lint_issues"])}</td><td>{r["svlang_issues"]}</td><td><a href="po/{esc(cat)}.po">PO</a> · <a href="raw/l10n-lint/{esc(cat)}.json">Lint JSON</a> · <a href="raw/svlang/{esc(cat)}.json">Svlang JSON</a></td></tr>'
body+='''</tbody></table></div><h2 id="method">Metod och begränsningar</h2><p>432 filer från locale-langpack och 47 sökvägar från locale har lästs med msgunfmt. Fem ISO-alias och en byteidentisk WebKit-kopia deduplicerades. 478 filer kunde återkompileras med oförändrad meddelandetabell. Git gav en dubblett efter dekompilering av portabla PRI-format; detta har reproducerats med en minimal giltig katalog och räknas som ett gettext-/extraktionsproblem.</p><p>MO-filer saknar oftast originalets formatflaggor, kommentarer och källreferenser. Oöversatta poster och fuzzy-underlag kan inte inventeras från de installerade binärerna. Gettexts kontroll är därför kompletterad med riktade formatprov och individuell bedömning.</p><p>Svlang kör skrivregler, svengelska och konsekvenskontroll. Naturlighetspoäng och full ordlistekontroll ingår inte. Alla 15 TM-exporter och termbankens CSV jämförs med exakt källtext; referenserna bevarar inte ursprunglig kontext/pluralidentitet. Skillnader är kandidater, inte automatiska rättelser.</p><p>Återstående heuristiska träffar omfattar bland annat lokaliserade datum och decimaler, översatta dokumentationsargument, justerade radbrytningar, tekniska syntaxer och korrekta egennamn. <a href="rapport.md">Full metod, begränsningar och verifiering</a> · <a href="source-integrity.json">Kontroll att systemfilerna är oförändrade</a>.</p><h2 id="fixes">Installerat och förbättrat</h2><p>Installerat: <code>l10n-lint 1.21.2+localeaudit1</code> och <code>svlang 0.2.1+localeaudit1</code>. Kommandon i <code>/usr/local/bin</code>, runtime i <code>/opt/yeager-l10n/2026-09-19/venv</code>. TM och termbank finns i <code>/usr/local/share/swedish-tm</code> respektive <code>/usr/local/share/swedish-foss-terminology</code>.</p><p>Fem förbättringar: krav på pluralhuvud, printf-suffix, avgränsning av kommandoflaggor, bevarade tekniska namn och godkänd stavning av iväg. <strong>274 + 83 tester godkända</strong>. Ändringarna är installerade lokalt och medföljer som patchar; de har inte publicerats till GitHub.</p><p><a href="tool-fixes/l10n-lint.patch">l10n-lint-patch</a> · <a href="tool-fixes/svlang.patch">svlang-patch</a> · <a href="tools.json">Versioner och commits</a> · <a href="tool-fixes/changes.json">Ändringar och tester</a></p><p class="muted">Fullständiga bevis, samtliga förekomster och förslag finns i findings.json. Alla förslag är för granskning; systemets översättningar har inte skrivits om.</p></main><script>const field=document.querySelector('#filter');function filter(){const q=field.value.trim().toLocaleLowerCase('sv');let n=0;document.querySelectorAll('[data-search]').forEach(e=>{const show=e.dataset.search.includes(q);e.classList.toggle('hidden',!show);if(show&&e.classList.contains('finding'))n++});document.querySelector('#shown').textContent=n+' av 57 fyndgrupper visas.'}field.addEventListener('input',filter);filter();</script></html>'''
(OUT/'rapport.html').write_text(body)
save('report-summary.json',{'finding_groups':len(findings),'finding_occurrences':sum(len(f['occurrences']) for f in findings),'priorities':dict(counts),'paths':len(manifest),'unique_catalogs':len(unique),'entries':summary['entries'],'target_forms':summary['target_forms'],'lint_before':old_total,'lint_after':current_total,'svlang_before':svold,'svlang_after':svtotal,'removed_tool_findings':old_total-current_total+svold-svtotal,'all_source_files_unchanged':read('source-integrity.json')['all_unchanged']})
print('Report generated',len(findings),'findings',len(candidates),'lint candidates',flush=True)

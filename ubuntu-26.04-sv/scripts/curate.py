"""Explicitly reviewed findings; no source catalog is changed."""
import collections,hashlib,json,subprocess
from pathlib import Path
import polib
OUT=Path('outputs/locale-granskning');entries=json.loads(Path('work/entries.json').read_text());manifest=json.loads((OUT/'manifest.json').read_text());catalogs={r['id']:r for r in manifest}
findings=[]
def add(cat,line,title,why,proposal=None,replace=None,severity='P2',category='Format',fmt=None,index=None):
    matches=[e for e in entries if e['catalog']==cat and e['line']==line and e['plural_index']==index]
    assert len(matches)==1,(cat,line,len(matches))
    e=matches[0]
    if replace:
        a,b=replace;assert a in e['msgstr'],(cat,line,a);proposal=e['msgstr'].replace(a,b)
    assert proposal and proposal!=e['msgstr'],(cat,line)
    identity=lambda x:(x['msgctxt'],x['msgid'],x['msgid_plural'],x['plural_index'],x['msgstr'])
    occurrences=[]
    for other in entries:
        if identity(other)==identity(e):
            for r in manifest:
                if r['canonical_id']==other['catalog']:
                    occurrences.append({'catalog':r['id'],'line':other['line'],'ordinal':other['ordinal'],'po':r['po'],'mo':r['mo'],'mo_sha256':r['mo_sha256'],'alias':r['id']!=other['catalog']})
    f={'id':f'F{len(findings)+1:03d}','severity':severity,'category':category,'title':title,'reason':why,'entry':e,'proposal':proposal,'occurrences':occurrences,'validation':'Individuellt jämförd med källtext och dekompilerad PO-post.'}
    if fmt:
        results={}
        for kind,value in [('before',e['msgstr']),('proposed',proposal)]:
            po=polib.POFile();po.metadata={'Language':'sv','Content-Type':'text/plain; charset=UTF-8','Plural-Forms':'nplurals=2; plural=(n != 1);'}
            po.append(polib.POEntry(msgid=e['msgid'],msgstr=value,flags=[fmt]))
            path=Path('work/format-check.po');po.save(str(path))
            p=subprocess.run(['msgfmt','--check-format','-o','/dev/null',str(path)],capture_output=True,text=True)
            results[kind]={'exit_code':p.returncode,'stderr':p.stderr}
        f['format_validation']={'synthetic_flag':fmt,**results}
        assert results['proposed']['exit_code']==0,(cat,line,results)
    findings.append(f)

add('locale-langpack/cinder',1695,'Fel nyckel i Python-formatfält','ret.status har blivit ret.statuss. Formatering med originalets nycklar ger KeyError.',replace=('%(ret.statuss)d','%(ret.status)d'),severity='P1',fmt='python-format')
add('locale-langpack/glance',1473,'Typbokstaven saknas efter image_id','%(image_id) saknar s. Python konsumerar mellanslaget och s i ordet som som formatsyntax: exempelvärdet image-1 följs av om i stället för som.',replace=('%(image_id) som','%(image_id)s som'),fmt='python-format')
add('locale-langpack/gdb',14147,'Två trasiga tidsformat','Båda %06ld har trunkerats till %06. Formatkontraktet och återgivningen av tidsvärden går förlorade.',replace=('%06 sekunder','%06ld sekunder'),severity='P1',fmt='c-format')
add('locale/OpenSP',799,'Fel argument för den saknade starttaggen','Den andra platshållaren ska vara %2; nu visas argument %1 två gånger.',replace=('starttaggen %1','starttaggen %2'),fmt='qt-format')
add('locale/OpenSP',874,'HTTP-adressen har tappat sin platshållare','%1 har ersatts med (%), så den berörda URL-adressen kan inte återges korrekt.',proposal='tom värd i HTTP-URL:en %1',fmt='qt-format')
add('locale/OpenSP',1120,'Identifieraren saknas i felmeddelandet','Originalets %1 saknas i översättningen.',replace=('identifierare:','identifierare %1:'),fmt='qt-format')
add('locale/OpenSP',1126,'Värdnumret saknas i felmeddelandet','Originalets %1 saknas i översättningen.',proposal='ogiltigt värdnummer %1',fmt='qt-format')
add('locale/OpenSP',1390,'Numrerad platshållare har blivit printf-format','%1 har ändrats till %d, vilket är en annan formatsyntax.',replace=('(%d)','(%1)'),fmt='qt-format')
for line,word in [(1537,'dataentitet'),(1546,'SDATA-entitet'),(1567,'subdokumententitet')]:
    add('locale/OpenSP',line,'Entitetens namn saknas','Originalets %1 saknas; felmeddelandet tappar uppgiften om vilken entitet som avses.',replace=(word+' ej',word+' %1 ej'),fmt='qt-format')
add('locale/dpkg',3412,'Översättningen lägger till ett obefintligt argument','Originalet innehåller ingen %s. Översättningen har kvar en platshållare och ett prefix som saknar motsvarighet i källtexten.',proposal='behöver ett sökvägsargument',fmt='c-format')
add('locale-langpack/binutils',9133,'Extra %s i meddelandet om felsökningssektion','Källtexten har ingen formateringsparameter; den svenska texten lägger till : %s.',replace=(': %s',''),fmt='c-format')
add('locale-langpack/binutils',9601,'Extra %s i meddelandet om BFD-data','Källtexten har ingen formateringsparameter; den svenska texten lägger till : %s.',replace=(': %s',''),fmt='c-format')
add('locale-langpack/cryptsetup',2486,'Rothash har blivit begärd hash och ett extra argument','Root hash har fått annan innebörd och översättningen innehåller en %s som originalet saknar.',proposal='Verifiering av rothashsignaturer stöds inte.',fmt='c-format')
add('locale-langpack/cryptsetup',2717,'Extra %u i meddelandet om metadata','Originalet anger inte någon numerisk posttyp men översättningen kräver ett sådant argument.',replace=(' av typ ”%u”',''),fmt='c-format')
add('locale-langpack/fetchmail',2123,'Extra %s i meddelandet om --moveto','Översättningen har ett formatargument som inte finns i originalet.',replace=('%s-konfigurationen','konfigurationen'),fmt='c-format')
add('locale-langpack/gas',11177,'Ett dollartecken har blivit %s','Originalets bokstavliga $ får inte ersättas med ett nytt formatargument.',replace=('”%s”','”$”'),fmt='c-format')
add('locale-langpack/gdb',3188,'Skiftlägesinställningen ersätts med ett fast påstående','Originalet återger inställningen via %s. Översättningen säger alltid att sökningen inte är skiftlägeskänslig.',proposal='Namnsökningens skiftlägeskänslighet är ”%s”.\n',category='Betydelse och format',fmt='c-format')
add('locale-langpack/gdb',9950,'&s används i stället för %s','Sektionens namn försvinner eftersom procenttecknet har blivit &.',proposal='Sektionen %s hittades inte',fmt='c-format')
add('locale-langpack/git',8271,'Extra %s i meddelandet om incheckningsgraf','Källtexten har ingen platshållare för filnamn men översättningen har %s.',replace=(' %s är',' är'),fmt='c-format')
add('locale-langpack/ld',1712,'Duplicerat instick får ett extra argument','Översättningen innehåller två %s medan originalet bara innehåller en. %P är länkarens egna direktiv och ska bevaras.',replace=('instick: %s','instick'))
add('locale-langpack/libgphoto2-6',9598,'Antalet återförsök har ersatts med %i','Originalets fasta två återförsök har blivit ett formatargument som inte finns i originalet.',proposal='Överföringen överskred tidsgränsen även efter två nya försök. Ger upp…',fmt='c-format')
add('locale-langpack/libgphoto2-6',8692,'Adressen till utvecklarlistan ersätts med %s','Originalet hänvisar till gphotos utvecklarlista utan formatargument. Översättningen kräver en extra %s.',replace=('skriv ett brev till %s (på Engelska)','skriv ett brev till gphotos utvecklarsändlista (på engelska)'),fmt='c-format')
add('locale-langpack/simple-scan',278,'Trasiga länktaggar i hjälptexten','Den första länken har felaktig escapning och saknar avslutande attributcitat och >. Den andra saknar även inledande <. Länktexten hamnar i attributen.',proposal='Kontrollera om din <a href="http://www.sane-project.org/sane-supported-devices.html">bildläsare stöds av SANE</a>, annars kan du rapportera problemet till <a href="https://alioth-lists.debian.net/cgi-bin/mailman/listinfo/sane-devel">sändlistan för SANE</a>.',category='Markup')
add('locale-langpack/synaptic',281,'Fel avslutning av big-taggen','<b><big> avslutas med </b></b>. Den inre taggen ska avslutas med </big>.',replace=('sätt?</b></b>','sätt?</big></b>'),category='Markup')
add('locale-langpack/slideshow-ubuntu-mate',164,'Netflix får fel avslutningstagg','</string> ska vara </strong>. Samma fel finns i OEM-bildspelet.',replace=('Netflix</string>','Netflix</strong>'),category='Markup')
add('locale-langpack/snappy',2305,'Trasig länk till felsökningshjälp','https: har blivit https; så länken är inte längre korrekt.',replace=('https;//','https://'),category='Länk')
for line,axis in [(287,'x'),(290,'y')]:
    add('locale/libmypaint',line,'Pennans vinkelvärden är omkastade ('+axis+'-led)','Originalet anger ±90 vid parallell penna och 0 vid vinkelrät penna. Översättningen anger motsatsen.',proposal=f'Pennans lutning i {axis}-led. Värdet är 90 eller −90 när pennan är parallell med ritplattan och 0 när den är vinkelrät mot ritplattan.',category='Betydelse')
for line,title,a,b in [(15064,'Medelfranskans tidsintervall avviker','1300-1600','1400-1600'),(15073,'Medeliriskans tidsintervall avviker','1100-1550','900-1200'),(18205,'Fornfranskans slutår avviker','842-1300','842-1400'),(18223,'Forniriskans slutår avviker','1100','900')]:
    add('locale/iso_639-3',line,title,'Årtalen överensstämmer inte med katalogens engelska källtext. Förslaget återställer källtextens intervall.',replace=(a,b),category='Sifferuppgift')

typos=[
('locale-langpack/NetworkManager',87,'rutttyp','ruttyp'),
('locale-langpack/NetworkManager',7022,'huvudrutttabellen','huvudruttabellen'),
('locale-langpack/app-install-data',4845,'nätverksanslutnngar','nätverksanslutningar'),
('locale-langpack/app-install-data',15555,'Allmänn','Allmän'),
('locale-langpack/ubiquity-debconf',810,'tidspunkt','tidpunkt'),
('locale-langpack/dpkg-dev',949,'körnng','körning'),
('locale-langpack/dpkg-dev',1649,'klasss','klass'),
('locale-langpack/glance',1398,'tilllåter','tillåter'),
('locale-langpack/mutt',1298,'öpppna','öppna'),
('locale-langpack/unity-control-center',343,'Tilllåt','Tillåt'),
('locale-langpack/unity-control-center',349,'Tilllåt','Tillåt'),
('locale-langpack/unity',81,'Tilllåter','Tillåter'),
('locale-langpack/unity',814,'Skugggfärg','Skuggfärg'),
('locale-langpack/xz-man',1120,'kommmer','kommer'),
]
for cat,line,a,b in typos:add(cat,line,'Stavfel: '+a,'Ett överflödigt eller saknat tecken ger ett felstavat svenskt ord.',replace=(a,b),severity='P3',category='Stavning')
for cat,line,a,b in [
('locale/OpenSP',646,'därför därför','därför'),
('locale/dpkg',133,'men men','men'),
('locale/dpkg',2424,'för för','för'),
('locale/gnome-builder',2868,'dina dina','dina'),
('locale-langpack/snappy',2749,'relative tider till till','relativa tider upp till'),
('locale-langpack/xfsprogs',5717,'ignoreras\nignoreras','ignoreras'),
('locale-langpack/xfsprogs',6391,'filsystemet\nfilsystemet','filsystemet'),
('locale-langpack/xz-man',1651,'1 beta beta','1 är beta'),
('locale-langpack/xz-man',1837,'med med','men med'),
]:add(cat,line,'Felaktig upprepning: '+a.replace('\n',' '),'Upprepningen är ett skrivfel i denna mening och har inte stöd i källtexten.',replace=(a,b),severity='P3',category='Språk')

# Reproduce Python formatting with inert example arguments (error or corrupt text).
for f,args in [(findings[0],{'ret.status':0,'ret.data':'OK'}),(findings[1],{'image_id':'image-1','task_id':'task-1'})]:
    results={}
    for key,value in [('source',f['entry']['msgid']),('before',f['entry']['msgstr']),('proposed',f['proposal'])]:
        try:results[key]={'ok':True,'output':value%args}
        except (ValueError,KeyError,TypeError) as exc:results[key]={'ok':False,'exception':type(exc).__name__,'message':str(exc)}
    assert results['source']['ok'] and results['proposed']['ok']
    assert not results['before']['ok'] or results['before']['output']!=results['proposed']['output']
    f['runtime_reproducer']=results

OUT.joinpath('findings.json').write_text(json.dumps(findings,ensure_ascii=False,indent=2)+'\n')
print('Curated',len(findings),'findings;',sum(len(f['occurrences']) for f in findings),'occurrences;',collections.Counter(f['severity'] for f in findings))

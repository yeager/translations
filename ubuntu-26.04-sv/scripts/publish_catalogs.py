"""Build reviewed PO corrections, exact patches, per-file provenance and reports."""
import collections, dataclasses, datetime, difflib, gettext, hashlib, json, re, shutil, subprocess
from pathlib import Path
import polib
from l10n_lint import POParser, L10nLinter
from svlang.checkers.skrivregler import SkrivreglerChecker
from svlang.checkers.svengelska import SvengelskaChecker

ROOT=Path('outputs/ubuntu-26.04-sv'); AUDIT=Path('outputs/locale-granskning')
def save(p,v):
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def copy(src,dst):dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
def run(args):
    p=subprocess.run(args,text=True,capture_output=True)
    return {'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
manifest=json.loads((AUDIT/'manifest.json').read_text()); byid={r['id']:r for r in manifest}
findings=json.loads((AUDIT/'findings.json').read_text()); planned=collections.defaultdict(list)
for f in findings:
    for o in f['occurrences']:
        if not o['alias']:planned[o['catalog']].append((f,o))
assert len(planned)==31 and sum(map(len,planned.values()))==61
packages={r['Package']:r for r in json.loads(Path('work/package-upstream.json').read_text())}
owners={line.split(': ',1)[1]:line.split(': ',1)[0] for line in Path('work/package-owners.txt').read_text().splitlines()}
# Primary project pages, cross-checked against package metadata, PO headers and copyright files.
projects={
'NetworkManager':('network-manager','NetworkManager','https://networkmanager.dev/','https://gitlab.freedesktop.org/NetworkManager/NetworkManager'),
'app-install-data':('app-install-data','Ubuntu app-install-data','https://launchpad.net/ubuntu/+source/app-install-data-ubuntu',None),
'binutils':('binutils','GNU Binutils','https://sourceware.org/binutils/',None),
'cinder':('cinder-common','OpenStack Cinder','https://opendev.org/openstack/cinder',None),
'cryptsetup':('cryptsetup','cryptsetup','https://gitlab.com/cryptsetup/cryptsetup',None),
'dpkg':('dpkg','dpkg','https://wiki.debian.org/Teams/Dpkg',None),
'dpkg-dev':('dpkg-dev','dpkg','https://wiki.debian.org/Teams/Dpkg',None),
'fetchmail':('fetchmail','fetchmail','https://www.fetchmail.info/',None),
'gas':('binutils','GNU Binutils / GNU assembler','https://sourceware.org/binutils/',None),
'gdb':('gdb','GNU GDB','https://sourceware.org/gdb/',None),
'git':('git','Git','https://git-scm.com/','https://github.com/git/git'),
'glance':('glance-common','OpenStack Glance','https://launchpad.net/glance','https://opendev.org/openstack/glance'),
'ld':('binutils','GNU Binutils / GNU linker','https://sourceware.org/binutils/',None),
'libgphoto2-2':('libgphoto2-6t64','libgphoto2','https://github.com/gphoto/libgphoto2',None),
'libgphoto2-6':('libgphoto2-6t64','libgphoto2','https://github.com/gphoto/libgphoto2',None),
'mutt':('mutt','Mutt','http://www.mutt.org/','https://gitlab.com/muttmua/mutt'),
'simple-scan':('simple-scan','GNOME Document Scanner','https://apps.gnome.org/SimpleScan/','https://gitlab.gnome.org/GNOME/simple-scan'),
'slideshow-oem-config-ubuntu-mate':('ubiquity-slideshow-ubuntu-mate','Ubiquity slideshow','https://launchpad.net/ubiquity-slideshow-ubuntu',None),
'slideshow-ubuntu-mate':('ubiquity-slideshow-ubuntu-mate','Ubiquity slideshow','https://launchpad.net/ubiquity-slideshow-ubuntu',None),
'snappy':('snapd','snapd','https://github.com/canonical/snapd',None),
'synaptic':('synaptic','Synaptic','https://github.com/mvo5/synaptic',None),
'ubiquity-debconf':('ubiquity','Ubiquity / Debian Installer messages','https://launchpad.net/ubiquity',None),
'unity':('unity','Unity','https://launchpad.net/unity',None),
'unity-control-center':('unity-control-center','Unity Control Center','https://launchpad.net/unity-control-center',None),
'xfsprogs':('xfsprogs','XFS utilities','https://xfs.wiki.kernel.org/',None),
'xz-man':('xz-utils','XZ Utils','https://tukaani.org/xz/',None),
'OpenSP':('libosp5','OpenSP / OpenJade','https://openjade.sourceforge.net/',None),
'gnome-builder':('gnome-builder','GNOME Builder','https://apps.gnome.org/Builder/','https://gitlab.gnome.org/GNOME/gnome-builder'),
'iso_639-3':('iso-codes','iso-codes','https://salsa.debian.org/iso-codes-team/iso-codes',None),
'libmypaint':('libmypaint-common','libmypaint','https://github.com/mypaint/libmypaint',None),
}
linter=L10nLinter({'language':'sv'}); skr=SkrivreglerChecker(); eng=SvengelskaChecker()
rows=[]
for cid,changes in sorted(planned.items()):
    r=byid[cid]; source=AUDIT/r['po']; content=source.read_text(encoding=r['encoding']); lines=content.splitlines(keepends=True)
    entries=POParser(content,str(source)).entries; replacements=[]; applied=[]
    for f,o in changes:
        e=f['entry']; candidates=[x for x in entries if x['msgid']==e['msgid'] and x.get('msgctxt')==e['msgctxt'] and x.get('msgid_plural','')==e['msgid_plural']]
        assert len(candidates)==1,(cid,f['id'],len(candidates))
        x=candidates[0]; key='msgstr' if e['plural_index'] is None else f"msgstr[{e['plural_index']}]"
        assert x[key]==e['msgstr']
        a,b=x['_spans'][key]; value=f['proposal']
        rendered=key+' "'+polib.escape(value)+'"\n' if '\n' not in value else key+' ""\n'+''.join('"'+polib.escape(s)+'"\n' for s in value.splitlines(keepends=True))
        replacements.append((a,b,rendered)); applied.append({'finding_id':f['id'],'severity':f['severity'],'title':f['title'],'reason':f['reason'],'original_line':o['line'],'msgctxt':e['msgctxt'],'msgid':e['msgid'],'msgid_plural':e['msgid_plural'],'plural_index':e['plural_index'],'before':e['msgstr'],'after':value,'format_validation':f.get('format_validation'),'runtime_reproducer':f.get('runtime_reproducer')})
    normalizations=[]
    if cid=='locale-langpack/git':
        for msgid in ['The bundle contains this ref:','The bundle requires this ref:']:
            matches=[e for e in entries if e['msgid']==msgid]; assert len(matches)==2
            redundant,portable=matches
            assert '%llu' in redundant['msgstr[1]'] and '%<PRIuMAX>' in portable['msgstr[1]']
            a=min(s[0] for s in redundant['_spans'].values());b=max(s[1] for s in redundant['_spans'].values())
            assert lines[b]=='\n'; replacements.append((a,b+1,''))
            normalizations.append({'msgid':msgid,'original_line':a+1,'action':'Removed redundant pre-expanded sysdep entry; retained portable PRIuMAX entry.','reason':'msgunfmt emits duplicate keys for this MO. Regeneration preserves the runtime message table.'})
    occupied=set()
    for a,b,replacement in sorted(replacements,reverse=True):
        assert not occupied.intersection(range(a,b));occupied.update(range(a,b));lines[a:b]=[replacement]
    corrected=''.join(lines); original=ROOT/'original'/f'{cid}.po';target=ROOT/'po'/f'{cid}.po';diffpath=ROOT/'diff'/f'{cid}.po.diff'
    copy(source,original);target.parent.mkdir(parents=True,exist_ok=True);target.write_text(corrected,encoding=r['encoding'])
    delta=''.join(difflib.unified_diff(content.splitlines(keepends=True),corrected.splitlines(keepends=True),fromfile=f'a/{cid}.po',tofile=f'b/{cid}.po'))
    diffpath.parent.mkdir(parents=True,exist_ok=True);diffpath.write_text(delta,encoding=r['encoding'])
    # Apply each patch independently and demand byte-for-byte equality.
    test=Path('work/patch-test.po');copy(original,test)
    patch=run(['patch','--batch','--fuzz=0',str(test),str(diffpath.resolve())]);assert patch['exit_code']==0,patch
    assert test.read_bytes()==target.read_bytes()
    mo=Path('work/corrected.mo');compile_result=run(['msgfmt','--check','--check-format','-o',str(mo),str(target)]);assert compile_result['exit_code']==0,(cid,compile_result)
    with open(r['mo'],'rb') as fh:oldtable=gettext.GNUTranslations(fh)._catalog
    with mo.open('rb') as fh:newtable=gettext.GNUTranslations(fh)._catalog
    compiled_headers={'original':oldtable.pop('',None),'corrected':newtable.pop('',None),'note':'Excluded from message comparison: msgfmt may normalize charset and creation-date metadata.'}
    expected=dict(oldtable)
    for c in applied:
        key=c['msgid'] if not c['msgctxt'] else c['msgctxt']+'\x04'+c['msgid']
        if c['plural_index'] is not None:key=(key,c['plural_index'])
        assert expected[key]==c['before'];expected[key]=c['after']
    assert newtable==expected,(cid,[(k,oldtable.get(k),newtable.get(k)) for k in set(oldtable)|set(newtable) if newtable.get(k)!=expected.get(k)][:5])
    parsed=polib.pofile(str(target));oldparsed=polib.pofile(str(original));assert parsed.metadata==oldparsed.metadata
    lint=linter.lint_file(str(target),corrected);issues=[x.to_dict() for x in lint.issues]
    sv=[]
    for e in parsed:
        for index,v in (e.msgstr_plural.items() if e.msgid_plural else [(None,e.msgstr)]):
            for checker in [skr,eng]:
                sv.extend({'po_line':e.linenum,'plural_index':index,**dataclasses.asdict(h)} for h in checker.check(v))
    after={'l10n-lint':{'count':len(issues),'issues':issues},'svlang':{'count':len(sv),'issues':sv}}
    save(ROOT/'validation'/f'{cid}.json',after)
    package,name,url,repo=projects[r['domain']];apt=packages.get(package,{})
    if not apt:
        raw=subprocess.run(['apt-cache','show',package],capture_output=True,text=True,check=True).stdout.split('\n\n')[0]
        apt=dict(line.split(': ',1) for line in raw.splitlines() if ': ' in line and not line.startswith(' '))
        apt={k:v for k,v in apt.items() if k in ['Package','Source','Version','Homepage']}
    owner=owners[r['mo']];installed=subprocess.run(['dpkg-query','-W','-f=${Version}',owner],capture_output=True,text=True,check=True).stdout
    sourcepackage=apt.get('Source',package).split(' ')[0]
    up={'project':name,'project_url':url,'repository_url':repo,'ubuntu_source_package':sourcepackage,'ubuntu_source_url':f'https://launchpad.net/ubuntu/+source/{sourcepackage}','evidence':{'apt_package_metadata':apt,'po_project_id':r['metadata'].get('Project-Id-Version'),'po_bug_report_address':r['metadata'].get('Report-Msgid-Bugs-To')},'note':'Project pointer, not a claim that this installed catalog matches current upstream. Apt versions describe available packages, not the version of a language-pack catalog.'}
    if r['domain']=='app-install-data':up['note']+=' Ubuntu source package is the maintained project reference available for this catalog.'
    if r['domain']=='ubiquity-debconf':up['note']+=' Header identifies Debian Installer; Ubiquity reuses these messages.'
    aliases=[{'id':m['id'],'mo':m['mo'],'sha256':m['mo_sha256']} for m in manifest if m['canonical_id']==cid and m['id']!=cid]
    beforelint=json.loads((AUDIT/'raw/l10n-lint'/f'{cid}.json').read_text());beforesv=json.loads((AUDIT/'raw/svlang'/f'{cid}.json').read_text())
    paths={k:str(p.relative_to(ROOT)) for k,p in [('corrected_po',target),('original_po',original),('diff',diffpath),('report',ROOT/'reports'/f'{cid}.md'),('metadata',ROOT/'metadata'/f'{cid}.json'),('validation',ROOT/'validation'/f'{cid}.json')]}
    metadata={'schema_version':1,'review_date':'2026-09-19','catalog':cid,'language':'sv','distribution':'Ubuntu 26.04.1 LTS (Resolute Raccoon)','paths':paths,'upstream':up,'origin':{'mo_path':r['mo'],'resolved_mo_path':r['resolved_mo'],'mo_sha256':r['mo_sha256'],'installed_owning_package':owner,'installed_owning_package_version':installed,'aliases':aliases,'extraction_command':['msgunfmt','--no-wrap',r['mo']],'gettext_version':'0.23.2','po_headers':r['metadata']},'sha256':{'original_po':sha(original),'corrected_po':sha(target),'diff':sha(diffpath)},'report':{'changed_translations':len(applied),'priorities':dict(collections.Counter(c['severity'] for c in applied)),'findings':applied,'extraction_normalizations':normalizations,'lint_before':len(beforelint['issues']),'lint_after':len(issues),'svlang_before':len(beforesv),'svlang_after':len(sv),'remaining_hits_are_unreviewed_candidates':True},'verification':{'msgfmt':compile_result,'diff_applies_without_fuzz':True,'diff_reproduces_corrected_po_bytes':True,'compiled_message_table_changes_exactly_match_reviewed_edits':True,'po_headers_unchanged':True,'system_mo_unchanged':sha(Path(r['mo']))==r['mo_sha256']}}
    for c in applied:
        e=next(e for e in parsed if e.msgid==c['msgid'] and e.msgctxt==c['msgctxt']);c['corrected_line']=e.linenum
    metadata['encoding']={'po':r['encoding'],'diff':r['encoding'],'metadata':'UTF-8','report':'UTF-8'}
    metadata['verification']['compiled_headers']=compiled_headers
    save(ROOT/paths['metadata'],metadata);rows.append(metadata)
    report=[f'# {cid}',f"{len(applied)} rättade översättningsposter. Ursprung: `{r['mo']}`.",f"Upstream: [{name}]({url})."+(f' [Källkod]({repo}).' if repo else ''),f"[Ubuntu-källpaket]({up['ubuntu_source_url']}). Installerat ägarpaket: `{owner} {installed}`.",f"[Rättad PO](../../{paths['corrected_po']}) · [Original](../../{paths['original_po']}) · [Diff](../../{paths['diff']}) · [Metadata](../../{paths['metadata']})",'Rättad PO godkänns av `msgfmt --check --check-format`. Diffen återger filen byte för byte. Den kompilerade meddelandetabellen skiljer sig från installerad MO endast genom rättningarna nedan. PO-huvudet är bevarat; rapporten dokumenterar ändringarnas datum.',f"Råträffar: l10n-lint {len(beforelint['issues'])} → {len(issues)}, svlang {len(beforesv)} → {len(sv)}. Kvarstående träffar är kandidater och innebär inte verifierade fel."]
    if normalizations:report.append('Två redundanta sysdep-poster från msgunfmt har dessutom tagits bort. De portabla PRIuMAX-posterna är bevarade. Återkompilering visar oförändrad runtime-tabell för dessa poster. Se metadata och diff.')
    for c in applied:
        report += [f"## {c['finding_id']} · {c['severity']} · {c['title']}",c['reason'],f"PO-rad: original {c['original_line']}, rättad {c['corrected_line']}.",'Källtext:\n\n```text\n'+c['msgid']+'\n```','Före:\n\n```text\n'+c['before']+'\n```','Efter:\n\n```text\n'+c['after']+'\n```']
    reportpath=ROOT/paths['report'];reportpath.parent.mkdir(parents=True,exist_ok=True);reportpath.write_text('\n\n'.join(report)+'\n')
    print(cid,len(applied),'verified',flush=True)
save(ROOT/'metadata.json',rows)
save(ROOT/'validation-summary.json',{'catalogs':len(rows),'changed_translations':sum(r['report']['changed_translations'] for r in rows),'finding_groups':len(findings),'occurrences_including_aliases':sum(len(f['occurrences']) for f in findings),'all_msgfmt_pass':all(r['verification']['msgfmt']['exit_code']==0 for r in rows),'all_compiled_semantic_changes_exact':all(r['verification']['compiled_message_table_changes_exactly_match_reviewed_edits'] for r in rows),'all_diffs_exact':True,'system_catalogs_modified':False})
for name in ['findings.json','findings.csv','scan-summary.json','references-summary.json','report-summary.json','tools.json','manifest.json','source-integrity.json','lint-kandidater.csv']:
    copy(AUDIT/name,ROOT/name)
for folder in ['tool-fixes','scripts']:shutil.copytree(AUDIT/folder,ROOT/folder,dirs_exist_ok=True)
for p in (AUDIT/'raw').glob('*'):
    if p.is_file():copy(p,ROOT/'raw'/p.name)
copy(AUDIT/'raw/fore-verktygsfix/scan-summary.json',ROOT/'raw/fore-verktygsfix/scan-summary.json')
for cid in planned:
    for tool in ['l10n-lint','svlang']:copy(AUDIT/'raw'/tool/f'{cid}.json',ROOT/'raw'/tool/f'{cid}.json')
copy(Path(__file__),ROOT/'scripts/publish_catalogs.py')
report=(AUDIT/'rapport.md').read_text().replace('](po/','](original/').replace('original/locale/iso_639_3.po','original/locale/iso_639-3.po')
report=report.replace('## Omfattning och metod','## Publicerade rättningar\n\nSamtliga 57 fyndförslag är införda i **31 PO-filer, 61 ändrade översättningsposter**. De 65 ursprungliga förekomsterna inkluderar fyra ISO-alias. [Filindex med upstream](README.md), [metadata för alla rättade filer](metadata.json) och [validering](validation-summary.json). Originalfilerna bevaras i `original/`; rättade filer ligger i `po/`. Git har dessutom två dokumenterade sysdep-normaliseringar. Systemets MO-filer är oförändrade.\n\n## Omfattning och metod')
(ROOT/'rapport.md').write_text(report)
readme=['# Ubuntu 26.04 – granskning av svenska översättningar','Granskad 19 september 2026 på Ubuntu 26.04.1 LTS. **31 rättade PO-filer, 61 ändrade översättningsposter från 57 verifierade fyndgrupper.** Originalen är extraherade med `msgunfmt --no-wrap` från de två installerade svenska katalogmapparna.','[Full rapport](rapport.md) · [Alla metadata](metadata.json) · [Valideringsresultat](validation-summary.json) · [Samtliga fynd](findings.json)','Varje rättad PO har en exakt diff, ett oförändrat dekompilerat original, en separat rapport och metadata med upstream, ägarpaket, version, MO-sökväg, SHA-256, PO-huvud, före/efter och validering. Länkarna till upstream identifierar projekten; katalogerna är Ubuntu-versionerna som faktiskt fanns installerade.','Samtliga 31 rättade PO-filer klarar `msgfmt --check --check-format`. Alla diffar har applicerats utan fuzz och ger exakt publicerade bytes. Återkompilering ger samma meddelandetabell som installerad MO utom de 61 avsedda rättningarna. Git har dessutom två redundanta sysdep-poster borttagna, vilket behövs för återkompilering; runtime-tabellen är bevarad. Systemets MO-filer har inte ändrats.','Automatisk granskning omfattade 479 MO-sökvägar, 473 unika kataloger och 230 304 poster. Rapportens råträffar avser originalen efter fem förbättringar i granskningsverktygen. Fynden är ett manuellt granskat urval, inte en fullständig språkgranskning.','| Katalog | Rättningar | PO | Diff | Rapport | Metadata | Upstream |','|---|---:|---|---|---|---|---|']
for r in rows:
    p=r['paths'];u=r['upstream'];readme.append(f"| {r['catalog']} | {r['report']['changed_translations']} | [PO]({p['corrected_po']}) | [Diff]({p['diff']}) | [Rapport]({p['report']}) | [JSON]({p['metadata']}) | [{u['project']}]({u['project_url']}) |")
readme += ['## Använd en diff','Diffens bas är filen under `original/`, inte en godtycklig aktuell upstream-PO. Exempel:\n\n```sh\ncp original/locale-langpack/cinder.po cinder.po\npatch --fuzz=0 cinder.po diff/locale-langpack/cinder.po.diff\nmsgfmt --check --check-format -o /tmp/cinder.mo cinder.po\n```','MO-formatet saknar bland annat ursprungliga källreferenser, de flesta formatflaggor, fuzzy-markeringar och oöversatta poster. Bevara upstreams befintliga PO och för över relevanta ändringar vid inskickning dit.','## Verktygsförbättringar','Fem ändringar i l10n-lint och svlang har testats (274 + 83 tester) och installerats lokalt. [Patchar och testunderlag](tool-fixes/) samt [versioner](tools.json) medföljer. De minskade originalmaterialets råträffar med 547. Verktygspatcharna har inte skickats till respektive upstream-repo.','## Underlag','`manifest.json` beskriver samtliga 479 inlästa sökvägar. Enbart de 31 rättade katalogernas PO-original och rårapporter ingår här. Den fullständiga lokala granskningsleveransen innehåller alla extraherade PO-filer. TM-, termbanks- och konsekvensavvikelser för hela materialet finns under `raw/`. ISO-alias `iso_639_3` täcks av filen `iso_639-3`; fyra fynd återkommer via aliaset.']
(ROOT/'README.md').write_text('\n\n'.join(readme[:6])+'\n\n'+'\n'.join(readme[6:8])+'\n'+'\n'.join(readme[8:8+len(rows)])+'\n\n'+'\n\n'.join(readme[8+len(rows):])+'\n')
# Final prose clarifications are applied by finalize_publication.py.
# All publication files are individually integrity-checkable.
(ROOT/'SHA256SUMS').write_text(''.join(f'{sha(p)}  {p.relative_to(ROOT)}\n' for p in sorted(ROOT.rglob('*')) if p.is_file() and p.name!='SHA256SUMS'))
print('Publication ready:',len(rows),'files;',sum(r['report']['changed_translations'] for r in rows),'edits')

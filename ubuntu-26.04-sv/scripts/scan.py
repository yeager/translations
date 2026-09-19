"""Read-only catalog audit using installed l10n-lint and svlang."""
import collections,csv,dataclasses,datetime,hashlib,json,subprocess
from pathlib import Path
import polib
from l10n_lint import L10nLinter,__version__ as lint_version
from svlang import __version__ as sv_version
from svlang.checkers.skrivregler import SkrivreglerChecker
from svlang.checkers.svengelska import SvengelskaChecker
from svlang.checkers.consistency import ConsistencyChecker

OUT=Path('outputs/locale-granskning'); manifest=json.loads((OUT/'manifest.json').read_text())
def save(p,x):
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
seen={}; catalogs=[]
for r in manifest:
    key=r['mo_sha256']
    if key in seen:r['canonical_id']=seen[key]
    else:
        seen[key]=r['id'];r['canonical_id']=r['id'];catalogs.append(r)
save(OUT/'manifest.json',manifest)
skr=SkrivreglerChecker(); eng=SvengelskaChecker(); consistency=ConsistencyChecker()
linter=L10nLinter({'language':'sv'})
summary=[];entry_rows=[];counts=collections.Counter()
for n,r in enumerate(catalogs,1):
    p=OUT/r['po']; po=polib.pofile(str(p)); text=p.read_bytes().decode(po.encoding)
    lint=linter.lint_file(str(p),text)
    issues=[x.to_dict() for x in lint.issues]
    save(OUT/'raw/l10n-lint'/f"{r['id']}.json",{'files_checked':lint.files_checked,'entries_checked':lint.entries_checked,'errors':lint.error_count,'warnings':lint.warning_count,'issues':issues})
    hits=[]
    for ordinal,e in enumerate(po,1):
        if e.obsolete:continue
        forms=e.msgstr_plural.items() if e.msgid_plural else [(None,e.msgstr)]
        for index,value in forms:
            base={'catalog':r['id'],'ordinal':ordinal,'line':e.linenum,'msgctxt':e.msgctxt,'msgid':e.msgid,'msgid_plural':e.msgid_plural,'plural_index':index,'msgstr':value}
            entry_rows.append(base)
            consistency.add(e.msgid,value,str(p)+':'+str(e.linenum),context=e.msgctxt or '',plural_source=e.msgid_plural,plural_index=index)
            for name,checker in [('skrivregler',skr),('svengelska',eng)]:
                for h in checker.check(value):
                    d=dataclasses.asdict(h);target_line=d.pop('line',None)
                    hits.append({'line':e.linenum,'ordinal':ordinal,'plural_index':index,'checker':name,'target_line':target_line,**d})
    save(OUT/'raw/svlang'/f"{r['id']}.json",hits)
    counts.update(i['rule'] for i in issues)
    summary.append({'catalog':r['id'],'entries':len(po),'lint_entries_checked':lint.entries_checked,'lint_issues':len(issues),'lint_errors':lint.error_count,'lint_warnings':lint.warning_count,'svlang_issues':len(hits)})
    if n%25==0:print('Scanned',n,'/',len(catalogs),flush=True)
save(OUT/'raw/svlang-consistency.json',[dataclasses.asdict(i) for i in consistency.check()])
save(Path('work/entries.json'),entry_rows)
save(OUT/'scan-summary.json',{'tools':{'l10n-lint':lint_version,'svlang':sv_version},'unique_catalogs':len(catalogs),'entries':sum(x['entries'] for x in summary),'target_forms':len(entry_rows),'lint_rules':dict(counts.most_common()),'catalogs':summary})
print('SCAN COMPLETE',len(catalogs),sum(x['entries'] for x in summary),counts,flush=True)

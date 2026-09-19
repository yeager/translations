import collections, datetime, gettext, hashlib, json, subprocess
from pathlib import Path
import polib

OUT = Path('outputs/locale-granskning')
OUT.mkdir(parents=True, exist_ok=True)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
manifest=[]
for group,root in [('locale-langpack','/usr/share/locale-langpack/sv/LC_MESSAGES'),('locale','/usr/share/locale/sv/LC_MESSAGES')]:
    for mo in sorted(Path(root).glob('*.mo')):
        po=OUT/'po'/group/(mo.stem+'.po'); po.parent.mkdir(parents=True,exist_ok=True)
        row={'id':group+'/'+mo.stem,'group':group,'domain':mo.stem,'mo':str(mo),'resolved_mo':str(mo.resolve()),'symlink':mo.is_symlink(),'mo_sha256':sha(mo),'bytes':mo.stat().st_size,'po':str(po.relative_to(OUT))}
        r=subprocess.run(['msgunfmt','--no-wrap','-o',str(po),str(mo)],capture_output=True,text=True)
        row['msgunfmt']={'exit_code':r.returncode,'stderr':r.stderr}
        if r.returncode==0:
            p=polib.pofile(str(po))
            row.update(entries=len(p),plural_entries=sum(bool(e.msgid_plural) for e in p),target_forms=sum(len(e.msgstr_plural) if e.msgid_plural else 1 for e in p),encoding=p.encoding,metadata=p.metadata,po_sha256=sha(po))
            r=subprocess.run(['msgfmt','--check','--check-format','-o','/dev/null',str(po)],capture_output=True,text=True)
            row['msgfmt']={'exit_code':r.returncode,'stderr':r.stderr}
            compiled=Path('work/roundtrip.mo')
            r=subprocess.run(['msgfmt','-o',str(compiled),str(po)],capture_output=True,text=True)
            row['roundtrip_exit_code']=r.returncode
            if r.returncode==0:
                with mo.open('rb') as f: original=gettext.GNUTranslations(f)._catalog
                with compiled.open('rb') as f: regenerated=gettext.GNUTranslations(f)._catalog
                row['roundtrip_messages_equal']={k:v for k,v in original.items() if k!=''}=={k:v for k,v in regenerated.items() if k!=''}
        manifest.append(row)
        if len(manifest)%100==0: print('Extracted',len(manifest),flush=True)
save(OUT/'manifest.json',manifest)
print('Complete',len(manifest),'paths;',sum(r.get('entries',0) for r in manifest),'entries;',len(set(r['mo_sha256'] for r in manifest)),'unique binaries',flush=True)

import collections,csv,json,hashlib
from pathlib import Path
import polib
OUT=Path('outputs/locale-granskning')
def save(p,x):
    p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
rows=[]
for r in json.loads((OUT/'manifest.json').read_text()):
    if r['canonical_id']!=r['id']:continue
    for ordinal,e in enumerate(polib.pofile(str(OUT/r['po'])),1):
        for index,value in (e.msgstr_plural.items() if e.msgid_plural else [(None,e.msgstr)]):
            source=e.msgid_plural if index is not None and int(index)!=0 else e.msgid
            rows.append({'catalog':r['id'],'line':e.linenum,'ordinal':ordinal,'plural_index':index,'msgctxt':e.msgctxt,'source':source,'target':value})
sources={r['source'] for r in rows}; memory=collections.defaultdict(lambda:collections.defaultdict(list));stats=[]
for p in sorted(Path('/usr/local/share/swedish-tm').glob('sv-*.po')):
    po=polib.pofile(str(p));matched=0
    for e in po:
        if e.msgid in sources and e.msgstr and not e.fuzzy and not e.obsolete:
            memory[e.msgid][e.msgstr].append(p.name); matched+=1
    stats.append({'file':p.name,'entries':len(po),'matching_sources':matched,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
    print('Indexed',p.name,len(po),matched,flush=True)
terms={}
termfile=Path('/usr/local/share/swedish-foss-terminology/termbank-flat.csv')
with termfile.open(newline='',encoding='utf-8') as f:
    term_rows=0
    for r in csv.DictReader(f):
        term_rows+=1
        if r['source'] in sources:terms[r['source']]={'canonical':r['canonical'],'confidence':float(r['confidence'])}
tm_counts=collections.Counter();term_counts=collections.Counter();tm_diff=[];term_diff=[]
for r in rows:
    choices=memory.get(r['source'])
    if not choices:tm_counts['source_absent']+=1
    elif r['target'] in choices:tm_counts['exact_pair_match']+=1
    else:
        tm_counts['different_target']+=1
        tm_diff.append({**r,'alternatives':dict(choices)})
    t=terms.get(r['source'])
    if not t:term_counts['source_absent']+=1
    elif r['target']==t['canonical']:term_counts['canonical_match']+=1
    else:
        term_counts['different_target']+=1;term_diff.append({**r,**t})
save(OUT/'raw/tm-differences.json',tm_diff)
save(OUT/'raw/terminology-differences.json',term_diff)
save(OUT/'references-summary.json',{'comparison':'Exact source and target strings; contexts and plural identities are unavailable in the reference exports. Differences are review candidates, never automatic corrections.','tm_files':stats,'tm':dict(tm_counts),'terminology':dict(term_counts),'term_rows':term_rows,'termbank_sha256':hashlib.sha256(termfile.read_bytes()).hexdigest()})
save(Path('work/tm-matches.json'),dict(memory))
print('REFERENCES COMPLETE',tm_counts,term_counts,flush=True)

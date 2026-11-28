from pathlib import Path
from collections import Counter,defaultdict
import polib,re,json
root=Path(__file__).parent
pot=polib.pofile(str(root/'gnome-terminal.master.pot'))
original=polib.pofile(str(root/'gnome-terminal.master.sv.original.po'))
reviewed=polib.pofile(str(root/'gnome-terminal.master.sv.reviewed.po'))
def active(c): return [e for e in c if not e.obsolete]
def sig(e): return (e.msgctxt or '',e.msgid,e.msgid_plural)
P,O,R=map(active,(pot,original,reviewed))
assert Counter(map(sig,P))==Counter(map(sig,R)), 'msgid/context/plural mismatch with latest POT'
assert Counter(map(sig,P))==Counter(map(sig,O)), 'downloaded PO does not match latest POT'
assert not any('fuzzy' in e.flags for e in R)
def untranslated(e):
 vals=list(e.msgstr_plural.values()) if e.msgid_plural else [e.msgstr]
 return not any(vals)
assert not [e.msgid for e in R if untranslated(e)]
fmt=re.compile(r'%(?:\d+\$)?[-+#0 ]*(?:\d+|\*)?(?:\.(?:\d+|\*))?(?:hh|h|ll|l|j|z|t|L)?[diouxXeEfFgGaAcspn%]')
tags=re.compile(r'</?[A-Za-z][A-Za-z0-9]*(?:\s+[^<>@]+)?\s*/?>')
urls=re.compile(r'(?i)\b(?:https?|ftp)://[^\s<>]+')
errors=[]
source_map={sig(e):e for e in P}
for e in R:
 src=source_map[sig(e)]
 translations=list(e.msgstr_plural.items()) if e.msgid_plural else [(0,e.msgstr)]
 for index,translation in translations:
  if not translation: continue
  source_text=(src.msgid_plural if e.msgid_plural and index>0 else src.msgid)
  for label,pattern in [('printf',fmt),('markup',tags),('url',urls)]:
   if sorted(pattern.findall(source_text))!=sorted(pattern.findall(translation)):
    errors.append((e.msgid,label,pattern.findall(source_text),pattern.findall(translation)))
  if src.msgid.count('_')!=translation.count('_'):
   errors.append((e.msgid,'accelerator-count',src.msgid.count('_'),translation.count('_')))
  if re.search(r'_(?:Å|Ä|Ö|å|ä|ö)',translation):
   errors.append((e.msgid,'Nordic accelerator',translation))
assert not errors,errors
orig_groups=defaultdict(list); reviewed_groups=defaultdict(list)
for e in O: orig_groups[sig(e)].append(e)
for e in R: reviewed_groups[sig(e)].append(e)
changed=0; fuzzy_reviewed=0
for key,es in reviewed_groups.items():
 for old,new in zip(orig_groups[key],es):
  if new.msgstr!=old.msgstr or new.msgstr_plural!=old.msgstr_plural: changed+=1
  if 'fuzzy' in old.flags: fuzzy_reviewed+=1
fuzzy=sum('fuzzy' in e.flags for e in O)
missing=sum(untranslated(e) and 'fuzzy' not in e.flags for e in O)
report={'pot_active':len(P),'original_translated':len(O)-fuzzy-missing,'original_fuzzy':fuzzy,'original_untranslated':missing,'reviewed_translated':len(R)-sum('fuzzy' in e.flags for e in R)-sum(untranslated(e) for e in R),'reviewed_fuzzy':sum('fuzzy' in e.flags for e in R),'reviewed_untranslated':sum(untranslated(e) for e in R),'text_changed_entries':changed,'previously_fuzzy_reviewed':fuzzy_reviewed,'structural_errors':len(errors)}
(root/'validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))

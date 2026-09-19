from pathlib import Path
import hashlib,json,re,shutil
root=Path('outputs/ubuntu-26.04-sv')
# Describe exactly what the semantic comparison covers.
note='Jämförelsen gäller översatta meddelanden, utan metadatahuvudet. Gettext kan normalisera det kompilerade huvudets teckenkodning och skapandedatum; före/efter finns i metadata. PO-filerna och diffarna behåller ursprunglig teckenkodning (OpenSP: ISO-8859-1).'
p=root/'README.md';s=p.read_text();s=s.replace('\n\nAutomatisk granskning', '\n\n'+note+'\n\nAutomatisk granskning');p.write_text(s)
for p in [root/'rapport.md',*sorted((root/'reports').rglob('*.md'))]:
    s=p.read_text();parts=s.split('\n\n',2);s='\n\n'.join(parts[:2])+ '\n\n'+note+'\n\n'+parts[2];p.write_text(s)
old='de är inte publicerade till GitHub.';new='de är inte införda i verktygens upstream-repon.'
for p in [root/'rapport.md',Path('outputs/locale-granskning/rapport.md'),Path('outputs/locale-granskning/rapport.html'),Path('work/build_report.py')]:
    s=p.read_text();p.write_text(s.replace(old,new))
# Keep published build scripts consistent with wording in the reports.
p=Path('work/publish_catalogs.py');s=p.read_text();s=s.replace("# All publication files are individually integrity-checkable.","# Final prose clarifications are applied by finalize_publication.py.\n# All publication files are individually integrity-checkable.");p.write_text(s)
for name in ['publish_catalogs.py','finalize_publication.py','build_report.py']:shutil.copy2(Path('work')/name,root/'scripts'/name)
errors=[];count=0
for p in root.rglob('*.md'):
    s=re.sub(r'```.*?```','',p.read_text(),flags=re.S)
    for link in re.findall(r'\]\(([^)]+)\)',s):
        if re.match(r'\w+://',link) or link.startswith('#'):continue
        target=p.parent/link.split('#')[0]
        count+=1
        if not target.exists():errors.append((str(p),link))
assert not errors,errors
metadata=json.loads((root/'metadata.json').read_text())
for m in metadata:
    for v in m['paths'].values():assert (root/v).exists(),v
    for key in ['original_po','corrected_po','diff']:
        assert hashlib.sha256((root/m['paths'][key]).read_bytes()).hexdigest()==m['sha256'][key]
    assert m['verification']['system_mo_unchanged']
# Validate the source integrity again immediately before publication.
manifest=json.loads((root/'manifest.json').read_text())
assert all(hashlib.sha256(Path(r['mo']).read_bytes()).hexdigest()==r['mo_sha256'] for r in manifest)
(root/'SHA256SUMS').write_text(''.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(root)}\n' for p in sorted(root.rglob('*')) if p.is_file() and p.name!='SHA256SUMS'))
print('Local links checked:',count,'; metadata records:',len(metadata),'; original MOs unchanged:',len(manifest))

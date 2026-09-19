from pathlib import Path
import re
import polib

source = Path('work/translations/Blender/blender-ui-ui-sv.po')
outdir = Path('work/blender-endstop-deltas')
outdir.mkdir(exist_ok=True)
po = polib.pofile(str(source))

# The l10n-lint issue order matches the Weblate end-stop queue. Entries up to
# rank 741 cover UI rows already reviewed directly through 751, so never emit
# them from this batch. Match l10n-lint's abbreviation exclusion exactly.
rank = 0
candidates = []
for entry in po:
    if entry.obsolete or not entry.msgid or not entry.msgstr:
        continue
    src = entry.msgid.strip()
    dst = entry.msgstr.strip()
    if len(src) <= 4 or src.endswith('.') or src.endswith('...') or not dst.endswith('.'):
        continue
    if re.search(r'\b(Mr|Mrs|Ms|Dr|Prof|etc|vs|e\.g|i\.e)\.', src, re.IGNORECASE):
        continue
    rank += 1
    if rank <= 741:
        continue
    candidates.append(polib.POEntry(
        msgid=entry.msgid, msgstr=entry.msgstr.rstrip()[:-1],
        msgctxt=entry.msgctxt, comment=entry.comment, tcomment=entry.tcomment,
        occurrences=entry.occurrences, flags=entry.flags,
        previous_msgctxt=entry.previous_msgctxt, previous_msgid=entry.previous_msgid,
        previous_msgid_plural=entry.previous_msgid_plural,
    ))

if rank != 2887:
    raise SystemExit(f'unexpected candidate count {rank}; expected 2887')
if len(candidates) != 2146:
    raise SystemExit(f'unexpected remaining count {len(candidates)}; expected 2146')
for path in outdir.glob('blender-ui-sv-endstop-*.po'):
    path.unlink()
base, extra = divmod(len(candidates), 10)
start = 0
for part in range(1, 11):
    size = base + (1 if part <= extra else 0)
    delta = polib.POFile()
    delta.metadata = dict(po.metadata)
    delta.metadata['X-Review-Part'] = f'{part}/10'
    delta.metadata['X-Review-Scope'] = 'l10n-lint verified end-stop fixes after Weblate queue row 751'
    for entry in candidates[start:start + size]:
        delta.append(entry)
    path = outdir / f'blender-ui-sv-endstop-{part:02d}-of-10.po'
    delta.save(str(path))
    print(f'{path}: {size}')
    start += size

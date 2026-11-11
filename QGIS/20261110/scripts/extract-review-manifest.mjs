#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';

const usage = 'Usage: node extract-review-manifest.mjs OUTPUT.json [FIRST_BATCH] [LAST_BATCH]';
const [output, firstArg = '253', lastArg = '274'] = process.argv.slice(2);

if (!output || !/^\d+$/.test(firstArg) || !/^\d+$/.test(lastArg)) {
  throw new Error(usage);
}

const first = Number(firstArg);
const last = Number(lastArg);
if (first > last) throw new Error('FIRST_BATCH must not exceed LAST_BATCH');

const root = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..');
const batchesDir = path.join(root, 'batches');
const rawPath = path.join(root, 'raw', 'qgis-application-sv-transifex-live-20261110.ts');
const raw = fs.readFileSync(rawPath, 'utf8');

const escapeXml = (value) => value
  .replaceAll('&', '&amp;')
  .replaceAll('<', '&lt;')
  .replaceAll('>', '&gt;')
  .replaceAll('"', '&quot;');

const decodeDocumentEscapes = (value) => value.replaceAll('\\n', '\n');
const row = /^\| `(.+?)` \| `.*?` \| `(.+?)` \|$/;
const changes = [];

for (const name of fs.readdirSync(batchesDir).sort()) {
  const match = /^(\d+)-.*\.md$/.exec(name);
  if (!match) continue;
  const batch = Number(match[1]);
  if (batch < first || batch > last) continue;

  for (const line of fs.readFileSync(path.join(batchesDir, name), 'utf8').split('\n')) {
    const columns = row.exec(line);
    if (!columns) continue;
    changes.push({
      batch,
      source: decodeDocumentEscapes(columns[1]),
      target: decodeDocumentEscapes(columns[2]),
    });
  }
}

const sourceExists = (source) => {
  const encoded = escapeXml(source);
  return raw.includes(`<source>${encoded}</source>`)
    || raw.includes(`<source>${encoded.replaceAll("'", '&apos;')}</source>`);
};

const missing = changes.filter(({ source }) => !sourceExists(source));
if (missing.length) {
  throw new Error(`Source strings missing from raw snapshot:\n${missing.map(({ batch, source }) => `${batch}: ${source}`).join('\n')}`);
}

const manifest = {
  project: 'qgis/QGIS',
  resource: 'qgis-application',
  language: 'sv',
  source_snapshot: 'raw/qgis-application-sv-transifex-live-20261110.ts',
  status: 'local-review-only',
  notes: 'Generated review manifest. Resolve current Transifex units and compare their target text before generating an import delta.',
  batches: [...new Set(changes.map(({ batch }) => batch))],
  changes,
};

fs.writeFileSync(output, `${JSON.stringify(manifest, null, 2)}\n`);
console.log(`${changes.length} candidates from batches ${first}–${last} written to ${output}`);

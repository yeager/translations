# OpenClaw Control UI – svenska kärnetiketter

Datum: 2026-11-15  
Upstream: [PR #199526](https://github.com/openclaw/openclaw/pull/199526)

Sju delade poster i Control UI:s svenska översättningsminne har granskats och
uppdaterats. De gäller sammanlagt 26 synliga positioner.

| Segment | Engelska | Svenska |
| --- | --- | --- |
| `aboutPage.linkSupport` | Support | Stöd |
| `quickSettings.security.execPolicyValue.auto` | Auto | Automatiskt |
| `agents.tabs.skills` | Skills | Färdigheter |
| `pluginsPage.intentTrending` | Trending | Populära |
| `templatesCatalog.filePurpose.heartbeat` | heartbeat monitors | heartbeat-övervakare |
| `linkReader.patchTruncated` | full patch | alla ändringar |
| `agents.toolCatalog.descriptions.applyPatch` | Patch files | Lägg in ändringar i filer |

De delade segmenten omfattar bland annat appens stödlänk, inställningar för
automatiskt läge, färdigheter i agenter, chatt och inställningar samt den
populära kategorin i tilläggskatalogen. De omfattar också beskrivningen av
ändringsverktyget och texten om heartbeat-övervakning. Källan och
översättningen finns i `ui/src/i18n/.i18n/sv.tm.jsonl` i upstream-PR:n.

Kontroller som passerar: JSONL-parsning, Hunspell-sv, svlang, diffkontroll och
Gitleaks. `l10n-lint` stöder inte JSONL-filer och är därför inte tillämpligt på
just denna del av OpenClaws katalog.

# OpenClaw Control UI – svenska kärnetiketter

Datum: 2026-11-15  
Upstream: [PR #199526](https://github.com/openclaw/openclaw/pull/199526)

Femton delade poster i Control UI:s svenska översättningsminne har granskats
och uppdaterats. De gäller sammanlagt 34 synliga positioner.

| Segment | Engelska | Svenska |
| --- | --- | --- |
| `aboutPage.linkSupport` | Support | Stöd |
| `quickSettings.security.execPolicyValue.auto` | Auto | Automatiskt |
| `agents.tabs.skills` | Skills | Färdigheter |
| `pluginsPage.intentTrending` | Trending | Populära |
| `templatesCatalog.filePurpose.heartbeat` | heartbeat monitors | heartbeat-övervakare |
| `linkReader.patchTruncated` | full patch | alla ändringar |
| `agents.toolCatalog.descriptions.applyPatch` | Patch files | Lägg in ändringar i filer |
| `profilePage.identity.gitCoauthorGithub` | commits | incheckningar |
| `chat.sessionDiff.uncommittedStay` | Uncommitted changes | Ej incheckade ändringar |
| `configHints.tools%2Egithub%2EgitAuthor%2Ename.help.v1-z5bl1f-1h` | committer | den som gör incheckningen |
| `chat.sessionDiff.uncommitted` | Uncommitted | Ej incheckade |
| `configHints.tools%2Egithub%2EgitAuthor%2Eemail.help.v1-kol5g6-1i` | committer | den som gör incheckningen |
| `configHints.gateway%2Eauth%2EtrustedProxy%2EgitCoauthor%2EemailHeader.help.v1-1j8gxp7-2h` | commits | incheckningar |
| `profilePage.identity.linkedEmailsDescription` | commit co-authoring | medförfattarskap i incheckningar |
| `profilePage.identity.gitCoauthorDescription` | commit history | incheckningshistoriken |

De delade segmenten omfattar bland annat appens stödlänk, inställningar för
automatiskt läge, färdigheter i agenter, chatt och inställningar samt den
populära kategorin i tilläggskatalogen. De omfattar också beskrivningen av
ändringsverktyget, texten om heartbeat-övervakning och ordvalet för Git-
incheckningar. Källan och
översättningen finns i `ui/src/i18n/.i18n/sv.tm.jsonl` i upstream-PR:n.

Kontroller som passerar: JSONL-parsning, Hunspell-sv, svlang, diffkontroll och
Gitleaks. `l10n-lint` passerar för hela översättningsminnet.

# OpenClaw Control UI – svenska kärnetiketter

Datum: 2026-11-15  
Upstream: [PR #199526](https://github.com/openclaw/openclaw/pull/199526)

Trettiosex delade poster i Control UI:s svenska översättningsminne har
granskats och uppdaterats. De gäller sammanlagt 56 synliga positioner.

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
| `presence.rosterTitle` | Online | Anslutna |
| `presence.offline` | Offline | Frånkopplad |
| `githubPublication.effectPullRequest` | pull request | pull-begäran |
| `githubPublication.target` | Pull request: {repository} → {base} | Pull-begäran: {repository} → {base} |
| `chat.pullRequests.empty` | No pull requests yet. | Inga pull-begäranden ännu. |
| `profilePage.identity.prAttributionShort` | Appends this link to new pull requests: | Lägger till den här länken i slutet av nya pull-begäranden: |
| `chat.pullRequests.actions` | Actions for pull request {reference} | Åtgärder för pull-begäran {reference} |
| `chat.pullRequests.dismiss` | Dismiss pull request {reference} | Avfärda pull-begäran {reference} |
| `chat.pullRequests.ciSummaryMany` | {count} pull requests with CI: {parts} | {count} pull-begäranden med CI: {parts} |
| `chat.pullRequests.ciSummaryOne` | 1 pull request with CI: {parts} | 1 pull-begäran med CI: {parts} |
| `githubConnections.agentsHelp` | Publish PR | publicera pull-begäranden |
| `chat.pullRequests.linkLabel` | Pull request {reference}: {title} | Pull-begäran {reference}: {title} |
| `chat.pullRequests.countOne` | 1 pull request | 1 pull-begäran |
| `profilePage.identity.prAttributionDescription` | Appends this link to new pull requests. | Lägger till den här länken i slutet av nya pull-begäranden. |
| `chat.activityPills.publication.review` | Review pull request publication on GitHub | Granska publiceringen av en pull-begäran på GitHub |
| `profilePage.identity.prAttribution` | Add OpenClaw attribution to pull requests | Lägg till ett omnämnande av OpenClaw i pull-begäranden |
| `updates.page.lastCommitAt` | Last commit | Senaste incheckning |
| `aboutPage.copyBuild` | Copy version and commit | Kopiera version och incheckning |
| `aboutPage.commit` | Commit | Incheckning |
| `aboutPage.copiedCommit` | Commit hash copied | Hash för incheckning kopierad |
| `aboutPage.copyCommit` | Copy full commit hash | Kopiera fullständig hash för incheckning |

De delade segmenten omfattar bland annat appens stödlänk, inställningar för
automatiskt läge, färdigheter i agenter, chatt och inställningar samt den
populära kategorin i tilläggskatalogen. De omfattar också beskrivningen av
ändringsverktyget, texten om heartbeat-övervakning och ordvalet för Git-
incheckningar samt närvarolistan och frånkopplad-statusen. Källan och
översättningen finns i `ui/src/i18n/.i18n/sv.tm.jsonl` i upstream-PR:n.

Kontroller som passerar: JSONL-parsning, Hunspell-sv, svlang, diffkontroll och
en fokuserad Gitleaks-kontroll av ändringarna. `l10n-lint` stöder inte detta
översättningsminnes JSONL-format och räknas därför inte som en passerad
kontroll. PR:n behöver fortfarande skärmbildsbevis från ett byggt svenskt
Control UI före merge.

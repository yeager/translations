# OpenClaw Native – svenska systemetiketter

Datum: 2026-11-15  
Upstream: [PR #199519](https://github.com/openclaw/openclaw/pull/199519)

Trettionio synliga systemetiketter i den svenska katalogen för Android och Apple-
apparna har granskats i källkodens användningssammanhang och uppdaterats.

| Segment | Engelska | Svenska |
| --- | --- | --- |
| `native.android.138ab14214d42c03` | Code Execution | Kodkörning |
| `native.android.5e87ca897023dc65` | Plugins | Tillägg |
| `native.android.63c3956ad510fe1e` | COMMIT | INCHECKNING |
| `native.android.d4fae140d4d1dabe` | Online and ready | Ansluten och klar |
| `native.apple.7625e3594d0ea81d` | Online for | Ansluten i |
| `native.apple.7891827948836f43` | Online · Idle | Ansluten · Inaktiv |
| `native.apple.946bdee25ed9b91a` | Online · Active | Ansluten · Aktiv |
| `native.apple.c7752044b02389cb` | Offline — turn it on to continue | Frånkopplad — slå på den för att fortsätta |
| `native.apple.8ed2f28696ae9ce7` | Get support | Få stöd |
| `native.android.58020f117fba52cb` | camera list | Kameralista |
| `native.android.8da8c80a72399f1a` | camera PTZ | PTZ-kamera |
| `native.android.a479b236e0ea5d98` | Presence | Närvaro |
| `native.android.9ca4a48091ddbbb1` | Sub-agent | Underagent |
| `native.android.1bdc5e3a158dbefe` | channel | kanal |
| `native.android.3f949b4dab96a2a8` | edit | redigera |
| `native.android.1fe779d8ad41ff7d` | emoji list | emojilista |
| `native.android.680f68fa7bbec4c8` | event create | skapa händelse |
| `native.android.4e36da9d176996cb` | poll | omröstning |
| `native.android.9138e82a0b3c6043` | present | presentera |
| `native.android.67b20f6603de4ecf` | reactions | reaktioner |
| `native.android.3a2e7c2ffac91d66` | sticker | klistermärke |
| `native.android.ba0ac53bdaa0a06a` | stop | stoppa |
| `native.android.3eb1dd47a3669d49` | tabs | flikar |
| `native.android.9127900aaed99dcc` | thread create | skapa tråd |
| `native.android.93b0779b3b292e8d` | wake | väck |
| `native.android.8c1c9792173e00db` | `$online/${summary.nodes.size} online` | `$online/${summary.nodes.size} anslutna` |
| `native.android.b5022307c878a3cb` | `$onlineNodes of $nodeCount online` | `$onlineNodes av $nodeCount anslutna` |
| `native.android.fc351549e1c62e03` | `$onlineNodes online` | `$onlineNodes anslutna` |
| `native.apple.7ea4001cda9c17da` | offline | frånkopplad |
| `native.apple.8af3455dfc1e92b6` | online | ansluten |
| `native.apple.3d179a5633fd4a50` | Gateway is offline | Gateway är frånkopplad |
| `native.apple.e018ebb26dbe4fc5` | Gateway is online | Gateway är ansluten |
| `native.apple.4b1707775e3d4ded` | Watch node is online | Klocknoden är ansluten |
| `native.apple.b96c69383bb1ea99` | AI agent online | AI-agent ansluten |
| `native.android.3ddf963e90bc6292` | Copy patch | Kopiera ändringen |
| `native.android.4e004c74d37ebc21` | Large diff: some files or patches were omitted… | Omfattande ändringsjämförelse: vissa filer eller ändringar har utelämnats… |
| `native.android.6abc80a0a79a1ccb` | This file’s patch was truncated. | Ändringen för den här filen har kortats ned. |
| `native.android.8feaee691786066c` | No text patch available | Ingen textändring tillgänglig |
| `native.android.c149ec0ef7adff0b` | Apply Patch | Tillämpa ändring |

Ordet *online* har ersatts endast i dessa statusetiketter, där användaren
behöver förstå anslutningsläget. Produktnamn, kodtermer och platshållare har
lämnats oförändrade. Tankstrecket i den sista raden behålls eftersom det finns
i källtexten. Verktygsnamnen använder svenska åtgärdsord och UI-termer.
`emojilista` är en avsiktlig svensk sammansättning som ännu inte finns i
Hunspell-sv.

Kontroller som passerar: JSON-parsning, Hunspell-sv för de nya orden, svlang
och Gitleaks. `l10n-lint` stöder inte hela den versionsstyrda inhemska JSON-
katalogen; dess syntaxvarning är därför ett verktygsbegränsning, inte ett
resultat från katalogens egen JSON-validering.

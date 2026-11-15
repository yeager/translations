# OpenClaw Native – svenska systemetiketter

Datum: 2026-11-15  
Upstream: [PR #199519](https://github.com/openclaw/openclaw/pull/199519)

Tretton synliga systemetiketter i den svenska katalogen för Android och Apple-
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

Ordet *online* har ersatts endast i dessa statusetiketter, där användaren
behöver förstå anslutningsläget. Produktnamn, kodtermer och platshållare har
lämnats oförändrade. Tankstrecket i den sista raden behålls eftersom det finns
i källtexten.

Kontroller som passerar: JSON-parsning, Hunspell-sv för de nya orden, svlang
och Gitleaks. `l10n-lint` stöder inte hela den versionsstyrda inhemska JSON-
katalogen; dess syntaxvarning är därför ett verktygsbegränsning, inte ett
resultat från katalogens egen JSON-validering.

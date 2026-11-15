# Avogadro – svensk status

Senast verifierad: 15 november 2026.

Avogadro är aktivt; avogadrolibs 2.1.0 publicerades 23 oktober 2026. Hosted
Weblate visar full svensk täckning: `avogadroapp` 237/237 och `avogadrolibs`
2 229/2 229, båda med 0 fuzzy-poster. Jämförelsen mellan de arkiverade
granskade PO-filerna från 19 september och de aktuella Weblate-exporterna
visar inga skillnader i översättningstext för gemensamma poster. Nyare
källsträngar har redan översatts upstream.

## Kontroller

`avogadroapp` passerar `msgfmt --check`. Appens sex Weblate-varningar har
granskats: två formatnamn ska vara oförändrade och de återstående träffarna
gäller korrekta acceleratorer eller termer som `3D-vy`.

`avogadrolibs` har en verklig `msgfmt`-varning i den aktuella Weblate-exporten:
den engelska texten *2% change* är markerad som C-format, vilket får
gettext att tolka `% c` som en platsmarkör. Den svenska formuleringen *2 % av
kamerans avstånd* kan inte matcha en sådan påstådd platsmarkör utan att bli
felaktig svenska. Detta är ett källflaggfel, inte en svensk översättning som
ska förvanskas. Övriga l10n-lint-träffar är främst produktnamn, acceleratorer,
pluralformer, HTML eller svensk meningsstruktur och kräver individuell
granskning innan ändring.

Gitleaks och `git diff --check` är godkända. Hunspell kördes inte eftersom
användaren har begränsat dess CPU-belastning. Ingen ny svensk översättning har
skapats eller skickats i denna återläsning.

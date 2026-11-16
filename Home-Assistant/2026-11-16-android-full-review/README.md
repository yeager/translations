# Home Assistant Companion for Android, svenska

Datum: 16 november 2026  
Källa: Home Assistant Companion for Android, Lokalise API  
Komponent: `android`  
Status: lokalt färdiggranskad och arkiverad. Inte uppladdad till Lokalise vid arkiveringstillfället.

`home-assistant-android-sv-20261116.delta.po` innehåller de 283 ändrade
strängarna från en radgranskning av komponentens 1 675 svenska poster. Den
kompletta råexporten finns kvar oförändrad i den lokala arbetskatalogen och
har inte kopierats hit som redigeringsunderlag.

Kontroller:

- `msgfmt --check`: godkänd.
- `l10n-lint`: 0 fel; 15 granskade varningar om bland annat lokalt anpassade
  exempel-URL:er, produktnamn, API-termer och medveten svensk interpunktion.
- `svlang`: undersökt; de flesta träffarna är falska positiva för korta
  gränssnittstexter och PO-escape-sekvenser. En verklig intervallform rättades.
- Projektets `hunspell-sv`: körd med sänkt prioritet och CPU-övervakning.
  Högsta observerade CPU var 0 procent. Okända token är främst produktnamn,
  protokoll och domäntermer.
- `git diff --check`: inga blankstegsproblem.
- `gitleaks`: inga hemligheter funna.

Den här arkivstatusen är inte ett påstående om att ändringarna är uppladdade,
godkända eller publicerade i Lokalise eller i en programrelease.

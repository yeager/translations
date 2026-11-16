# Music Assistant – svensk Lokalise-granskning

Senast uppdaterad: 16 november 2026

Arkivet innehåller svenska strängar för Music Assistant Server och Music
Assistant Mobile App. Varje katalog med ändrade strängar har eget underlag
med källtext, svensk måltext och uppgift om inskick eller återläsning.

## Verifierad status

- **Mobile App:** De fem senast granskade strängarna för insomningstimern är
  sparade och återlästa via Lokalise API. Den kontrollen omfattade alla 615
  svenska poster och visade 0 tomma och 0 oöversatta värden.
- **Desktop App:** De två sista dokumenterade tomma svenska strängarna är
  sparade och återlästa. Lokalises dåvarande filter visade 0 oöversatta
  svenska poster.
- **Server:** De åtta återstående ARD Audiothek-strängarna har granskats,
  sparats och återlästs via Lokalise API. En ny fullständig kontroll med
  korrekt svenskt språk-ID returnerar 0 oöversatta svenska strängar.

`msgfmt` är inte tillämpligt på Lokalises JSON-resurser. Respektive
strängarbete har kontrollerats med l10n-lint, svlang, Hunspell-sv,
diffkontroll och Gitleaks. En sparad eller återläst sträng är inte detsamma
som en verifierad programrelease.

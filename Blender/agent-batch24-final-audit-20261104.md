# Slutgranskning: Blender Manual batch 24 — länkning och tillägg

Granskad fil: `blender-manual-sv-review-batch-20261104-24.po`
Underlag: råexporten `blender-manual-manual-sv.po`, den dubbelgranskade
införandeplanen `agent-linkappend-batch-plan-20261104.md`, dess slutkontroll
och den lokala Blender UI-exporten från 2026-11-04.

## Resultat

Alla 22 poster godkänns. Varje källpost återfinns i råexporten vid den
angivna `link_append.rst`-referensen och varje måltext överensstämmer med
den godkända införandeplanen.

| Område | Bedömning |
| --- | --- |
| Menyvägar | Godkända. `Arkiv --> Länka...`, `Lägg till --> Samlingsinstans`, `Kontextmeny --> Datablock --> Flytta` och `Objekt --> Relationer --> Gör lokalt...` använder verifierade UI-former. |
| Länkning och tillägg | Godkända. `Länka`, `samlingsinstans`, `instanssamlingar`, `instansobjektdata`, `direkt länkad objektdata` och `direkt tillagd objektdata` har rätt funktionsbetydelse. |
| Bibliotek och datakällor | Godkända. `biblioteksåsidosättanden`, `Falsk användare`, `Flytta` och formuleringen om bibliotekets nya plats är tekniskt korrekta. |
| RST och kod | Godkända. Samtliga `:doc:`, `:ref:` och `:menuselection:` har oförändrade destinationsmål, och API-namn samt `blend` lämnas intakta. |
| Gör lokalt | Godkänd. Formuleringarna beskriver Blender-funktionens lokala datablock, inte språklokalisering. |

## Verktygskontroll

- `msgfmt --check`: godkänd.
- `l10n-lint`: 0 fel och 0 varningar.
- `git diff --check`: inga fel för Blender-ändringarna.
- `gitleaks detect --no-git --source`: inga hemligheter hittades.
- Hunspell-träffarna är RST-roller, API-identifierare, engelska `msgid` och
  etablerade Blender- eller USD-termer, inte svenska stavfel.
- `msgcmp` kan inte köras mot hela råexporten eftersom den exporten innehåller
  dubblettdefinitioner; de 22 referenserna kontrollerades därför var för sig
  mot råexporten.

Status: godkänd för att räknas in i den samlade, ännu ej uppladdade
manualbatchen.

# Bitwarden Browser och Desktop: Crowdin API-batch 37

Datum: 2026-10-29

Två nya Browser-strängar och fyra nya Desktop-strängar hämtades direkt från
Crowdins API. Samtliga granskades mot komponenternas befintliga svenska
terminologi, där `item` konsekvent är **objekt** och `Controlled access` är
**Kontrollerad åtkomst**.

## Kontroller före insändning

- `svlang skrivregler`: inga skrivregelfel.
- `l10n-lint`: inga fel i måltextkatalogerna.
- Hunspell-sv: endast den avsiktliga platshållaren `$COUNT$`.
- Platshållarparitet: godkänd; `$COUNT$` bevarad exakt.
- Scoped Gitleaks: inga fynd.

## API-insändning och återläsning

| Komponent | Projekt | Poster | Nya översättnings-id:n | Verifierad status |
| --- | ---: | ---: | --- | --- |
| Browser | 268134 | 2 | 1981041, 1981043 | 2 343 av 2 343 svenska strängar, 100 % översatt |
| Desktop | 299360 | 4 | 1981045, 1981047, 1981049, 1981051 | 2 178 av 2 178 svenska strängar, 100 % översatt |

Översättningarna skickades som vanliga, ogranskade Crowdin-förslag. De är inte
automatiskt godkända; Browser har 22 % och Desktop 24 % godkända strängar enligt
API:t vid återläsningen.

Den fullständiga, maskinläsbara batchen finns i
`bitwarden-browser-desktop-sv-crowdin-api-batch37-20261029.json`.

# RetroArch: Xemu, svensk status 2026-11-11

- Plattform: Crowdin, RetroArch, språk `sv-SE`, komponent `xemu-libretro.json` (fil-id `60535`).
- Avläst status: projektet är 99 % översatt och 34 % godkänt. Xemu-komponenten är 94 % översatt och har 65 återstående ord.
- Kvarvarande post: `XEMU_ASPECT_RATIO_INFO_0` (sträng-id `6232405`).
- Lokal deltafil: `retroarch-sv-xemu-aspect-ratio-20261111.po`.
- Terminologi: `TERMINOLOGY.md`.

Den svenska formuleringen är kontextgranskad. Alternativet *Auto* blir
*Automatiskt*, i enlighet med RetroArchs övriga svenska UI. `msgfmt --check
--check-header`, svlangs skrivregler och svengelskakontroll, diffkontroll och
Gitleaks är godkända. Hunspell-SV markerar endast `Chihiro`, `Widescreen`,
`bredbild` och `bredbildskorrigering`; de är produktnamn eller avsiktliga
facktermer. l10n-lint har inga fel och en varning från den engelska
källtextens `16-9`, inte från den svenska måltexten.

Ingen ändring har sparats i Crowdin. Vid den senaste åtkomstkontrollen saknades
den tidigare webbsessionen och Crowdin CLI saknade projektkonfiguration. När en
etablerad kanal åter är tillgänglig ska deltat sparas och den lagrade måltexten
läsas tillbaka exakt.

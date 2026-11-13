# Audacity: tonhöjdsförskjutning

- Datum: 2026-11-13
- Källcommit: `371828b`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 4 svenska PO-poster i Time Scale och fördröjningseffekten.

Batchen normaliserar substantivtermen *Pitch Shift* till **tonhöjdsförskjutning**. Källkodens kommentarer bekräftar att alternativen flyttar tonhöjden utan att ändra tempo. Den imperativa knappåtgärden **Ändra tonhöjd** berörs inte.

Kontroller: `msgfmt` (4 443 översatta poster), avgränsad Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks. Inga av verktygen träffar någon ändrad post.

# Audacity: molnkontots dialoger

- Datum: 2026-11-13
- Källcommit: `82bac37`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 7 svenska PO-poster för audio.com-konto, lagringsgräns och projektversionskonflikt.

Batchen använder **koppla konto** konsekvent, gör lagringsrådet konkret med ”frigöra utrymme” och beskriver tydligt vilken projektversion som ska förbli öppen. Efter en lyckad synkronisering sägs ändringarna synkroniseras **med molnet**, inte uppdateras ”till” molnet. Produktnamnet `audio.com` och den tekniska termen `token` lämnas oförändrade.

Kontroller: `msgfmt` (4 443 översatta poster), avgränsad Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks. Hunspell-sv markerar enbart `audio.com` och `audio.com-konto`. Varken l10n-lint eller svlang träffar någon ändrad sträng.

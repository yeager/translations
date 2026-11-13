# Audacity: spårjustering och fortsatt inspelning

- Datum: 2026-11-13
- Källcommit: `d762230`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 2 svenska PO-poster i spår- och transportmenyerna.

Batchen ersätter en bokstavlig och missvisande formulering för justering av spår ände mot ände. Den gör också kommandot *Append Record* till den naturliga uppmaningen **Fortsätt spela in**.

Kontroller: `msgfmt` (4 443 översatta poster), avgränsad Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks. Inga av verktygen träffar någon ändrad post.

# Audacity: samplingsbegrepp i benchmarkdiagnostik

- Datum: 2026-11-13
- Källcommit: `6911732`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 2 svenska PO-poster i benchmarkdiagnostiken.

Batchen använder **samplar** när en mängd digitala ljudvärden räknas och **samplingsvärde** för ett enskilt värde. Den tar därmed bort den kvarvarande engelska termen ”sample” utan att ändra formatplatshållare eller diagnostikens innebörd.

Kontroller: `msgfmt` (4 443 översatta poster), Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks. Hunspell-sv markerar endast C-formatplatshållarna `lld` och `.1f`. Varken l10n-lint eller svlang träffar någon ändrad sträng.

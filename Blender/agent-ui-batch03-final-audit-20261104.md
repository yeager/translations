# Slutgranskning: Blender UI batch 03

Granskad fil: `blender-ui-sv-review-batch-20261104-03.po`.
Underlag: UI-råexporten från 2026-11-04, kandidat- och
motgranskningsrapporterna för `Library Override` samt `TERMINOLOGY.md`.

| Källreferens | Bedömning | Resultat |
| --- | --- | --- |
| `BlendImportContextItem.library_override_id` | Godkänd | `Biblioteksåsidosättningen` följer närliggande UI-beskrivningar och är inte en operatörsetikett. |
| `IDOverrideLibrary.is_in_hierarchy` | Godkänd | `biblioteksåsidosättning` och `åsidosättningshierarki` är sakligt och terminologiskt sammanhängande. |
| `IDOverrideLibrary.is_system_override` | Godkänd | Samma termfamilj bevarar den tekniska hierarkibetydelsen och skiljer den från operatörsformen `biblioteksöverskrivning`. |

## Verktygskontroll

- `msgfmt --check`: godkänd.
- `l10n-lint`: inga fel eller varningar.
- `svlang skrivregler`: inga skrivregelfel.
- Hunspell-resten `åsidosättningshierarkin` är en korrekt facksammansättning;
  övriga träffar är PO-metadata, engelska källtexter eller API-identifierare.
- Gitleaks: inga träffar.
- `git diff --check`: inga fel för batchen.

Batch 03 kan arkiveras som lokalt slutgranskad. Den är inte uppladdad.

# Audacity: mittfrekvens i spektralredigering

- Datum: 2026-11-13
- Källcommit: `b0fc550`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 1 svensk PO-post i den parametriska spektralredigeringen.

Batchen gör feltexten konsekvent med övriga gränssnittet genom att använda **mittfrekvens** i stället för *centerfrekvens*.

Kontroller: `msgfmt` (4 443 översatta poster), avgränsad Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks. Hunspell-sv känner inte igen den tekniska sammansättningen *mittfrekvensen*; den etablerade termen **mittfrekvens** används redan i samma gränssnitt. Övriga kontroller träffar ingen ändrad post.

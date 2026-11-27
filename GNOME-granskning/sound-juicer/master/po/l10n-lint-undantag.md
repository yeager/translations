# l10n-lint-undantag — Sound Juicer/master/po

`l10n-lint --language sv --reference sound-juicer.master.latest.pot` gav 0 fel och 2 varningar:

- `02110-1301` är ZIP+4-postnumret i Free Software Foundations postadress; bindestrecket ska behållas och är inget talintervall.
- Singular- och pluralformerna för `Catalog No(s).` blir båda `Katalognummer: ` på svenska. Formen är identisk i singular och plural; avslutande blanksteg bevaras eftersom strängen följs av värdet.

Informationsnotiser om acceleratorer gäller avsiktligt flyttade ASCII-genvägar. Identiska metadataetiketter som `Artist` och `Genre` är etablerade svenska ord.

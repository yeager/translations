# PyPA Warehouse, svensk granskning

## Underlag

- Original: pypa-warehouse-sv (1).po
- Granskad arbetsfil: pypa-warehouse-sv-reviewed-complete-20261020.po
- Uppladdningsklar ändringsfil: pypa-warehouse-sv-reviewed-delta-20261020.po

## Resultat

| Kontroll | Resultat |
| --- | --- |
| Oöversatta singularsträngar | 0 |
| Oöversatta pluralsträngar | 0 |
| Fuzzy-strängar | 0 |
| msgfmt --check | Godkänd |
| Gitleaks | Inga läckor |
| l10n-lint | 0 fel, 10 varningar |

## l10n-lint-varningar

De återstående varningarna är inte översättningsfel:

- invariant svenska pluralform, till exempel projekt och underhållare
- intervall inuti kodtaggar, exempelvis a-z och 0-9
- avsiktliga ändringar av skiljetecken eller gränstecken när svensk meningsbyggnad och HTML-taggar kräver det
- en befintlig längdkvotsvarning för en kort rubrik

## Leverans

Ändringsfilen innehåller 1 078 uppdaterade poster: 1 061 singularer och 17 pluraler. Filen är inte skickad till någon extern översättningsplattform.

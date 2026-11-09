# Blender UI — enskild nyckelbildruta

Datum: 2026-11-09  
Katalog: `blender-ui-ui-sv (6).po`  
SHA-256: `7cbf644d990d1d648e91fa42b6ed214545661fc4e2db2dba461f49dbfd3a408f`

## Omfattning

51 enskilda former av *nyckelbild* kontrollerades i källkodshänvisning och
UI-sammanhang. De förekommer i animeringsverktyg, Graph Editor,
färgtemainställningar, NLA och Grease Pencil.

## Beslut

Alla 51 poster avser Blenders tekniska keyframe-objekt. De använder därför
**nyckelbildruta** respektive **nyckelbildrutan**. Detta omfattar även den
korta källformen *key* när API- eller kodkontexten visar att den betyder en
keyframe.

Sammansättningar som *nyckelbildskant*, *nyckelbildsstatus* och
*nyckelbildskalningsfaktor* granskas separat, eftersom de kan vara etablerade
kompakta etiketter där en direkt utvidgning skulle försämra läsbarheten.

## Kontroll

Deltafilen har 51 poster utan fuzzy-markeringar. `msgfmt`, l10n-lint,
svlang, konsistenskontroll och Gitleaks passerade. Hunspell-sv markerar
projektnamn, NLA-termer, metadata och källidentifierare, men inga svenska
stavfel i de ändrade måltexterna. Dokumentet bekräftar lokal granskning, inte
en import i Blender Translate.

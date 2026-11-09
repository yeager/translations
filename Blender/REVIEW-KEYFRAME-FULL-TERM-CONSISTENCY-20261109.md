# Blender UI — keyframe och keyframing

Datum: 2026-11-09  
Katalog: `blender-ui-ui-sv (6).po`  
SHA-256: `7cbf644d990d1d648e91fa42b6ed214545661fc4e2db2dba461f49dbfd3a408f`

## Omfattning

90 poster med den korta svenska formen *nyckelbild* har granskats i sitt
konkreta animeringssammanhang. De finns i Graph Editor, Dope Sheet,
inställningspaneler, NLA, Grease Pencil och meddelandetexter.

## Beslut

När källtexten avser den enskilda animeringspunkten eller flera sådana är
termen **nyckelbildruta**. Den ersätter *nyckelbild* med rätt böjning i
samtliga 90 poster. Det gäller även då källtexten skriver *keys*, eftersom
den koden och de intilliggande hjälptexterna avser keyframes.

Två panelrubriker avser i stället arbetsflödet: *Keyframing* blir
**Nyckelbildsättning**, och *Keyframing Settings* blir *Inställningar för
nyckelbildsättning*. Preferensåtgärden *Zoom Keyframes* får den idiomatiska
etiketten *Zooma in på nyckelbildrutor*.

## Kontroll

Deltafilen innehåller 90 poster utan fuzzy-markeringar. `msgfmt`, l10n-lint,
svlang, konsistenskontroll och Gitleaks passerade. Hunspell-sv:s relevanta
träffar är tekniska projektsammansättningar och egennamn, bland annat
*Bézier-nyckelbildrutor*. Detta dokumenterar lokal kvalitetssäkring, inte en
bekräftad import i Blender Translate.

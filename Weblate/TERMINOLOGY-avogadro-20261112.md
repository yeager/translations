# Avogadro, svensk terminologi

Källa: Avogadro-komponenterna `avogadroapp` och `avogadrolibs` i Hosted
Weblate, granskning och komplettering 2026-11-12.

| Engelskt begrepp | Rekommenderad svenska | Kontext och undantag |
| --- | --- | --- |
| atom index | atomindex | Skrivs ihop i valideringsmeddelanden. API-fält och kodnamn som `index` lämnas oförändrade. |
| atomic number | atomnummer | Kemisk uppgift i UI och API-dokumentation. |
| bond | bindning | Kemisk bindning. Fältnamnet `bondTo` lämnas oförändrat. |
| bond order | bindningsordning | Fältnamnet `bondOrder` lämnas oförändrat. |
| coordinate set | koordinatuppsättning | I navigering mellan strukturers bildrutor. |
| critical point | kritisk punkt | I QTAIM-relaterade sökningar; precisera med nukleär eller bindnings- vid behov. |
| dihedral angle | dihedralvinkel | Används tillsammans med torsion i programmet. JSON-fältet `dihedral` lämnas oförändrat. |
| electron density | elektrondensitet | |
| force field | kraftfält | |
| geometry constraint | geometrisk begränsning | API-begrepp. Fält som `constraints` och `value` lämnas oförändrade. |
| lattice / unit cell | gitter / enhetscell | `spaceGroup` är ett API-namn. Den beskrivande termen är rymdgrupp. |
| renderer | renderare | Felmeddelanden och bildexport. |
| rendering | rendera / renderad | Verb respektive particip. |
| supersampling | supersampling | Namnet på renderingsinställningen behålls som etablerad teknisk term. |
| virtual trackball | virtuell styrkula | Navigeringshjälp. |
| zero-based | nollbaserad | Indexering i API-dokumentation. |

## Kod och format

Produktnamn, filformat, program och API-identifierare översätts inte:
`PDB`, `PLY`, `OpenGL`, `ffmpeg`, `avconv`, `addAtom`, `atoms`, `bondTo`,
`bondOrder`, `color`, `element`, `hallNumber`, `position`, `spaceGroup` och
`value`. Bevara JSON-syntax, citattecken, platshållare, radbrytningar och
tabbar exakt.

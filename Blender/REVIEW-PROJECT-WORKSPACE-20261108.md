# Blender UI – granskning av projektarbetsytan (2026-11-08)

## Omfattning

15 (ej generiska dubbletter) svenska UI-strängar i Blenders projektarbetsyta
granskades mot källhänvisningarna i `space_project`, framför allt
`project_ops.cc` och `space_project.py`. Funktionen skapar och öppnar ett
Blender-projekt: en katalog med gemensamma inställningar, `.blend`-filer,
resursbibliotek och projektkonfiguration.

## Resultat

Samtliga kontrollerade strängar är idiomatiska och korrekta. Ingen deltafil
skapades, eftersom en import med identiska strängar endast skulle hoppas över.

| Engelsk term eller meddelande | Svensk översättning | Bedömning |
| --- | --- | --- |
| Project Root Folder | Projektrotmapp | Korrekt sammansättning för projektets rotkatalog. |
| Artwork | Bildmaterial | Korrekt i projektskapandets katalogindelning. |
| Create a new project … | Skapa ett nytt projekt … | Korrekt instruktion. |
| Overridden by the environment variable | Åsidosätts av miljövariabeln | Korrekt teknisk term. |
| Folder already contains/is inside/part of a project | Mappen innehåller redan … / ligger i … / ingår redan … | Korrekt och tydligt. |
| Asset Libraries | resursbibliotek | Följer Blender-terminologin. |
| Untitled Project | Namnlöst projekt | Korrekt. |
| Invalid project root folder | Ogiltig projektrotmapp | Korrekt. |
| Failed to create/write/load | Det gick inte att skapa/skriva/läsa in | Idiomatiska felmeddelanden. |

## Kontroller

- Källkontext kontrollerad i Blender-koden.
- Ingen ändring av översatt text; därför finns ingen importfil för denna
  kontrollgrupp.

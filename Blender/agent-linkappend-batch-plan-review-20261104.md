# Slutkontroll: Blender Manual — `link_append.rst`

Underlag: `agent-linkappend-batch-plan-20261104.md`, råexporten
`blender-manual-manual-sv.po` och UI-katalogen `blender-ui-ui-sv.po` från
2026-11-04.

## Resultat

Alla 22 poster i införandeplanen har verifierad källpost i råexporten och
kan föras in i en deltafil. De tidigare avvisade kandidaterna finns inte
med. För varje post har RST-rollerna och deras destinationer kontrollerats
mot källan.

| Område | Slutbedömning |
| --- | --- |
| Menyvägar | Godkända: `Arkiv --> Länka...`, `Lägg till --> Samlingsinstans`, `Kontextmeny --> Datablock --> Flytta` och `Objekt --> Relationer --> Gör lokalt...` följer UI-katalogen. |
| Outliner och filbläddrare | Godkända: `Blender-fil`, `Filbläddrare` och `Ladda om` är belagda svenska UI-former. |
| Länkning och tillägg | Godkända: `Länka`, `samlingsinstans`, `instanssamlingar`, `instansobjektdata`, `direkt länkad objektdata` och `direkt tillagd objektdata` återger respektive funktion utan att ändra mekaniken. |
| Bibliotek | Godkända: `biblioteksåsidosättanden`, `Falsk användare`, `Flytta` och formuleringen om att ange bibliotekets nya plats är semantiskt riktiga. |
| Lokalisering i Blender-betydelse | Godkända: `Gör lokalt`, `göra objektens beroenden lokala` och `göras lokala` avser datablockens lokala kopior, inte språklokalisering. |

## Avgränsning

Följande ska fortfarande inte tas med: den felaktigt angivna fristående
källposten vid `link_append.rst:103` och konkurrerande formuleringar som
inte har en exakt UI- eller råexportbeläggning. Införandet ska endast använda
de 22 `msgstr`-värdena i införandeplanen och därefter valideras med hela
verktygskedjan.

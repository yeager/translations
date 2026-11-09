# Blender UI — granskning av renderings- och återgivningsterminologi

Datum: 2026-11-09  
Katalog: `blender-ui-ui-sv (6).po`  
SHA-256: `7cbf644d990d1d648e91fa42b6ed214545661fc4e2db2dba461f49dbfd3a408f`

## Omfattning

39 ändrade poster med *render* eller *rendering* i källtexten har
radgranskats mot sina Blender-API-sammanhang. Granskningen avser både
operatorer och tekniska hjälptexter för Cycles, EEVEE, kompositören,
videosekvensredigeraren och färghantering.

## Terminologiskt beslut

**rendera**, **rendering**, **renderad** och **renderingsresultat** används
när Blender beräknar eller producerar bildresultatet. Det gäller bland annat
renderingspass, renderingstid, renderingscache och renderingsintervall.

**återges** används däremot när en redan existerande volym eller bild visas
av en motor. Formuleringen om EEVEE Legacy beskriver just sådan visning och
är därför korrekt: den är inte ett undantag som ska spridas till vanliga
renderingsoperatorer. Inställningspanelen *Text Rendering* betecknar däremot
Blenders funktion för att rendera text och skrivs därför **Textrendering**,
inte *Textåtergivning*.

## Slutsats

Den enda ändringen är den lokala UI-deltan för **Textrendering**. Två poster som
berör sekvensredigeraren finns i lokala deltafiler från tidigare granskning:
*sekvensredigerarscen* och frasen *remsor i sekvensredigeraren*. De ska
importeras från den aktuella samlade deltafilen, inte skrivas om i den lokala
källexporten.

Detta dokument bekräftar lokal granskning; det bekräftar inte en Weblate-
import.

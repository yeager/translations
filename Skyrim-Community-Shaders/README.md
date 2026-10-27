# Skyrim Community Shaders: svensk portningsbas

Den aktuella grenen `dev` i `community-shaders/skyrim-community-shaders`
granskades den 27 oktober 2026 vid commit
`064d124ab70095e10cb22847e9e03a2a643c9f0c`. Projektet har ingen svensk
översättningskatalog.

`skyrim-community-shaders-sv-port-20261027.json` innehåller endast säkert
återanvändbara strängar från Open Shaders: en gemensam nyckel tas med när den
engelska källtexten är identisk i båda projekten och den svenska texten redan
är lokalt granskad. Resultatet är 2 132 svenska strängar.

Av 3 818 översättningsbara engelska källnycklar är 2 814 textmässigt identiska
med Open Shaders, 118 har ändrad engelsk källtext och 886 saknas helt i Open
Shaders. Bland de identiska nycklarna saknar 681 en befintlig svensk text.
En ytterligare tidigare arkiverad text avviker i formatmarkör och har lämnats
utanför porten. De 1 686 återstående nycklarna behöver därför radvis
översättning eller granskning innan en
komplett `sv.json` och en upstream-PR kan skapas.

Denna portningsbas är inte uppladdad eller skickad upstream. Den är kontrollerad
mot Community Shaders-källan; varje efterföljande delta ska kontrolleras mot
samma gren före en PR.

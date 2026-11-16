# Cataclysm-DDA: aktiviteter, tillverkning och träning, batch 18

Denna batch har 25 sammanhängande strängar i `src/activity_actor.cpp`:
lådor och dörrar, kassaskåp, montering och tömning av utrustning,
tillverkningsarbeten samt träningsintensitet.

**Kontroller:** samtliga platshållare är bevarade, `l10n-lint` har inga fynd,
och Gitleaks samt `git diff --check` passerar. Hunspell-SV träffar endast den
avsiktliga spelplatshållaren `<npcname>`. svlangs tre V2-träffar är falska
positiva i grammatiskt korrekta satser.

**Uppladdning:** 25 måltexter sparades via Transifex API. Varje post
återlästes med `GET` och matchade den granskade måltexten, 25 av 25.

Källkontroll av `activity_actor.cpp` visade senare att en platsmarkör står för
ett objektnamn utan artikel. Texten för det för stora föremålet omformulerades
för att undvika både obestämd form och felaktigt genus, och återlästes efter
uppdateringen.

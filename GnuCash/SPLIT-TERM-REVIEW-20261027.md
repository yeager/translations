# GnuCash: termgranskning av `split` 2026-10-27

GnuCash använder `split` som ett fackbegrepp för en av flera delar i en
transaktion. Projektets egen svenska ordlista i `gnucash-glossary-sv.po`
anger uttryckligen `split` → `split` med förklaringen ”One of the two or
several parts a transaction is divided into”. Samma ordlista översätter dock
`split transaction` till `delad transaktion`.

Den aktuella katalogen använder flera kontextberoende former: `delning`,
`del`, `transaktionsdel` och `split`. Exempelvis är den kontextmärkta
fallbakstexten i `Split.cpp` översatt till `Delning`, medan söktypen i
`dialog-search.c` har `Split` som källtext och i nuläget svensk måltext
`Delar`. Källkoden använder också respektive etikett för att skapa den
separata texten `New Split`.

Det finns alltså inget stöd för en mekanisk massändring till vare sig
`delning` eller `split`. De tre berörda avvikelserna har därför lämnats utanför
59-postersdeltat:

- den kontextmärkta `Split`-etiketten för en flerpartsstransaktion;
- söktypen `Split`;
- den längre texten om en dold mål-`split`.

`Delning` är en möjlig svensk benämning i den första kontexten, men är inte
bevis för att samma ord fungerar i sökgränssnittet eller i registerrader.
`Destinations-spliten` är däremot en olämplig blandform och ska inte återföras.
En ändring av dessa tre kräver att GnuCash fastställer vilken av sina egna
ordliste- och katalogkonventioner som ska gälla.

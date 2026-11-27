# GIMP Help — master — toolbox — svenska

- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/gimp-help/master/toolbox/sv/>.
- Källor hämtade direkt från GNOME den 2026-11-27; senaste POT skapades 2026-11-24 22:42 UTC. POT-storlek 90 289 byte, SHA-256 `230e60b5f356f4bda5fda4382f43dab6c86db2214fef5037fe361a237813cf9c`.
- Senaste PO på servern: 155 814 byte; Last-Modified 2026-11-24 22:42:57 GMT; SHA-256 `b53cd9b57325a710326bc5faf018ea5718f716a62420f61a7705aae824c1d452`.
- Upstream före granskningen var 28/42/408 av 478 PO-poster. Aktivitetssidan visar uppladdningen 2026-11-27 18:00 UTC med ”Granskad och klar” och sammanslagen fil 478/0/0; statistikpanelen visar ännu cachade 28/42/408.
- Genomgång: alla 428 användarvisade strängar i senaste POT radgranskades. 368 nya översättningar lades till, 32 fuzzy/befintliga texter rättades och 28 befintliga översättningar behölls. Resultat: 428/428 användarvisade strängar översatta, 0 tomma och 0 fuzzy. PO-diffen omfattar 400 ändrade översättningsposter.
- POT-filen innehåller dessutom 50 `@@image:`-poster. Källkommentaren säger uttryckligen att deras textvärde inte används; de hålls tomma och undantas från översättningskravet. De 10 upstream-fuzzy-markeringarna på sådana poster är borttagna i den lokala granskade filen. Bildfilerna har inte bildredigerats.
- Terminologi kontrollerades mot GIMP:s befintliga svenska UI och `swedish-tm`; TM-träffar användes som underlag och verifierades i sammanhang. `Miter` använder den etablerade GIMP-etiketten **Spetsig**.
- Översättarmetadata: Daniel Nylander <gnome@danielnylander.se>, 2026-11-27.
- GNOME-inskick: 2026-11-27 18:00 UTC via Damned Lies API; aktivitetssida och sammanslagen fil verifierar 478/0/0.

## Validering

- `msgfmt --check`: godkänd.
- `msgcmp`: godkänd för hela PO:n, inklusive exakt synkroniserade `@@image:`-poster.
- `l10n-lint --language sv --reference <senaste POT> --disable source-equals-translation`: 0 fel, 0 varningar och 15 informationsnotiser om gränstecken runt giltig XML-markup. Regeln stängdes av enbart för de 50 källmarkerade metadataenheterna vars `msgstr` avsiktligt kopierats från `msgid`; `missing-translation` var aktiv och inga tomma poster återstod.
- Egen kontroll: 0 saknade synliga texter; exakt POT-täckning; 0 avvikelser i XML-taggar, länkmål, platshållare, formateringsmarkörer och DocBook-placeholders.
- Hunspell-SV 2026.11.27: varningar kontextgranskade; undantag finns i [hunspell-undantag.md](hunspell-undantag.md). Inga stavfel återstår.

## Uppladdning 2026-11-27

Inskickad via Damned Lies API 2026-11-27 18:00 UTC med kommentaren **Granskad och klar**. Senaste POT hämtades på nytt 2026-11-28 och är byte-identisk med granskningsbasen (SHA-256 `230e60b5f356f4bda5fda4382f43dab6c86db2214fef5037fe361a237813cf9c`). Aktivitetssidan och sammanslagen fil bekräftar 478/0/0 och exakt matchning med den granskade filen; statistikpanelen visar ännu 28/42/408.

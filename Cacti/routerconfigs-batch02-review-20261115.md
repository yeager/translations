# Cacti RouterConfigs, svensk granskningsbatch 02

Datum: 2026-11-15  
Källa: `cacti/routerconfigs`, svensk Weblate-export efter batch 01  
Omfattning: 25 tidigare tomma strängar

## Inriktning

Batchen omfattar återstående beskrivningar av schemaläggning, säkerhetskopiering, diffar och sekretessmaskning. Kommandon, produktnamn, reguljära uttryck, avgränsare, HTML-entiteten `&lt;secret hidden&gt;`, `&lt;CR&gt;`, platshållarna `%d` och `%s` samt Cisco- och NX-OS-strängarna har bevarats.

## Granskningsbeslut

- *Backup* är konsekvent översatt till *säkerhetskopia* eller *säkerhetskopiering* beroende på satsens funktion.
- `diff`, `TFTP`, `SNMP`, `PEM`, `base64`, `Any Key`, `(changed)` och konfigurationsnycklar har lämnats oförändrade där de är tekniska identifierare eller synlig programtext.
- `Monthly on Day`, `Rerun Every`, `No Change` och övriga valbara UI-värden återges med samma svenska benämningar som i batch 01 eller med en uttrycklig svensk referens.
- Varningen om hemliga värden behåller säkerhetsinnebörden: de lagrade säkerhetskopiorna ändras inte och avmaskning är avstängd som standard.

## Kontroller

- `msgfmt --check`
- `l10n-lint`
- `svlang`
- `hunspell-sv`
- `git diff --check`
- `gitleaks detect --no-git --source … --redact`

Resultat och eventuella kontextberoende undantag dokumenteras efter valideringen.

## Valideringsresultat

- `msgfmt --check`: godkänd. Deltafilens avsiktligt minimala huvud saknar revisionsmetadata, vilket bara ger standardvarningar och inte påverkar import eller formatvalidering.
- `l10n-lint`: inga fel. Varningen för `y/n` är en falsk positiv eftersom `Save \\[y/n\\]` är ett ordagrant reguljärt uttryck i ett exempel och måste behållas.
- `svlang`: tekniska identifierare, konfigurationsnycklar, reguljära uttryck, `%d`, `%s` och långa källstyrda säkerhetsbeskrivningar ger väntade falska positiva träffar. Svensk ordföljd och betydelse har granskats manuellt.
- `hunspell-sv`: inga ord att rapportera efter filtrering av tekniska identifierare och källkodsliknande exempel.
- `gitleaks`: godkänd.
- `git diff --check`: godkänd.

## Upstreamstatus

Uppladdad till Cacti Weblate 2026-11-15 med läget **Lägg till som översättning** och konfliktregeln **Ändra endast oöversatta strängar**. Weblate bekräftade: 25 bearbetade, 0 hoppade över, 0 saknade och 25 uppdaterade strängar.

Efter importen är 368 av 381 strängar översatta. De 13 återstående är sedan tidigare markerade som *behöver åtgärdas* och behandlas i en separat granskningsbatch, så de befintliga översättningarna inte skrivs över av misstag.

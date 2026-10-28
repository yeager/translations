# Postorius: rollmeddelanden

Kontrollerad 2026-10-27 mot den aktuella svenska Postorius-exporten från
Hosted Weblate. Komponenten är helt översatt, med 664 av 664 aktiva
strängar.

De femton källsträngarna i
`postorius-sv-role-messages-pending-20261026.po` finns inte längre i den
aktuella katalogen. Det gäller bland annat `List Owners`, `List Moderators`,
`List Members` samt motsvarande knappar och tommeddelanden. Filen kommer från
en äldre källrevision och får inte laddas upp, eftersom Weblate då skulle
rapportera saknade strängar eller försöka återinföra föråldrad text.

Ingen ny import behövs för denna fil. Följ i stället nya källsträngar i
Postorius och granska de tio avfärdade kontrollerna i sin aktuella kontext.

## Uppströms i18n-rättning 2026-10-29

Samma problem kvarstår i Postorius aktuella `master`: rollnamnet används för
att bygga engelska fraser dynamiskt, vilket gör dem omöjliga att anpassa
naturligt på svenska och andra språk. Den aktuella, fristående rättningen
`postorius-role-messages-i18n-20261029.patch` ersätter det med kompletta
översättningsbara fraser för ägare, moderatorer, medlemmar och icke-medlemmar.

Patchen bygger på `64d3c2bfc9350e1906c021f982f37c09162d62e4` från
27 oktober 2026. Berörd testfil passerar med 2 tester och 8 deltester.
Diffkontroll, Python-kompilering och en avgränsad Gitleaks-kontroll passerar.
Den lokala committen är `b473f064b9342afaec4a600a480dcdc40f24d0b4`.
En GitLab-merge request återstår eftersom denna miljö saknar en inloggad
GitLab-klient.

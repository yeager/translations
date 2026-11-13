# Slutstatus: Inkscape 1.4.x, svenska

Datum: 13 november 2026.

## Omfattning

- Komponent: `1-4-x/inkscape` på Inkscape Weblate.
- Katalogen innehåller 10 914 aktiva poster.
- 1 224 poster är unika jämfört med den färdiggranskade utvecklingsgrenen. Samtliga har granskats rad för rad; gemensamma poster har inte dubbelgranskats.
- De sista lokala ändringarna skickades i batcherna 1101-1200 och 1201-1224. Weblate accepterade 12 respektive 8 av 12 respektive 8 poster.

## Verifiering

- `msgfmt --check`: godkänd för deltabatcher och slutkatalog.
- `msgattrib --untranslated`: inga oöversatta aktiva poster.
- `l10n-lint`: 67 varningar, 0 fel. Varningarna gäller den befintliga pluralformeln, avsiktligt identiska produkt- och versionsnamn samt kända typografiska kontroller.
- `svlang consistency`: godkänd. `svlang check` gav två falska V2-träffar för korrekta svenska satser.
- `hunspell-sv`: träffar endast domänspecifika och korrekta ord: `Affinity-filer`, `dubblettnoder` och `importeraren`.
- `git diff --check` och Gitleaks: godkända.

## Upstreamstatus

Direktavläsning från Weblate den 13 november 2026 visar 10 913 av 10 913 poster översatta, 0 fuzzy-poster och 331 poster med fallerande Weblate-kontroller. De 331 kontrollerna är ett separat kvarvarande kvalitetsarbete och ska inte förväxlas med de lokala verktygsresultaten ovan.

Ett första urval om 50 poster är dokumenterat i [WEBLATE-CHECK-SAMPLING-1-4-20261113.md](WEBLATE-CHECK-SAMPLING-1-4-20261113.md). Urvalet visade inga verifierade språkfel; inga kontroller har avfärdats automatiskt.

Samtliga 331 kontrollträffar är därefter kategoriserade i [WEBLATE-CHECK-CATEGORIZATION-1-4-20261113.md](WEBLATE-CHECK-CATEGORIZATION-1-4-20261113.md). Kategoriseringen fann inga verifierade språk-, markup- eller platshållarfel.

## Status

Lokalt radgranskad, arkiverad, pushad till `yeager/translations`, uppladdad till Weblate och återläst. Weblates granskningsstatus är avstängd för komponenten, så inga poster kan märkas som granskade i tjänsten. Weblates kvarvarande kontrollvarningar är ännu inte kategoriserade eller åtgärdade.

# DuckStation: lokal språkgranskning, 27 oktober 2026

`duckstation-qt_sv-kvalitetsfixar-20261027.delta.ts` innehåller nio unika
ändringar från den svenska Qt-katalogens återstående lintträffar:

* två felsökningskommandon får svenska verb i stället för `patcha`;
* två texturtexter ersätter `flooring` och den talspråkliga formuleringen
  `fixa` med fackmässig svenska;
* två inställningstexter använder `maskinvaruåtergivare` och tar bort felaktigt
  kommatecken före `och`;
* HTML-hjälptexterna för renderarbyte och gränssnitt får svensk meningsbyggnad;
* Android-varningen delas upp i två meningar så att platshållaren `%1$s` och
  radbrytningarna bevaras utan kommateckenfel.

Den fullständiga lokala katalogen har dessutom sex kvarvarande varningar som
inte ändras automatiskt: tre med inledande blanksteg före en måttenhet, den
korrekta sammansättningen `Mappplatser`, en felträff på ordet
`efterbehandling` över en HTML-rubrik och brödtext, samt en styrelsespecifik
termfråga. Deltat duplicerar inte den tidigare 14-postersfilen.

Filen är lokal och ej uppladdad. Eftersom DuckStations katalog har fler än
1 000 strängar ska en kommande Weblate-import även fortsatt ske med små
deltafiler efter jämförelse mot aktuell måltext.

## Upstreamjämförelse

Den aktuella upstreamkatalogen i `master` hämtades 2026-10-27 och har
SHA-256 `ff2fe70be8b7a160fa27f9619ef3577c77cb276b797a573c848bb31e6352f2c0`.
Samtliga nio kontext- och källtextnycklar finns kvar och har en annan svensk
måltext uppströms. Inget av kvalitetsdeltats meddelanden har alltså redan
landat. En l10n-lint-informationsrad för den avsiktligt flyttade
kortkommandobokstaven i ”Ändra instruktion” är inte en varning eller ett fel.

## Kontrollresultat

XML-syntaxkontroll, l10n-lint och Gitleaks passerar utan fel eller varningar.
l10n-lints enda informationsrad beskriver den avsiktligt flyttade
kortkommandobokstaven i `Ändra instruktion`. Svlangs enda träff är engelska
källordet `performance` i TS-filens `<source>`; den svenska måltexten använder
`prestandamässig`. Hunspell fångar inga svenska rättningskandidater efter att
`renderare` har ersatts med `återgivare`.

## Uppföljning 2026-10-29

Deltat skickades därefter som en del av PR #3817. Den aktuella katalogen i
`master` innehåller samtliga nio måltexter exakt som i denna fil. Deltat är
därför inskickat och mergeverifierat.

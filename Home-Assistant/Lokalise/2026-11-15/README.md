# Home Assistant Core, Lokalise, svenska

Datum: 2026-11-15

De sparade batcherna `101`–`119` omfattar 276 fel- och skyddsetiketter för
Sofar-växelriktarens nätövervakning, kylflänsar, ingångssäkringar och
felinformation.

Lokalise API-sparningen har återlästs: samtliga 276 strängar är markerade som
översatta och inte overifierade. Arbetet är arkiverat i detta repo. Det finns
ingen verifierad upstream-granskning, merge eller publicerad Home Assistant-
release kopplad till batchen.

`msgfmt` är inte tillämpligt på Lokalise-JSON. JSON-, l10n-lint-,
svlang-, Hunspell-, diff- och Gitleaks-kontroller dokumenteras tillsammans med
batchens arkivering.

Den 16 november återställdes dessutom åtta enspråkiga poster med avsiktligt
tom engelsk källa från felaktiga värden “Tom” till tom svensk text via
Lokalise API. Värden med engelska *Empty* för behållare, nivåer och
förbrukningsmaterial har inte ändrats, eftersom *Tom* där är korrekt i sitt
sammanhang. Den efterföljande kontextgranskningen visade att 40
`state::off`-värden med engelska *Clear* felaktigt hade “Tom” eller “Tomt”.
De har uppdaterats till **Klar** via API. En ny full sökning över 74 606
svenska poster bekräftade att bara tio korrekta *Empty → Tom*-värden återstår.

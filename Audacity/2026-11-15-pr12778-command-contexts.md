# Audacity PR #12778: aktuella urvalskommandon

Datum: 2026-11-15

Den öppna upstream-PR:n [#12778](https://github.com/audacity/audacity/pull/12778)
uppdaterades i commit `f9601045b4ba29ca8742e803e04adf73ce372751`.

## Ändring

Audacitys aktuella registrering använder Qt-katalogens kontexter `command` och
`command_description`. Den svenska TS-katalogen innehöll bara äldre
`action`-poster. Fyra verkliga poster har därför lagts till:

- `Left of playback position` -> `Vänster om uppspelningsposition`
- `Right of playback position` -> `Höger om uppspelningsposition`
- Verktygstips för båda kommandona, med korrekt urvalsintervall.

## Verifiering

- Källkoden i `trackeditcommandsregister.cpp` kontrollerades för aktiv kontext.
- `xmllint --noout` godkänd.
- Qt `lrelease` skapade en QM-fil med 4 054 färdiga översättningar.
- Hunspell-sv gav inga träffar för de fyra nya svenska texterna.
- `git diff --check` godkänd.
- Gitleaks godkänd.
- l10n-lint kördes på helkatalogen och rapporterade historiska problem i
  befintliga poster. Inga av de fyra tillagda posterna rapporterades.
- svlang kunde inte avsluta en helkatalogskörning inom verktygets tidsgräns.

## Upstreamstatus

Ändringen är pushad och direkt återläst från PR-grenen. Den relevanta
CodeRabbit-tråden är löst. PR:n är fortfarande öppen och väntar på upstream-
granskning; den är inte mergead eller publicerad i en release.

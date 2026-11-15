# PCSX2, riktad svensk Crowdin-granskning 2026-11-15

## Underlag

- Projektets senaste release: v2.8.2, publicerad 2026-09-04.
- Granskad export: `pcsx2-qt_en_sv-SE.xliff` med 5 345 poster.
- Projektets etablerade översättningskanal är Crowdin.

## Resultat

Exporten innehöll äldre felaktiga måltexter för bland annat `Vulkan`, `B 1`,
`PC` och en sekundenhet. API-kontrollen visade att korrekta svenska alternativ
redan finns sparade för dessa strängar. De har därför inte skickats på nytt och
inga röster eller godkännanden har ändrats.

`Force Feedback` behölls oförändrat enligt projektspecifik terminologi.

En förbättring saknades som alternativ i Crowdin och skickades via API:

- `OSDFontPickerDialog`: tydligare instruktion för att välja en lokal
  teckensnittsfil, Crowdin-översättning 450297.

## Verifiering

- Crowdin API läste tillbaka den inskickade texten.
- XML-kontroll med `xmllint` passerade.
- Gitleaks passerade utan träffar.
- svlang passerade utan skrivregelfel.
- Hunspell-sv fann inga stavfel i den inskickade svenska texten.
- l10n-lint fann en känd falsk positiv för den tekniska strängen
  `%1x%2 (%3x)` och 50 äldre varningar i den kompletta exporten. Inga nya
  fel infördes av den inskickade ändringen.

## Upstreamstatus

Ändringen är inskickad direkt till Crowdin. Den är inte samma sak som en
upstream-merge eller en utgåva. De äldre felaktiga kandidaterna behöver
projektets ordinarie urvals- eller granskningsflöde för att sluta väljas vid
export.

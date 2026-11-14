# PCSX2: USB-etiketten B 1, 14 november 2026

Den nedladdade svenska XLIFF-exporten innehåller fortfarande en felkopplad
måltext för sträng `7213`, `USB['B 1']`: `Identifierad till konto:
<b>%1</b>`. Den korrekta UI-etiketten är `B 1`.

Deltafilen innehåller bara den strängen. XML-validering, l10n-lint, svlang,
lågprioriterad Hunspell-SV, diffkontroll och Gitleaks passerade. `msgfmt` är
inte tillämpligt på XLIFF.

## Upstream-resultat

Den 14 november 2026 skickades deltafilen till Crowdin-projekt `561203`, fil
`15`, språk `sv-SE`, med `importEqSuggestions` aktiverat och utan
autogodkännande. Importsvaret var 0 importerade, 0 godkända och 1 hoppad över
av QA som dubblett.

Ett direktförslag för samma sträng avvisades också som dubblett. API:t visar
att den aktiva måltexten fortfarande är den felkopplade texten och har status
`failed`. Det betyder att en identisk `B 1`-kandidat redan finns i projektet,
men att den inte är den aktiva översättningen. Ingen röst, godkännandeåtgärd
eller ändring av befintlig kandidat har gjorts. Detta är ett verifierat
upstream-inskick utan upstream-granskning eller aktivering.

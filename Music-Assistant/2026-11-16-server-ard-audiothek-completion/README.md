# Music Assistant Server: ARD Audiothek

Datum: 16 november 2026

Lokalise API visade åtta oöversatta svenska strängar i ARD Audiothek.
Källtexterna kontrollerades direkt mot projektets engelska basresurs. Orden
följer befintlig svensk terminologi: *uppdateringstoken*, *prenumeration*,
*lyssningshistorik* och *logga in*.

`accounts.ard.de` och platshållaren `{0}` är bevarade. JSON-struktur,
l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks körs mot den rena
kontrollfilen före inskick. `msgfmt` är inte tillämpligt på JSON-resursen.

Samtliga åtta strängar sparades via Lokalise API med `is_unverified: false`
och lästes sedan tillbaka med exakt samma måltext. En ny API-fråga med rätt
språk-ID och filtret `filter_untranslated=1` returnerar 0 svenska oöversatta
serversträngar. Detta bekräftar sparandet i Lokalise, inte en extern
granskning eller programrelease.

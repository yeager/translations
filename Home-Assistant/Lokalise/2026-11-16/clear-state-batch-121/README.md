# Home Assistant Core – Clear-tillstånd, batch 121

Datum: 2026-11-16

40 binärsensortillstånd med den engelska källtexten *Clear* hade felaktigt
översatts som “Tom” eller “Tomt”. Det förväxlar tillståndet *Clear* med
*Empty*. De normaliseras till **Klar**.

Berörda grupper är generiska binärsensorer, UniFi Protect, SmartThings och
Reolinks detektering av bland annat djur, ansikten, rörelse, paket, personer,
husdjur och fordon. De är alla `state::off`-värden, alltså tillstånd och inte
uppmaningar. Därför är verbformen “Rensa” inte lämplig här.

Status: alla 40 poster uppdaterades via Lokalise API och lästes tillbaka med
samma översättnings-ID:n. API:t bekräftar `is_untranslated: 0` och
`is_fuzzy: false` för varje post. Arkivposten är pushad till vårt arkiv; detta
är inte ett upstream-godkännande eller en release.

Kontroller: JSON, källtextens enhetliga betydelse, l10n-lint, svlang,
Hunspell, kontroll av tre identiska tecken i följd, diffkontroll och Gitleaks.
`msgfmt` är inte tillämpligt på JSON-kataloger.

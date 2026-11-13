# Audacity: molnsparandets val och status

- Datum: 2026-11-13
- Källcommit: `4ff4ba6`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 6 svenska PO-poster för molnsparande och synkronisering med audio.com.

Batchen skiljer konsekvent mellan att spara **i molnet** och **på datorn**, och ersätter det talspråkliga ”synkar” med statusformen ”synkroniseras”. Synlighetsnivån `Public` översätts till **Offentlig**, vilket är tydligt i projektets åtkomstinställningar. Produktnamnet `audio.com` lämnas oförändrat.

Kontroller: `msgfmt` (4 443 översatta poster), avgränsad Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks. Hunspell-sv markerar enbart produktnamnet `audio.com`. Varken l10n-lint eller svlang träffar någon ändrad sträng.

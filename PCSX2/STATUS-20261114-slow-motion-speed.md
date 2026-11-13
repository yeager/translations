# PCSX2: hastighet för långsam uppspelning, 14 november 2026

Sträng `6373` beskriver emuleringsinställningen för slow motion och dess
snabbtangent. Den tidigare måltexten blandade in engelska `slow-motion` och
saknade svensk sammansättning. Deltafilen använder projektets etablerade term
`långsam uppspelning` i både etikett och hjälptext.

Kontroller före inskick: XML, l10n-lint, platshållare, Hunspell-sv med sänkt
prioritet på endast den nya måltexten, svlang, diffkontroll och Gitleaks.
`msgfmt` är inte tillämpligt på XLIFF. Upstream-resultat dokumenteras efter
API-import och återläsning.

# PCSX2: VU1-hastighet, 14 november 2026

Sträng `11536` är hjälptexten för VU1:s omedelbara körning i avancerade
emuleringsinställningar. Den aktiva svenska texten delade felaktigt upp
sammansättningen `hastighetsförbättring` och återgav `modest` som `lagom`.
Den granskade formuleringen använder `måttlig hastighetsökning`, behåller VU1
som tekniknamn och behåller sakinformationen om möjliga grafiska fel.

Kontroller före inskick: XML, l10n-lint, platshållare, Hunspell-sv med sänkt
prioritet på endast den nya måltexten, svlang, diffkontroll och Gitleaks.
`msgfmt` är inte tillämpligt på XLIFF. Upstream-resultat dokumenteras efter
API-import och återläsning.

## Verifierat inskick

Crowdins API tog emot deltafilen för projekt `561203`, fil `15`, språk
`sv-SE`. Direkt återläsning för sträng `11536` bekräftar den nya ogranskade
kandidaten `450031` med exakt den arkiverade måltexten. Kandidaten är
inskickad upstream, men är inte upstreamgranskad eller vald som aktiv
översättning.

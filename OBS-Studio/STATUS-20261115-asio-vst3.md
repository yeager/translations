# OBS Studio, svensk lokaliseringsstatus 2026-11-15

- Releasekontroll: OBS Studio `33.0.1`, publicerad 2026-10-29.
- Källan innehåller 42 engelska instickskataloger. Före arbetet fanns svensk
  katalog i 38 av dem.
- Tre saknade kataloger hade synliga strängar: ASIO-utmatning, Windows ASIO
  och VST3. Den fjärde, macOS Virtual Camera, är tom även på engelska och
  behövde därför ingen katalog.

## Inskick

28 svenska strängar har skickats i PR
[obsproject/obs-studio#14209](https://github.com/obsproject/obs-studio/pull/14209):

- `plugins/asio-output-ui/data/locale/sv-SE.ini`
- `plugins/win-asio/data/locale/sv-SE.ini`
- `plugins/obs-vst3/data/locale/sv-SE.ini`

Katalogerna följer OBS befintliga svenska terminologi, inklusive `utmatning`,
`ljudspår`, `drivrutin`, `Sidechain` och `Läs in`. Alla nycklar jämfördes mot
respektive engelsk källkatalog.

## Kontroller

- `git diff --check` passerade.
- svlang passerade utan skrivregelfel.
- Gitleaks passerade utan träffar.
- Hunspell-sv markerade bara produkt- och facktermerna ASIO, VST3, Sidechain
  och `utmatning(ar)`.
- l10n-lint har inget stöd för OBS INI-format och kunde därför inte köras som
  katalogkontroll.

## Upstreamstatus

PR #14209 stängdes utan merge 2026-11-15. En projektmedlem bekräftade att OBS
hanterar alla översättningar via Crowdin. Katalogerna ska därför inte skickas
som GitHub-PR utan läggas in i Crowdin tillsammans med de övriga verifierade
svenska ändringarna. Ingen merge eller utgåva är verifierad.

# NxNative Launcher – svensk lokalisering

Senast uppdaterad: 2026-10-28

## Underlag

- Upstream: <https://github.com/rennan101/nxnative_Launcher>
- Granskad revision: `2cca1871ac6348878c2ca808e7b89cb4860d27be`
- Senaste upstreamändring: 2026-10-28. Projektet uppfyller därmed
  arkivets färskhetskrav på högst 48 månader.
- Arbetsgren: `l10n/swedish`, commit `cec4a72f539dfea1e2e8d325bf6f5e57ccf314c8`.
- Upstream: [PR #3](https://github.com/rennan101/nxnative_Launcher/pull/3),
  skickad 2026-10-28 och väntar på underhållargranskning.

## Leverans

Projektet hade ingen befintlig l10n-struktur. Leveransen lägger till
SwiftPM-resurser, `L10n`, `L10nText` och `L10nLabel`, så att framtida språk
enbart behöver få en egen `.lproj/Localizable.strings`-fil. Den svenska
katalogen innehåller 55 kontrollerade nycklar för navigering, bibliotek,
portningsflöde, kontroller, systemdialoger, loggar och personlig anpassning.

`Localizable.strings`, hjälpkoden, en lokaliseringsguide och
`check_localization.py` är arkiverade här som en exakt kopia av leveransen.

## Kontroller

- `swift build` – godkänd.
- `plutil -lint` – godkänd.
- `check_localization.py` – 55 använda nycklar finns i svenska katalogen.
- `l10n-lint --language sv` – godkänd utan anmärkningar.
- `svlang skrivregler` – godkänd utan anmärkningar.
- Hunspell-träffar granskade: `NxNative`, `Launcher`, `.app`, `.ipa`, `Xbox`
  och tekniska sammansättningar är avsiktliga.
- Gitleaks på den nya resurskatalogen – inga hemligheter.

## Återstår

Fler hårdkodade texter finns i sekundära vyer. De kan flyttas successivt till
samma katalog; denna första etapp introducerar inga engelska reservvärden för
de 55 berörda synliga texterna. Följ även PR #3:s CI och granskning.

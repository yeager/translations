# PCSX2, Crowdin-status 2026-11-15

- Källa: Crowdin-projektet `PCSX2 Emulator` (projekt `561203`), språk `sv-SE`.
- Versionskontroll: PCSX2 `v2.8.2`, publicerad 2026-09-04.
- Underlag: exporten `pcsx2-qt_en_sv-SE.xliff` med 5 345 poster.
- Resultat: den riktade kontrollen visade att flera äldre felaktiga måltexter
  redan har korrekta svenska alternativ i Crowdin. Inga dubbla förslag,
  omröstningar eller godkännanden ändrades.
- Inskickat via API: en tidigare saknad förbättring för
  `OSDFontPickerDialog`, Crowdin-översättning `450297`.
- Terminologi: `Force Feedback` är kvar på engelska enligt projektbeslutet.
- Kontroller: XML, svlang, Hunspell-sv för den inskickade texten och Gitleaks
  passerade. l10n-lint rapporterar en känd falsk positiv för den tekniska
  multiplikatorsträngen `%1x%2 (%3x)` samt äldre varningar i exporten.
- Upstreamläge: ändringen är inskickad till Crowdin och lästes tillbaka via
  API. Den är inte ett upstream-godkännande eller en utgåva; projektets
  ordinarie granskningsflöde avgör vilket sparat alternativ som väljs vid
  nästa export.

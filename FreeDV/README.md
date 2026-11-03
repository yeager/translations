# FreeDV 3.0.0-dev1 – svenska

Filen `freedv-3.0.0-dev1.sv.po` är en komplett svensk översättning av
Translation Projects förlaga `freedv-3.0.0-dev1.pot`.

Kontroller 2026-11-03:

- 571 av 571 meddelanden är översatta.
- `msgfmt --check` godkändes.
- Kontroll av C-formatmarkörer och radbrytningar fann inga avvikelser.
- FreeDV:s egna tekniska dokumentation och användarmanual användes för en
  domängranskning av radio-, CAT-, PTT-, VOX-, lokator- och ljudtermer.
- Katalogen kontrollerades i `l10n-lint` utan fel eller varningar. Kvarvarande
  informationsnotiser gäller avsiktligt identiska tekniska symboler, flyttade
  kortkommandon och svensk decimalnotation.
- FreeDV 2.4.1 startade på macOS med svensk språkbegäran, men den signerade
  appen innehåller endast den engelska lokaliseringen. Den kan därför inte
  vara ett runtimebevis för en 3.0.0-dev1-katalog utan att installera ett nytt
  språkpaket eller bygga utvecklingsversionen.
- Gitleaks hittade inga hemligheter i arbetskatalogen.

SHA-256: `687e68259a434224c64be7ce209513957843a0b2c29684f44ffdfed0b19b4fca`

Filen är avsedd att mejlas till Translation Project för granskning och
integrering.

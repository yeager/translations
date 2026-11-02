# ScummVM, svensk granskningssats 1 (2026-11-02)

- Omfattning: 39 UI-, spelstyrnings- och MIDI-strängar från huvudkomponenten
  `scummvm/scummvm`, exporterade när 167 strängar återstod.
- Arkiv: `scummvm-sv.batch-20261102-01.reviewed.delta.po`.
- SHA-256: `22c2a6b74ce9a83b708da35bab1b1d1056201b371363cf711d60252933e4b39d`.
- Kontroll: `msgfmt` passerar med enbart vanliga Weblate-huvudvarningar;
  l10n-lint, svlang och Gitleaks passerar.
- Upstream: importfilen är klar för Weblate. Ingen projekt-API-token fanns i
  nyckelringen vid arbetstillfället, så den ska importeras i den inloggade
  Weblate-webbplatsen innan satsen markeras som skickad.

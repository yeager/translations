# Luanti, svenska inbyggda kommandon, 13 november 2026

Luanti skiljer mellan motorgränssnittet i Weblate och den inbyggda komponenten
med servermeddelanden och kommandohjälp. Den här batchen fyller 26 svenska
poster i `builtin/locale/__builtin.sv.tr`: hjälptexter, behörighetslistor,
felmeddelanden och positionsformat.

Kontroller:

- varje källnyckel kontrollerad mot projektets aktuella `template.txt`
- kontroll av dubbletter och format: godkänd
- Hunspell-sv: godkänd; endast kommandosyntax och koordinatplatshållare markeras
- svlang: endast förväntade varningar för den bevarade kommandosyntaxen
- l10n-lint: stöder inte Luantis `.tr`-format
- diffkontroll: godkänd
- Gitleaks för deltat: godkänd

Upstream: inskickad som [Luanti PR #17754](https://github.com/luanti-org/luanti/pull/17754)
den 13 november 2026. PR:en är öppen och väntar på granskning; den är inte
mergad.

# Wildcard — main/po — svensk granskning

- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/wildcard/main/po/sv/>
- Granskad: 2026-11-23
- Aktuell POT: 64 aktiva strängar
- Nya översättningar: 0
- Korrigerade befintliga översättningar: 12

## Ändringar och validering

Tekniska hjälprader för reguljära uttryck, flaggor och snabbreferensen har
språkrättats utan att ändra regex-exempel eller platshållare. PO-rubriken
uppdateras med Daniel Nylander som senaste översättare.

`msgfmt --check` och `msgcmp --use-fuzzy` är godkända. `l10n-lint` rapporterar
0 fel och 0 varningar; den enda informationsnotisen gäller svenska citattecken
i en exempelsträng. Hunspell-undantag är bland annat `lookaround-konstruktioner`,
`Perl-stil` och `reguttr`.

Den granskade filen är komplett och fuzzy-fri. Ingen inskickning till GNOME
har gjorts i detta steg.

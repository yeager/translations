# Wildcard — main/po — svensk granskning

- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/wildcard/main/po/sv/>
- Ursprunglig granskning: 2026-11-23
- Riktad Hunspell-korrigering: 2026-11-27
- Aktuell POT: 64 aktiva strängar
- Nya översättningar: 0
- Korrigerade befintliga översättningar: 13 (netto jämfört med originalfilen)

## Ändringar och validering

Tekniska hjälprader för reguljära uttryck, flaggor och snabbreferensen har
språkrättats utan att ändra regex-exempel eller platshållare. Hunspell-kontrollen
upptäckte tre formuleringar med `nyrad`; de är ändrade till `radbrytningar`, och
bildtexten beskriver nu snabbreferensdialogrutan naturligt. PO-rubriken anger
Daniel Nylander som senaste översättare.

`msgfmt --check` och `msgcmp --use-fuzzy` är godkända. `l10n-lint` rapporterar
0 fel och 0 varningar; den enda informationsnotisen gäller svenska citattecken
i en exempelsträng. Hunspell markerar de tekniska uttrycken `lookaround-konstruktioner`,
`Perl-stil`, regexexemplet `ab` och regexfacktermerna `flerradsflaggan`,
`skiftlägesokänslighetsflaggan` och `unicode-flaggan`. De kontrollerades i
sammanhang; `name` och `group` är bokstavliga gruppnamn i regexexempel.
Undantagen dokumenteras därför i `hunspell-undantag.md` och ändras inte.
`l10n-lint` rapporterar 0 fel och 0 varningar; två informationsnotiser gäller
svenska citattecken där originalet saknar avslutande citattecken.

Den granskade filen är komplett och fuzzy-fri. Ingen inskickning till GNOME har ännu gjorts.

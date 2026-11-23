# Elastic — main/po — svensk granskning

- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/elastic/main/po/sv/>
- Granskad: 2026-11-23
- Aktuell POT: 64 aktiva strängar
- Nya översättningar: 0
- Korrigerade befintliga översättningar: 14

Hela katalogen är radgranskad mot senaste POT. Språk, UI-åtgärder och
fysikförklaringar är rättade till idiomatisk svenska. Kodspråk, libadwaita,
parametrar och formatsträngarna `%.2lf` och `%.0lf` är bevarade.

`msgfmt --check` och `msgcmp --use-fuzzy` är godkända. `l10n-lint` har inga
fel eller varningar; den enda informationsnotisen gäller en avsiktligt flyttad
och giltig ASCII-accelerator i `_Reset` → `Åte_rställ`. Hunspell-sv-
undantagen är tekniska namn, kodspråk och formatsträngar. Ingen inskickning
till GNOME har gjorts i detta steg.

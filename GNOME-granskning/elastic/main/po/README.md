# Elastic — main/po — svensk granskning

- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/elastic/main/po/sv/>
- Granskad: 2026-11-23
- Aktuell POT: 64 strängar, hämtad direkt från Damned Lies 2026-11-27; POT-datum 2026-09-26, senaste mall uppladdad 2026-11-18
- Aktuell POT: 64 aktiva strängar
- Nya översättningar: 0
- Korrigerade befintliga översättningar: 14

Hela katalogen är radgranskad mot senaste POT. Språk, UI-åtgärder och
fysikförklaringar är rättade till idiomatisk svenska. Kodspråk, libadwaita,
parametrar och formatsträngarna `%.2lf` och `%.0lf` är bevarade.

`msgfmt --check` och `msgcmp --use-fuzzy` är godkända. `l10n-lint` har inga
fel eller varningar; den enda informationsnotisen gäller en avsiktligt flyttad
och giltig ASCII-accelerator i `_Reset` → `Åte_rställ`. Hunspell flaggar endast tekniska namn, kodspråk och formatsträngar samt den korrekta svenska sammansättningen `fjäderfysikbaserade`; undantagen är dokumenterade i `hunspell-undantag.md`.

Ingen inskickning till GNOME har ännu gjorts.

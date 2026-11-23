# gnome-session — main/po — svensk granskning

- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/gnome-session/main/po/sv/>
- Granskad: 2026-11-23
- Aktuell POT: 43 aktiva strängar
- Nya översättningar: 0
- Korrigerade befintliga översättningar: 10

Hela katalogen är radgranskad mot senaste POT. Grammatik och idiomatik är
rättade i sessionstjänstens UI- och CLI-texter; bland annat används
`standardindata`, korrekt imperativ och tydligare formuleringar för
initiering, tjänstfel och blockerare. Kommandon, systemd-enheter, argument,
formatsträngen `%s: %m\n` och tekniska identifierare är oförändrade.

`msgfmt --check`, `msgcmp --use-fuzzy` och `l10n-lint` är godkända utan fel
eller varningar. Hunspell-sv-undantagen är bevarade tekniska termer,
systemd-enheter, kommandoradsargument och engelska giltiga argumentvärden.
Ingen inskickning till GNOME har gjorts i detta steg.

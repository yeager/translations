# ashpd — main/demo-client — svensk granskning

- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/ashpd/main/demo-client/sv/>
- Granskad: 2026-11-23
- Aktuell POT: 38 aktiva strängar
- Nya översättningar: 0
- Korrigerade befintliga översättningar: 4

Hela demo-klientens katalog är radgranskad mot senaste POT. Etiketterna för
snabbmeddelandesvar och samtalsåtgärder är rättade till naturlig svensk
gränssnittstext; `högtalarläge` används konsekvent för speakerphone.

`msgfmt --check`, `msgcmp --use-fuzzy` och `l10n-lint` är godkända utan fel
eller varningar. Hunspell-sv-undantaget `ASHPD-demo` är produktnamnet. Ingen
inskickning till GNOME har gjorts i detta steg.

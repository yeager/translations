# Warp Hjälp — main/help (sv)

- Aktivitet: https://l10n.gnome.org/vertimus/warp/main/help/sv/
- Käll-POT: `warp-help.main.pot`, senaste hämtning 2026-11-26 (POT skapad 2026-11-18 21:02 UTC)
- Utgångsstatistik: 55 översatta, 0 oöversatta, 0 fuzzy
- Slutstatistik: 55 översatta, 0 oöversatta, 0 fuzzy
- Ändrade befintliga strängar: 28
- Nya översättningar: 0

Hela katalogen granskades mot senaste POT. Rättade bland annat stela
meningskonstruktioner, stavning, relaterad terminologi och beskrivningarna av
QR-koder och filöverföring. “Transmit Relay” översattes konsekvent med
“reläserver”. Metavariabeln `{code}` lokaliserades till `{kod}` enligt
projektets instruktion; klammerformen är bevarad.

`msgfmt --check --check-format` och `msgcmp` passerar. `l10n-lint` rapporterar
ett formatfel för `{code}` → `{kod}` eftersom det tolkar metavariabeln som en
Python-platshållare. Detta är ett avsiktligt och godkänt undantag enligt
instruktionen att översättningsbara metavariabler ska lokaliseras. Dessutom
finns en informationsnotis för kommandot `wormhole receive`, som avsiktligt
inte översätts. XML-taggar, länkar, övriga platshållare och radbrytningar är
kontrollerade. `hunspell-sv`-undantag finns i `hunspell-unknown.txt` och gäller
produktnamn, kommandon, tekniska identifierare och sammansatta facktermer.

Ingen ändring har skickats till GNOME.

# NetworkManager-openvpn — main — svenska gränssnittet

- Aktivitet i Damned Lies: https://l10n.gnome.org/vertimus/networkmanager-openvpn/main/po/sv/
- Senaste POT hämtad 2026-11-25: https://l10n.gnome.org/POT/NetworkManager-openvpn.main/NetworkManager-openvpn.main.pot
- POT SHA-256: `a5416cabac725e5b7f7f33db2a919c0e1811651ae488e99f60d5f21d4549e819`
- Katalogen matchar POT: 169 aktiva strängar, 0 fuzzy och 0 oöversatta.
- Granskning: 62 befintliga översättningar korrigerade; 0 nya översättningar.
- Last-Translator i den granskade filen: Daniel Nylander <gnome@danielnylander.se>.

## Kontroller

- `msgfmt --check`: godkänd.
- `msgcmp` mot den hämtade POT-filen: godkänd; samma aktiva katalogposter.
- `l10n-lint --language sv --reference NetworkManager-openvpn.main.pot`: 0 fel och 1 varning. Varningen gäller pluralmeddelandet `option %s expects between %u and %u argument`: svenskans singular och plural är båda `argument`, så formerna ska vara identiska.
- Egen kontroll av printf-platshållare, CLI-flaggor, antal pluralformer, acceleratorer och radbrytningar: inga avvikelser. Sex lintnotiser om markup gäller metavariablerna `<file>` som översatts till `<fil>`; vinkelparenteserna och positionerna är bevarade.
- `hunspell-sv`: kontrollerad. Rimliga undantag är OpenVPN/NetworkManager, kryptografiska algoritmer och protokoll, OpenVPN-konfigurationsdirektiv, certifikatfält samt tekniska sammansättningar som `datagramfragmentering`, `kolonseparerad`, `insticksmodulfilen`, `pingintervall` och `Sökvägs-MTU-upptäckt`.

Ingen fil har skickats in till GNOME.

## Filer

- [Original PO](networkmanager-openvpn.main.sv.original.po)
- [Granskad PO](networkmanager-openvpn.main.sv.reviewed.po)
- [Diff](networkmanager-openvpn.main.sv.diff)
- [Senaste POT](NetworkManager-openvpn.main.pot)

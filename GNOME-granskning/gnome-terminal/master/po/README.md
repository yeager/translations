# GNOME Terminal — `master/po` — svenska gränssnittet

Katalogen hämtades på nytt och radgranskades den 2026-11-28 mot den senaste POT-filen. GNOME Damned Lies visar aktuell status som **381 översatta, 91 fuzzy och 34 oöversatta** av 506 strängar (aktivitet uppdaterad 2026-11-23).

- [GNOME-aktivitetssida](https://l10n.gnome.org/vertimus/gnome-terminal/master/po/sv/)
- [Aktuell POT](https://l10n.gnome.org/POT/gnome-terminal.master/gnome-terminal.master.pot)
- [Aktuell svensk PO](https://l10n.gnome.org/POT/gnome-terminal.master/gnome-terminal.master.sv.po)
- POT skapad 2026-09-12; SHA-256 `fdb0cf5e37b02f7629582617e6aef0136b7600e5783bf2a3d718ca1552ed5dec`
- PO SHA-256 `01f58b744312cade274002997041441ae397f6b52bf9af9ae562316e35b35654`

En lokal katalog från 2023, med 521 aktiva poster, hade granskats 2026-11-23 endast för acceleratorer och översättarmetadata. Den var inte synkroniserad med aktuell POT (2026-09-12) och GNOME:s då aktuella PO hade 91 fuzzy och 34 tomma strängar. Den här granskningen avser den aktuella 506-strängarskatalogen.

## Resultat

| Mätning | Före | Efter lokal granskning |
|---|---:|---:|
| Aktiva strängar enligt senaste POT | 506 | 506 |
| Översatta | 381 | 506 |
| Fuzzy | 91 | 0 |
| Oöversatta | 34 | 0 |
| Nya översättningar | — | 34 |
| Rättade befintliga översättningar | — | 228 |
| Granskade fuzzy-poster | — | 91 (85 textförslag rättade, 6 bekräftade) |
| Alla ändrade textvärden | — | 262 |

De rättade strängarna omfattar inställningsbeskrivningar, terminalkommandon, flikåtgärder, kortkommandon, färgprofiler och äldre fuzzy-förslag. Sex käll-URL:er hade fuzzy-värden som pekade på andra sidor; de återställdes till exakt sina respektive käll-URL:er. Översättbara metavariabler som `FILE`, `DIRNAME`, `ROLE`, `TITLE`, `PROFILE-NAME`, `COMMAND`, `GEOMETRY` och `ZOOM` har svenska namn där de är användarvisade.

## Validering

- `msgfmt --check --check-format`: godkänd.
- `msgcmp --use-fuzzy` mot senaste POT: godkänd.
- `l10n-lint --language sv --no-terminology`: 0 fel och 0 varningar. Kvarvarande informationsnotiser gäller mnemonicens flytt inom översatta etiketter, ett licens-ID som avsiktligt står kvar, och ett långt svenskt namn för filbeskrivarmetavariabeln.
- Egen kontroll mot aktuell POT: 0 saknade/extra källnycklar, 0 fuzzy, 0 tomma strängar, 0 fel i formatmarkörer/markup/URL:er/acceleratorantal. Inga acceleratormarkörer använder `å`, `ä` eller `ö`.
- `hunspell -d sv_SE -l` kördes på alla svenska strängar. Produktnamn, protokoll, konfigurationsnycklar och tekniska sammansättningar är dokumenterade i [`hunspell-exceptions.md`](hunspell-exceptions.md); verktygsutdata finns i [`hunspell-output.txt`](hunspell-output.txt).
- `swedish-tm` konsulterades och de granskade källparen importeras till GNOME-TM; se [`tm-check.md`](tm-check.md). GNOME-terminologilistan uppdaterades med terminaltermer.

Ingen ändring har skickats till GNOME Damned Lies.

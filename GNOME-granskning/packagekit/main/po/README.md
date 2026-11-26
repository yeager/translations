# PackageKit — main/po (sv)

- Damned Lies-aktivitet: https://l10n.gnome.org/vertimus/packagekit/main/po/sv/
- Svenska översättningar sköts externt i [Weblate](https://hosted.weblate.org/projects/packagekit/translations/); Damned Lies är skrivskyddat.
- POT hämtad 2026-11-26; senaste POT har 2026-11-20 som skapandedatum.
- Status före den lokala granskningen i Damned Lies: 413 översatta, 1 fuzzy, 4 oöversatta (418 totalt).
- Lokal status efter granskningen mot senaste POT: 418 översatta, 0 fuzzy, 0 oöversatta.
- Nya översättningar: 4.
- Rättade befintliga översättningar: 92.

Alla 418 aktiva strängar radgranskades. Felöversättningen i `Failed to make the daemon yield` rättades efter kontroll av PackageKit-källkoden. Kommandon och metavariabler bevarades, medan användarsynliga argumentbeskrivningar översattes. `Last-Translator` är Daniel Nylander <gnome@danielnylander.se>.

Validering: `msgfmt --check --check-format` godkänd med 418 översatta meddelanden; `msgcmp --use-fuzzy` godkänd. `l10n-lint --language sv` rapporterar 0 fel och 0 varningar; tre informationsnoteringar gäller medvetet svensk formulering/böjning. Egna kontroller av platshållare, pluralformer, markup, URL:er, acceleratorer och radbrytningar passerar. Hunspell kördes med `hunspell -d sv_SE`; undantag dokumenteras i `hunspell-undantag.md`.

Efter användarens begäran skickades den granskade filens 91 matchande ändringar till hosted Weblate via API (`method=translate`, `conflicts=replace-translated`). Weblate accepterade 91 och hoppade över 325 oförändrade rader. Efter uppladdningen verifierade API:t 416/416 översatta, 0 fuzzy och 0 felande kontroller; den hämtade filen har samma 416 nycklar och översättningar som uppladdningsfilen.

Uppladdningens diff, källfil, resulterande PO och lintresultat finns i `packagekit.weblate.sv.upload.diff`, `packagekit.weblate.sv.original.po`, `packagekit.weblate.sv.upload.po` och `weblate-upload-lint.json`. Fem strängar i den senaste GNOME-katalogen saknas i Weblates äldre källfil och importerades därför inte. Tre äldre Weblate-strängar saknas i den senaste GNOME-POT-filen och bevarades oförändrade. Inget har skickats till Damned Lies.

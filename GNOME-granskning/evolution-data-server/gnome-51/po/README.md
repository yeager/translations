# evolution-data-server — gnome-51/po

- **GNOME-katalog:** [evolution-data-server/gnome-51/po/sv](https://l10n.gnome.org/vertimus/evolution-data-server/gnome-51/po/sv/)
- **Aktuell POT/PO hämtade:** 2026-11-28 från Damned Lies API.
- **Före granskning:** 88/88 aktiva poster översatta, 0 fuzzy, 0 oöversatta. De tre pluralposterna hade redan båda pluralformerna ifyllda.
- **Efter granskning:** 88/88 aktiva poster översatta, 0 fuzzy, 0 oöversatta. 0 nya översättningar och 76 ändrade befintliga poster.
- **Granskning:** samtliga 88 aktiva poster jämförda med senaste POT; äldre, obsoleta poster lämnades oförändrade.
- **Inskickning:** inte inskickad till GNOME enligt arbetsinstruktionen.

## Validering

- `msgfmt --check --check-format`: godkänd.
- `msgcmp --use-fuzzy` mot aktuell POT: godkänd; samma 88 aktiva nycklar.
- Platshållare, pluralformer, markup och tekniska nycklar: jämförda, inga avvikelser.
- Acceleratorer: inga i denna katalog.
- `l10n-lint --language sv`: 0 fel och 5 kvarvarande varningar. Varningarna gäller att svenska förklaringar har fullständiga meningar där källan saknar avslutande punkt samt att översatta parenteser/citat omsluter engelska exempelvärden (`minutes`, `hours`, `days`, `gpg2`, OAuth2-exempel). De bevarar betydelsen och de exakta identifierarna.
- `hunspell -d sv_SE -l`: alla flaggade ord granskades. Undantag är API-/biblioteksnamn och OAuth2/SMTP/GIO/GNetworkMonitor-identifierare, kodnycklar och exempelvärden (`always-online`, `notify-last-snooze-from-start`, `reminders-past`, `name=value`, `USER`, `REALNAME`, `HOST`, `true`, `false`, `gpg`, `gpg2`, domännamn), samt giltiga tekniska sammansättningar som `Kontakt-UID`, `OAuth2-klient-ID`, `krypterare` och `mappöversikten`. Inga ord lades till i ordlistan.

## Filer

- Original: `evolution-data-server.gnome-51.sv.original.po`
- Granskad: `evolution-data-server.gnome-51.sv.reviewed.po`
- Diff: `evolution-data-server.gnome-51.sv.diff`
- POT: `evolution-data-server.gnome-51.pot`

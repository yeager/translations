# Music Assistant – svensk lokaliseringsstatus

Senast uppdaterad: 15 november 2026.

## Lokalise

Music Assistant Server har **100 % svensk täckning** i Lokalise enligt
projektets statistik: 41 901 basord och 0 ord kvar att översätta. Senaste
granskade strängbatch är 236.

En tom källsträng för `provider.plex_connect.config_entries.plextv_divider.label`
kan fortsatt visas i listan över oöversatta poster. Den har en sparad svensk
etikett, `Plex.tv`, med `is_untranslated: false` och påverkar inte statistikens
100 %-resultat.

## Status för leverans

- Lokal granskning: klar för arkiverade batchar.
- Arkivering och push till `yeager/translations`: klar.
- Sparad och läst tillbaka via Lokalise API: klar.
- Projektets redaktionella granskning, publicering eller release: inte
  verifierad här.

JSON användes för dessa deltafiler; `msgfmt` är därför inte tillämpligt.

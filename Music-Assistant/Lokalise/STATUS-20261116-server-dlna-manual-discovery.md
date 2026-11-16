# Music Assistant Server – svenska DLNA-fält

Datum: 2026-11-16
Projekt: MA Server (`264744796a2c5fd1b48fb5.28236063`)
Komponent: DLNA-konfiguration för manuell enhetsupptäckt
Kanal: Lokalise API v2

## Omfattning

Två nya svenska måltexter granskades i sin kontext som DLNA-inställningar:

- `provider.dlna.config_entries.manual_discovery_ip_addresses.description`
- `provider.dlna.config_entries.manual_discovery_ip_addresses.label`

De beskriver hur en enhet som inte upptäcks automatiskt läggs till med
IPv4-adress eller URL till dess enhetsbeskrivning. IPv4, exempeladresser,
port, URL och `description.xml` är bevarade exakt.

## Resultat

Lokalise accepterade båda API-skrivningarna med HTTP 200. Direkt återläsning
bekräftar svensk måltext med `is_untranslated: 0`, `is_fuzzy: false` och
`is_unverified: false` för båda nycklarna.

`svlang skrivregler` gav inga fynd. Hunspell-SV gav inga språkfynd.
`msgfmt` och `l10n-lint` är inte tillämpliga på denna tvåsträngars
Lokalise-API-batch utan PO-deltafil. Diffkontroll och Gitleaks kördes för
arkivposten före push.

## Upstreamstatus

Strängarna är sparade och återlästa i Lokalise. Detta bekräftar inte
projektgranskning, merge eller en utgiven programversion.

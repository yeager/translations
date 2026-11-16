# Home Assistant Core: RFXtrx, batch 127

29 svenska RFXtrx-strängar för enhetskonfiguration och felhantering.
Etablerade former från Home Assistant-TM har återanvänts, bland annat
`Avstängningsfördröjning`, `Läge för persienner` och `RFXtrx-alternativ`.

Kontroller: JSON, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks.
`msgfmt` är inte tillämpligt för Lokalise JSON/API-batcher.

Alla 29 poster sparades med Lokalise API, `is_unverified: false`, och
återlästes med respektive översättnings-ID. Detta bekräftar sparning, inte
extern granskning eller utgivning.

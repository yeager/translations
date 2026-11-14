# HP-skrivare, värdetikett, batch 31

Värdet `component::hp_printer::config::step::reconfigure::data::host`
sparades direkt i Home Assistant Core-projektet på Lokalise och återlästes
2026-11-14 som **Värd**.

Källan använder en Lokalise-nyckelreferens till Home Assistants etablerade
gemensamma term. Referensen sparades i stället för att duplicera engelska
"Host", och den upplösta svenska texten återlästes.

Kontroll: värdet sparades i Lokalise och återlästes. `msgfmt`, l10n-lint,
svlang och Hunspell är inte tillämpliga på denna direktredigerade,
exportlösa JSON-batch. Arkivets diffkontroll och Gitleaks kördes före push.

Status: sparad i projektets etablerade upstreamkanal. Granskning,
synkronisering och release är inte verifierade.

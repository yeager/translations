# Home Assistant Core – HTTP HTTPS-kryptering, svenska

Datum: 2026-11-15

Fyra titlar i HTTP-integreringens åtgärdsflöde för en föråldrad TLS-profil
har granskats som en sammanhängande UI-grupp och sparats via Lokalise API.

| Nyckel | Källa | Svenska |
| --- | --- | --- |
| `confirm_intermediate_v6::title` | Update the HTTPS encryption settings | Uppdatera inställningarna för HTTPS-kryptering |
| `confirm_modern_v6::title` | Update the HTTPS encryption settings | Uppdatera inställningarna för HTTPS-kryptering |
| `ignore::title` | Update the HTTPS encryption settings | Uppdatera inställningarna för HTTPS-kryptering |
| `init::title` | Update the HTTPS encryption settings | Uppdatera inställningarna för HTTPS-kryptering |

## Upstreamstatus

- Lokal granskning: klar.
- Sparad via Lokalise API: klar, fyra översättningar.
- API-återläsning: klar. Varje post har korrekt översättnings- och nyckel-ID,
  målspråk `sv` och `is_unverified=false`.
- Projektgranskning och release: inte verifierade.

## Kontroller

- `l10n-lint`, `svlang` och `hunspell-sv`: körs mot kontrollfilen i denna
  batch.
- `msgfmt`: ej tillämpligt; katalogen är JSON-baserad och ingen PO-fil har
  exporterats.
- `git diff --check` och Gitleaks: körs före arkiveringens push.

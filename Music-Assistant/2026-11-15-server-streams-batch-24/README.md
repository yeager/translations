# Music Assistant Server – ljudströmmar, batch 24

Datum: 2026-11-15

## Omfattning

20 svenska konfigurationssträngar för övertoning, nattlig ljudanalys,
ljudbuffert, publicerad IP-adress, Smart Fades och uppspelningskällor.

## Terminologi och kontext

- *Övertoning*, *ljudbuffert*, *strömningstjänst*, *spår*, *album* och
  *spellista* följer etablerad terminologi i projektet.
- Smart Fades, IP, IPv4, IPv6, CPU, Docker, Plex, Subsonic och kodvärdet
  `auto` behålls som tekniska namn.
- Markdownstruktur och adresser har bevarats i buffert- och IP-hjälptexterna.

## Kontroller

- Källtext och nycklar kontrollerade mot aktuell `en.json` och `strings.json`.
- `l10n-lint --language sv`: godkänd.
- `svlang skrivregler`: godkänd.
- Hunspell-svenska: återstående träffar är produktnamn, tekniknamn och
  kodvärdet `auto`.
- JSON-syntax och diffkontroll: godkända.
- Gitleaks: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt eftersom resursformatet är JSON.

## Status

Lokalt granskad och arkiverad. Inte uppladdad, inskickad, granskad eller
integrerad upstream. Batchen väntar på fungerande Lokalise-åtkomst.

# Music Assistant Server – webbserver, batch 22

Datum: 2026-11-15

## Omfattning

23 svenska texter för webbserverns konfiguration: adressbindning, externa
URL:er, SSL/TLS, certifikat, privata nycklar, verifiering och säkerhetsvarning.

## Terminologi och kontext

- Detta är administrativa och säkerhetskänsliga inställningar; varningar har
  behållit samma tydliga handlingsuppmaning som engelsk källa.
- HTTPS, SSL/TLS, PEM, RSA, ECDSA, OAuth, VPN, API, IPv4, IPv6, Docker,
  Sendspin och kodvärdena `0.0.0.0` och `host` bevaras som tekniska namn.
- *Omvänd proxy*, *värdnamn*, *nätverksgränssnitt* och *webbserver* används
  konsekvent på svenska.
- Platshållaren `{0}` och filsystemssökvägar har bevarats exakt.

## Kontroller

- Källtext, nycklar, platshållare och radbrytningar kontrollerade mot aktuell
  `en.json` och `strings.json`.
- `l10n-lint --language sv`: godkänd.
- `svlang skrivregler`: godkänd.
- Hunspell-svenska: återstående träffar är avsiktliga produktnamn,
  protokoll, certifikatformat och krypteringsförkortningar.
- JSON-syntax och diffkontroll: godkända.
- Gitleaks: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt eftersom resursformatet är JSON.

## Status

Lokalt granskad och arkiverad. Inte uppladdad, inskickad, granskad eller
integrerad upstream. Batchen täcker samtliga aktuella nycklar för
`core.webserver` och väntar på fungerande Lokalise-åtkomst.

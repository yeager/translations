# Bitwarden Web – svenska

## 2026-11-11, batch 01

- Komponent: Web (`308189`).
- Omfattning: 25 tidigare oöversatta strängar för granskningslogg, policyer och import.
- Upstream: 25 Crowdin-förslag skapade och verifierade, id `2007753`–`2007801` (udda id). Samtliga väntar på Bitwardens granskning (`approvalStatus: null`) och är inte godkända eller publicerade.

## Kontroller

- Platshållarkontroll: godkänd för samtliga 25 strängar.
- Hunspell-sv: endast produktnamn, platshållare och accepterade sammansättningar återstår som förväntade träffar.
- svlang: inga anglicismer eller skrivregelsträffar. Längd- och V2-markeringar är falska positiva för UI-fragment och platshållartexter.
- Diffkontroll och Gitleaks: godkända.
- msgfmt och l10n-lint: inte direkt tillämpliga på Crowdin-API:ets gransknings-JSON.

## 2026-11-11, batch 02

- Omfattning: 25 tidigare oöversatta strängar för import och återkallat godkännande av åtkomst.
- Upstream: 25 Crowdin-förslag skapade och verifierade, id `2007803`–`2007851` (udda id). Samtliga väntar på Bitwardens granskning (`approvalStatus: null`).
- Kontroller: platshållarkontroll, Hunspell-sv, svlang, diffkontroll och Gitleaks godkända. svlangs V2-markeringar är falska positiva för UI-fragment och platshållare; msgfmt och l10n-lint är inte direkt tillämpliga på API-JSON.

## 2026-11-11, batch 03

- Omfattning: 25 tidigare oöversatta strängar för åtkomstregler, delade mappar och Bitwarden Send.
- Upstream: 25 Crowdin-förslag skapade och verifierade, id `2007853`–`2007901` (udda id). Samtliga väntar på Bitwardens granskning (`approvalStatus: null`).
- Kontroller: platshållarkontroll, Hunspell-sv, svlang, diffkontroll och Gitleaks godkända. svlangs V2-markeringar är falska positiva för UI-fragment och platshållare; msgfmt och l10n-lint är inte direkt tillämpliga på API-JSON.

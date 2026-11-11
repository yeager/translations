# Bitwarden Desktop – svenska

## 2026-11-11, batch 01

- Komponent: Desktop (`299360`).
- Omfattning: 41 tidigare oöversatta strängar för import och Bitwarden Send.
- Upstream: 41 Crowdin-förslag skapade och verifierade, id `2007651`–`2007735` (med luckor i den globala id-serien). Samtliga väntar på Bitwardens granskning (`approvalStatus: null`) och är inte godkända eller publicerade.

## Kontroller

- Platshållarkontroll: godkänd för samtliga 41 strängar.
- Hunspell-sv: endast produktnamn, platshållare och den accepterade sammansättningen `skrivbordsapp` återstår som förväntade träffar.
- svlang: inga anglicismer eller skrivregelsträffar. V2- och längdmarkeringar är falska positiva för UI-fragment och platshållartexter.
- Diffkontroll och Gitleaks: godkända.
- msgfmt och l10n-lint: inte direkt tillämpliga på Crowdin-API:ets gransknings-JSON.

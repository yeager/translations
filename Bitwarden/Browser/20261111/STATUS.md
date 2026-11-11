# Bitwarden Browser – svenska

## 2026-11-11, batch 01

- Komponent: Browser (`268134`), fil `main/src/_locales/en/messages.json` (`26`).
- Omfattning: 25 tidigare oöversatta strängar för synkroniserad upplåsning och importdestination.
- Status före inskick: lokal kandidatsamling granskad med kontext och platshållarkontroll.
- Upstream: 25 Crowdin-förslag skapade och verifierade 2026-11-11, id `2007233`–`2007281` (udda id). Samtliga har `approvalStatus: null`; de väntar därför på Bitwardens granskning och är inte godkända eller publicerade.

## Kontroller

- Platshållarkontroll: godkänd för samtliga 25 strängar.
- Hunspell-sv: endast produktnamn och platshållare återstår som förväntade träffar.
- svlang: inga anglicismer eller skrivregelsträffar; V2-markeringarna är falska positiva från platshållare och flerledade UI-fragment.
- l10n-lint och msgfmt: inte tillämpliga direkt på Crowdin-API:ets gransknings-JSON; den är ingen komplett lokaliseringsresurs.
- Diffkontroll och Gitleaks: godkända.

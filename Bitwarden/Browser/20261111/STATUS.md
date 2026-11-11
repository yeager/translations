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

## 2026-11-11, batch 02

- Omfattning: 27 tidigare oöversatta strängar för begränsade importtyper, Bitwarden Send och tidsbegränsad åtkomst.
- Upstream: 27 Crowdin-förslag skapade och verifierade, id `2007283`–`2007335` (udda id). Samtliga väntar på Bitwardens granskning (`approvalStatus: null`).
- Kontroller: platshållarkontroll, Hunspell-sv, diffkontroll och Gitleaks godkända. Hunspell träffar endast produktnamn och en avsiktlig avstavning; msgfmt och l10n-lint är inte direkt tillämpliga på API-JSON.

## 2026-11-11, batch 03

- Omfattning: 35 tidigare oöversatta strängar för tidsbegränsad privilegierad åtkomst.
- Upstream: 35 Crowdin-förslag skapade och verifierade, id `2007347`–`2007419` (med luckor i den globala id-serien). Samtliga väntar på Bitwardens granskning (`approvalStatus: null`).
- Kontroller: platshållarkontroll, Hunspell-sv, diffkontroll och Gitleaks godkända. Hunspell träffar endast produktnamn och platshållare; msgfmt och l10n-lint är inte direkt tillämpliga på API-JSON.

## 2026-11-11, batch 04

- Omfattning: 34 tidigare oöversatta strängar för ansökan om tidsbegränsad åtkomst.
- Upstream: 34 Crowdin-förslag skapade och verifierade, id `2007441`–`2007507` (udda id). Samtliga väntar på Bitwardens granskning (`approvalStatus: null`).
- Kontroller: platshållarkontroll, Hunspell-sv, svlang, diffkontroll och Gitleaks godkända. svlangs V2-markeringar är falska positiva för UI-fragment och platshållare; msgfmt och l10n-lint är inte direkt tillämpliga på API-JSON.

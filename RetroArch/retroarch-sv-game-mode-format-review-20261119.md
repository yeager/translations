# RetroArch – Spelläge och prestandaprofil, svensk QA-rättning 2026-11-19

En befintlig svensk översättning i `msg_hash_us.json` har granskats via Crowdins QA-API. Förslaget är inte sparat eller skickat till Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 6220277 | Raises RetroArch's disk access priority and holds the system's performance power profile (through power-profiles-daemon or tuned-ppd), which can improve performance, reduce latency and fix audio crackling. The performance profile only applies when plugged in. The previous profile is restored when Game Mode is turned off or RetroArch exits. | Ökar RetroArchs prioritet för diskåtkomst och låser systemets prestandaprofil genom power-profiles-daemon eller tuned-ppd. Det kan förbättra prestandan, minska fördröjningen och rätta till sprakande ljud. Prestandaprofilen används bara när datorn är ansluten till ström. Föregående profil återställs när GameMode stängs av eller RetroArch avslutas. | Ökar RetroArchs prioritet för diskåtkomst och håller systemets prestandaprofil aktiv (via power-profiles-daemon eller tuned-ppd), vilket kan förbättra prestandan, minska fördröjningen och åtgärda sprakande ljud. Prestandaprofilen används bara när datorn är ansluten till ström. Den föregående profilen återställs när Spelläge stängs av eller RetroArch avslutas. |

## Kontroller

- Källans parenteser kring systemtjänsterna är återställda; Crowdins ursprungliga parentes-QA-träff är därmed löst.
- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` och Crowdins slutliga QA markerar endast tjänstenamnen `power-profiles-daemon` och `tuned-ppd`.
- Inga platshållare eller annan teknisk formatering har ändrats.

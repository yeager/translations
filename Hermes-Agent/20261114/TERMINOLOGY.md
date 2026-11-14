# Hermes Agent – svensk terminologi

Källa: aktuell kärnkatalog i `NousResearch/hermes-agent` vid
`abeeef4d491cba7ea6126a2f54d81c879da5059f`, befintliga svenska Hermes-
översättningar och användargränssnittets säkerhets- och betalningsflöden.

| Engelska | Svenska | Kontext och undantag |
| --- | --- | --- |
| approval | godkännande | Säkerhetsbeslut före en åtgärd. |
| approve | godkänn | Imperativ knapp- eller kommandotext. |
| deny | neka | Säkerhetsbeslut; inte *avslå* i korta UI-val. |
| allowlist | tillåtelselista | Teknisk lista över tillåtna åtgärder. |
| unattended session | obevakad session | Session utan person som kan svara på en begäran. |
| prompt | prompt | Behålls som etablerad CLI-term; *fråga* används bara för UI-frågor. |
| rewind | spela tillbaka | Avser att återgå i transkriptet till en tidigare prompt. |
| context window / context length | kontextfönster / kontextlängd | Den synliga UI-termen lokaliseras, konfigurationsnyckeln lämnas exakt. |
| token | token | Teknisk enhet i modellgränssnittet. |
| billing | fakturering | Samlat område för kort, saldo och debitering. |
| top-up | påfyllning | Påfyllning av saldo; inte *laddning*. |
| balance | saldo | Användarens tillgängliga medel. |
| card on file | registrerat kort | Kort sparat hos betalningsleverantören. |
| auto-reload | automatisk påfyllning | Funktion som fyller på saldo enligt tröskelvärde. |
| threshold | tröskelvärde | Gräns som utlöser automatisk påfyllning. |
| Remote Spending | fjärrbetalning | Synligt funktionsnamn; versaliseras bara när originalet gör det. |
| authorize | auktorisera | Teknisk behörighetsåtgärd, särskilt för terminal och kort. |
| authenticate | autentisera | Identitetskontroll; ska inte blandas ihop med auktorisering. |
| charge | debitera / debitering | Verb respektive resultat/åtgärd. |
| portal | portalen | Produktens egen webbportal, utan översatt produktnamn. |
| organization admin | organisationsadministratör | Rollnamn; *ägare* för owner. |
| heartbeat | pulssignal | Återkommande automatisering som körs när en session är inaktiv; kommandot `/heartbeat` lämnas exakt. |
| checkpoint | återställningspunkt | Sparat fil- och sessionstillstånd som används av `/rollback`; konfigurationsnyckeln `checkpoints` lämnas exakt. |

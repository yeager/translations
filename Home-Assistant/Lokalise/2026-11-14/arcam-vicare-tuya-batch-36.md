# Arcam, ViCare och Tuya – batch 36

Datum: 2026-11-14

Följande 15 svenska strängar har granskats i sin komponentkontext, sparats i
Lokalise och lästs tillbaka i redigeraren:

| Komponent | Källa | Svenska |
| --- | --- | --- |
| Arcam | The device rejected the command. | Enheten avvisade kommandot. |
| Arcam | The device does not support the command. | Enheten stöder inte kommandot. |
| ViCare | Heating heat production today | Värmeproduktion för uppvärmning i dag |
| ViCare | DHW heat production today | Värmeproduktion för tappvarmvatten i dag |
| ViCare | Heat production | Värmeproduktion |
| HP Printer | Uses an SSL certificate | Använder ett SSL-certifikat |
| Tuya | On / power_on | På |
| Tuya | Off / power_off | Av |
| Tuya | On | På |
| Tuya | Off | Av |
| Tuya | Previous state | Föregående tillstånd |
| Tuya | Undervoltage early warning | Tidigt varningsmeddelande om underspänning |
| Tuya | Temperature difference fault | Fel i temperaturskillnad |
| Tuya | Phase loss | Fasbortfall |
| Tuya | Overvoltage early warning | Tidigt varningsmeddelande om överspänning |

`värmeproduktion` och `tappvarmvatten` verifierades mot Viessmanns svenska
produktdokumentation. `Fasbortfall` är den etablerade svenska facktermen.

## Kontroller

- l10n-lint: godkänd
- svlang: 10/10 naturliga formuleringar i vardera av de två underlagen
- Hunspell-sv: endast `Fasbortfall`, en etablerad fackterm som saknas i
  ordlistan
- diffkontroll och Gitleaks: godkända
- msgfmt: ej tillämpligt; Lokalise arbetar här med JSON-strängdata, inte PO

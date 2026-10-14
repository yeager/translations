# Uppströmsstatus för svenska tankstreck, 14 oktober 2026

Kontrollen omfattar svenska översättningar där måltexten innehöll ett tankstreck utan att motsvarande källsträng använde samma tecken. Bindestreck, minustecken, intervall och källstyrda litterala värden bevaras.

| Komponent | Status | Underlag eller nästa steg |
| --- | --- | --- |
| ownCloud Web, `pkg` | Uppdaterad | En översättning ändrades via Transifex och lästes tillbaka via API. |
| Fedora ABRT | Förslag inskickat | Weblate accepterade ett förslag. Rollen får inte ersätta den befintliga översättningen. |
| Translation Project | Patchar klara | 15 aktuella PO-kataloger och 180 poster finns i `tp-sv/upstream-patches/2026-10-14/`. Färsk fil ska hämtas precis före inskickning. |
| Shadow | Ingen ändring behövs | Aktuell TP-fil saknar berörda tankstreck. |
| Wireshark | Patch klar | Fyra ändringar i aktuell TS-katalog finns i `Wireshark/upstream-patches/2026-10-14/`. |
| PCSX2 | Patch klar, väntar | En källstyrd litteral ändring finns i `PCSX2/upstream-patches/2026-10-14/`. CrowdIn-tokenen kan läsa men inte bygga export. PCSX2:s egna bidragsregler kräver mänsklig verifiering före publicering. |
| Blender Manual | Inte kontrollerad mot färsk fil | Väntar enligt tidigare prioritering på en nyare Blender-version än 4.5. |
| Ubuntu språkpaket | Kräver inloggad Launchpad-export | Publika exportadresser ger inloggningsflöde, inte PO-filer. |
| Ubuntu DDTP Universe | Inte kontrollerad mot färsk fil | Behöver aktuell Launchpad-export. |

Alla sparade patchar har kontrollerats med relevant formatkontroll, uppdaterad `l10n-lint` och Gitleaks. `msgfmt` användes för PO-filer, `xmllint` för TS-filer.

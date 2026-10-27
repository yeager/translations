# Lokal kontrollstatus för Cacti 2026-10-27

Den här kontrollen avser arkiverade fullfiler, inte den aktuella statusen i
Cacti Translate. Den ska därför inte användas som bevis för upstreamstatus.

| Komponent | Lokal fil | Resultat | Bedömning |
| --- | --- | --- | --- |
| NPC | `cacti-npc-sv.po` | 42 poster, inga fel eller varningar i l10n-lint; inga anglicismer i svlang | Inga nya lokala ändringar behövs. |
| GPS Maps | `cacti-gpsmaps-sv.po` | 37 poster, inga fel eller varningar i l10n-lint; inga anglicismer i svlang | Inga nya lokala ändringar behövs. |
| Cycle | `cacti-cycle-sv.po` | Två oförändrade engelska måltexter identifierades | Båda har redan svenska rättningar i `cacti-cycle-sv-granskning-20261026.po`; skapa inte dubbletter. |
| Audit | `cacti-audit-sv.po` | En intervallvarning och två träffar på Syslog-facilitet | Intervallrättningen finns redan i `cacti-audit-sv-after-number-range-20261020.po`. Syslog-facilitet är dokumenterad som en avsiktlig fackterm i den gemensamma ordlistan. |
| HMIB | `cacti-hmib-sv.po` | Sex oförändrade engelska måltexter och två varningar om versalisering | De engelska texterna har redan rättningar i `cacti-hmib-sv-after-ui-cleanup-20261020.po`. Versaliseringen av CPU/CPUs behöver endast ändras efter kontroll i den aktuella komponenten. |
| Thold | `cacti-thold-sv.po` | Flera historiska språk- och mallbrister | Nyligen arkiverade `cacti-thold-meddelandemallar-20261027.po` rättar åtta mallposter. Äldre etikett- och kommandoändringar finns redan i tidigare Thold-deltan. |
| Monitor | `cacti-monitor-sv.po` | 241 översatta poster, inga formatfel och inga anglicismer i svlang. l10n-lint hittar en intervallvarning. | Intervallrättningen finns redan i `cacti-monitor-sv-granskning-20261026.po`. Separata arkiverade deltan täcker även administratörsanteckning, tidsstatus, drifttid och rutor/nedtid; skapa inte en dubblettfil. |

Kontrollen har gjorts med `msgfmt`, `l10n-lint` och `svlang`. Nya
översättningsdeltan granskas dessutom med Hunspell och Gitleaks innan de
arkiveras.

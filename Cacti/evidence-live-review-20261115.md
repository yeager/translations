# Cacti `evidence`: svensk livegranskning 2026-11-15

## Aktuell källa och omfattning

- Tjänst: Cacti Translate / Weblate, komponent `cacti/evidence`.
- Komponenten var nåbar och olåst vid kontrollen.
- En färsk svensk PO-export innehåller 88 av 88 översatta poster, inga fuzzy
  poster och inga tomma måltexter.
- `msgfmt --check` godkände exporten. Källfilens två vanliga metadata-varningar
  avser en tom standardrevision och påverkar inte PO-syntaxen.

## Kontrollträffar

Weblate rapporterar tio fallerande kontroller för fyra svenska poster:

| Källa | Svensk måltext | Bedömning |
| --- | --- | --- |
| `Select any device, template, select any scan date or try search` | `Välj en enhet eller mall, ett skanningsdatum eller sök.` | Svensk fullständig instruktion med korrekt slutpunkt; behålls. |
| `No data. Allow periodic scan and store history in settings` | `Inga data. Aktivera periodisk skanning och lagring av historik i inställningarna.` | Svensk fullständig instruktion med korrekt slutpunkt; behålls. |
| `If you use only \`Scan Date\`, …` | `Om du bara använder ”Skanningsdatum” …` | Svensk fullständig instruktion med korrekt slutpunkt; behålls. |
| `Entity MIB` | `Entity MIB` | Etablerad MIB-beteckning; ska inte översättas. |

Inga översättningar laddades upp, eftersom kontrollträffarna inte visar något
språk- eller formatfel. Uppströmsgranskning eller releasepublicering är inte
verifierad.

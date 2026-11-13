# Obtainium – hämtnings-, import- och uppdateringstexter

Datum: 2026-11-14  
Komponent: `assets/translations/sv.json`  
Källversion: `v1.7.4`, publicerad 2026-11-01

## Granskning

Den svenska JSON-katalogen täcker alla 642 aktuella nycklar, men innehåller
fortfarande en större ny säkerhets- och uppdateringsdel på engelska. Den här
första batchen rättar sju vanliga texter med tydlig UI-kontext:

- uppackningsfel för hämtat arkiv
- misslyckad hämtning och hämtningsstorlek
- aviseringskanal för hämtat objekt
- filtrering med reguljära uttryck
- nedgraderingar bland uppdateringar
- import från Androids mapp Hämtade filer

## Kontroller

- JSON-syntax: godkänd
- Nyckeltäckning före och efter ändringen: 642/642
- `l10n-lint`: godkänd
- Hunspell-sv: inga stavfel i ändringarna
- `git diff --check`: godkänd
- Gitleaks: godkänd
- `msgfmt`: inte tillämpligt på JSON

## Upstream

Ändringarna är inskickade som
[ImranR98/Obtainium#3516](https://github.com/ImranR98/Obtainium/pull/3516).
PR:en är öppen; upstreamgranskning och merge återstår.

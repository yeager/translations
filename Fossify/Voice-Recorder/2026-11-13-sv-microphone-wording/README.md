# Fossify Röstinspelare – svenska mikrofonlägen

Datum: 2026-11-13  
Komponent: `app/src/main/res/values-sv/strings.xml`

## Granskning

Den svenska resursfilen jämfördes med den engelska källfilen. Samtliga 32
aktuella nycklar finns i båda filerna.

Fyra gränssnittstexter rättades:

- `Kamera` → `Kamera (video)`
- `Röstkommunikation` → `Röstkommunikation (automatisk förstärkning)`
- `Röstframförande` → `Röstläge med låg latens`
- `Inspelningen var för kort för att spela in!` → `Inspelningen blev för kort.`

Mikrofonlägena används för Androids ljudkällor. De tekniska skillnaderna
video, automatisk förstärkning och låg latens behöver därför synas i den
svenska inställningen.

## Kontroller

- XML-syntax: godkänd
- Nyckeltäckning: 32/32
- `l10n-lint`: godkänd
- Hunspell-sv: inga stavfel i ändringarna
- `svlang`: enbart en generell passiv-varning för den korta provtexten; ingen
  åtgärd behövs
- `git diff --check`: godkänd
- Gitleaks: godkänd
- Android-lint: inte körd lokalt eftersom Java Runtime saknas

## Upstream

Ändringarna är inskickade för granskning som
[FossifyOrg/Voice-Recorder#454](https://github.com/FossifyOrg/Voice-Recorder/pull/454).
PR:en är öppen; upstreamgranskning och merge återstår.

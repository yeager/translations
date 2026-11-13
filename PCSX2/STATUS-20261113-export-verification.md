# PCSX2: verifiering av svensk Crowdin-export

- Datum: 2026-11-13
- Export: `pcsx2-qt_en_sv-SE.xliff`
- SHA-256: `4a3b0aca533492d382daa314bc090b6e28bc00e7649b3da5b8227c213e66fe72`

Den aktuella XLIFF-exporten omfattar 5 345 översättningsenheter. Samtliga har
`state="translated"`. Exporten innehåller därmed inga oöversatta enheter att
komplettera i denna omgång.

En äldre lokal Qt-TS-export innehåller fem poster markerade `unfinished`. De
avser endast två strängar i tre gränssnittskontexter: **Target Page
Rearranging** och dess beskrivning. Samma enheter är översatta i den aktuella
XLIFF-exporten med *Omordning av målsidor* respektive *Ordnar om
minnessidorna för ett mål om spelet ändrar layouten på den aktuella
VRAM-adressen.* TS-filen används därför inte som underlag för en import.

Kontroller som passerade:

- `xmllint --noout` för XLIFF-filen
- Gitleaks för XLIFF-filen
- `lrelease` för den äldre TS-filen

Ingen ändringsfil skapades och inget skickades upp i denna kontroll, eftersom
den aktuella exporten redan innehåller översättningarna. Detta verifierar en
lokal export, inte godkännande eller merge uppströms.

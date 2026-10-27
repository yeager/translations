# Scene Manager: tid och flikar 10 — granskningsprotokoll

## Omfattning

16 källsträngar: avsnitt, flikar, status, funktionsval och inställningar för tid på dagen.

## Terminologi

- `overwrite file` är **åsidosättningsfil** och `User Settings` är **användarinställningar**.
- `feature` och `sub feature` är **funktion** och **underfunktion**.
- `Time of Day` är **tid på dagen**, inklusive i sammansättningen `time-of-day settings`.
- `Exterior Only` är **Endast utomhus**.

## Bevarade format

Tidsformatet `[{0} {1:.1f} h]` är oförändrat, inklusive hakparenteser, platshållare och precisionsspecifikation. Inga källradbrytningar förekommer.

## Kontrollkedja

JSON, `l10n-lint`, `svlang`, Hunspell, Gitleaks samt markör- och radbrytningsjämförelse körs mot batchfilen.

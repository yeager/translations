# Blender UI: verifiering av export 9, 2026-11-11

## Underlag

- Föregående fullständiga export: `blender-ui-ui-sv (8).po`.
- Verifieringsexport: `blender-ui-ui-sv (9).po`.
- Arkiverad importdelta:
  `blender-ui-sv-changes-since-1600-20261110-reconciled.po`.

## Resultat

Export 9 har samma **40 434** aktiva strängnycklar som export 8. Jämförelsen
visar **178** ändrade svenska måltexter. Deltat innehåller samma 178
översättningar och samtliga förekommer med exakt samma måltext i export 9:

| Kontroll | Resultat |
| --- | ---: |
| Deltats översatta poster | 178 |
| Ändrade måltexter mellan export 8 och 9 | 178 |
| Deltamåltexter som återfinns exakt i export 9 | 178 |
| Saknade eller avvikande deltamåltexter | 0 |
| Exportändringar utanför deltat | 0 |

`msgfmt --check --check-header --statistics` godkänner export 9 med
**40 434 översatta meddelanden**. Detta verifierar att hela den arkiverade
178-postersdeltan är införd i den nya Blender Translate-exporten. Det är inte
ett bevis för separat upstream-granskning, godkännande eller release.

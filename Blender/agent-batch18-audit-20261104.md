# Oberoende granskning: Blender Manual batch 18

Datum: 2026-11-04  
Granskad fil: `blender-manual-sv-review-batch-20261104-18.po`  
Jämförelser: den lokala råexporten för Blender Manual och den lokala
Blender UI-exporten.

## Resultat

| Källa | Bedömning | Kommentar |
| --- | --- | --- |
| `UsdGeomMesh` till meshobjekt | Godkänd | Kodmarkering och RST-länk är bevarade; *meshobjekt* är en naturlig, etablerad sammansättning. |
| `UsdVolVolume` till volymobjekt | Godkänd | `UsdVolVolume` och `OpenVDB` är korrekt bevarade som tekniska namn. |
| `UsdGeomPoints` till punktmolnsobjekt | Godkänd | *punktmoln* och *punktmolnsobjekt* anger rätt objekttyp. |
| `USD Shapes` till USD-former | Godkänd | Kort, idiomatisk rubrik utan felaktig versalisering. |
| `Display Purpose` till visningssyfte | Godkänd | RST-länkens URL och markering är identiska med källan. |
| `Material Purpose` till materialsyfte | Godkänd | Korrekt svensk sammansättning. |
| `allPurpose`-material | Godkänd | Det normerade USD-värdet är ordagrant bevarat. |
| `preview` med `allPurpose` som reserv | Godkänd | Det normerade värdet och reservordningen är bevarade. |
| `full` med reservordning | Ändra | Lägg till källans avslutande punkt: `... i den ordningen, som reserv.` |
| `Import USD Preview` | Ändra | Följ Blender UI-exportens etablerade namn: `Importera USD Preview`, inte `Importera USD-förhandsgranskning`. `USD Preview` är namnet på formatets/shaderns funktion. |
| `USD Preview Surface shaders` | Ändra | Följ UI-exportens terminologi och bindestreck: `Konvertera USD Preview Surface-shaders till Principled BSDF-shadernätverk.` |
| Texturer som inte kan lösas | Godkänd | *kan inte hittas* förmedlar här korrekt att sökvägsupplösningen kan misslyckas och är mer läsbart än en bokstavlig översättning. |
| `Textures Directory` till texturkatalog | Godkänd | Tydlig och korrekt teknisk sammansättning. |
| `File Name Collision` till filnamnskollision | Godkänd | Korrekt svensk sammansättning och betydelse. |
| `Use Existing` till använd befintlig | Godkänd | Stämmer med samma UI-sträng i den lokala Blender UI-exporten. |

## Kontrollresultat

- Exakta `msgid`-värden finns i råexporten och RST-markeringarna i batchen
  motsvarar källan.
- `msgfmt --check`: godkänd.
- `l10n-lint`: 0 fel, 0 varningar. Informationsnotiserna för `USD` är
  falska positiva träffar på tekniskt namn; kontrollens gränsteckennotis
  fångar den saknade avslutande punkten ovan.
- Gitleaks: inga hemligheter hittades.

Slutsats: 12 av 15 poster kan tas med oförändrade. Tre följdrättelser ovan
ska göras innan batchen räknas som slutligt godkänd.

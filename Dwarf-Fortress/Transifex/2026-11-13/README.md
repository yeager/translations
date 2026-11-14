# Dwarf Fortress – Transifex – 2026-11-13

Den här katalogen innehåller svenska granskningsbatcher för Dwarf Fortress Steam-resursen `text_set`.

Den innehåller även fortlöpande, separata deltafiler för resursen
`hardcoded_steam`. Råexporter lämnas orörda; varje ändringsbatch dokumenteras
och arkiveras separat.

## Omfattning

- Projekt: Dwarf Fortress
- Komponent: `text_set`
- Språk: svenska (`l:sv`)
- Källa: Transifex REST API, resurs `o:dwarf-fortress-translation:p:dwarf-fortress-steam:r:text_set`
- Batch 1: 10 tidigare oöversatta berättelserader
- Batch 2: 7 tidigare oöversatta boktitelsmallar
- Batch 3: 10 tidigare oöversatta boktitelsmallar
- Batch 4: 10 tidigare oöversatta boktitelsmallar
- Batch 5: 10 tidigare oöversatta boktitelsmallar
- Batch 6: 10 tidigare oöversatta boktitelsmallar
- Batch 7: 10 tidigare oöversatta boktitelsmallar
- Batch 8: 9 tidigare oöversatta boktitelsmallar
- Batch 9: 10 tidigare oöversatta boktitelsmallar
- Batch 10: 3 tidigare oöversatta boktitelsmallar
- Batch 11: 6 tidigare oöversatta boktitelsmallar
- Batch 12: 3 tidigare oöversatta boktitelsmallar
- Batch 13: 1 tidigare oöversatt berättelserad
- Batch 14: 10 tidigare oöversatta boktitelsmallar
- Batch 15: 10 tidigare oöversatta boktitelsmallar
- Batch 16: 10 tidigare oöversatta boktitelsmallar
- Batch 17: 11 tidigare oöversatta dialograder
- Batch 18: 10 tidigare oöversatta äventyrardialoger
- Batch 19: 1 tidigare oöversatt dialogfragment
- Råinventering: 349 oöversatta strängar före batchen. Råfilen är en oförändrad API-export från 2026-11-12.

## Status

Lokalt granskat, validerat, arkiverat och uppladdat via Transifex REST API 2026-11-13. Batch 1 gav HTTP 200 med 10 uppdateringar, batch 2 HTTP 200 med 7 uppdateringar, batch 3–7 och 9 HTTP 200 med 10 uppdateringar vardera, batch 8 HTTP 200 med 9 uppdateringar och batch 10 HTTP 200 med 3 uppdateringar. Direkt återläsning verifierade samtliga 89 måltexter.

Efter batch 18 visar en ny paginerad API-inventering 199 oöversatta svenska strängar i komponenten.

Detta är inte en markering som granskad i Transifex. De uppladdade raderna har översatts; granskningsstatus hanteras enligt projektets egna behörighetsflöde.

### `hardcoded_steam`

- Källa: Transifex REST API, resurs
  `o:dwarf-fortress-translation:p:dwarf-fortress-steam:r:hardcoded_steam`.
- Batcherna `hardcoded-steam-batch01` till `hardcoded-steam-batch56` har
  granskats i separata deltafiler och skickats in via API.
- Senaste verifierade batch: 56, med 7 strängar. API:t bekräftade importen och
  direkt återläsning matchade samtliga måltexter.
- Den aktuella API-frågan med `filter[translated]=false` returnerar fortsatt
  fler än en sida med oöversatta strängar. Något totalt antal får därför inte
  anges utan en fullständig paginerad inventering.
- Uppladdning betyder inte att strängarna är granskade, finaliserade eller
  publicerade i en release.

### Uppdatering 2026-11-14

- Batcherna 58–78 för `hardcoded_steam` består av 493 nya, separata svenska
  deltaöversättningar. Varje batch har skickats via Transifex JSON:API,
  kontrollerats lokalt och lästs tillbaka direkt från API:t efter import.
- Batchernas JSON-filer, statusposter och den uppdaterade terminologin finns i
  `../2026-11-14/`. Råexporter har inte ändrats.
- Senast verifierade komponentstatus via Transifex API: 2 762 översatta,
  23 657 oöversatta, 26 419 totalt och 915 granskade strängar.
- De uppladdade strängarna är inte därmed markerade som granskade, finaliserade
  eller publicerade. Dessa statusar hanteras separat av Transifex och projektet.

## Filer

- `dwarf-fortress-text-set-batch01-sv-20261113.jsonl`: oförändrad deltafil med de tio uppladdade måltexterna.
- `dwarf-fortress-text-set-batch02-sv-20261113.jsonl`: oförändrad deltafil med de sju uppladdade boktitelsmallarna.
- `dwarf-fortress-text-set-batch03-sv-20261113.jsonl`: oförändrad deltafil med de tio uppladdade boktitelsmallarna.
- `dwarf-fortress-text-set-batch04-sv-20261113.jsonl`: oförändrad deltafil med de tio uppladdade boktitelsmallarna.
- `dwarf-fortress-text-set-batch05-sv-20261113.jsonl`: oförändrad deltafil med de tio uppladdade boktitelsmallarna.
- `dwarf-fortress-text-set-batch06-sv-20261113.jsonl`: oförändrad deltafil med de tio uppladdade boktitelsmallarna.
- `dwarf-fortress-text-set-batch07-sv-20261113.jsonl`: oförändrad deltafil med de tio uppladdade boktitelsmallarna.
- `dwarf-fortress-text-set-batch08-sv-20261113.jsonl`: oförändrad deltafil med de nio uppladdade boktitelsmallarna.
- `dwarf-fortress-text-set-batch09-sv-20261113.jsonl`: oförändrad deltafil med de tio uppladdade boktitelsmallarna.
- `dwarf-fortress-text-set-batch10-sv-20261113.jsonl`: oförändrad deltafil med de tre uppladdade boktitelsmallarna.
- `dwarf-fortress-text-set-batch11-sv-20261113.jsonl`: oförändrad deltafil med de sex uppladdade boktitelsmallarna.
- `dwarf-fortress-text-set-batch12-sv-20261113.jsonl`: oförändrad deltafil med de tre uppladdade boktitelsmallarna.
- `dwarf-fortress-text-set-batch13-sv-20261113.jsonl`: oförändrad deltafil med den uppladdade berättelseraden.
- `dwarf-fortress-text-set-batch14-sv-20261113.jsonl`: oförändrad deltafil med de tio uppladdade boktitelsmallarna.
- `dwarf-fortress-text-set-batch15-sv-20261113.jsonl`: oförändrad deltafil med de tio uppladdade boktitelsmallarna.
- `dwarf-fortress-text-set-batch16-sv-20261113.jsonl`: oförändrad deltafil med de tio uppladdade boktitelsmallarna.
- `dwarf-fortress-text-set-batch17-sv-20261113.jsonl`: oförändrad deltafil med de elva uppladdade dialograderna.
- `dwarf-fortress-text-set-batch18-sv-20261113.jsonl`: oförändrad deltafil med de tio uppladdade äventyrardialogerna.
- `dwarf-fortress-text-set-batch19-sv-20261113.jsonl`: oförändrad deltafil med det uppladdade dialogfragmentet.
- `dwarf-fortress-text-set-missing-raw-20261112.json`: oförändrad råexport av den inventering som låg till grund för batchen.
- `TERMINOLOGY.md`: beslut för återkommande speltermer i denna batch.
- `STATUS.md` samt batchspecifika statusfiler: kontroller och verifieringsresultat.
- `dwarf-fortress-hardcoded-steam-batch*-sv-20261113.json`: separata, rena
  deltafiler för `hardcoded_steam`.

Råexporten ska inte redigeras. Korrigeringar och kommande granskning ska ligga i nya deltafiler.

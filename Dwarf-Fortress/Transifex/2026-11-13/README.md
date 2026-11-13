# Dwarf Fortress – Transifex – 2026-11-13

Den här katalogen innehåller svenska granskningsbatcher för Dwarf Fortress Steam-resursen `text_set`.

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
- Råinventering: 349 oöversatta strängar före batchen. Råfilen är en oförändrad API-export från 2026-11-12.

## Status

Lokalt granskat, validerat, arkiverat och uppladdat via Transifex REST API 2026-11-13. Batch 1 gav HTTP 200 med 10 uppdateringar, batch 2 HTTP 200 med 7 uppdateringar samt batch 3–5 HTTP 200 med 10 uppdateringar vardera. Direkt återläsning verifierade samtliga 47 måltexter.

Efter batch 5 visar en ny paginerad API-inventering 302 oöversatta svenska strängar i komponenten.

Detta är inte en markering som granskad i Transifex. De uppladdade raderna har översatts; granskningsstatus hanteras enligt projektets egna behörighetsflöde.

## Filer

- `dwarf-fortress-text-set-batch01-sv-20261113.jsonl`: oförändrad deltafil med de tio uppladdade måltexterna.
- `dwarf-fortress-text-set-batch02-sv-20261113.jsonl`: oförändrad deltafil med de sju uppladdade boktitelsmallarna.
- `dwarf-fortress-text-set-batch03-sv-20261113.jsonl`: oförändrad deltafil med de tio uppladdade boktitelsmallarna.
- `dwarf-fortress-text-set-batch04-sv-20261113.jsonl`: oförändrad deltafil med de tio uppladdade boktitelsmallarna.
- `dwarf-fortress-text-set-batch05-sv-20261113.jsonl`: oförändrad deltafil med de tio uppladdade boktitelsmallarna.
- `dwarf-fortress-text-set-missing-raw-20261112.json`: oförändrad råexport av den inventering som låg till grund för batchen.
- `TERMINOLOGY.md`: beslut för återkommande speltermer i denna batch.
- `STATUS.md` samt `STATUS-batch02.md` till och med `STATUS-batch05.md`: kontroller och verifieringsresultat.

Råexporten ska inte redigeras. Korrigeringar och kommande granskning ska ligga i nya deltafiler.

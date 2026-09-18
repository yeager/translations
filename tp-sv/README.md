# Granskade svenska TP-översättningar

Granskning 2026-09-18: samtliga 9 483 aktiva poster i de 15 domänerna nedan är genomlästa. PO-filerna innehåller sammanlagt 2 008 rättade poster. Hela TP-granskningen pågår fortfarande.

Granskningen omfattar betydelse, terminologi, språkbruk och formatsträngar, med l10n-lint 1.20.2, [Swedish FOSS terminology](https://github.com/yeager/swedish-foss-terminology) och [Swedish TM](https://github.com/yeager/swedish-tm) som stöd. Programmens dokumentation och källkod har kontrollerats där sammanhanget kräver det. CLISP:s ändrade pluraluttryck har dessutom provkörts med en Common Lisp-tolk.

Varje diff jämför den kompletta redigerade PO-filen med den befintliga svenska filen hos Translation Project, i exakt den version som länkas i tabellen. Diffarna har provapplicerats utan tolerans och återskapar respektive redigerad PO-fil byte för byte. Alla publicerade PO-filer klarar `msgfmt --check --check-format`. Befintliga fuzzy-markeringar, kommentarer och upphovsuppgifter är bevarade; gettext hoppar normalt över formatkontroll av fuzzy-poster.

| Domän | Version | Granskade poster | Rättade poster | PO | Diff | Original hos TP |
| --- | --- | ---: | ---: | --- | --- | --- |
| a2ps | 4.15.5 | 157 | 10 | [PO](a2ps-4.15.5.sv.po) | [Diff](diff/a2ps-4.15.5.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/a2ps-4.15.5.sv.po) |
| anubis | 4.3 | 307 | 21 | [PO](anubis-4.3.sv.po) | [Diff](diff/anubis-4.3.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/anubis-4.3.sv.po) |
| aspell | 0.60.8.2 | 302 | 14 | [PO](aspell-0.60.8.2.sv.po) | [Diff](diff/aspell-0.60.8.2.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/aspell-0.60.8.2.sv.po) |
| bash | 5.3-rc2 | 612 | 42 | [PO](bash-5.3-rc2.sv.po) | [Diff](diff/bash-5.3-rc2.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/bash-5.3-rc2.sv.po) |
| beebase | 1.2 | 891 | 21 | [PO](beebase-1.2.sv.po) | [Diff](diff/beebase-1.2.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/beebase-1.2.sv.po) |
| bfd | 2.46.90 | 2040 | 867 | [PO](bfd-2.46.90.sv.po) | [Diff](diff/bfd-2.46.90.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/bfd-2.46.90.sv.po) |
| binutils | 2.46.90 | 2751 | 562 | [PO](binutils-2.46.90.sv.po) | [Diff](diff/binutils-2.46.90.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/binutils-2.46.90.sv.po) |
| bison | 3.7.90 | 253 | 45 | [PO](bison-3.7.90.sv.po) | [Diff](diff/bison-3.7.90.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/bison-3.7.90.sv.po) |
| bison-runtime | 3.5.90 | 9 | 4 | [PO](bison-runtime-3.5.90.sv.po) | [Diff](diff/bison-runtime-3.5.90.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/bison-runtime-3.5.90.sv.po) |
| buzztrax | 0.10.0 | 362 | 86 | [PO](buzztrax-0.10.0.sv.po) | [Diff](diff/buzztrax-0.10.0.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/buzztrax-0.10.0.sv.po) |
| ccd2cue | 0.5 | 46 | 21 | [PO](ccd2cue-0.5.sv.po) | [Diff](diff/ccd2cue-0.5.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/ccd2cue-0.5.sv.po) |
| ccide | 0.6.6pre1 | 25 | 1 | [PO](ccide-0.6.6pre1.sv.po) | [Diff](diff/ccide-0.6.6pre1.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/ccide-0.6.6pre1.sv.po) |
| cflow | 1.8 | 165 | 6 | [PO](cflow-1.8.sv.po) | [Diff](diff/cflow-1.8.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/cflow-1.8.sv.po) |
| chambercourt | 0.9.40 | 12 | 1 | [PO](chambercourt-0.9.40.sv.po) | [Diff](diff/chambercourt-0.9.40.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/chambercourt-0.9.40.sv.po) |
| clisp | 2.49.60 | 1551 | 307 | [PO](clisp-2.49.60.sv.po) | [Diff](diff/clisp-2.49.60.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/clisp-2.49.60.sv.po) |

För att applicera en diff: lägg motsvarande svenska originalfil i aktuell katalog och kör exempelvis:

```sh
patch --fuzz=0 -p1 < diff/clisp-2.49.60.sv.po.diff
```

Exakta källadresser, hämtningstidpunkter och SHA-256-kontrollsummor finns i [review-manifest.json](review-manifest.json).

De tidigare befintliga util-linux-filerna omfattas inte av denna granskningsomgång.

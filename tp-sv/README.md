# Granskade svenska TP-översättningar

Granskning 2026-09-18: samtliga 23 626 aktiva poster i de 28 domänerna nedan är genomlästa. PO-filerna innehåller sammanlagt 6 671 rättade poster. Hela TP-granskningen pågår fortfarande.

Granskningen omfattar betydelse, terminologi, språkbruk och formatsträngar, med l10n-lint 1.20.3 inklusive [rättningen för portabla PRI-format](https://github.com/yeager/l10n-lint/pull/10), senaste rättade svlang, hunspell-sv och aspell-sv samt [Swedish FOSS terminology](https://github.com/yeager/swedish-foss-terminology) och [Swedish TM](https://github.com/yeager/swedish-tm) som stöd. Programmens dokumentation och källkod har kontrollerats där sammanhanget kräver det. CLISP:s ändrade pluraluttryck har dessutom provkörts med en Common Lisp-tolk.

PO-filernas befintliga uppdelning på fysiska rader bevaras för oförändrade textdelar. Ren PO-omformatering räknas inte som en rättad post.

Varje diff jämför den kompletta redigerade PO-filen med den befintliga svenska filen hos Translation Project, i exakt den version som länkas i tabellen. Diffarna har provapplicerats utan tolerans och återskapar respektive redigerad PO-fil byte för byte. Alla publicerade PO-filer klarar `msgfmt --check --check-format`. Befintliga fuzzy-markeringar, kommentarer och upphovsuppgifter är bevarade; gettext hoppar normalt över formatkontroll av fuzzy-poster.

| Domän | Version | Granskade poster | Rättade poster | PO | Diff | Original hos TP |
| --- | --- | ---: | ---: | --- | --- | --- |
| a2ps | 4.15.5 | 157 | 10 | [PO](a2ps-4.15.5.sv.po) | [Diff](diff/a2ps-4.15.5.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/a2ps-4.15.5.sv.po) |
| anubis | 4.3 | 307 | 21 | [PO](anubis-4.3.sv.po) | [Diff](diff/anubis-4.3.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/anubis-4.3.sv.po) |
| aspell | 0.60.8.2 | 302 | 14 | [PO](aspell-0.60.8.2.sv.po) | [Diff](diff/aspell-0.60.8.2.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/aspell-0.60.8.2.sv.po) |
| bash | 5.3-rc2 | 612 | 43 | [PO](bash-5.3-rc2.sv.po) | [Diff](diff/bash-5.3-rc2.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/bash-5.3-rc2.sv.po) |
| beebase | 1.2 | 891 | 22 | [PO](beebase-1.2.sv.po) | [Diff](diff/beebase-1.2.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/beebase-1.2.sv.po) |
| bfd | 2.46.90 | 2040 | 870 | [PO](bfd-2.46.90.sv.po) | [Diff](diff/bfd-2.46.90.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/bfd-2.46.90.sv.po) |
| binutils | 2.46.90 | 2751 | 562 | [PO](binutils-2.46.90.sv.po) | [Diff](diff/binutils-2.46.90.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/binutils-2.46.90.sv.po) |
| bison | 3.7.90 | 253 | 45 | [PO](bison-3.7.90.sv.po) | [Diff](diff/bison-3.7.90.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/bison-3.7.90.sv.po) |
| bison-runtime | 3.5.90 | 9 | 4 | [PO](bison-runtime-3.5.90.sv.po) | [Diff](diff/bison-runtime-3.5.90.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/bison-runtime-3.5.90.sv.po) |
| buzztrax | 0.10.0 | 362 | 86 | [PO](buzztrax-0.10.0.sv.po) | [Diff](diff/buzztrax-0.10.0.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/buzztrax-0.10.0.sv.po) |
| ccd2cue | 0.5 | 46 | 22 | [PO](ccd2cue-0.5.sv.po) | [Diff](diff/ccd2cue-0.5.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/ccd2cue-0.5.sv.po) |
| ccide | 0.6.6pre1 | 25 | 1 | [PO](ccide-0.6.6pre1.sv.po) | [Diff](diff/ccide-0.6.6pre1.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/ccide-0.6.6pre1.sv.po) |
| cflow | 1.8 | 165 | 6 | [PO](cflow-1.8.sv.po) | [Diff](diff/cflow-1.8.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/cflow-1.8.sv.po) |
| chambercourt | 0.9.40 | 12 | 1 | [PO](chambercourt-0.9.40.sv.po) | [Diff](diff/chambercourt-0.9.40.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/chambercourt-0.9.40.sv.po) |
| clisp | 2.49.60 | 1551 | 307 | [PO](clisp-2.49.60.sv.po) | [Diff](diff/clisp-2.49.60.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/clisp-2.49.60.sv.po) |
| coreutils | 9.12-pre1 | 2443 | 428 | [PO](coreutils-9.12-pre1.sv.po) | [Diff](diff/coreutils-9.12-pre1.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/coreutils-9.12-pre1.sv.po) |
| cpio | 2.15 | 317 | 47 | [PO](cpio-2.15.sv.po) | [Diff](diff/cpio-2.15.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/cpio-2.15.sv.po) |
| cppi | 1.17 | 61 | 7 | [PO](cppi-1.17.sv.po) | [Diff](diff/cppi-1.17.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/cppi-1.17.sv.po) |
| cpplib | 16.1-b20260222 | 319 | 37 | [PO](cpplib-16.1-b20260222.sv.po) | [Diff](diff/cpplib-16.1-b20260222.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/cpplib-16.1-b20260222.sv.po) |
| cryptsetup | 2.8.8-rc0 | 921 | 223 | [PO](cryptsetup-2.8.8-rc0.sv.po) | [Diff](diff/cryptsetup-2.8.8-rc0.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/cryptsetup-2.8.8-rc0.sv.po) |
| datamash | 1.4.12.1 | 133 | 22 | [PO](datamash-1.4.12.1.sv.po) | [Diff](diff/datamash-1.4.12.1.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/datamash-1.4.12.1.sv.po) |
| denemo | 2.6-rc2 | 6301 | 2379 | [PO](denemo-2.6-rc2.sv.po) | [Diff](diff/denemo-2.6-rc2.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/denemo-2.6-rc2.sv.po) |
| dfarc | 3.14 | 137 | 43 | [PO](dfarc-3.14.sv.po) | [Diff](diff/dfarc-3.14.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/dfarc-3.14.sv.po) |
| dico | 2.10.90 | 644 | 211 | [PO](dico-2.10.90.sv.po) | [Diff](diff/dico-2.10.90.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/dico-2.10.90.sv.po) |
| diffutils | 3.10.242 | 265 | 127 | [PO](diffutils-3.10.242.sv.po) | [Diff](diff/diffutils-3.10.242.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/diffutils-3.10.242.sv.po) |
| dink | 1.08.20190120 | 2221 | 1038 | [PO](dink-1.08.20190120.sv.po) | [Diff](diff/dink-1.08.20190120.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/dink-1.08.20190120.sv.po) |
| direvent | 5.5 | 267 | 81 | [PO](direvent-5.5.sv.po) | [Diff](diff/direvent-5.5.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/direvent-5.5.sv.po) |
| doodle | 0.7.2 | 114 | 14 | [PO](doodle-0.7.2.sv.po) | [Diff](diff/doodle-0.7.2.sv.po.diff) | [Original](https://translationproject.org/PO-files/sv/doodle-0.7.2.sv.po) |

För att applicera en diff: lägg motsvarande svenska originalfil i aktuell katalog och kör exempelvis:

```sh
patch --fuzz=0 -p1 < diff/clisp-2.49.60.sv.po.diff
```

Exakta källadresser, hämtningstidpunkter och SHA-256-kontrollsummor finns i [review-manifest.json](review-manifest.json).

De tidigare befintliga util-linux-filerna omfattas inte av denna granskningsomgång.

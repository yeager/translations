# Batch 132: ögonblicksbildsdialog

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 18 aktiva meddelanden i `UITakeSnapshotDialog` har granskats
radvis tillsammans med dialogens åtgärdsknappar och pluraltext.

## Resultat

Åtgärdsverbet har normaliserats från `spara` till `ta` i dialogrubriken,
bekräftelseåtgärden och avbrytande hjälpttext. Det motsvarar källans `Take
Snapshot` och etablerad terminologi i VirtualBox-katalogen.

Ändringarna finns i lokal commit `99647ee` och är ännu inte pushade till PR:n.

## Kontroller

- XPath-räkning: 18 aktiva meddelanden.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt granskat och arkiverat. Upstream-inskick väntar tills den fullständiga
kataloggranskningen är klar.

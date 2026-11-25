# GNOME Firmware — master / po

- Aktivitet: <https://l10n.gnome.org/vertimus/gnome-firmware/master/po/sv/>
- PO och POT hämtades från Damned Lies 2026-11-25; POT-datum 2026-10-27. Båda originalfilerna är arkiverade här.
- Före granskning enligt aktuell PO: 263 översatta, 1 fuzzy, 5 oöversatta (269 poster).
- Efter granskning: 269 översatta, 0 fuzzy, 0 oöversatta.
- Ändringar: 5 nya översättningar och 45 korrigeringar av befintlig svenska; 50 aktiva poster ändrades. Granskningen omfattade hela katalogen. Rättade bland annat batteri-/strömmeddelanden, firmwareterminologi, missvisande pluraler, ordvalet ”Erhållande av …” och grammatik i statusmeddelanden.
- Terminologi: *firmware* → *fast programvara*, *device programmer* → *enhetsprogrammerare*, *Vendor ID* → *tillverkar-ID* (plural *tillverkar-ID:n*), *CAB archive* → *CAB-arkiv*.
- Validering: `msgfmt --check --statistics` och `msgcmp` godkända. Egen kontroll av platshållare, pluralformer och acceleratorer utan avvikelse. `l10n-lint`: 0 fel och 0 varningar; endast informationsnotiser om korrekt flyttade acceleratorer.
- Hunspell: kontrollerat med `hunspell -d sv_SE`. Kvarvarande okända token finns i `hunspell-unknown.txt`: produkt-/protokollnamnen AppStream, LVFS, fwupd; giltiga tekniska sammansättningar och avledningar; samt ordfragment från acceleratormarkeringen `_` (bl.a. `_Avbryt`, `_Nedgradera`). Inga felstavningar i löptext lämnades.
- GNOME-inskick: inget. Granskningen är arkiverad lokalt och inte skickad till GNOME.

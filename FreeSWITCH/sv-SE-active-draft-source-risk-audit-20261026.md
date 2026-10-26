# Aktiva manusutkast: källrisker

Granskningen gäller de fem manusutkast som den lokala källsökningen kopplar till aktiva FreeSWITCH-anrop. Inget manus har ändrats till godkänt och inget ljud är godkänt.

## Å, ä och ö i `say_spell`

Utkasten `ascii/132.wav` (*ä*), `ascii/134.wav` (*å*) och `ascii/148.wav` (*ö*) väljs via `ascii/<heltal>`. I `mod_say_sv.c` vid commit `02857682b56626f06f72b91730415084b892bfee` itererar `say_spell` bytevis, anropar `tolower((int)*p)` och använder resultatet som resurs-ID. En isolerad modell av byteoperationen visar att CP437-bytesekvenserna 0x84, 0x86 och 0x94 ger de förväntade ID-numren 132, 134 och 148. Samma bokstäver i UTF-8 ger i stället byteparen 195+164, 195+165 och 195+182. Modellen verifierar inte vilket format verkliga anropare använder.

Den tillgängliga FreeSWITCH-checkouten saknar headers, konfiguration och körbar runtime; inget anropsprov har därför körts. Om `char` är signed är dessutom `tolower` på högbitbyte odefinierat enligt C. De tre manusen ligger kvar som `DRAFT_NOT_APPROVED`. Innan de kan godkännas behövs full runtimekontroll av indataformat och valda resursvägar, samt en definierad lowercase-hantering för högbitbyte. Beräkningsmodellen finns i `spell-byte-mapping-runtime-model.json` och `test_spell_byte_mapping.py`.

## Voicemail: samma fras i två betydelser

`voicemail_greeting_selected` spelar `vm-meddelande_nummer`, säger numret och spelar `vm-markerad`. Den engelska makron säger `vm-greeting`, numret och `vm-selected`. Den svenska sekvensen säger alltså ”meddelande nummer [n] markerad” i stället för ”hälsning [n] vald”; dessutom böjs *markerad* inte efter neutrumordet *meddelande*. Samtidigt använder `voicemail_say_message_number` samma `vm-meddelande_nummer` korrekt. Den filen kan därför inte rättas globalt utan att den andra sekvensen blir fel.

Det finns redan ett lokalt förslag som delar upp hälsningstexten i `vm-halsning_nummer` (*Hälsning nummer*) och `vm-ar_vald` (*är vald*). Det behöver kopplas in i FreeSWITCH-grenen innan dessa två nya ljudresurser kan vara aktiva. De två föreslagna fraserna kontrollerades på nytt: l10n-lint med projektets ordlista gav 0 fel och varningar, svlang gav 0 skrivregelproblem och anglicismer och svensk Hunspell gav 0 okända ord. Det gäller textfragmenten, inte ljud eller källintegration.

## Beslut

De fem posterna står kvar som `DRAFT_NOT_APPROVED`. Källgranskningen identifierar en osäker teckenavkodning och en bekräftad voicemailöversättningsmiss, men kan inte godkänna uttalet i några WAV-filer. Se [maskinläsbar audit](active-draft-source-risk-audit-2026-10-26.json), [föreslagen voicemailkorrigering](proposed-pr3242-greeting-selected-correction.patch) och [täckningsaudit](draft-resource-global-coverage.json).

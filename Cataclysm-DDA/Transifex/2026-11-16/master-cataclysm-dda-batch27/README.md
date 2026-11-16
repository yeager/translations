# Cataclysm-DDA, svenska: batch 27

Tio aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De fortsätter med slutmeddelanden från samma
mekanik för att krossa lik och avslutas med ett slaktmeddelande.

Källkontexten kontrollerades mot aktuell upstream-källkod i
`pulp_activity_actor::send_final_message`. Måltexten undviker fasta svenska
ägandepronomen framför verktygsplatshållare eftersom verktygets grammatiska
genus är okänt vid körning. `pulp` översätts konsekvent som `krossa lik`.

## Kontroller före API-inskick

- Platsmarkörer, inklusive `%1$s` och `%2$s`, ska stämma mellan källa och mål.
- Singular och plural kontrolleras var för sig för den enda pluralsträngen.
- `l10n-lint --language sv --json-format auto` ska passera utan varningar eller fel.
- Hunspell-SV och svlang ska granskas manuellt för sammansättningar,
  platshållare och projektspecifika termer.
- Ingen otillåten em dash får tillföras. `msgfmt` är inte tillämpligt eftersom
  Transifex API tar enskilda JSON-översättningar, inte en PO-katalog.

## Inskick och återläsning

Den 16 november 2026 sparades samtliga tio översättningar via Transifex API.
En ny, oberoende GET-återläsning jämförde sedan måltexten, inklusive båda
pluralformerna, med denna batch. Alla 10 av 10 stämde exakt.

svlang markerade två förväntade falska träffar: en infinitivfras och en
grammatiskt korrekt `eftersom`-bisats. Hunspell-SV markerade endast de
projektspecifika sammansättningarna `okrossad`, `okrossade` och `okrossat`.

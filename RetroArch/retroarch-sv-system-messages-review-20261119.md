# RetroArch – systemmeddelanden, svensk granskningsbatch 2026-11-19

Åtta oöversatta svenska strängar i RetroArchs huvudfil msg_hash_us.json har granskats från aktuella Crowdin API-svar. Förslagen är inte sparade eller skickade till Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 6234797 | Display Pacing On VBlank Events | — | Bildsynkronisering vid VBlank-händelser |
| 6238633 | Show 'Quit' | — | Visa ”Avsluta” |
| 6238635 | Show the 'Quit' option in the Main Menu. | — | Visa alternativet ”Avsluta” i huvudmenyn. |
| 6238637 | Show 'Restart' | — | Visa ”Starta om” |
| 6238639 | Show the 'Restart' option in the Main Menu. | — | Visa alternativet ”Starta om” i huvudmenyn. |
| 6239313 | Android Disconnect Workaround | — | Tillfällig lösning för Android-frånkoppling |
| 6239321 | Run-Ahead could not restore the core's state. The core was reset and Run-Ahead has been disabled. | — | Run-Ahead kunde inte återställa kärnans tillstånd. Kärnan återställdes och Run-Ahead har inaktiverats. |
| 6239351 | Answer the Security Warning first. | — | Svara först på säkerhetsvarningen. |

## Kontroller

- Inga platshållare, markup-taggar eller URL:er förekommer i batchen.
- l10n-lint med svenska regler passerade utan anmärkningar.
- Hunspell-sv markerade VBlank-händelser och Run-Ahead som tekniska/projektspecifika termer.
- Crowdins förhandsvalidering markerade bara VBlank-händelser som möjlig felstavning. Ingen annan QA-kategori flaggade batchen.

## Firmwaremeddelanden med bekräftade radbrytningar

Crowdins editor bekräftar att källsträngarna 6234787 och 6234789 använder riktiga radbrytningar. Förslagen nedan ska därför använda samma radbrytningar, inte bokstavliga \n-sekvenser.

**6234787**

> Om du väljer OK hämtas och installeras den firmware som är märkt med ”Den här firmware kan hämtas.”.  
> All annan saknad firmware måste tillhandahållas enligt lokal lagstiftning.  
>
> Välj Avbryt för att fortsätta utan att hämta.  
>
> Obs! Du kan stänga av dessa meddelanden i Inställningar -> Kärna -> Meddelanden om saknad firmware.

**6234789**

> Välj OK för att starta utan denna firmware, eller Avbryt för att avbryta starten av kärnan.  
>
> Obs! Du kan stänga av dessa meddelanden i Inställningar -> Kärna -> Meddelanden om saknad firmware.

l10n-lint godkänner formatet. Crowdins API-förhandsvalidering rapporterar felaktigt att måltexterna saknar radbrytningar, men accepterar felaktigt bokstavliga \n-sekvenser. Editorvyn visar att linterregeln följer den faktiska källformateringen. Förslagen är fortfarande utkast och har inte sparats i Crowdin.

## Omfattning

Detta är en avgränsad batch från de 81 oöversatta strängarna i huvudfilen vid API-hämtningen. Den ersätter inte en fullständig svensk granskning av RetroArch.

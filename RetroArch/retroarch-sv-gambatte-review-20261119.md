# RetroArch Gambatte – svensk granskningsbatch 2026-11-19

Fyra befintliga svenska Gambatte-översättningar i filen gambatte-libretro.json har granskats via Crowdin API. Förslagen är inte sparade eller skickade till Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 4591575 | Enables colorization of Game Boy games. 'Auto' selects the 'best' (most colorful/appropriate) palette. 'GBC' selects game-specific Game Boy Color palette if defined, otherwise 'GBC - Dark Green'. 'SGB' selects game-specific Super Game Boy palette if defined, otherwise 'SGB - 1A'. 'Internal' uses 'Internal Palette' core option. 'Custom' loads user-created palette from system directory. | Aktiverar färgläggning av Game Boy-spel. ”Auto” väljer den ”bästa” … ”Intern” använder ”Intern palett” kärninställningen. | Aktiverar färgläggning av Game Boy-spel. ”Auto” väljer den ”bästa” (mest färgglada eller lämpliga) paletten. ”GBC” väljer den spelspecifika Game Boy Color-paletten om den är definierad, annars ”GBC - Mörkgrön”. ”SGB” väljer den spelspecifika Super Game Boy-paletten om den är definierad, annars ”SGB - 1A”. ”Intern” använder kärninställningen ”Intern palett”. ”Anpassad” läser in en användarskapad palett från systemkatalogen. |
| 4591589 | Selects palette used for colorizing Game Boy games when 'GB Colorization' is set to 'Internal', or when 'GB Colorization' is set to 'Auto' and game has no pre-defined SGB/GBC palette. 'GB' palettes mimic the display of original Game Boy hardware. 'GBC' palettes are identical to the built-in presets of the Game Boy Color. 'SGB' palettes are identical to the built-in presets of the Super Game Boy. | Väljer en palett som används … GB-paletter återskapar skärmen hos ursprunglig Game Boy-hårdvara. | Väljer den palett som används för att färglägga Game Boy-spel när ”GB-färgläggning” är inställd på ”Intern”, eller när ”GB-färgläggning” är inställd på ”Automatiskt” och spelet saknar en fördefinierad SGB- eller GBC-palett. GB-paletter efterliknar skärmen på den ursprungliga Game Boy-maskinvaran. GBC-paletter är identiska med de inbyggda förinställningarna för Game Boy Color. SGB-paletter är identiska med de inbyggda förinställningarna för Super Game Boy. |
| 4592109 | Selects internal colorization palette when 'Internal Palette' is set to 'PixelShift - Pack 1'. | Väljer intern färgsättningspalett … | Väljer intern färgläggningspalett när ”Intern palett” är inställd på ”PixelShift - Pack 1”. |
| 4592233 | Simulates LCD ghosting effects. 'Simple' performs a 50:50 mix of the current and previous frames. 'LCD Ghosting' mimics natural LCD response times by combining multiple buffered frames. 'Simple' blending is required when playing games that rely on LCD ghosting for transparency effects (Wave Race, Ballistic, Chikyuu Kaihou Gun ZAS...). | Simulerar LCD-efterbildseffekter. ”Enkel” utför en 50:50-mix … med inkonsekventa citattecken och termen LCD-spökeffekter. | Simulerar LCD-efterbildseffekter. ”Enkel” blandar den aktuella och föregående bildrutan i förhållandet 50:50. ”LCD-efterbilder” efterliknar naturliga LCD-svarstider genom att kombinera flera buffrade bildrutor. Läget ”Enkel” krävs när du spelar spel som använder LCD-efterbilder för genomskinlighetseffekter (Wave Race, Ballistic, Chikyuu Kaihou Gun ZAS...). |

## Kontroller

- RetroArchs projekt-TM söktes via API. Den bekräftade den befintliga PixelShift-strängen, men den här batchen förbättrar dess svenska term.
- l10n-lint med svenska regler passerade utan anmärkningar.
- Crowdin QA och Hunspell markerade Game Boy, GBC, SGB, PixelShift, LCD-efterbildseffekter och speltitlar. Det är produktnamn, kodnamn eller korrekta svenska sammansättningar, inte visade stavfel.
- Parenteserna i sträng 4591575 bevaras efter Crowdins QA-kontroll.

## Omfattning

Gambatte har 357 QA-flaggar i den aktuella API-hämtningen. Majoriteten är avsiktligt oöversatta palett- och produktnamn; denna batch omfattar endast fyra tydliga språkförbättringar.

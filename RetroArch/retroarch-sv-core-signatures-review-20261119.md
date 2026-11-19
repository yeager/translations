# RetroArch – kärnsignaturer, svensk granskningsbatch 2026-11-19

18 oöversatta svenska strängar i RetroArchs huvudfil `msg_hash_us.json` har granskats från aktuella Crowdin API-svar. Alla var oöversatta vid hämtningen. Förslagen är inte sparade eller skickade till Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 6234707 | Warn before running a core that libretro didn't sign or that has changed since. | — | Varna innan en kärna körs som libretro inte har signerat eller som har ändrats sedan dess. |
| 6234709 | This build trusts a test signing key: cores anyone can sign will run. Not for everyday use. | — | Den här versionen litar på en testsigneringsnyckel: kärnor som vem som helst kan signera kommer att köras. Inte för daglig användning. |
| 6234711 | RetroArch now checks core signatures. Your cores stay trusted; Update Installed Cores gets signed ones. | — | RetroArch kontrollerar nu kärnsignaturer. Dina kärnor fortsätter att vara betrodda; Uppdatera installerade kärnor hämtar signerade kärnor. |
| 6234713 | This core isn't signed by libretro. | — | Den här kärnan är inte signerad av libretro. |
| 6234715 | This core has been changed since libretro signed it. | — | Den här kärnan har ändrats sedan libretro signerade den. |
| 6234717 | This is an older version of the core than one you've used before. Older versions can have security problems. | — | Det här är en äldre version av kärnan än den du har använt tidigare. Äldre versioner kan ha säkerhetsproblem. |
| 6234719 | This core is signed with a key RetroArch doesn't know. | — | Den här kärnan är signerad med en nyckel som RetroArch inte känner till. |
| 6234721 | RetroArch couldn't read this core to check it. | — | RetroArch kunde inte läsa den här kärnan för att kontrollera den. |
| 6234723 | Cores are programs with full access to your device and files. Only continue if you built this core yourself or got it from someone you trust. | — | Kärnor är program med fullständig åtkomst till din enhet och dina filer. Fortsätt bara om du själv har byggt kärnan eller fått den från någon du litar på. |
| 6234725 | You can turn these checks off in Settings > Core > Check Core Signatures. | — | Du kan stänga av kontrollerna i Inställningar > Kärna > Kontrollera kärnsignaturer. |
| 6234727 | Core download failed the signature check and was not installed. | — | Hämtningen av kärnan klarade inte signaturkontrollen och installerades inte. |
| 6234729 | Core download is older than one already used; installed core kept. | — | Den hämtade kärnan är äldre än en version som redan har använts; den installerade kärnan behölls. |
| 6234731 | Turning this off lets RetroArch run cores that may have been tampered with, including ones downloaded by the Online Updater. Only do this if you build or install cores yourself and understand the risk. | — | Om du stänger av detta kan RetroArch köra kärnor som kan ha manipulerats, även sådana som har hämtats av Nätuppdateraren. Gör bara detta om du själv bygger eller installerar kärnor och förstår risken. |
| 6234733 | This can't be changed now: RetroArch couldn't read its list of trusted cores. | — | Det går inte att ändra detta nu: RetroArch kunde inte läsa listan över betrodda kärnor. |
| 6234735 | Core not loaded: RetroArch couldn't confirm it is safe. To trust it, start RetroArch with a menu, load the core and choose Always Trust. | — | Kärnan lästes inte in: RetroArch kunde inte bekräfta att den är säker. Starta RetroArch med en meny, läs in kärnan och välj Alltid betrodd för att lita på den. |
| 6234737 | Core loaded this time only: the trusted cores list is full, so RetroArch couldn't remember it. | — | Kärnan lästes bara in den här gången: listan över betrodda kärnor är full, så RetroArch kunde inte komma ihåg den. |
| 6234739 | Core not loaded: %s isn't trusted. To trust it, load it from Load Core and choose Always Trust. | — | Kärnan lästes inte in: %s är inte betrodd. Läs in den från Läs in kärna och välj Alltid betrodd för att lita på den. |
| 6234741 | Core not loaded: RetroArch is still checking the installed cores. Try again in a moment. | — | Kärnan lästes inte in: RetroArch kontrollerar fortfarande de installerade kärnorna. Försök igen om en stund. |

## Konsekvens och syntax

- `%s` i sträng 6234739 är bevarad.
- Inga markup-taggar, URL:er eller övriga platshållare förekommer i batchen.
- `libretro` och `RetroArch` lämnas oförändrade som projektnamn.
- `Nätuppdateraren`, `Läs in kärna` och `Alltid betrodd` är synliga gränssnittstermer och bör läsas tillbaka mot editorens faktiska etiketter vid eventuell publicering.

## Verktygskontroller

- Crowdin API användes för att hämta de aktuella engelska källsträngarna och bekräfta att målsträngarna saknade svensk översättning.
- RetroArchs projekt-TM söktes via API:ets concordance-funktion. Den gav inga användbara matchningar för dessa nya säkerhetssträngar.
- `l10n-lint --language sv` passerade utan anmärkningar för PO-underlaget.
- `hunspell -d sv_SE` markerade `libretro`, `RetroArch` och `testsigneringsnyckel`. De två första är namn; `testsigneringsnyckel` är en korrekt svensk sammansättning.
- Crowdins förhandsvalidering gav en enda träff: stavningskontrollen markerade `testsigneringsnyckel`. Ingen annan QA-kategori flaggade batchen.

## Omfattning

Detta är en avgränsad säkerhetsbatch från 81 oöversatta strängar i huvudfilen vid den aktuella API-hämtningen. Den ersätter inte en fullständig svensk granskning av RetroArch.

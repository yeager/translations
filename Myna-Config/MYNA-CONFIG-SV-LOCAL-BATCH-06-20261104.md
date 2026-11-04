# Myna Config: svensk lokal batch 06

Datum: 2026-11-04

Arbetsfil: `candidates/2026-11-04/myna-config-sv-local-batch-06.po`

## Kontext

Myna är Canonicals lokala tal-till-text för Ubuntu. Diktering startas och
stoppas med en skrivbordsgenväg; ljudet transkriberas lokalt och den färdiga
texten matas in i det fokuserade programmet via IBus. Denna batch täcker
modellbyte, modellinstallation, återläsning av inställningar och diagnostik.
Platshållarna `{model}` och `{setting}` bevaras oförändrade.

## Poster i denna batch

| Källa | Svenska |
| --- | --- |
| Changing model | Byter modell |
| Install | Installera |
| Install {model} | Installera {model} |
| Installing {model} failed | Det gick inte att installera {model} |
| Wait for the current change to finish. | Vänta tills den aktuella ändringen är klar. |
| Applying and restarting the model… | Tillämpar och startar om modellen… |
| Changing “{setting}” could not be confirmed | Det gick inte att bekräfta ändringen av ”{setting}” |
| Could not read the installed models. | Det gick inte att läsa de installerade modellerna. |
| No active model | Ingen aktiv modell |
| Choose a model on the General tab. | Välj en modell på fliken Allmänt. |
| Several models are connected | Flera modeller är anslutna |
| Choose one model on the General tab. | Välj en modell på fliken Allmänt. |
| Diagnostics copied. Paste them into the issue. | Diagnostiken har kopierats. Klistra in den i ärendet. |
| Could not open the web browser | Det gick inte att öppna webbläsaren |
| Copy privacy-safe diagnostics | Kopiera integritetsskyddande diagnostik |
| Diagnostics copied to clipboard | Diagnostiken har kopierats till urklipp |
| Dictation is not installed | Diktering är inte installerad |
| No model installed | Ingen modell är installerad |
| No input method set up | Ingen inmatningsmetod har konfigurerats |
| The model kept a different value than the one you chose. | Modellen behöll ett annat värde än det du valde. |

## Kontroller

`msgfmt --check` passerar. `git diff --check` passerar. Gitleaks hittar inga
hemligheter i arbetsfilen. `l10n-lint` och `svlang` finns inte i denna
skal-miljös sökväg; den manuella kontextgranskningen omfattar deras vanliga
fokusområden för platshållare, tekniska termer och svensk UI-stil.

## Status

Lokalt granskad och arkiverad kandidat. Inte skickad upstream.

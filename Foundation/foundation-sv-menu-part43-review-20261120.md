# Foundation – menu.json, granskningsomgång 43

Datum: 2026-11-20  
Metod: Crowdin API; samtliga tio förslag kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Källsträng | Sparad/föreslagen svenska | Resultat |
|---|---|---|---|
| ASSET_EXTENSION_GUIVRE_GARDEN_TITLE | Guivre Garden | Guivreträdgården | Dubblett i Crowdin. |
| ASSET_EXTENSION_GUIVRE_GARDEN_DESC | The Guivre Garden… | Ny svensk beskrivning | Sparad (HTTP 201). |
| ASSET_EXTENSION_INSTALLING | Installation in Progress | Installation pågår | Dubblett i Crowdin. |
| EXTENSION_NEW_GAME_LIBRARY_CHANGE_DETECTED_POPUP_TITLE | Change Detected in Game Library | Ändring upptäckt i spelbiblioteket | Dubblett i Crowdin. |
| EXTENSION_NEW_GAME_INSTALL_MISSING_DLCS | Foundation will install… | Foundation installerar alla ägda DLC:er som saknas. | Sparad (HTTP 201). |
| EXTENSION_NEW_GAME_RESTORE_OWNED_DLCS_POPUP_TITLE | Restore Owned DLCs | Återställ ägda DLC:er | Sparad (HTTP 201). |
| ASSET_EXTENSION_NOT_INSTALLED | Not installed | Inte installerat | Dubblett i Crowdin. |
| EDIT_EXTENSIONS_AND_MODS | Edit DLCs & Mods | Redigera DLC:er och moddar | Sparad (HTTP 201). |
| EXTENSION_SELECTION | DLC Selection | DLC-val | Dubblett i Crowdin. |
| LOAD_SAVE_MISSING_NON_REQUIRED_EXTENSION | This save contains content… | Ny svensk tvåstycksvarning | Sparad (HTTP 201). |

Radbrytningen i sparfilsvarningen bevarades. l10n-lint och Hunspell gav inga fel; Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.
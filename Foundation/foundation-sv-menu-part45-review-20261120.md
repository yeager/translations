# Foundation – menu.json, granskningsomgång 45

Datum: 2026-11-20  
Metod: Crowdin API; samtliga tio förslag kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Källsträng | Sparad/föreslagen svenska | Resultat |
|---|---|---|---|
| LOAD_SAVE_EXTENSION_NOT_ENABLED_WARNING | A new DLC has been installed… | Svensk tvåstegsfråga med bevarad radbrytning | Sparad (HTTP 201). |
| LOAD_SAVE_EXTENSION_NOT_ENABLED_INFO | *Once enabled… | *När vissa DLC:er… | Sparad (HTTP 201). |
| LOAD_SAVE_MULTIPLE_EXTENSIONS_NOT_ENABLED_WARNING | New DLCs have been installed… | Svensk tvåstegsfråga med bevarad radbrytning | Sparad (HTTP 201). |
| ASSET_EXTENSION_KS_CHURCH_TITLE | Founders Church | Grundarnas kyrka | Dubblett i Crowdin. |
| ASSET_EXTENSION_KS_CHURCH_DESC | This reward is dedicated… | Ny svensk beskrivning | Sparad (HTTP 201). |
| SUBSCRIBE_NEWSLETTER_BUTTON / WINDOW_TITLE | Sign up to our newsletter | Prenumerera på vårt nyhetsbrev | Dubblett i Crowdin. |
| SUBSCRIBE_NEWSLETTER_WINDOW_DESC | Get the latest news… | Svensk nyhetsbrevstext | Sparad (HTTP 201). |
| SUBSCRIBE_NEWSLETTER_WINDOW_SIGNUP | Sign Up | Prenumerera | Dubblett i Crowdin. |
| SUBSCRIBE_NEWSLETTER_WINDOW_PROCESSING | Processing… | Bearbetar… | Dubblett i Crowdin. |

Radbrytningar och den inledande asterisken i DLC-informationen bevarades. l10n-lint och Hunspell gav inga fel; Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.
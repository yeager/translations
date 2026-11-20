# Foundation – menu.json, granskningsomgång 44

Datum: 2026-11-20  
Metod: Crowdin API; samtliga förslag kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Källsträng | Sparad/föreslagen svenska | Resultat |
|---|---|---|---|
| LOAD_SAVE_MISSING_REQUIRED_EXTENSION | This save contains content… | Tvåradig svensk installationsvarning | Sparad (HTTP 201). |
| LOAD_SAVE_MISSING_EXTENSION_TITLE | Missing Required DLC(s) | Saknade obligatoriska DLC(er) | Sparad (HTTP 201). |
| LOAD_SAVE_MISSING_CONTENT_PACK_TITLE | Missing Optional Pack | Saknat valfritt paket | Sparad (HTTP 201). |
| SELECTION_DLCTYPE_HEADER_DLC | DLCs | DLC:er | Sparad (HTTP 201). |
| SELECTION_DLCTYPE_HEADER_PACK | Packs | Paket | Dubblett i Crowdin. |
| EXTENSION_WINDOW_TITLE | DLCs & Packs | DLC:er och paket | Sparad (HTTP 201). |
| LOAD_SAVE_CANT_DISABLE_EXTENSION | DLC cannot be disabled… | DLC kan inte inaktiveras i den här sparfilen | Sparad (HTTP 201). |
| VISIT_STORE_BUTTON | Visit Store | Besök butiken | Dubblett i Crowdin. |
| PROMO_BUY_NOW | Buy Now! | Köp nu! | Dubblett i Crowdin. |
| PROMO_AVAILABLE_NOW | Available Now! | Tillgängligt nu! | Dubblett i Crowdin. |

Radbrytningen i installationsvarningen bevarades. l10n-lint och Hunspell gav inga fel; Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.
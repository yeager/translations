# Foundation – menu.json, granskningsomgång 42

Datum: 2026-11-20  
Metod: Crowdin API; samtliga förslag kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Källsträng | Sparad/föreslagen svenska | Resultat |
|---|---|---|---|
| PROMO_WISHLIST_NOW | Wishlist Now! | Lägg till på önskelistan nu! | Sparad (HTTP 201). |
| MENU_HARVEST_FESTIVAL_DLC_DESC | Master the land…Harvest Festivals! | Ny svensk DLC-beskrivning | Sparad (HTTP 201). |
| MENU_GUIVRE_GARDEN_SUPPORTER_PACK_DESC | The Guivre Garden… | Ny svensk beskrivning med två stycken | Sparad (HTTP 201). |
| PROMO_HARVEST_FESTIVAL_DLC / ASSET_EXTENSION_AGRICULTURE_TITLE | Harvest Festival | Skördefestival | Sparade (HTTP 201). |
| ASSET_EXTENSION_AGRICULTURE_OFFICIAL_TITLE | Foundation: Harvest Festival | Foundation: Skördefestival | Dubblett i Crowdin. |
| BACK_TO_MAIN_MENU | Back to Main Menu | Tillbaka till huvudmenyn | Dubblett i Crowdin. |
| SELECT_MODS_LOCK_DESC | You don't have any mods… | Ny svensk instruktion | Sparad (HTTP 201). |
| SELECT_DLC | Select DLCs & Packs | Välj DLC:er och paket | Sparad (HTTP 201). |
| ASSET_EXTENSION_AGRICULTURE_DESC | Master the land… | Ny svensk beskrivning med bevarad radbrytning | Sparad (HTTP 201). |

Radbrytningar bevarades i de två längre informationssträngarna. l10n-lint och Hunspell gav inga fel; Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.
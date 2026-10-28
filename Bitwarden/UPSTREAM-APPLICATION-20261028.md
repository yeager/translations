# Bitwarden: tillämpningskarta för arkiverade deltan

De här filerna är lokala granskningsdeltan. De får inte importeras som om de
vore kompletta kataloger. Tillämpa varje post på samma nyckel i den angivna
svenska målkatalogen och jämför sedan mot den aktuella engelska källan.

| Komponent | Arkivfiler | Målkatalog | Poster |
| --- | --- | --- | ---: |
| Web | `bitwarden-web-current-missing-sv-20261027-01.json`–`22.json` | `apps/web/src/locales/sv/messages.json` i `bitwarden/clients` | 263 |
| Browser | `bitwarden-browser-current-missing-sv-20261027.json` | `apps/browser/src/_locales/sv/messages.json` i `bitwarden/clients` | 10 |
| Desktop | `bitwarden-desktop-current-missing-sv-20261027.json` | `apps/desktop/src/locales/sv/messages.json` i `bitwarden/clients` | 46 |
| Mobile | `bitwarden-mobile-current-untranslated-sv-20261028-01.json`–`02.json` | `src/Core/Resources/Localization/AppResources.sv.resx` i `bitwarden/mobile` | 23 |
| Authenticator Android | `bitwarden-authenticator-android-current-untranslated-sv-20261028-01.json`–`04.json` | `authenticator/src/main/res/values-sv-rSE/strings.xml` i `bitwarden/authenticator-android` | 46 |
| Authenticator iOS | `bitwarden-authenticator-ios-current-untranslated-sv-20261028-01.json`–`04.json` | `AuthenticatorShared/UI/Platform/Application/Support/Localizations/sv.lproj/Localizable.strings` i `bitwarden/authenticator-ios` | 60 |

Före en PR ska varje målkatalog hämtas på nytt, nycklarna jämföras med den
aktuella engelska katalogen, format och platshållare valideras och den
resulterande diffen granskas. Arkivstatus är inte detsamma som upstreamstatus.

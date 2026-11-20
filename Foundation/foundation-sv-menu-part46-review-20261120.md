# Foundation – menu.json, granskningsomgång 46

Datum: 2026-11-20  
Metod: Crowdin API; samtliga förslag kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Källsträng | Sparad/föreslagen svenska | Resultat |
|---|---|---|---|
| SUBSCRIBE_NEWSLETTER_WINDOW_THANKYOU | Thank you for signing up! | Tack för din prenumeration! | Dubblett i Crowdin. |
| SUBSCRIBE_NEWSLETTER_WINDOW_ERROR | Error sending request | Det gick inte att skicka begäran | Sparad (HTTP 201). |
| SUBSCRIBE_NEWSLETTER_WINDOW_ERROR_EMAIL | Invalid email | Ogiltig e-postadress | Dubblett i Crowdin. |
| SUBSCRIBE_NEWSLETTER_EMAIL | Enter your email address... | Ange din e-postadress... | Dubblett i Crowdin. |

l10n-lint och Hunspell gav inga fel; Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.
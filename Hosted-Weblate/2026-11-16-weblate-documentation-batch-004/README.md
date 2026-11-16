# Hosted Weblate – Weblate Documentation – svenska – batch 004

Datum: 2026-11-16

## Omfattning

Fyra tomma säkerhetsrelaterade dokumentationssträngar har kontextgranskats och sparats direkt i Hosted Weblate.

| Engelska | Svenska |
| --- | --- |
| The :guilabel:`Security report` link appears once findings or validation reports exist. Findings remain available with their history after handling them. Filter by status, type, or scan. Select :guilabel:`Validation reports` to return to previous uploads, including reports with no matches and reports still running or that failed. Reports record the uploaded filename and the administrator who submitted it. Individual reports include resolved and dismissed findings by default. Finding history links to each report that detected the issue, and finding details list these reports under :guilabel:`Detected in reports`. Use the breadcrumbs to move between user management, the security report, validation reports, and findings. | Länken :guilabel:`Säkerhetsrapport` visas när det finns fynd eller valideringsrapporter. Fynden är tillgängliga med sin historik även efter att de har hanterats. Filtrera efter status, typ eller skanning. Välj :guilabel:`Valideringsrapporter` för att återgå till tidigare uppladdningar, inklusive rapporter utan matchningar och rapporter som fortfarande körs eller har misslyckats. Rapporterna registrerar det uppladdade filnamnet och administratören som skickade in den. Enskilda rapporter innehåller lösta och avfärdade fynd som standard. Fyndhistoriken länkar till varje rapport som upptäckte problemet, och fyndinformationen listar dessa rapporter under :guilabel:`Upptäckt i rapporter`. Använd brödsmulorna för att växla mellan användarhantering, säkerhetsrapporten, valideringsrapporter och fynd. |
| Open findings on the current page are selected by default. Select or clear checkboxes in the browser, then submit an action. Actions apply only to checked findings shown on that page; selections do not carry across pages. Bulk actions require confirmation: | Öppna fynd på den aktuella sidan är valda som standard. Markera eller avmarkera kryssrutor i webbläsaren och skicka sedan in en åtgärd. Åtgärder gäller bara för markerade fynd som visas på den sidan; urval följer inte med mellan sidor. Massåtgärder kräver bekräftelse: |
| :guilabel:`Reset passwords for selected accounts` disables matching local passwords, invalidates sessions, revokes all API tokens, and notifies accounts with an e-mail address. Single sign-on and two-factor authentication settings are preserved. Passwords changed since validation are skipped and their obsolete findings resolved. | :guilabel:`Återställ lösenord för valda konton` inaktiverar matchande lokala lösenord, ogiltigförklarar sessioner, återkallar alla API-token och meddelar konton med en e-postadress. Inställningar för enkel inloggning och tvåfaktorsautentisering bevaras. Lösenord som har ändrats sedan valideringen hoppas över och deras föråldrade fynd löses. |
| :guilabel:`Dismiss selected findings` records the administrator's decision without changing credentials or notifying the account. A later upload confirming the exposure reopens the finding; retrying the same scan does not. | :guilabel:`Avfärda valda fynd` registrerar administratörens beslut utan att ändra inloggningsuppgifter eller meddela kontot. En senare uppladdning som bekräftar exponeringen öppnar fyndet igen; det gör inte en ny körning av samma skanning. |

## Terminologi och kontroller

- `finding` är **fynd**, `security report` är **säkerhetsrapport** och `validation report` är **valideringsrapport**.
- UI-namn i `:guilabel:` och API-token har bevarats i korrekt format.
- Direkt sparat upstream i Hosted Weblate. Detta är inte en separat upstream-granskning eller merge.
- Diffkontroll: godkänd (ny arkivpost).
- Gitleaks: godkänd.
- `msgfmt`: ej tillämpligt; Hosted Weblate gav ingen lokal gettext-export för batchen.
- `l10n-lint`, `svlang` och `hunspell-sv`: ej körda, eftersom ingen lokal översättningsfil exporterades från Hosted Weblate.

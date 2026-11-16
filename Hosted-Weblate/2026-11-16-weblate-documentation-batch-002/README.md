# Hosted Weblate – Weblate Documentation – svenska – batch 002

Datum: 2026-11-16

## Omfattning

Fem ytterligare tomma dokumentationssträngar har granskats i behörighets-, gransknings- och sekretesskontext och sparats direkt i Hosted Weblate.

| Engelska | Svenska |
| --- | --- |
| Project entries require ``project.edit`` on that project. Workspace entries require ``workspace.edit_members`` on that workspace. Site administrators can read all entries, including site-wide team changes. Team administration alone does not grant access to the detailed audit log. | Projektposter kräver ``project.edit`` på det projektet. Arbetsyteposter kräver ``workspace.edit_members`` på den arbetsytan. Webbplatsadministratörer kan läsa alla poster, inklusive ändringar av grupper på hela webbplatsen. Enbart gruppadministration ger inte åtkomst till den detaljerade granskningsloggen. |
| Stale assignments that have moved outside a scoped team retain their identifiers without exposing names from another project. | Föråldrade tilldelningar som har flyttats utanför en avgränsad grupp behåller sina identifierare utan att exponera namn från ett annat projekt. |
| Entries retain team names and changes after a team is deleted. After a project or workspace is removed, its retained records are available only to site administrators. Retention follows :setting:`AUDITLOG_EXPIRY`. | Poster behåller gruppnamn och ändringar efter att en grupp har tagits bort. När ett projekt eller en arbetsyta har tagits bort är dess bevarade poster bara tillgängliga för webbplatsadministratörer. Gallringsperioden styrs av :setting:`AUDITLOG_EXPIRY`. |
| Public translation history omits sensitive team membership changes, including existing records. The detailed audit log starts when this feature is installed; earlier team-definition changes cannot be reconstructed. Audit entries are internal security records, separate from portable user settings and backup contents. | Offentlig översättningshistorik utelämnar känsliga ändringar av gruppmedlemskap, även befintliga poster. Den detaljerade granskningsloggen börjar när funktionen installeras; tidigare ändringar i gruppdefinitioner kan inte återskapas. Granskningsposter är interna säkerhetsposter och är separata från flyttbara användarinställningar och innehåll i säkerhetskopior. |
| An invitation can also include team administration. The invitation states this explicitly, and the user becomes a team administrator only after accepting it. Team administrators can add or remove team members. | En inbjudan kan också omfatta gruppadministration. Det anges uttryckligen i inbjudan och användaren blir gruppadministratör först efter att ha godtagit den. Gruppadministratörer kan lägga till eller ta bort gruppmedlemmar. |

## Terminologi och kontroller

- `team` är **grupp**, `team member` är **gruppmedlem** och `team administrator` är **gruppadministratör**.
- `audit log` är **granskningslogg** och `audit entry` är **granskningspost**.
- reStructuredText-rollen `:setting:` och inställningsnamnet `AUDITLOG_EXPIRY` har bevarats oförändrade.
- Direkt sparat upstream i Hosted Weblate. Detta är inte en separat upstream-granskning eller merge.
- Diffkontroll: godkänd (ny arkivpost).
- Gitleaks: godkänd.
- `msgfmt`: ej tillämpligt; Hosted Weblate gav ingen lokal gettext-export för batchen.
- `l10n-lint`, `svlang` och `hunspell-sv`: ej körda, eftersom ingen lokal översättningsfil exporterades från Hosted Weblate.

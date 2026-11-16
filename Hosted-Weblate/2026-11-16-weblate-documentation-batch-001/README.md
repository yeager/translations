# Hosted Weblate – Weblate Documentation – svenska – batch 001

Datum: 2026-11-16

## Omfattning

Fem tomma dokumentationssträngar har granskats rad för rad i sin reStructuredText- och UI-kontext och sparats direkt i Hosted Weblate.

| Engelska | Svenska |
| --- | --- |
| Before moving a component to another project, remove it from teams defined in its current project. Moving a category requires removing its components from such teams as well. Removing the last component from a team grants its roles to the whole project, so review the team's membership and roles first. | Innan du flyttar en komponent till ett annat projekt ska du ta bort den från de grupper som har definierats i dess nuvarande projekt. Om du flyttar en kategori måste du också ta bort dess komponenter från sådana grupper. Om den sista komponenten tas bort från en grupp får hela projektet gruppens roller, så granska först gruppens medlemmar och roller. |
| Teams left with moved components by an earlier release show those assignments by component ID. The assignments grant no access to the destination project. You can remove them through the :doc:`REST API</api>` after reviewing the effect of an empty component selection on the original project. | Grupper som har kvar komponenter som flyttats av en tidigare version visar dessa tilldelningar med komponent-ID. Tilldelningarna ger ingen åtkomst till målprojektet. Du kan ta bort dem via :doc:`REST API</api>` efter att ha granskat hur ett tomt komponenturval påverkar det ursprungliga projektet. |
| Each team can have team administrators, who can add and remove users within the team. Administrators relying on this designation must satisfy the team's enforced two-factor authentication. Their team management access is suspended while they are blocked in any project covered by the team, or while a covered project requires two-factor authentication they have not configured. For a team covering multiple projects, the restriction applies to the whole team. | Varje grupp kan ha gruppadministratörer som kan lägga till och ta bort användare inom gruppen. Administratörer som har den här beteckningen måste uppfylla gruppens krav på tvåfaktorsautentisering. Deras åtkomst till gruppadministration är avstängd medan de är spärrade i något projekt som omfattas av gruppen eller medan ett omfattat projekt kräver tvåfaktorsautentisering som de inte har konfigurerat. För en grupp som omfattar flera projekt gäller begränsningen hela gruppen. |
| Open :guilabel:`Team audit log` from a team's page or from project or workspace access control. Site administrators can also open it from :guilabel:`Manage teams`. | Öppna :guilabel:`Granskningslogg för grupper` från en grupps sida eller från åtkomstkontrollen för projekt eller arbetsyta. Webbplatsadministratörer kan också öppna den från :guilabel:`Hantera grupper`. |
| The log records team creation, deletion, roles, language and component selection, enforced two-factor authentication, automatic assignment rules, memberships, and team administrator changes with the initiating account. Administrator grants and removals also appear in the affected account's activity log. | Loggen registrerar skapande och borttagning av grupper, roller, val av språk och komponenter, obligatorisk tvåfaktorsautentisering, regler för automatisk tilldelning, medlemskap och ändringar av gruppadministratörer, tillsammans med kontot som initierade ändringen. Tilldelning och borttagning av administratörsbehörighet visas också i aktivitetsloggen för det berörda kontot. |

## Terminologi och kontroll

- `team` är normaliserat till **grupp** och `team administrator` till **gruppadministratör**.
- `audit log` är normaliserat till **granskningslogg**.
- reStructuredText-roller och målet för `:doc:` har bevarats. Ett initialt fel i :doc:-markeringen rättades före batchens avslut.
- Hosted Weblate hade efter batchen 3 080 tomma dokumentationssträngar, jämfört med 3 085 före batchen.
- Direkt sparat upstream i Hosted Weblate. Detta är inte en separat upstream-granskning eller merge.
- Diffkontroll: godkänd (ny arkivpost).
- Gitleaks: godkänd.
- `msgfmt`: ej tillämpligt; Hosted Weblate gav ingen lokal gettext-export för batchen.
- `l10n-lint`, `svlang` och `hunspell-sv`: ej körda, eftersom ingen lokal översättningsfil exporterades från Hosted Weblate.

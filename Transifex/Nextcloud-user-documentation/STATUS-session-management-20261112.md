# Nextcloud användardokumentation – sessionshantering, 2026-11-12

Projekt: `o:nextcloud:p:nextcloud-user-documentation`.
Resurs: `user-manual-locale-source-session-management-pot--master`.

10 strängar om anslutna webbläsare, enheter, token och enhetsspecifika lösenord granskades rad för rad. Sphinx-referensen `:doc:`user_2fa`` bevarades.

Kontroller: l10n-lint, svlang, Hunspell, `git diff --check` och Gitleaks godkända. Hunspell-träffar består av produktnamn, Sphinx-markering och tekniska termer. `msgfmt` är inte tillämpligt eftersom Transifex-resursen är JSON-baserad.

Uppladdning: Transifex API returnerade HTTP 200 för 10 uppdateringar. En separat API-läsning efter inskicket visade 0 oöversatta svenska strängar i resursen.

Status: lokalt granskat, arkiverat och uppladdat. Upstream-granskning eller publicering är inte verifierad.

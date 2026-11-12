# OpenCloud – svensk Transifex-status

Källa: Transifex-projektet `opencloud-eu`; granskad produktversion var OpenCloud Web `v8.2.2`, publicerad 2026-11-11.

Den 12 november 2026 granskades och skickades 119 tidigare oöversatta svenska strängar i 15 komponenter. Varje komponent skickades i en separat Transifex API-batch eftersom API:t avvisar blandade resurser i samma batch. HTTP 200 och en efterföljande API-inventering bekräftar 0 oöversatta svenska strängar i hela projektet.

Arkivet innehåller oförändrade JSON-deltafiler, komponentvisa statusfiler och berörda terminologilistor. För JSON-resurser är `msgfmt` inte tillämpligt; formatvalideringen utfördes med l10n-lint och Transifex API:s godkända import. svlang, Hunspell, `git diff --check` och Gitleaks kördes för varje ändringsbatch; platshållare dokumenteras som förväntade Hunspell-träffar där de förekommer.

Status: lokalt granskat, arkiverat i `yeager/translations`, skickat och verifierat i Transifex. Upstream-granskning eller publicering kan inte härledas från Transifex API och påstås därför inte.

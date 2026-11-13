# Zammad development: komplett svensk komponent, 13 november 2026

Utvecklingskomponenten `zammad-development` har nu 5 418 av 5 418 översatta svenska strängar enligt Weblates statistik. Alla 96 poster som vid start antingen var tomma eller markerade för redigering granskades i sitt gränssnitts- eller kodsammanhang och uppdaterades med Weblates API.

Arbetet bestod av tre verifierade delar:

- 19 poster i chattvyn: [zammad-development-chat-repair-20261113.json](zammad-development-chat-repair-20261113.json).
- 58 ytterligare chattposter, inklusive tillgänglighet, kö, överföring och ärendeskapande.
- 17 återstående poster: betygsfält, valideringsfel, SSO, AI-svar, en e-postmall med ERB/HTML och kunskapsbasetiketter.

Före varje uppdatering kontrollerades att källsträngen fortfarande var densamma. Varje PATCH-svar lästes sedan tillbaka med målvärdet och tillståndet `translated`. Slutlig statistik: 5 418 totalt, 5 418 översatta, 0 redigeringsmarkerade, 0 felande kontroller och 2 083 särskilt granskar-godkända. De nya översättningarna är alltså inskickade och lästa tillbaka, men de icke godkända posterna är inte ännu särskilt granskar-godkända eller del av en utgiven Zammad-version.

Samma dag lästes stable-komponenten också tillbaka: 5 336 av 5 336 svenska strängar är översatta, utan redigeringsmarkeringar eller felande kontroller. De tidigare noterade två tomma stable-posterna är därför inte längre en aktiv restpunkt.

De två separata komponenterna för hostade tillägg kontrollerades därefter via samma Weblate-API: `zammad-hosted-extensions` och `zammad-hosted-extensions-stable` visar båda 249 av 249 översatta svenska strängar, 0 redigeringsmarkeringar och 0 felande kontroller. Vardera komponenten har 152 särskilt granskar-godkända poster. Kontrollen bekräftar täckning och sparat läge, men innebär inte att de återstående posterna har fått ett nytt granskar-godkännande eller har ingått i en Zammad-release.

Kontroller för de lokala batchunderlagen: JSON-validering, platshållar- och mallparitet, Hunspell-sv, l10n-lint, diffkontroll och Gitleaks. `msgfmt` är inte tillämpligt på Weblates enhetsposter. `svlang` analyserade även engelska källfält i JSON-underlagen och gav därför inga användbara svenska resultat i detta format.

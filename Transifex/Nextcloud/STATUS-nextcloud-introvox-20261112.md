# IntroVox – svensk granskningsstatus 2026-11-12

Komponent: `o:nextcloud:p:nextcloud:r:introvox`.

Projekt- och kontextkontroll: IntroVox 2.1.0 publicerades den 26 oktober 2026 för Nextcloud 32–35. Appen erbjuder guidade rundturer i Nextcloud och dess appar.

Den lokala kandidatfilen `introvox-admin-sv-delta-20261112.jsonl` innehåller 8 granskade administrativa och introducerande UI-strängar. l10n-lint, svlang, `git diff --check` och Gitleaks är godkända. Hunspell träffade endast den sammansatta tekniska termen `stegdata`. `msgfmt` är inte tillämpligt eftersom Transifex-resursen är JSON-baserad.

Uppladdning: Transifex API avvisade batchen med HTTP 409: den relaterade källsträngen är låst. En fullständig, paginerad API-kontroll visar att komponentens samtliga 367 oöversatta svenska strängar är taggade `locked`.

Status: 8 strängar är lokalt granskade och arkiverade som kandidater. Inget har uppladdats till IntroVox. Komponenten är externt blockerad tills projektet låser upp strängarna.

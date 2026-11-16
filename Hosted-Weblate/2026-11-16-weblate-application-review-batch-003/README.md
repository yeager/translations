# Weblate Application – svenska, granskningsbatch 003

Datum: 2026-11-16  
Projekt: Hosted Weblate / Weblate  
Komponent: Application

## Omfattning

Tio ändrade källsträngar granskades radvis och sparades direkt i Hosted Weblate.

| Engelska | Sparad svenska |
| --- | --- |
| Could not open the workbook archive. | Kunde inte öppna arbetsboksarkivet. |
| Too many translation requests. | För många översättningsbegäranden. |
| Too many concurrent translation requests for this service. | För många samtidiga översättningsbegäranden för den här tjänsten. |
| Too many uploads, please try again later. | För många uppladdningar, försök igen senare. |
| Install on the component owning the repository. | Installera på komponenten som äger förrådet. |
| The component owning this repository is not available to you. | Komponenten som äger det här förrådet är inte tillgänglig för dig. |
| Open repository add-ons | Öppna förrådstillägg |
| Deleted user | Borttagen användare |
| Administrative team changes | Administrativa gruppändringar |
| No team audit entries found. | Inga granskningsposter för gruppen hittades. |

## Status och verifiering

- Lokal granskning: klar, 10/10 strängar.
- Sparat upstream: klart, direkt i Hosted Weblate.
- Import/uppladdning: inte tillämpligt; editor sparade varje sträng direkt.
- Avläsning efter sparning: `state:needs-editing` minskade från 39 till 29 strängar.
- Upstream-granskning och merge: inte separata steg för direkt sparade Weblate-enheter.

## Kontroller

- Kontroll mot källtext, källplats och Weblates ordlista.
- Diffkontroll: utförd mot arkivposten.
- Gitleaks: passerade utan fynd.
- `msgfmt`: inte tillämpligt; ingen lokal gettext-export fanns.
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda utan lokal katalogfil.

# GnuCash Program: Weblate-kontroll

Datum: 2026-10-29

## Upstreamflöde

GnuCash-underhållaren stängde [PR #2341](https://github.com/Gnucash/gnucash/pull/2341)
utan merge och hänvisade till projektets svenska komponent i Hosted Weblate.

## Jämförelse

En färsk PO-export från `gnucash/gnucash/sv` hämtades direkt från Hosted
Weblate och kontrollerades med `msgfmt --check --check-format`. Jämförelsen
mot den arkiverade, granskade 59-postersdeltan visar:

- 59 av 59 källsträngar finns i aktuell export.
- 59 av 59 svenska måltexter är identiska med den granskade deltan.
- Inga av deltats poster behöver därför importeras eller sparas på nytt.

Den äldre GitHub-jämförelsen avsåg grenen `stable`; Weblate är den
auktoritativa, aktuella översättningskanalen.

## Resultat

Den granskade programkatalogen är redan synkroniserad uppströms. De tre
medvetet orörda `split`-posterna omfattas inte av denna verifiering och ska
fortsätta invänta ett uttryckligt termbeslut.

## Livekontroll i Weblate

Den 29 oktober 2026 kontrollerades komponentens svenska översikt direkt i
Hosted Weblate. Den visar 5 749 av 5 749 strängar översatta (100 %), utan
ofärdiga poster. Detta bekräftar att den tidigare GitHub-PR:ens 59-poster inte
ska laddas upp som en ny fil; de aktuella svenska måltexterna finns redan i
den auktoritativa Weblate-komponenten.

# Home Assistant Core – Flux LED-effekter, svenska

Datum: 2026-11-15

20 synliga effektetiketter för Flux LED har granskats rad för rad, sparats via
Lokalise API och återlästs via API. Färg + effekt är normaliserat; `RGB` är
bevarat som formatnamn.

| Källa | Svenska |
| --- | --- |
| Blue fade | Blå toning |
| Blue strobe | Blått stroboskop |
| Color jump | Färghopp |
| Color loop | Färgslinga |
| Color strobe | Färgstroboskop |
| Custom | Anpassad |
| Cyan fade | Cyan toning |
| Cyan strobe | Cyanfärgat stroboskop |
| Cycle RGB | RGB-cykel |
| Cycle seven colors | Växla mellan sju färger |
| Green/blue cross fade | Grön/blå korsvis toning |
| Green fade | Grön toning |
| Green strobe | Grönt stroboskop |
| Music | Musik |
| Purple fade | Lila toning |
| Purple strobe | Lila stroboskop |
| Random | Slumpmässig |
| Red/blue cross fade | Röd/blå korsvis toning |
| Red fade | Röd toning |
| Red strobe | Rött stroboskop |

## Upstreamstatus

- Lokal granskning: klar.
- Sparad via Lokalise API: klar, 20 översättningar.
- API-återläsning: klar. Alla 20 rätta nycklar har `sv` och
  `is_unverified=false`.
- Projektgranskning och release: inte verifierade.

## Kontroller

- `l10n-lint`, `svlang` och `hunspell-sv`: körs mot kontrollfilen.
- `msgfmt`: ej tillämpligt; katalogen är JSON-baserad och ingen PO-fil har
  exporterats.
- `git diff --check` och Gitleaks: körs före arkiveringens push.

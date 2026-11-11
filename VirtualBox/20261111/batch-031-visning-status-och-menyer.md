# Batch 031: visning, status och menyer

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

- Skärmfunktioner, grafikkontroller, grafikminne och virtuella skärmar: 21
  aktiva meddelanden.
- Statusrad, menyrad och miniverktygsfält: 22 aktiva meddelanden.

Samtliga 43 aktiva meddelanden granskades radvis.

## Ändringar

- `Grafikkontroller` används konsekvent.
- Statusraden och den virtuella maskinens menyer har tydliga ägandeformer.
- Menyåtgärder samt helskärms- och sömlöst läge har idiomatisk svenska.

Ändringarna infördes i lokal commit `478dc34`.

## Kontroller

- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt verifierad och arkiverad. Ändringarna inväntar fullständig radvis
granskning före samlad push till PR #848.

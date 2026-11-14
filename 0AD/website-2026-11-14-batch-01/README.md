# 0 A.D.-webbplatsen – svensk batch 1

Datum: 2026-11-14

Projekt: `play0ad-website` på Transifex. Komponent: **UI strings**.

## Radgranskning

- `release_line`: `{{ .Name }}, released {{ .Date }}.` →
  `{{ .Name }}, släppt {{ .Date }}.`
  Båda Go-mallplatshållarna bevarades och svensk interpunktion används.

## Status

Strängen skickades direkt i Transifex och återlästes efter sparning.
Transifex visar översatt av `yeager`; den är ännu inte projektgranskad eller
släppt. Importresultat för batchen: 1 uppdaterad, 0 hoppade över och 0 saknade.

`msgfmt` är inte tillämpligt eftersom underlaget är JSON, inte en PO-katalog.

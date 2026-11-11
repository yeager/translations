# Batch 001: format, tangenter och dialogtexter

Datum: 2026-11-11
Komponent: `src/VBox/Frontends/VirtualBox/nls/VirtualBox_sv.ts`
Utgångspunkt: VirtualBox PR #848, revision `7b2f494a0b0301f6f85423d1f4d4abc30222c5df`

## Granskade och ändrade strängar

- Två SSH-nyckeldialoger: konsekvent `publik nyckel`, komplett kortvariant
  och bevarade `%1`, `%2` samt HTML.
- Fyra procentvärden: mellanrum före procenttecken enligt svensk typografi.
- Tre menygenvägar: acceleratorn flyttades från `Ö` respektive `Å` till
  `p`, `g` och `t`, eftersom nordiska tecken inte ska vara snabbtangenter.
- `Scroll Lock`: standardiserad tangentbordsbeteckning.
- Musfångstverktygstips: saknat kolon före `%1` återställt.
- Två minnesvarningar: svensk procenttypografi och saknat `finns` rättat.
- Processorgräns och MAC-adress: grammatikfel rättade.
- Proxyexempel: tekniskt URL-exempel återställt exakt med källans citattecken.
- Två längre hjälpdialoer: innehåll, svensk ordföljd och avslutande
  interpunktion granskade. Felaktiga former som `värdtangentskombinationen`,
  `avfånga` och `normal operation` ersattes.

## Medvetna undantag

- Språkmetadata med källvärdet `--` ska vara tomma för svenska och är därför
  inte översättningsluckor.
- `{0-9,A-F}` är en bokstavlig teckenuppsättning och behåller källans
  bindestreck och kommatering.
- `D&D` betyder dra och släpp, inte en accelerator.
- `Svenska`, `s.` och `min.` är korrekta svenska måltexter trots generiska
  varningar om längd eller versalisering.

## Upstream

Inte uppladdad. PR #848 uppdateras först när hela katalogen är granskad och
alla batcher har validerats tillsammans.

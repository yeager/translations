# Pinta: svensk hjälpetikett

Datum: 14 november 2026

## Lokal granskning

Pinta är ett ritprogram med en svensk gettext-katalog i `po/sv.po`.
Den aktuella huvudgrenen innehåller 644 översatta poster utan tomma eller
luddiga översättningar. I hjälpdialogen för kortkommandon fanns en faktisk
stavning: `Hjålp`. Den är korrigerad till `Hjälp`.

Den generiska GTK-knappen `_OK` saknar avsiktligt snabbtangentsmarkör i
svensk text. Det är den enda återstående l10n-lint-varningen och är inte en
svensk språkavvikelse.

## Kontroller

- `msgfmt --check --statistics`: godkänd, 644 översatta poster.
- l10n-lint: inga fel; endast den avsiktliga `_OK`-varningen ovan.
- svlang: godkänd för den ändrade etiketten.
- Hunspell-sv: körd med låg CPU-prioritet för den ändrade etiketten; inga
  träffar och ingen kvarvarande process.
- diffkontroll och Gitleaks: godkända.

## Upstreamstatus

Ändringen är inskickad som [PintaProject/Pinta#2389](https://github.com/PintaProject/Pinta/pull/2389).
Den är en öppen pull request vid arkiveringstillfället och är ännu inte
upstreamgranskad, mergad eller utgiven.

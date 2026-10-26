# PS5X360 – svenska

Arkivet innehåller den svenska katalogen och den kompletta källändringen för
PS5X360 vid upstreamversion `v1.0.2` (2026-10-22).

## Innehåll

- `ps5x360-i18n-sv-20261026.inc` – 348 svenska katalograder för den
  portugisiska nyckelbaserade översättningsfunktionen.
- `ps5x360-sv-l10n-20261026.patch` – svenska språkvalet, katalogkopplingen,
  Xenia-språk-ID 13 och README-ändringarna.

## Granskning

Katalogen har jämförts mot samtliga 346 unika nyckel-/källtextpar. Den
bevarar formatplatshållare och inledande eller avslutande mellanslag. En
fristående C++-kontroll kompilerar språkstödet med varningar som fel och
verifierar att svenska väljs för både gränssnittet och Xenia-språk-ID 13.

`l10n-lint` rapporterar inga varningar för den deduplicerade PO-kontrollen.
Gitleaks hittade inga hemligheter i den svenska katalogen. Hunspell-träffarna
består av produktnamn, filformat, speltermer och tekniska namn som Xenia,
VSync, CAS och FSR.

Upstreamstatus: skickad som [PR #120](https://github.com/BrinooTk/PS5X360/pull/120).
Den är öppen och väntar på underhållargranskning. Godkännande och publicering
avgörs av projektets underhållare.

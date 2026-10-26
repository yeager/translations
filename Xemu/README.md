# Xemu – PR #2837

Uppströms-PR: <https://github.com/xemu-project/xemu/pull/2837>

Den 26 oktober 2026 kompletterades grenen `i18n-sv-xui` med commit
`03e0e9a6a3`, som behandlar de kvarvarande paketeringsproblemen för den nya
gettext-baserade XUI-lokaliseringen:

- uppdateraren kan skapa kataloger och föräldrakataloger när den extraherar
  framtida paket;
- Windows-paketen hålls platta under övergången, så redan utgivna uppdaterare
  inte avbryts av katalogposter i ZIP-filen;
- katalogbygget är fortsatt valfritt när gettext inte finns.

Kontroller: `bash -n build.sh`, `git diff --check` och avgränsad
Gitleaks-kontroll godkända. Full lokal byggning kräver beroenden som inte
finns i denna miljö; `clang-format` saknas också lokalt.

2026-10-27: Uppströmskontrollen är arkiverad i
`upstream-check-20261027.md`. PR:n är öppen utan CI eller underhållargranskning.
De konkreta botanmärkningarna om numeriskt språkformat, katalogbygge,
filväljarsträngar och popupetiketter är redan åtgärdade i den aktuella
huvud-committen. Ingen överlappande ny fix skickades.

NXEMU #489 granskades samtidigt. Underhållaren flyttar gränssnittet till
RmlUi och vill därefter använda `.po`-filer med språkval; ingen ytterligare
ändring är lämplig på den nuvarande PR:n.

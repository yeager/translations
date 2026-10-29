# AnyPS5 PR #12615: rättning av fångstdiagnostik

- Datum: 2026-10-29
- PR: <https://github.com/boykopovar/AnyPS5/pull/12615>
- Huvudcommit: `6fd775ed8a1302264cb78ab96788622ddf6618b3`
- Bas: `ba5b5330b3` (`origin/main` vid rebase)

## Rättning

Den kompletta diagnosen för döda tangenter översätts nu före den generella
ersättningen av ordet `and`. Därmed kan den inte längre delvis ändras innan
helmeningsmatchningen körs. Samma ordningsfel rättades för den arabiska
diagnostikgrenen.

Ett regressionsprov anropar `captureKey()` med en död tangent och verifierar
hela diagnostiken på svenska och arabiska.

## Verifiering

- `npm test --prefix tools/input-mapper`: 26 av 26 godkända.
- `python3 tools/check_conventions.py --base origin/main`: godkänd.
- Diffkontroll mot `origin/main`: godkänd.
- Scoped Gitleaks för ändrade filer: inga läckor.
- GitHub Actions på huvudcommitten: `conventions` och `labels` godkända.
- `pr_overlap.py`: körningen startades mot 1 402 öppna PR:er. Den är inte en
  förutsättning för den lokala rättningen och hade inte slutförts när grenen
  pushades.

# Blender Manual – uppladdningskandidater 4 november 2026

Källa: de radvis granskade deltafilerna
`../../blender-manual-sv-review-batch-20261104-01.po` till och med
`../../blender-manual-sv-review-batch-20261104-50.po`.

`create-manual-upload-batches.py` bygger först en samlad PO med `msgcat
--use-first --no-location` och delar sedan den i Weblate-säkra filer. Den
sammanlagda katalogen innehåller 550 översatta meddelanden enligt `msgfmt`.

| Fil | Översatta meddelanden | Status |
| --- | ---: | --- |
| `blender-manual-sv-reviewed-01.po` | 100 | Lokal kandidat, inte uppladdad |
| `blender-manual-sv-reviewed-02.po` | 100 | Lokal kandidat, inte uppladdad |
| `blender-manual-sv-reviewed-03.po` | 100 | Lokal kandidat, inte uppladdad |
| `blender-manual-sv-reviewed-04.po` | 100 | Lokal kandidat, inte uppladdad |
| `blender-manual-sv-reviewed-05.po` | 100 | Lokal kandidat, inte uppladdad |
| `blender-manual-sv-reviewed-06.po` | 50 | Lokal kandidat, inte uppladdad |

## Kontroller

- Varje kandidat och den samlade katalogen passerar `msgfmt --check`.
- `git diff --check` passerar för generatorn och kandidatfilerna.
- Gitleaks har skannat hela kandidatkatalogen utan träffar.
- Råexporten i `../../exports/2026-11-04/` har inte ändrats.

Ladda upp filerna i nummerordning till den **generiska** Manual-komponenten,
inte till versionskomponenterna 4.5, 5.2 eller 5.3. Efter varje uppladdning
ska Weblate-resultatet kontrolleras innan nästa kandidat skickas.

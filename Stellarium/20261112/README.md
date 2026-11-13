# Stellarium – svenska översättningar

Datum: 2026-11-12
Projekt: `o:stellarium:p:stellarium`
Komponent: `po/stellarium-skycultures-descriptions/stellarium-skycultures-descriptions.pot` (master)
Källa: Transifex API, oöversatta svenska strängar.
Projektaktivitet: Stellarium v26.3 släpptes 2026-09-28.

## Granskade batcher

- Granskade och ändrade: 73 oöversatta strängar i fyra komponenter.
- `stellarium-skycultures-descriptions`: 1 sträng.
- `stellarium-skycultures`: 15 strängar.
- `stellarium-planetary-features`: 26 strängar.
- `stellarium`: 31 strängar.
- Status: uppladdad till Transifex via API. Alla fyra uppladdningar svarade HTTP 200. En ny API-avläsning efter synkronisering visar 0 oöversatta strängar i respektive komponent.
- Terminologi: se `TERMINOLOGY.md`.

## Kontroller

- `l10n-lint` saknar fel. Informations- och varningsträffarna gäller bevarade uttalsformer och källans årtal med bindestreck.
- `svlang`, formatparitetskontroll för taggar/platshållare, `git diff --check` och `gitleaks` passerade på deltafilerna.
- `hunspell-sv` träffade `svalfisk`; termen behålls som en direkt återgivning av källans namn på motivet och är dokumenterad i deltafilens kontext.
- `msgfmt` kan inte köras på Transifex JSON-deltafilen. Ingen rå `.po`-export har ändrats.

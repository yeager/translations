# Hosted Weblate – Weblate Application – svenska – granskningsbatch 007

Datum: 2026-11-16

## Omfattning

Den avslutande kvalitetsgranskningen av Weblate Application har sparats direkt i Hosted Weblate.

| Engelska | Tidigare svenska | Sparad svenska |
| --- | --- | --- |
| Template replacement exceeds its size limit. | Mallen ersättning överskrider storleksgränsen. | Mallersättningen överskrider storleksgränsen. |
| None | Inget | Ingen |

Två Weblate-kontroller avfärdades efter kontextgranskning:

- `Bot` är ett avsiktligt identiskt tekniskt namn i säkerhetsfyndsvyn.
- `OCR-data` behåller den etablerade förkortningen OCR.

Två förslag avvisades eftersom de försämrade precisionen:

- `TLS-uppgifter` ersatte inte den mer precisa befintliga termen `TLS-autentiseringsuppgifter`.
- `Regex-inmatningen … per flertal` ersatte inte `Indata för reguljära uttryck … per pluralform`.

## Verifierad status

- Hosted Weblate Application: 5 966 av 5 966 strängar översatta och granskade.
- Översatt utan problem: 100 %.
- Fallerande kontroller: 0 (`has:check`).
- Öppna förslag: 0 (`has:suggestion`).
- Direkt sparat upstream i Hosted Weblate. Detta är inte en separat upstream-granskning eller merge.

## Kontroller

- Diffkontroll: godkänd (ny arkivpost).
- Gitleaks: godkänd.
- `msgfmt`: ej tillämpligt; Hosted Weblate gav ingen lokal gettext-export för batchen.
- `l10n-lint`, `svlang` och `hunspell-sv`: ej körda, eftersom ingen lokal översättningsfil exporterades från Hosted Weblate.

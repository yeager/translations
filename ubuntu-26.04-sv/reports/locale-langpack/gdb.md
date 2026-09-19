# locale-langpack/gdb

3 rättade översättningsposter. Ursprung: `/usr/share/locale-langpack/sv/LC_MESSAGES/gdb.mo`.

Jämförelsen gäller översatta meddelanden, utan metadatahuvudet. Gettext kan normalisera det kompilerade huvudets teckenkodning och skapandedatum; före/efter finns i metadata. PO-filerna och diffarna behåller ursprunglig teckenkodning (OpenSP: ISO-8859-1).

Upstream: [GNU GDB](https://sourceware.org/gdb/).

[Ubuntu-källpaket](https://launchpad.net/ubuntu/+source/gdb). Installerat ägarpaket: `language-pack-sv-base 1:26.04+20260818`.

[Rättad PO](../../po/locale-langpack/gdb.po) · [Original](../../original/locale-langpack/gdb.po) · [Diff](../../diff/locale-langpack/gdb.po.diff) · [Metadata](../../metadata/locale-langpack/gdb.json)

Rättad PO godkänns av `msgfmt --check --check-format`. Diffen återger filen byte för byte. Den kompilerade meddelandetabellen skiljer sig från installerad MO endast genom rättningarna nedan. PO-huvudet är bevarat; rapporten dokumenterar ändringarnas datum.

Råträffar: l10n-lint 2261 → 2256, svlang 8 → 8. Kvarstående träffar är kandidater och innebär inte verifierade fel.

## F003 · P1 · Två trasiga tidsformat

Båda %06ld har trunkerats till %06. Formatkontraktet och återgivningen av tidsvärden går förlorade.

PO-rad: original 14147, rättad 14148.

Källtext:

```text
Trace started at %ld.%06ld secs, stopped %ld.%06ld secs later.

```

Före:

```text
Spårningen startade vid %ld.%06 sekunder och avslutades %ld.%06 sekunder senare

```

Efter:

```text
Spårningen startade vid %ld.%06ld sekunder och avslutades %ld.%06ld sekunder senare

```

## F019 · P2 · Skiftlägesinställningen ersätts med ett fast påstående

Originalet återger inställningen via %s. Översättningen säger alltid att sökningen inte är skiftlägeskänslig.

PO-rad: original 3188, rättad 3188.

Källtext:

```text
Case sensitivity in name search is "%s".

```

Före:

```text
Namnsökningen är inte skiftlägeskänslig

```

Efter:

```text
Namnsökningens skiftlägeskänslighet är ”%s”.

```

## F020 · P2 · &s används i stället för %s

Sektionens namn försvinner eftersom procenttecknet har blivit &.

PO-rad: original 9950, rättad 9951.

Källtext:

```text
Section %s not found
```

Före:

```text
Kapitel &s hittades inte
```

Efter:

```text
Sektionen %s hittades inte
```

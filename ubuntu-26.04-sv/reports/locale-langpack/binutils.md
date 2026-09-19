# locale-langpack/binutils

2 rättade översättningsposter. Ursprung: `/usr/share/locale-langpack/sv/LC_MESSAGES/binutils.mo`.

Jämförelsen gäller översatta meddelanden, utan metadatahuvudet. Gettext kan normalisera det kompilerade huvudets teckenkodning och skapandedatum; före/efter finns i metadata. PO-filerna och diffarna behåller ursprunglig teckenkodning (OpenSP: ISO-8859-1).

Upstream: [GNU Binutils](https://sourceware.org/binutils/).

[Ubuntu-källpaket](https://launchpad.net/ubuntu/+source/binutils). Installerat ägarpaket: `language-pack-sv-base 1:26.04+20260818`.

[Rättad PO](../../po/locale-langpack/binutils.po) · [Original](../../original/locale-langpack/binutils.po) · [Diff](../../diff/locale-langpack/binutils.po.diff) · [Metadata](../../metadata/locale-langpack/binutils.json)

Rättad PO godkänns av `msgfmt --check --check-format`. Diffen återger filen byte för byte. Den kompilerade meddelandetabellen skiljer sig från installerad MO endast genom rättningarna nedan. PO-huvudet är bevarat; rapporten dokumenterar ändringarnas datum.

Råträffar: l10n-lint 531 → 529, svlang 8 → 8. Kvarstående träffar är kandidater och innebär inte verifierade fel.

## F013 · P2 · Extra %s i meddelandet om felsökningssektion

Källtexten har ingen formateringsparameter; den svenska texten lägger till : %s.

PO-rad: original 9133, rättad 9133.

Källtext:

```text
can't create debugging section
```

Före:

```text
kan inte skapa felsökningssektionen: %s
```

Efter:

```text
kan inte skapa felsökningssektionen
```

## F014 · P2 · Extra %s i meddelandet om BFD-data

Källtexten har ingen formateringsparameter; den svenska texten lägger till : %s.

PO-rad: original 9601, rättad 9601.

Källtext:

```text
error copying private BFD data
```

Före:

```text
fel vid kopiering av privat BFD-data: %s
```

Efter:

```text
fel vid kopiering av privat BFD-data
```

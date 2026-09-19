# locale-langpack/gas

1 rättade översättningsposter. Ursprung: `/usr/share/locale-langpack/sv/LC_MESSAGES/gas.mo`.

Jämförelsen gäller översatta meddelanden, utan metadatahuvudet. Gettext kan normalisera det kompilerade huvudets teckenkodning och skapandedatum; före/efter finns i metadata. PO-filerna och diffarna behåller ursprunglig teckenkodning (OpenSP: ISO-8859-1).

Upstream: [GNU Binutils / GNU assembler](https://sourceware.org/binutils/).

[Ubuntu-källpaket](https://launchpad.net/ubuntu/+source/binutils). Installerat ägarpaket: `language-pack-sv-base 1:26.04+20260818`.

[Rättad PO](../../po/locale-langpack/gas.po) · [Original](../../original/locale-langpack/gas.po) · [Diff](../../diff/locale-langpack/gas.po.diff) · [Metadata](../../metadata/locale-langpack/gas.json)

Rättad PO godkänns av `msgfmt --check --check-format`. Diffen återger filen byte för byte. Den kompilerade meddelandetabellen skiljer sig från installerad MO endast genom rättningarna nedan. PO-huvudet är bevarat; rapporten dokumenterar ändringarnas datum.

Råträffar: l10n-lint 124 → 123, svlang 18 → 18. Kvarstående träffar är kandidater och innebär inte verifierade fel.

## F018 · P2 · Ett dollartecken har blivit %s

Originalets bokstavliga $ får inte ersättas med ett nytt formatargument.

PO-rad: original 11177, rättad 11177.

Källtext:

```text
instruction requires label sans '$'
```

Före:

```text
instruktion kräver etikett utan ”%s”
```

Efter:

```text
instruktion kräver etikett utan ”$”
```

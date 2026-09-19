# locale-langpack/ld

1 rättade översättningsposter. Ursprung: `/usr/share/locale-langpack/sv/LC_MESSAGES/ld.mo`.

Jämförelsen gäller översatta meddelanden, utan metadatahuvudet. Gettext kan normalisera det kompilerade huvudets teckenkodning och skapandedatum; före/efter finns i metadata. PO-filerna och diffarna behåller ursprunglig teckenkodning (OpenSP: ISO-8859-1).

Upstream: [GNU Binutils / GNU linker](https://sourceware.org/binutils/).

[Ubuntu-källpaket](https://launchpad.net/ubuntu/+source/binutils). Installerat ägarpaket: `language-pack-sv-base 1:26.04+20260818`.

[Rättad PO](../../po/locale-langpack/ld.po) · [Original](../../original/locale-langpack/ld.po) · [Diff](../../diff/locale-langpack/ld.po.diff) · [Metadata](../../metadata/locale-langpack/ld.json)

Rättad PO godkänns av `msgfmt --check --check-format`. Diffen återger filen byte för byte. Den kompilerade meddelandetabellen skiljer sig från installerad MO endast genom rättningarna nedan. PO-huvudet är bevarat; rapporten dokumenterar ändringarnas datum.

Råträffar: l10n-lint 89 → 88, svlang 1 → 1. Kvarstående träffar är kandidater och innebär inte verifierade fel.

## F022 · P2 · Duplicerat instick får ett extra argument

Översättningen innehåller två %s medan originalet bara innehåller en. %P är länkarens egna direktiv och ska bevaras.

PO-rad: original 1712, rättad 1712.

Källtext:

```text
%P: %s: duplicated plugin

```

Före:

```text
%P: %s: duplicerat instick: %s

```

Efter:

```text
%P: %s: duplicerat instick

```

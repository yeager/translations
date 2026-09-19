# locale-langpack/fetchmail

1 rättade översättningsposter. Ursprung: `/usr/share/locale-langpack/sv/LC_MESSAGES/fetchmail.mo`.

Jämförelsen gäller översatta meddelanden, utan metadatahuvudet. Gettext kan normalisera det kompilerade huvudets teckenkodning och skapandedatum; före/efter finns i metadata. PO-filerna och diffarna behåller ursprunglig teckenkodning (OpenSP: ISO-8859-1).

Upstream: [fetchmail](https://www.fetchmail.info/).

[Ubuntu-källpaket](https://launchpad.net/ubuntu/+source/fetchmail). Installerat ägarpaket: `language-pack-sv-base 1:26.04+20260818`.

[Rättad PO](../../po/locale-langpack/fetchmail.po) · [Original](../../original/locale-langpack/fetchmail.po) · [Diff](../../diff/locale-langpack/fetchmail.po.diff) · [Metadata](../../metadata/locale-langpack/fetchmail.json)

Rättad PO godkänns av `msgfmt --check --check-format`. Diffen återger filen byte för byte. Den kompilerade meddelandetabellen skiljer sig från installerad MO endast genom rättningarna nedan. PO-huvudet är bevarat; rapporten dokumenterar ändringarnas datum.

Råträffar: l10n-lint 24 → 23, svlang 1 → 1. Kvarstående träffar är kandidater och innebär inte verifierade fel.

## F017 · P2 · Extra %s i meddelandet om --moveto

Översättningen har ett formatargument som inte finns i originalet.

PO-rad: original 2123, rättad 2123.

Källtext:

```text
fetchmail: configuration invalid, --moveto is only valid for IMAP servers

```

Före:

```text
fetchmail: %s-konfigurationen är ogiltig, --moveto är endast giltigt för IMAP-servrar

```

Efter:

```text
fetchmail: konfigurationen är ogiltig, --moveto är endast giltigt för IMAP-servrar

```

# locale-langpack/dpkg

1 rättade översättningsposter. Ursprung: `/usr/share/locale-langpack/sv/LC_MESSAGES/dpkg.mo`.

Jämförelsen gäller översatta meddelanden, utan metadatahuvudet. Gettext kan normalisera det kompilerade huvudets teckenkodning och skapandedatum; före/efter finns i metadata. PO-filerna och diffarna behåller ursprunglig teckenkodning (OpenSP: ISO-8859-1).

Upstream: [dpkg](https://wiki.debian.org/Teams/Dpkg).

[Ubuntu-källpaket](https://launchpad.net/ubuntu/+source/dpkg). Installerat ägarpaket: `language-pack-sv-base 1:26.04+20260818`.

[Rättad PO](../../po/locale-langpack/dpkg.po) · [Original](../../original/locale-langpack/dpkg.po) · [Diff](../../diff/locale-langpack/dpkg.po.diff) · [Metadata](../../metadata/locale-langpack/dpkg.json)

Rättad PO godkänns av `msgfmt --check --check-format`. Diffen återger filen byte för byte. Den kompilerade meddelandetabellen skiljer sig från installerad MO endast genom rättningarna nedan. PO-huvudet är bevarat; rapporten dokumenterar ändringarnas datum.

Råträffar: l10n-lint 118 → 117, svlang 3 → 3. Kvarstående träffar är kandidater och innebär inte verifierade fel.

## F012 · P2 · Översättningen lägger till ett obefintligt argument

Originalet innehåller ingen %s. Översättningen har kvar en platshållare och ett prefix som saknar motsvarighet i källtexten.

PO-rad: original 3433, rättad 3433.

Källtext:

```text
need a pathname argument
```

Före:

```text
--%s behöver ett sökvägsnamnargument
```

Efter:

```text
behöver ett sökvägsargument
```

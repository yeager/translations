# locale-langpack/slideshow-oem-config-ubuntu-mate

1 rättade översättningsposter. Ursprung: `/usr/share/locale-langpack/sv/LC_MESSAGES/slideshow-oem-config-ubuntu-mate.mo`.

Jämförelsen gäller översatta meddelanden, utan metadatahuvudet. Gettext kan normalisera det kompilerade huvudets teckenkodning och skapandedatum; före/efter finns i metadata. PO-filerna och diffarna behåller ursprunglig teckenkodning (OpenSP: ISO-8859-1).

Upstream: [Ubiquity slideshow](https://launchpad.net/ubiquity-slideshow-ubuntu).

[Ubuntu-källpaket](https://launchpad.net/ubuntu/+source/ubiquity-slideshow-ubuntu). Installerat ägarpaket: `language-pack-sv-base 1:26.04+20260818`.

[Rättad PO](../../po/locale-langpack/slideshow-oem-config-ubuntu-mate.po) · [Original](../../original/locale-langpack/slideshow-oem-config-ubuntu-mate.po) · [Diff](../../diff/locale-langpack/slideshow-oem-config-ubuntu-mate.po.diff) · [Metadata](../../metadata/locale-langpack/slideshow-oem-config-ubuntu-mate.json)

Rättad PO godkänns av `msgfmt --check --check-format`. Diffen återger filen byte för byte. Den kompilerade meddelandetabellen skiljer sig från installerad MO endast genom rättningarna nedan. PO-huvudet är bevarat; rapporten dokumenterar ändringarnas datum.

Råträffar: l10n-lint 2 → 0, svlang 0 → 0. Kvarstående träffar är kandidater och innebär inte verifierade fel.

## F027 · P2 · Netflix får fel avslutningstagg

</string> ska vara </strong>. Samma fel finns i OEM-bildspelet.

PO-rad: original 164, rättad 164.

Källtext:

```text
Ubuntu MATE comes with <strong>Firefox</strong> pre-installed and <strong>Google Chrome</strong> is in the Software Boutique so you can watch content from your favourite streaming services such as <strong>Netflix</strong> and <strong>YouTube</strong>.
```

Före:

```text
Ubuntu MATE har <strong>Firefox</strong> förinstallerat, och <strong>Google Chrome</strong> finns i Programbutiken så att du kan titta på innehåll från dina favorit-streaming-tjänster, såsom <strong>Netflix</string> och <strong>YouTube</strong>.
```

Efter:

```text
Ubuntu MATE har <strong>Firefox</strong> förinstallerat, och <strong>Google Chrome</strong> finns i Programbutiken så att du kan titta på innehåll från dina favorit-streaming-tjänster, såsom <strong>Netflix</strong> och <strong>YouTube</strong>.
```

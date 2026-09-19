# locale-langpack/simple-scan

1 rättade översättningsposter. Ursprung: `/usr/share/locale-langpack/sv/LC_MESSAGES/simple-scan.mo`.

Jämförelsen gäller översatta meddelanden, utan metadatahuvudet. Gettext kan normalisera det kompilerade huvudets teckenkodning och skapandedatum; före/efter finns i metadata. PO-filerna och diffarna behåller ursprunglig teckenkodning (OpenSP: ISO-8859-1).

Upstream: [GNOME Document Scanner](https://apps.gnome.org/SimpleScan/). [Källkod](https://gitlab.gnome.org/GNOME/simple-scan).

[Ubuntu-källpaket](https://launchpad.net/ubuntu/+source/simple-scan). Installerat ägarpaket: `language-pack-gnome-sv-base 1:26.04+20260818`.

[Rättad PO](../../po/locale-langpack/simple-scan.po) · [Original](../../original/locale-langpack/simple-scan.po) · [Diff](../../diff/locale-langpack/simple-scan.po.diff) · [Metadata](../../metadata/locale-langpack/simple-scan.json)

Rättad PO godkänns av `msgfmt --check --check-format`. Diffen återger filen byte för byte. Den kompilerade meddelandetabellen skiljer sig från installerad MO endast genom rättningarna nedan. PO-huvudet är bevarat; rapporten dokumenterar ändringarnas datum.

Råträffar: l10n-lint 20 → 16, svlang 0 → 0. Kvarstående träffar är kandidater och innebär inte verifierade fel.

## F025 · P2 · Trasiga länktaggar i hjälptexten

Den första länken har felaktig escapning och saknar avslutande attributcitat och >. Den andra saknar även inledande <. Länktexten hamnar i attributen.

PO-rad: original 278, rättad 278.

Källtext:

```text
Please check if your <a href="http://www.sane-project.org/sane-supported-devices.html">scanner is supported by SANE</a>, otherwise report the issue to the <a href="https://alioth-lists.debian.net/cgi-bin/mailman/listinfo/sane-devel">SANE mailing list</a>.
```

Före:

```text
Se om din <a href=\"http://www.sane-project.org/sane-supported-devices.html bildläsare stöds av SANE</a>, annars kan du rapportera problemet till a href="https://alioth-lists.debian.net/cgi-bin/mailman/listinfo/sane-devel sändlistan för SANE</a>."
```

Efter:

```text
Kontrollera om din <a href="http://www.sane-project.org/sane-supported-devices.html">bildläsare stöds av SANE</a>, annars kan du rapportera problemet till <a href="https://alioth-lists.debian.net/cgi-bin/mailman/listinfo/sane-devel">sändlistan för SANE</a>.
```

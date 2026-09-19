# locale-langpack/libgphoto2-2

2 rättade översättningsposter. Ursprung: `/usr/share/locale-langpack/sv/LC_MESSAGES/libgphoto2-2.mo`.

Jämförelsen gäller översatta meddelanden, utan metadatahuvudet. Gettext kan normalisera det kompilerade huvudets teckenkodning och skapandedatum; före/efter finns i metadata. PO-filerna och diffarna behåller ursprunglig teckenkodning (OpenSP: ISO-8859-1).

Upstream: [libgphoto2](https://github.com/gphoto/libgphoto2).

[Ubuntu-källpaket](https://launchpad.net/ubuntu/+source/libgphoto2). Installerat ägarpaket: `language-pack-sv-base 1:26.04+20260818`.

[Rättad PO](../../po/locale-langpack/libgphoto2-2.po) · [Original](../../original/locale-langpack/libgphoto2-2.po) · [Diff](../../diff/locale-langpack/libgphoto2-2.po.diff) · [Metadata](../../metadata/locale-langpack/libgphoto2-2.json)

Rättad PO godkänns av `msgfmt --check --check-format`. Diffen återger filen byte för byte. Den kompilerade meddelandetabellen skiljer sig från installerad MO endast genom rättningarna nedan. PO-huvudet är bevarat; rapporten dokumenterar ändringarnas datum.

Råträffar: l10n-lint 54 → 52, svlang 0 → 0. Kvarstående träffar är kandidater och innebär inte verifierade fel.

## F023 · P2 · Antalet återförsök har ersatts med %i

Originalets fasta två återförsök har blivit ett formatargument som inte finns i originalet.

PO-rad: original 6856, rättad 6856.

Källtext:

```text
Transmission timed out even after 2 retries. Giving up...
```

Före:

```text
Överföringen tog för lång tid och avbröts efter %i försök. Ger upp…
```

Efter:

```text
Överföringen överskred tidsgränsen även efter två nya försök. Ger upp…
```

## F024 · P2 · Adressen till utvecklarlistan ersätts med %s

Originalet hänvisar till gphotos utvecklarlista utan formatargument. Översättningen kräver en extra %s.

PO-rad: original 6161, rättad 6161.

Källtext:

```text
Some notes about Epson cameras:
- Some parameters are not controllable remotely:
  * zoom
  * focus
  * custom white balance setup
- Configuration has been reverse-engineered with
  a PhotoPC 3000z, if your camera acts differently
  please send a mail to the gphoto developer mailing list (in English)

```

Före:

```text
Några anteckningar om Epson-kameror:
- Vissa parametrar går inte att fjärrstyra:
  * zoom
  * fokus
  * anpassad vitbalansinställning
- Konfigurationen har blivit avkodad med
  en PhotoPC 3000z, om din kamera beter sig annorlunda
  skriv ett brev till %s (på Engelska)

```

Efter:

```text
Några anteckningar om Epson-kameror:
- Vissa parametrar går inte att fjärrstyra:
  * zoom
  * fokus
  * anpassad vitbalansinställning
- Konfigurationen har blivit avkodad med
  en PhotoPC 3000z, om din kamera beter sig annorlunda
  skriv ett brev till gphotos utvecklarsändlista (på engelska)

```

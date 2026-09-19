# locale-langpack/cryptsetup

2 rättade översättningsposter. Ursprung: `/usr/share/locale-langpack/sv/LC_MESSAGES/cryptsetup.mo`.

Jämförelsen gäller översatta meddelanden, utan metadatahuvudet. Gettext kan normalisera det kompilerade huvudets teckenkodning och skapandedatum; före/efter finns i metadata. PO-filerna och diffarna behåller ursprunglig teckenkodning (OpenSP: ISO-8859-1).

Upstream: [cryptsetup](https://gitlab.com/cryptsetup/cryptsetup).

[Ubuntu-källpaket](https://launchpad.net/ubuntu/+source/cryptsetup). Installerat ägarpaket: `language-pack-sv-base 1:26.04+20260818`.

[Rättad PO](../../po/locale-langpack/cryptsetup.po) · [Original](../../original/locale-langpack/cryptsetup.po) · [Diff](../../diff/locale-langpack/cryptsetup.po.diff) · [Metadata](../../metadata/locale-langpack/cryptsetup.json)

Rättad PO godkänns av `msgfmt --check --check-format`. Diffen återger filen byte för byte. Den kompilerade meddelandetabellen skiljer sig från installerad MO endast genom rättningarna nedan. PO-huvudet är bevarat; rapporten dokumenterar ändringarnas datum.

Råträffar: l10n-lint 40 → 38, svlang 0 → 0. Kvarstående träffar är kandidater och innebär inte verifierade fel.

## F015 · P2 · Rothash har blivit begärd hash och ett extra argument

Root hash har fått annan innebörd och översättningen innehåller en %s som originalet saknar.

PO-rad: original 2486, rättad 2486.

Källtext:

```text
Root hash signature verification is not supported.
```

Före:

```text
Begärd hashsignaturverifiering %s stöds inte.
```

Efter:

```text
Verifiering av rothashsignaturer stöds inte.
```

## F016 · P2 · Extra %u i meddelandet om metadata

Originalet anger inte någon numerisk posttyp men översättningen kräver ett sådant argument.

PO-rad: original 2717, rättad 2717.

Källtext:

```text
Unexpected metadata entry found when parsing startup key.
```

Före:

```text
Oväntad metadatapost av typ ”%u” funnen vid tolkning av uppstartsnyckel.
```

Efter:

```text
Oväntad metadatapost funnen vid tolkning av uppstartsnyckel.
```

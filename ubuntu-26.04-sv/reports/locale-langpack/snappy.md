# locale-langpack/snappy

2 rättade översättningsposter. Ursprung: `/usr/share/locale-langpack/sv/LC_MESSAGES/snappy.mo`.

Jämförelsen gäller översatta meddelanden, utan metadatahuvudet. Gettext kan normalisera det kompilerade huvudets teckenkodning och skapandedatum; före/efter finns i metadata. PO-filerna och diffarna behåller ursprunglig teckenkodning (OpenSP: ISO-8859-1).

Upstream: [snapd](https://github.com/canonical/snapd).

[Ubuntu-källpaket](https://launchpad.net/ubuntu/+source/snapd). Installerat ägarpaket: `language-pack-sv-base 1:26.04+20260818`.

[Rättad PO](../../po/locale-langpack/snappy.po) · [Original](../../original/locale-langpack/snappy.po) · [Diff](../../diff/locale-langpack/snappy.po.diff) · [Metadata](../../metadata/locale-langpack/snappy.json)

Rättad PO godkänns av `msgfmt --check --check-format`. Diffen återger filen byte för byte. Den kompilerade meddelandetabellen skiljer sig från installerad MO endast genom rättningarna nedan. PO-huvudet är bevarat; rapporten dokumenterar ändringarnas datum.

Råträffar: l10n-lint 110 → 107, svlang 27 → 27. Kvarstående träffar är kandidater och innebär inte verifierade fel.

## F028 · P2 · Trasig länk till felsökningshjälp

https: har blivit https; så länken är inte längre korrekt.

PO-rad: original 2305, rättad 2305.

Källtext:

```text
%s was not found in your $PATH. If you've not restarted your session since you installed snapd, try doing that. Please see https://forum.snapcraft.io/t/9469 for more details.
```

Före:

```text
%s hittades inte i din $PATH. Om du inte har startat om din session sedan du installerade snapd, testa att göra det. Se https;//forum.snapcraft.io/t/9469 för fler detaljer.
```

Efter:

```text
%s hittades inte i din $PATH. Om du inte har startat om din session sedan du installerade snapd, testa att göra det. Se https://forum.snapcraft.io/t/9469 för fler detaljer.
```

## F053 · P3 · Felaktig upprepning: relative tider till till

Upprepningen är ett skrivfel i denna mening och har inte stöd i källtexten.

PO-rad: original 2749, rättad 2749.

Källtext:

```text
Display absolute times (in RFC 3339 format). Otherwise, display relative times up to 60 days, then YYYY-MM-DD.
```

Före:

```text
Visa absoluta tider (i formatet RFC 3339). Visa annars relative tider till till 60 dagar, sedan ÅÅÅÅ-MM-DD.
```

Efter:

```text
Visa absoluta tider (i formatet RFC 3339). Visa annars relativa tider upp till 60 dagar, sedan ÅÅÅÅ-MM-DD.
```

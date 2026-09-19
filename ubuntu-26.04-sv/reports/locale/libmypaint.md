# locale/libmypaint

2 rättade översättningsposter. Ursprung: `/usr/share/locale/sv/LC_MESSAGES/libmypaint.mo`.

Jämförelsen gäller översatta meddelanden, utan metadatahuvudet. Gettext kan normalisera det kompilerade huvudets teckenkodning och skapandedatum; före/efter finns i metadata. PO-filerna och diffarna behåller ursprunglig teckenkodning (OpenSP: ISO-8859-1).

Upstream: [libmypaint](https://github.com/mypaint/libmypaint).

[Ubuntu-källpaket](https://launchpad.net/ubuntu/+source/libmypaint). Installerat ägarpaket: `libmypaint-common 1.6.0-4build1`.

[Rättad PO](../../po/locale/libmypaint.po) · [Original](../../original/locale/libmypaint.po) · [Diff](../../diff/locale/libmypaint.po.diff) · [Metadata](../../metadata/locale/libmypaint.json)

Rättad PO godkänns av `msgfmt --check --check-format`. Diffen återger filen byte för byte. Den kompilerade meddelandetabellen skiljer sig från installerad MO endast genom rättningarna nedan. PO-huvudet är bevarat; rapporten dokumenterar ändringarnas datum.

Råträffar: l10n-lint 5 → 1, svlang 0 → 0. Kvarstående träffar är kandidater och innebär inte verifierade fel.

## F029 · P2 · Pennans vinkelvärden är omkastade (x-led)

Originalet anger ±90 vid parallell penna och 0 vid vinkelrät penna. Översättningen anger motsatsen.

PO-rad: original 287, rättad 287.

Källtext:

```text
Declination of stylus tilt on X-Axis. 90/-90 when stylus is parallel to tablet and 0 when it's perpendicular to tablet.
```

Före:

```text
Pennans lutning i x-led relativt ritbrädans yta. Är 0 när pennan är parallell och 90.0 när den hålls vinkelrät.
```

Efter:

```text
Pennans lutning i x-led. Värdet är 90 eller −90 när pennan är parallell med ritplattan och 0 när den är vinkelrät mot ritplattan.
```

## F030 · P2 · Pennans vinkelvärden är omkastade (y-led)

Originalet anger ±90 vid parallell penna och 0 vid vinkelrät penna. Översättningen anger motsatsen.

PO-rad: original 290, rättad 290.

Källtext:

```text
Declination of stylus tilt on Y-Axis. 90/-90 when stylus is parallel to tablet and 0 when it's perpendicular to tablet.
```

Före:

```text
Pennans lutning i y-led relativt ritbrädans yta. Är 0 när pennan är parallell och 90.0 när den hålls vinkelrät.
```

Efter:

```text
Pennans lutning i y-led. Värdet är 90 eller −90 när pennan är parallell med ritplattan och 0 när den är vinkelrät mot ritplattan.
```

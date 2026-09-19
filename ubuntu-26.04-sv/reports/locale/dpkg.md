# locale/dpkg

3 rättade översättningsposter. Ursprung: `/usr/share/locale/sv/LC_MESSAGES/dpkg.mo`.

Jämförelsen gäller översatta meddelanden, utan metadatahuvudet. Gettext kan normalisera det kompilerade huvudets teckenkodning och skapandedatum; före/efter finns i metadata. PO-filerna och diffarna behåller ursprunglig teckenkodning (OpenSP: ISO-8859-1).

Upstream: [dpkg](https://wiki.debian.org/Teams/Dpkg).

[Ubuntu-källpaket](https://launchpad.net/ubuntu/+source/dpkg). Installerat ägarpaket: `dpkg 1.23.7ubuntu1`.

[Rättad PO](../../po/locale/dpkg.po) · [Original](../../original/locale/dpkg.po) · [Diff](../../diff/locale/dpkg.po.diff) · [Metadata](../../metadata/locale/dpkg.json)

Rättad PO godkänns av `msgfmt --check --check-format`. Diffen återger filen byte för byte. Den kompilerade meddelandetabellen skiljer sig från installerad MO endast genom rättningarna nedan. PO-huvudet är bevarat; rapporten dokumenterar ändringarnas datum.

Råträffar: l10n-lint 152 → 147, svlang 3 → 3. Kvarstående träffar är kandidater och innebär inte verifierade fel.

## F012 · P2 · Översättningen lägger till ett obefintligt argument

Originalet innehåller ingen %s. Översättningen har kvar en platshållare och ett prefix som saknar motsvarighet i källtexten.

PO-rad: original 3412, rättad 3413.

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

## F050 · P3 · Felaktig upprepning: men men

Upprepningen är ett skrivfel i denna mening och har inte stöd i källtexten.

PO-rad: original 133, rättad 133.

Källtext:

```text
  %s provides %s but is %s.

```

Före:

```text
%s tillhandahåller %s men men är %s.

```

Efter:

```text
%s tillhandahåller %s men är %s.

```

## F051 · P3 · Felaktig upprepning: för för

Upprepningen är ett skrivfel i denna mening och har inte stöd i källtexten.

PO-rad: original 2424, rättad 2425.

Källtext:

```text
cannot set security execution context for maintainer script
```

Före:

```text
kan inte sätta säkerhetsexekveringssammanhang för för utvecklarskript
```

Efter:

```text
kan inte sätta säkerhetsexekveringssammanhang för utvecklarskript
```

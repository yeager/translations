# locale/OpenSP

9 rättade översättningsposter. Ursprung: `/usr/share/locale/sv/LC_MESSAGES/OpenSP.mo`.

Jämförelsen gäller översatta meddelanden, utan metadatahuvudet. Gettext kan normalisera det kompilerade huvudets teckenkodning och skapandedatum; före/efter finns i metadata. PO-filerna och diffarna behåller ursprunglig teckenkodning (OpenSP: ISO-8859-1).

Upstream: [OpenSP / OpenJade](https://openjade.sourceforge.net/).

[Ubuntu-källpaket](https://launchpad.net/ubuntu/+source/opensp). Installerat ägarpaket: `libosp5 1.5.2-15.2ubuntu2`.

[Rättad PO](../../po/locale/OpenSP.po) · [Original](../../original/locale/OpenSP.po) · [Diff](../../diff/locale/OpenSP.po.diff) · [Metadata](../../metadata/locale/OpenSP.json)

Rättad PO godkänns av `msgfmt --check --check-format`. Diffen återger filen byte för byte. Den kompilerade meddelandetabellen skiljer sig från installerad MO endast genom rättningarna nedan. PO-huvudet är bevarat; rapporten dokumenterar ändringarnas datum.

Råträffar: l10n-lint 49 → 30, svlang 0 → 0. Kvarstående träffar är kandidater och innebär inte verifierade fel.

## F004 · P2 · Fel argument för den saknade starttaggen

Den andra platshållaren ska vara %2; nu visas argument %1 två gånger.

PO-rad: original 799, rättad 799.

Källtext:

```text
document type does not allow element %1 here; assuming missing %2 start-tag
```

Före:

```text
dokumenttypen tillåter ej elementet %1 här; antar att starttaggen %1 saknas
```

Efter:

```text
dokumenttypen tillåter ej elementet %1 här; antar att starttaggen %2 saknas
```

## F005 · P2 · HTTP-adressen har tappat sin platshållare

%1 har ersatts med (%), så den berörda URL-adressen kan inte återges korrekt.

PO-rad: original 874, rättad 874.

Källtext:

```text
empty host in HTTP URL %1
```

Före:

```text
tom värd i HTTP-URL:en(%)
```

Efter:

```text
tom värd i HTTP-URL:en %1
```

## F006 · P2 · Identifieraren saknas i felmeddelandet

Originalets %1 saknas i översättningen.

PO-rad: original 1120, rättad 1120.

Källtext:

```text
invalid formal public identifier %1: no SPACE after public text class
```

Före:

```text
ogiltig formell publik identifierare: inget SPACE efter publik textklass
```

Efter:

```text
ogiltig formell publik identifierare %1: inget SPACE efter publik textklass
```

## F007 · P2 · Värdnumret saknas i felmeddelandet

Originalets %1 saknas i översättningen.

PO-rad: original 1126, rättad 1126.

Källtext:

```text
invalid host number %1
```

Före:

```text
ogiltigt värdnummer
```

Efter:

```text
ogiltigt värdnummer %1
```

## F008 · P2 · Numrerad platshållare har blivit printf-format

%1 har ändrats till %d, vilket är en annan formatsyntax.

PO-rad: original 1390, rättad 1390.

Källtext:

```text
normalized length of attribute value literal must not exceed LITLEN (%1); length was %2
```

Före:

```text
längden av normaliserad attributvärdesliteral får ej överskrida LITLEN (%d); längden var %2
```

Efter:

```text
längden av normaliserad attributvärdesliteral får ej överskrida LITLEN (%1); längden var %2
```

## F009 · P2 · Entitetens namn saknas

Originalets %1 saknas; felmeddelandet tappar uppgiften om vilken entitet som avses.

PO-rad: original 1537, rättad 1537.

Källtext:

```text
reference to external data entity %1 not allowed in XML
```

Före:

```text
referens till extern dataentitet ej tillåtet i XML
```

Efter:

```text
referens till extern dataentitet %1 ej tillåtet i XML
```

## F010 · P2 · Entitetens namn saknas

Originalets %1 saknas; felmeddelandet tappar uppgiften om vilken entitet som avses.

PO-rad: original 1546, rättad 1546.

Källtext:

```text
reference to internal SDATA entity %1 not allowed in XML
```

Före:

```text
referens till intern SDATA-entitet ej tillåtet i XML
```

Efter:

```text
referens till intern SDATA-entitet %1 ej tillåtet i XML
```

## F011 · P2 · Entitetens namn saknas

Originalets %1 saknas; felmeddelandet tappar uppgiften om vilken entitet som avses.

PO-rad: original 1567, rättad 1567.

Källtext:

```text
reference to subdocument entity %1 not allowed in XML
```

Före:

```text
referens till subdokumententitet ej tillåtet i XML
```

Efter:

```text
referens till subdokumententitet %1 ej tillåtet i XML
```

## F049 · P3 · Felaktig upprepning: därför därför

Upprepningen är ett skrivfel i denna mening och har inte stöd i källtexten.

PO-rad: original 646, rättad 646.

Källtext:

```text
character %1 is not significant in the reference concrete syntax and so cannot occur in a comment in the SGML declaration
```

Före:

```text
tecknet %1 är ej signifikant i den konkreta referenssyntaxen och får därför därför ej förekomma i en kommentar i SGML-deklarationen
```

Efter:

```text
tecknet %1 är ej signifikant i den konkreta referenssyntaxen och får därför ej förekomma i en kommentar i SGML-deklarationen
```

# locale-langpack/xz-man

3 rättade översättningsposter. Ursprung: `/usr/share/locale-langpack/sv/LC_MESSAGES/xz-man.mo`.

Jämförelsen gäller översatta meddelanden, utan metadatahuvudet. Gettext kan normalisera det kompilerade huvudets teckenkodning och skapandedatum; före/efter finns i metadata. PO-filerna och diffarna behåller ursprunglig teckenkodning (OpenSP: ISO-8859-1).

Upstream: [XZ Utils](https://tukaani.org/xz/).

[Ubuntu-källpaket](https://launchpad.net/ubuntu/+source/xz-utils). Installerat ägarpaket: `language-pack-sv-base 1:26.04+20260818`.

[Rättad PO](../../po/locale-langpack/xz-man.po) · [Original](../../original/locale-langpack/xz-man.po) · [Diff](../../diff/locale-langpack/xz-man.po.diff) · [Metadata](../../metadata/locale-langpack/xz-man.json)

Rättad PO godkänns av `msgfmt --check --check-format`. Diffen återger filen byte för byte. Den kompilerade meddelandetabellen skiljer sig från installerad MO endast genom rättningarna nedan. PO-huvudet är bevarat; rapporten dokumenterar ändringarnas datum.

Råträffar: l10n-lint 202 → 197, svlang 0 → 0. Kvarstående träffar är kandidater och innebär inte verifierade fel.

## F048 · P3 · Stavfel: kommmer

Ett överflödigt eller saknat tecken ger ett felstavat svenskt ord.

PO-rad: original 1120, rättad 1120.

Källtext:

```text
Future versions may add new line types and new columns can be added to the existing line types, but the existing columns won't be changed.
```

Före:

```text
Framtida versioner kan lägga till fler radtyper och fler kolumner kan läggas til på de befintliga radtyperna, men de befintliga kolumnerna kommmer inte ändras.
```

Efter:

```text
Framtida versioner kan lägga till fler radtyper och fler kolumner kan läggas til på de befintliga radtyperna, men de befintliga kolumnerna kommer inte ändras.
```

## F056 · P3 · Felaktig upprepning: 1 beta beta

Upprepningen är ett skrivfel i denna mening och har inte stöd i källtexten.

PO-rad: original 1651, rättad 1651.

Källtext:

```text
Stability.  0 is alpha, 1 is beta, and 2 is stable.  I<S> should be always 2 when I<YYY> is even.
```

Före:

```text
Stabilitet.  0 är alfa, 1 beta beta och 2 är stabil. I<S> skall alltid vara 2 när I<YYY> är jämnt.
```

Efter:

```text
Stabilitet.  0 är alfa, 1 är beta och 2 är stabil. I<S> skall alltid vara 2 när I<YYY> är jämnt.
```

## F057 · P3 · Felaktig upprepning: med med

Upprepningen är ett skrivfel i denna mening och har inte stöd i källtexten.

PO-rad: original 1837, rättad 1837.

Källtext:

```text
These are like B<-6> but with higher compressor and decompressor memory requirements.  These are useful only when compressing files bigger than 8\ MiB, 16\ MiB, and 32\ MiB, respectively.
```

Före:

```text
Dessa liknar B<-6> med med högre krav på minne till komprimerare och dekomprimerare. Dessa är bara användbara vid komprimering av filer större än 8\ MiB, 16\ MiB respektive 32\ MiB.
```

Efter:

```text
Dessa liknar B<-6> men med högre krav på minne till komprimerare och dekomprimerare. Dessa är bara användbara vid komprimering av filer större än 8\ MiB, 16\ MiB respektive 32\ MiB.
```

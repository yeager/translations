# locale-langpack/mutt

1 rättade översättningsposter. Ursprung: `/usr/share/locale-langpack/sv/LC_MESSAGES/mutt.mo`.

Jämförelsen gäller översatta meddelanden, utan metadatahuvudet. Gettext kan normalisera det kompilerade huvudets teckenkodning och skapandedatum; före/efter finns i metadata. PO-filerna och diffarna behåller ursprunglig teckenkodning (OpenSP: ISO-8859-1).

Upstream: [Mutt](http://www.mutt.org/). [Källkod](https://gitlab.com/muttmua/mutt).

[Ubuntu-källpaket](https://launchpad.net/ubuntu/+source/mutt). Installerat ägarpaket: `language-pack-sv-base 1:26.04+20260818`.

[Rättad PO](../../po/locale-langpack/mutt.po) · [Original](../../original/locale-langpack/mutt.po) · [Diff](../../diff/locale-langpack/mutt.po.diff) · [Metadata](../../metadata/locale-langpack/mutt.json)

Rättad PO godkänns av `msgfmt --check --check-format`. Diffen återger filen byte för byte. Den kompilerade meddelandetabellen skiljer sig från installerad MO endast genom rättningarna nedan. PO-huvudet är bevarat; rapporten dokumenterar ändringarnas datum.

Råträffar: l10n-lint 96 → 95, svlang 9 → 9. Kvarstående träffar är kandidater och innebär inte verifierade fel.

## F043 · P3 · Stavfel: öpppna

Ett överflödigt eller saknat tecken ger ett felstavat svenskt ord.

PO-rad: original 1298, rättad 1298.

Källtext:

```text
Failure to open file to parse headers.
```

Före:

```text
Misslyckades med att öpppna fil för att tolka huvuden.
```

Efter:

```text
Misslyckades med att öppna fil för att tolka huvuden.
```

# locale-langpack/cinder

1 rättade översättningsposter. Ursprung: `/usr/share/locale-langpack/sv/LC_MESSAGES/cinder.mo`.

Jämförelsen gäller översatta meddelanden, utan metadatahuvudet. Gettext kan normalisera det kompilerade huvudets teckenkodning och skapandedatum; före/efter finns i metadata. PO-filerna och diffarna behåller ursprunglig teckenkodning (OpenSP: ISO-8859-1).

Upstream: [OpenStack Cinder](https://opendev.org/openstack/cinder).

[Ubuntu-källpaket](https://launchpad.net/ubuntu/+source/cinder). Installerat ägarpaket: `language-pack-sv-base 1:26.04+20260818`.

[Rättad PO](../../po/locale-langpack/cinder.po) · [Original](../../original/locale-langpack/cinder.po) · [Diff](../../diff/locale-langpack/cinder.po.diff) · [Metadata](../../metadata/locale-langpack/cinder.json)

Rättad PO godkänns av `msgfmt --check --check-format`. Diffen återger filen byte för byte. Den kompilerade meddelandetabellen skiljer sig från installerad MO endast genom rättningarna nedan. PO-huvudet är bevarat; rapporten dokumenterar ändringarnas datum.

Råträffar: l10n-lint 31 → 30, svlang 4 → 4. Kvarstående träffar är kandidater och innebär inte verifierade fel.

## F001 · P1 · Fel nyckel i Python-formatfält

ret.status har blivit ret.statuss. Formatering med originalets nycklar ger KeyError.

PO-rad: original 1695, rättad 1695.

Källtext:

```text
Error getting replication source details. Return code: %(ret.status)d Message: %(ret.data)s .
```

Före:

```text
Fel vid hämtning av replikationskällans detaljer. Returkod: %(ret.statuss)d Meddelande: %(ret.data)s .
```

Efter:

```text
Fel vid hämtning av replikationskällans detaljer. Returkod: %(ret.status)d Meddelande: %(ret.data)s .
```

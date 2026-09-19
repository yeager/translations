# locale-langpack/glance

2 rättade översättningsposter. Ursprung: `/usr/share/locale-langpack/sv/LC_MESSAGES/glance.mo`.

Jämförelsen gäller översatta meddelanden, utan metadatahuvudet. Gettext kan normalisera det kompilerade huvudets teckenkodning och skapandedatum; före/efter finns i metadata. PO-filerna och diffarna behåller ursprunglig teckenkodning (OpenSP: ISO-8859-1).

Upstream: [OpenStack Glance](https://launchpad.net/glance). [Källkod](https://opendev.org/openstack/glance).

[Ubuntu-källpaket](https://launchpad.net/ubuntu/+source/glance). Installerat ägarpaket: `language-pack-sv-base 1:26.04+20260818`.

[Rättad PO](../../po/locale-langpack/glance.po) · [Original](../../original/locale-langpack/glance.po) · [Diff](../../diff/locale-langpack/glance.po.diff) · [Metadata](../../metadata/locale-langpack/glance.json)

Rättad PO godkänns av `msgfmt --check --check-format`. Diffen återger filen byte för byte. Den kompilerade meddelandetabellen skiljer sig från installerad MO endast genom rättningarna nedan. PO-huvudet är bevarat; rapporten dokumenterar ändringarnas datum.

Råträffar: l10n-lint 7 → 5, svlang 0 → 0. Kvarstående träffar är kandidater och innebär inte verifierade fel.

## F002 · P2 · Typbokstaven saknas efter image_id

%(image_id) saknar s. Python konsumerar mellanslaget och s i ordet som som formatsyntax: exempelvärdet image-1 följs av om i stället för som.

PO-rad: original 1473, rättad 1473.

Källtext:

```text
The Image %(image_id)s object being created by this task %(task_id)s, is no longer in valid status for further processing.
```

Före:

```text
Avbildobjektet %(image_id) som skapas av den här uppgiften %(task_id)s, är inte längre i en giltig status för vidare behandling.
```

Efter:

```text
Avbildobjektet %(image_id)s som skapas av den här uppgiften %(task_id)s, är inte längre i en giltig status för vidare behandling.
```

## F042 · P3 · Stavfel: tilllåter

Ett överflödigt eller saknat tecken ger ett felstavat svenskt ord.

PO-rad: original 1398, rättad 1398.

Källtext:

```text
Some resource types allow more than one key / value pair per instance.  For example, Cinder allows user and image metadata on volumes. Only the image properties metadata is evaluated by Nova (scheduling or drivers). This property allows a namespace target to remove the ambiguity.
```

Före:

```text
Vissa resurstyper tillåter fler än ett nyckel-/värdepar per instans. Till exempel Cinder tilllåter användar- och bildmetadata på volymer. Bara bildegenskapers metadata utvärderas av Nova (schemaläggning eller drivrutiner). Denna egenskap tillåter en namnrymd att ta bort tvetydigheten.
```

Efter:

```text
Vissa resurstyper tillåter fler än ett nyckel-/värdepar per instans. Till exempel Cinder tillåter användar- och bildmetadata på volymer. Bara bildegenskapers metadata utvärderas av Nova (schemaläggning eller drivrutiner). Denna egenskap tillåter en namnrymd att ta bort tvetydigheten.
```

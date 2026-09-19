# locale-langpack/synaptic

1 rättade översättningsposter. Ursprung: `/usr/share/locale-langpack/sv/LC_MESSAGES/synaptic.mo`.

Jämförelsen gäller översatta meddelanden, utan metadatahuvudet. Gettext kan normalisera det kompilerade huvudets teckenkodning och skapandedatum; före/efter finns i metadata. PO-filerna och diffarna behåller ursprunglig teckenkodning (OpenSP: ISO-8859-1).

Upstream: [Synaptic](https://github.com/mvo5/synaptic).

[Ubuntu-källpaket](https://launchpad.net/ubuntu/+source/synaptic). Installerat ägarpaket: `language-pack-sv-base 1:26.04+20260818`.

[Rättad PO](../../po/locale-langpack/synaptic.po) · [Original](../../original/locale-langpack/synaptic.po) · [Diff](../../diff/locale-langpack/synaptic.po.diff) · [Metadata](../../metadata/locale-langpack/synaptic.json)

Rättad PO godkänns av `msgfmt --check --check-format`. Diffen återger filen byte för byte. Den kompilerade meddelandetabellen skiljer sig från installerad MO endast genom rättningarna nedan. PO-huvudet är bevarat; rapporten dokumenterar ändringarnas datum.

Råträffar: l10n-lint 13 → 11, svlang 0 → 0. Kvarstående träffar är kandidater och innebär inte verifierade fel.

## F026 · P2 · Fel avslutning av big-taggen

<b><big> avslutas med </b></b>. Den inre taggen ska avslutas med </big>.

PO-rad: original 281, rättad 281.

Källtext:

```text
<b><big>Mark upgrades in a smart way?</big></b>

The default upgrade method skips upgrades that would introduce conflicts or require installation of additional packages.

The smart upgrade (dist-upgrade) attempts to resolve conflicts and to fulfil all dependencies of upgrades in a smart way.

<b>Note:</b> The upgrades will be marked only. You still have to apply them afterwards.
```

Före:

```text
<b><big>Markera uppgraderingar på ett smart sätt?</b></b>

Standardmetoden för uppgradering hoppar över de uppgraderingar som skulle introducera konflikter eller kräva installation av ytterligare paket.

Den smarta uppgraderingen (dist-upgrade) försöker att lösa konflikter och uppfylla alla beroenden för uppgraderingen på ett smart sätt.

<b>Observera:</b> Uppgraderingarna kommer endast markeras. Du behöver fortfarande verkställa dem efteråt.
```

Efter:

```text
<b><big>Markera uppgraderingar på ett smart sätt?</big></b>

Standardmetoden för uppgradering hoppar över de uppgraderingar som skulle introducera konflikter eller kräva installation av ytterligare paket.

Den smarta uppgraderingen (dist-upgrade) försöker att lösa konflikter och uppfylla alla beroenden för uppgraderingen på ett smart sätt.

<b>Observera:</b> Uppgraderingarna kommer endast markeras. Du behöver fortfarande verkställa dem efteråt.
```

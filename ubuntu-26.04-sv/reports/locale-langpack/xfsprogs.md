# locale-langpack/xfsprogs

2 rättade översättningsposter. Ursprung: `/usr/share/locale-langpack/sv/LC_MESSAGES/xfsprogs.mo`.

Jämförelsen gäller översatta meddelanden, utan metadatahuvudet. Gettext kan normalisera det kompilerade huvudets teckenkodning och skapandedatum; före/efter finns i metadata. PO-filerna och diffarna behåller ursprunglig teckenkodning (OpenSP: ISO-8859-1).

Upstream: [XFS utilities](https://xfs.wiki.kernel.org/).

[Ubuntu-källpaket](https://launchpad.net/ubuntu/+source/xfsprogs). Installerat ägarpaket: `language-pack-sv-base 1:26.04+20260818`.

[Rättad PO](../../po/locale-langpack/xfsprogs.po) · [Original](../../original/locale-langpack/xfsprogs.po) · [Diff](../../diff/locale-langpack/xfsprogs.po.diff) · [Metadata](../../metadata/locale-langpack/xfsprogs.json)

Rättad PO godkänns av `msgfmt --check --check-format`. Diffen återger filen byte för byte. Den kompilerade meddelandetabellen skiljer sig från installerad MO endast genom rättningarna nedan. PO-huvudet är bevarat; rapporten dokumenterar ändringarnas datum.

Råträffar: l10n-lint 400 → 398, svlang 4 → 4. Kvarstående träffar är kandidater och innebär inte verifierade fel.

## F054 · P3 · Felaktig upprepning: ignoreras ignoreras

Upprepningen är ett skrivfel i denna mening och har inte stöd i källtexten.

PO-rad: original 5717, rättad 5717.

Källtext:

```text
ALERT: The filesystem has valuable metadata changes in a log which is being
ignored because the -n option was used.  Expect spurious inconsistencies
which may be resolved by first mounting the filesystem to replay the log.

```

Före:

```text
VARNING: Filsystemet har värdefulla metadataändringar i en logg som ignoreras
ignoreras eftersom flaggan -n användes.  Förvänta dig falska inkonsekvenser
som kan lösas genom att först montera filsystemet för att spela upp loggen igen.

```

Efter:

```text
VARNING: Filsystemet har värdefulla metadataändringar i en logg som ignoreras eftersom flaggan -n användes.  Förvänta dig falska inkonsekvenser
som kan lösas genom att först montera filsystemet för att spela upp loggen igen.

```

## F055 · P3 · Felaktig upprepning: filsystemet filsystemet

Upprepningen är ett skrivfel i denna mening och har inte stöd i källtexten.

PO-rad: original 6391, rättad 6390.

Källtext:

```text
ERROR: The log head and/or tail cannot be discovered. Attempt to mount the
filesystem to replay the log or use the -L option to destroy the log and
attempt a repair.

```

Före:

```text
FEL: Loggens huvud och/eller svans kan inte hittas. Försök att montera filsystemet
filsystemet för att spela upp loggen igen eller använd flaggan -L för att förstöra loggen och
försöka reparera den.

```

Efter:

```text
FEL: Loggens huvud och/eller svans kan inte hittas. Försök att montera filsystemet för att spela upp loggen igen eller använd flaggan -L för att förstöra loggen och
försöka reparera den.

```

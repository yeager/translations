# locale-langpack/ubiquity-debconf

1 rättade översättningsposter. Ursprung: `/usr/share/locale-langpack/sv/LC_MESSAGES/ubiquity-debconf.mo`.

Jämförelsen gäller översatta meddelanden, utan metadatahuvudet. Gettext kan normalisera det kompilerade huvudets teckenkodning och skapandedatum; före/efter finns i metadata. PO-filerna och diffarna behåller ursprunglig teckenkodning (OpenSP: ISO-8859-1).

Upstream: [Ubiquity / Debian Installer messages](https://launchpad.net/ubiquity).

[Ubuntu-källpaket](https://launchpad.net/ubuntu/+source/ubiquity). Installerat ägarpaket: `language-pack-gnome-sv-base 1:26.04+20260818`.

[Rättad PO](../../po/locale-langpack/ubiquity-debconf.po) · [Original](../../original/locale-langpack/ubiquity-debconf.po) · [Diff](../../diff/locale-langpack/ubiquity-debconf.po.diff) · [Metadata](../../metadata/locale-langpack/ubiquity-debconf.json)

Rättad PO godkänns av `msgfmt --check --check-format`. Diffen återger filen byte för byte. Den kompilerade meddelandetabellen skiljer sig från installerad MO endast genom rättningarna nedan. PO-huvudet är bevarat; rapporten dokumenterar ändringarnas datum.

Råträffar: l10n-lint 48 → 48, svlang 1 → 0. Kvarstående träffar är kandidater och innebär inte verifierade fel.

## F039 · P3 · Stavfel: tidspunkt

Ett överflödigt eller saknat tecken ger ett felstavat svenskt ord.

PO-rad: original 810, rättad 810.

Källtext:

```text
This may be due to using an old installer image, or it may be due to a bug in some of the packages listed above. More details may be found in /var/log/syslog. The installer will try to continue anyway, but may fail at a later point, and will not be able to install or remove other packages (possibly including itself) from the installed system. You should first look for newer versions of your installer image, or failing that report the problem to your distributor.
```

Före:

```text
Det här kan bero på användningen av en gammal installationsavbild, eller det kan bero på ett fel i några av de paket som listas ovan. Mer information kan hittas i filen /var/log/syslog. Installationsprogrammet kommer att försöka fortsätta ändå men kan misslyckas vid en senare tidspunkt, och kommer inte kunna installera eller ta bort andra paket (kanske även sig själv) från det installerade systemet. Du bör först leta efter nyare versioner av din installationsavbild, eller rapportera misslyckandet till din leverantör.
```

Efter:

```text
Det här kan bero på användningen av en gammal installationsavbild, eller det kan bero på ett fel i några av de paket som listas ovan. Mer information kan hittas i filen /var/log/syslog. Installationsprogrammet kommer att försöka fortsätta ändå men kan misslyckas vid en senare tidpunkt, och kommer inte kunna installera eller ta bort andra paket (kanske även sig själv) från det installerade systemet. Du bör först leta efter nyare versioner av din installationsavbild, eller rapportera misslyckandet till din leverantör.
```

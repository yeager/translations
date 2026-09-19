# locale-langpack/git

1 rättade översättningsposter. Ursprung: `/usr/share/locale-langpack/sv/LC_MESSAGES/git.mo`.

Jämförelsen gäller översatta meddelanden, utan metadatahuvudet. Gettext kan normalisera det kompilerade huvudets teckenkodning och skapandedatum; före/efter finns i metadata. PO-filerna och diffarna behåller ursprunglig teckenkodning (OpenSP: ISO-8859-1).

Upstream: [Git](https://git-scm.com/). [Källkod](https://github.com/git/git).

[Ubuntu-källpaket](https://launchpad.net/ubuntu/+source/git). Installerat ägarpaket: `language-pack-sv-base 1:26.04+20260818`.

[Rättad PO](../../po/locale-langpack/git.po) · [Original](../../original/locale-langpack/git.po) · [Diff](../../diff/locale-langpack/git.po.diff) · [Metadata](../../metadata/locale-langpack/git.json)

Rättad PO godkänns av `msgfmt --check --check-format`. Diffen återger filen byte för byte. Den kompilerade meddelandetabellen skiljer sig från installerad MO endast genom rättningarna nedan. PO-huvudet är bevarat; rapporten dokumenterar ändringarnas datum.

Råträffar: l10n-lint 756 → 747, svlang 84 → 84. Kvarstående träffar är kandidater och innebär inte verifierade fel.

Två redundanta sysdep-poster från msgunfmt har dessutom tagits bort. De portabla PRIuMAX-posterna är bevarade. Återkompilering visar oförändrad runtime-tabell för dessa poster. Se metadata och diff.

## F021 · P2 · Extra %s i meddelandet om incheckningsgraf

Källtexten har ingen platshållare för filnamn men översättningen har %s.

PO-rad: original 8271, rättad 8261.

Källtext:

```text
commit-graph file is too small
```

Före:

```text
incheckningsgraffilen %s är för liten
```

Efter:

```text
incheckningsgraffilen är för liten
```

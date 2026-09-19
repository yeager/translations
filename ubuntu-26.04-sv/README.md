# Ubuntu 26.04 – granskning av svenska översättningar

Granskad 19 september 2026 på Ubuntu 26.04.1 LTS. **31 rättade PO-filer, 61 ändrade översättningsposter från 57 verifierade fyndgrupper.** Originalen är extraherade med `msgunfmt --no-wrap` från de två installerade svenska katalogmapparna.

[Full rapport](rapport.md) · [Alla metadata](metadata.json) · [Valideringsresultat](validation-summary.json) · [Samtliga fynd](findings.json)

Varje rättad PO har en exakt diff, ett oförändrat dekompilerat original, en separat rapport och metadata med upstream, ägarpaket, version, MO-sökväg, SHA-256, PO-huvud, före/efter och validering. Länkarna till upstream identifierar projekten; katalogerna är Ubuntu-versionerna som faktiskt fanns installerade.

Samtliga 31 rättade PO-filer klarar `msgfmt --check --check-format`. Alla diffar har applicerats utan fuzz och ger exakt publicerade bytes. Återkompilering ger samma meddelandetabell som installerad MO utom de 61 avsedda rättningarna. Git har dessutom två redundanta sysdep-poster borttagna, vilket behövs för återkompilering; runtime-tabellen är bevarad. Systemets MO-filer har inte ändrats.

Jämförelsen gäller översatta meddelanden, utan metadatahuvudet. Gettext kan normalisera det kompilerade huvudets teckenkodning och skapandedatum; före/efter finns i metadata. PO-filerna och diffarna behåller ursprunglig teckenkodning (OpenSP: ISO-8859-1).

Automatisk granskning omfattade 479 MO-sökvägar, 473 unika kataloger och 230 304 poster. Rapportens råträffar avser originalen efter fem förbättringar i granskningsverktygen. Fynden är ett manuellt granskat urval, inte en fullständig språkgranskning.

| Katalog | Rättningar | PO | Diff | Rapport | Metadata | Upstream |
|---|---:|---|---|---|---|---|
| locale-langpack/NetworkManager | 2 | [PO](po/locale-langpack/NetworkManager.po) | [Diff](diff/locale-langpack/NetworkManager.po.diff) | [Rapport](reports/locale-langpack/NetworkManager.md) | [JSON](metadata/locale-langpack/NetworkManager.json) | [NetworkManager](https://networkmanager.dev/) |
| locale-langpack/app-install-data | 2 | [PO](po/locale-langpack/app-install-data.po) | [Diff](diff/locale-langpack/app-install-data.po.diff) | [Rapport](reports/locale-langpack/app-install-data.md) | [JSON](metadata/locale-langpack/app-install-data.json) | [Ubuntu app-install-data](https://launchpad.net/ubuntu/+source/app-install-data-ubuntu) |
| locale-langpack/binutils | 2 | [PO](po/locale-langpack/binutils.po) | [Diff](diff/locale-langpack/binutils.po.diff) | [Rapport](reports/locale-langpack/binutils.md) | [JSON](metadata/locale-langpack/binutils.json) | [GNU Binutils](https://sourceware.org/binutils/) |
| locale-langpack/cinder | 1 | [PO](po/locale-langpack/cinder.po) | [Diff](diff/locale-langpack/cinder.po.diff) | [Rapport](reports/locale-langpack/cinder.md) | [JSON](metadata/locale-langpack/cinder.json) | [OpenStack Cinder](https://opendev.org/openstack/cinder) |
| locale-langpack/cryptsetup | 2 | [PO](po/locale-langpack/cryptsetup.po) | [Diff](diff/locale-langpack/cryptsetup.po.diff) | [Rapport](reports/locale-langpack/cryptsetup.md) | [JSON](metadata/locale-langpack/cryptsetup.json) | [cryptsetup](https://gitlab.com/cryptsetup/cryptsetup) |
| locale-langpack/dpkg | 1 | [PO](po/locale-langpack/dpkg.po) | [Diff](diff/locale-langpack/dpkg.po.diff) | [Rapport](reports/locale-langpack/dpkg.md) | [JSON](metadata/locale-langpack/dpkg.json) | [dpkg](https://wiki.debian.org/Teams/Dpkg) |
| locale-langpack/dpkg-dev | 2 | [PO](po/locale-langpack/dpkg-dev.po) | [Diff](diff/locale-langpack/dpkg-dev.po.diff) | [Rapport](reports/locale-langpack/dpkg-dev.md) | [JSON](metadata/locale-langpack/dpkg-dev.json) | [dpkg](https://wiki.debian.org/Teams/Dpkg) |
| locale-langpack/fetchmail | 1 | [PO](po/locale-langpack/fetchmail.po) | [Diff](diff/locale-langpack/fetchmail.po.diff) | [Rapport](reports/locale-langpack/fetchmail.md) | [JSON](metadata/locale-langpack/fetchmail.json) | [fetchmail](https://www.fetchmail.info/) |
| locale-langpack/gas | 1 | [PO](po/locale-langpack/gas.po) | [Diff](diff/locale-langpack/gas.po.diff) | [Rapport](reports/locale-langpack/gas.md) | [JSON](metadata/locale-langpack/gas.json) | [GNU Binutils / GNU assembler](https://sourceware.org/binutils/) |
| locale-langpack/gdb | 3 | [PO](po/locale-langpack/gdb.po) | [Diff](diff/locale-langpack/gdb.po.diff) | [Rapport](reports/locale-langpack/gdb.md) | [JSON](metadata/locale-langpack/gdb.json) | [GNU GDB](https://sourceware.org/gdb/) |
| locale-langpack/git | 1 | [PO](po/locale-langpack/git.po) | [Diff](diff/locale-langpack/git.po.diff) | [Rapport](reports/locale-langpack/git.md) | [JSON](metadata/locale-langpack/git.json) | [Git](https://git-scm.com/) |
| locale-langpack/glance | 2 | [PO](po/locale-langpack/glance.po) | [Diff](diff/locale-langpack/glance.po.diff) | [Rapport](reports/locale-langpack/glance.md) | [JSON](metadata/locale-langpack/glance.json) | [OpenStack Glance](https://launchpad.net/glance) |
| locale-langpack/ld | 1 | [PO](po/locale-langpack/ld.po) | [Diff](diff/locale-langpack/ld.po.diff) | [Rapport](reports/locale-langpack/ld.md) | [JSON](metadata/locale-langpack/ld.json) | [GNU Binutils / GNU linker](https://sourceware.org/binutils/) |
| locale-langpack/libgphoto2-2 | 2 | [PO](po/locale-langpack/libgphoto2-2.po) | [Diff](diff/locale-langpack/libgphoto2-2.po.diff) | [Rapport](reports/locale-langpack/libgphoto2-2.md) | [JSON](metadata/locale-langpack/libgphoto2-2.json) | [libgphoto2](https://github.com/gphoto/libgphoto2) |
| locale-langpack/libgphoto2-6 | 2 | [PO](po/locale-langpack/libgphoto2-6.po) | [Diff](diff/locale-langpack/libgphoto2-6.po.diff) | [Rapport](reports/locale-langpack/libgphoto2-6.md) | [JSON](metadata/locale-langpack/libgphoto2-6.json) | [libgphoto2](https://github.com/gphoto/libgphoto2) |
| locale-langpack/mutt | 1 | [PO](po/locale-langpack/mutt.po) | [Diff](diff/locale-langpack/mutt.po.diff) | [Rapport](reports/locale-langpack/mutt.md) | [JSON](metadata/locale-langpack/mutt.json) | [Mutt](http://www.mutt.org/) |
| locale-langpack/simple-scan | 1 | [PO](po/locale-langpack/simple-scan.po) | [Diff](diff/locale-langpack/simple-scan.po.diff) | [Rapport](reports/locale-langpack/simple-scan.md) | [JSON](metadata/locale-langpack/simple-scan.json) | [GNOME Document Scanner](https://apps.gnome.org/SimpleScan/) |
| locale-langpack/slideshow-oem-config-ubuntu-mate | 1 | [PO](po/locale-langpack/slideshow-oem-config-ubuntu-mate.po) | [Diff](diff/locale-langpack/slideshow-oem-config-ubuntu-mate.po.diff) | [Rapport](reports/locale-langpack/slideshow-oem-config-ubuntu-mate.md) | [JSON](metadata/locale-langpack/slideshow-oem-config-ubuntu-mate.json) | [Ubiquity slideshow](https://launchpad.net/ubiquity-slideshow-ubuntu) |
| locale-langpack/slideshow-ubuntu-mate | 1 | [PO](po/locale-langpack/slideshow-ubuntu-mate.po) | [Diff](diff/locale-langpack/slideshow-ubuntu-mate.po.diff) | [Rapport](reports/locale-langpack/slideshow-ubuntu-mate.md) | [JSON](metadata/locale-langpack/slideshow-ubuntu-mate.json) | [Ubiquity slideshow](https://launchpad.net/ubiquity-slideshow-ubuntu) |
| locale-langpack/snappy | 2 | [PO](po/locale-langpack/snappy.po) | [Diff](diff/locale-langpack/snappy.po.diff) | [Rapport](reports/locale-langpack/snappy.md) | [JSON](metadata/locale-langpack/snappy.json) | [snapd](https://github.com/canonical/snapd) |
| locale-langpack/synaptic | 1 | [PO](po/locale-langpack/synaptic.po) | [Diff](diff/locale-langpack/synaptic.po.diff) | [Rapport](reports/locale-langpack/synaptic.md) | [JSON](metadata/locale-langpack/synaptic.json) | [Synaptic](https://github.com/mvo5/synaptic) |
| locale-langpack/ubiquity-debconf | 1 | [PO](po/locale-langpack/ubiquity-debconf.po) | [Diff](diff/locale-langpack/ubiquity-debconf.po.diff) | [Rapport](reports/locale-langpack/ubiquity-debconf.md) | [JSON](metadata/locale-langpack/ubiquity-debconf.json) | [Ubiquity / Debian Installer messages](https://launchpad.net/ubiquity) |
| locale-langpack/unity | 2 | [PO](po/locale-langpack/unity.po) | [Diff](diff/locale-langpack/unity.po.diff) | [Rapport](reports/locale-langpack/unity.md) | [JSON](metadata/locale-langpack/unity.json) | [Unity](https://launchpad.net/unity) |
| locale-langpack/unity-control-center | 2 | [PO](po/locale-langpack/unity-control-center.po) | [Diff](diff/locale-langpack/unity-control-center.po.diff) | [Rapport](reports/locale-langpack/unity-control-center.md) | [JSON](metadata/locale-langpack/unity-control-center.json) | [Unity Control Center](https://launchpad.net/unity-control-center) |
| locale-langpack/xfsprogs | 2 | [PO](po/locale-langpack/xfsprogs.po) | [Diff](diff/locale-langpack/xfsprogs.po.diff) | [Rapport](reports/locale-langpack/xfsprogs.md) | [JSON](metadata/locale-langpack/xfsprogs.json) | [XFS utilities](https://xfs.wiki.kernel.org/) |
| locale-langpack/xz-man | 3 | [PO](po/locale-langpack/xz-man.po) | [Diff](diff/locale-langpack/xz-man.po.diff) | [Rapport](reports/locale-langpack/xz-man.md) | [JSON](metadata/locale-langpack/xz-man.json) | [XZ Utils](https://tukaani.org/xz/) |
| locale/OpenSP | 9 | [PO](po/locale/OpenSP.po) | [Diff](diff/locale/OpenSP.po.diff) | [Rapport](reports/locale/OpenSP.md) | [JSON](metadata/locale/OpenSP.json) | [OpenSP / OpenJade](https://openjade.sourceforge.net/) |
| locale/dpkg | 3 | [PO](po/locale/dpkg.po) | [Diff](diff/locale/dpkg.po.diff) | [Rapport](reports/locale/dpkg.md) | [JSON](metadata/locale/dpkg.json) | [dpkg](https://wiki.debian.org/Teams/Dpkg) |
| locale/gnome-builder | 1 | [PO](po/locale/gnome-builder.po) | [Diff](diff/locale/gnome-builder.po.diff) | [Rapport](reports/locale/gnome-builder.md) | [JSON](metadata/locale/gnome-builder.json) | [GNOME Builder](https://apps.gnome.org/Builder/) |
| locale/iso_639-3 | 4 | [PO](po/locale/iso_639-3.po) | [Diff](diff/locale/iso_639-3.po.diff) | [Rapport](reports/locale/iso_639-3.md) | [JSON](metadata/locale/iso_639-3.json) | [iso-codes](https://salsa.debian.org/iso-codes-team/iso-codes) |
| locale/libmypaint | 2 | [PO](po/locale/libmypaint.po) | [Diff](diff/locale/libmypaint.po.diff) | [Rapport](reports/locale/libmypaint.md) | [JSON](metadata/locale/libmypaint.json) | [libmypaint](https://github.com/mypaint/libmypaint) |

## Använd en diff

Diffens bas är filen under `original/`, inte en godtycklig aktuell upstream-PO. Exempel:

```sh
cp original/locale-langpack/cinder.po cinder.po
patch --fuzz=0 cinder.po diff/locale-langpack/cinder.po.diff
msgfmt --check --check-format -o /tmp/cinder.mo cinder.po
```

MO-formatet saknar bland annat ursprungliga källreferenser, de flesta formatflaggor, fuzzy-markeringar och oöversatta poster. Bevara upstreams befintliga PO och för över relevanta ändringar vid inskickning dit.

## Verktygsförbättringar

Fem ändringar i l10n-lint och svlang har testats (274 + 83 tester) och installerats lokalt. [Patchar och testunderlag](tool-fixes/) samt [versioner](tools.json) medföljer. De minskade originalmaterialets råträffar med 547. Verktygspatcharna har inte skickats till respektive upstream-repo.

## Underlag

`manifest.json` beskriver samtliga 479 inlästa sökvägar. Enbart de 31 rättade katalogernas PO-original och rårapporter ingår här. Den fullständiga lokala granskningsleveransen innehåller alla extraherade PO-filer. TM-, termbanks- och konsekvensavvikelser för hela materialet finns under `raw/`. ISO-alias `iso_639_3` täcks av filen `iso_639-3`; fyra fynd återkommer via aliaset.

# locale-langpack/dpkg-dev

2 rättade översättningsposter. Ursprung: `/usr/share/locale-langpack/sv/LC_MESSAGES/dpkg-dev.mo`.

Jämförelsen gäller översatta meddelanden, utan metadatahuvudet. Gettext kan normalisera det kompilerade huvudets teckenkodning och skapandedatum; före/efter finns i metadata. PO-filerna och diffarna behåller ursprunglig teckenkodning (OpenSP: ISO-8859-1).

Upstream: [dpkg](https://wiki.debian.org/Teams/Dpkg).

[Ubuntu-källpaket](https://launchpad.net/ubuntu/+source/dpkg). Installerat ägarpaket: `language-pack-sv-base 1:26.04+20260818`.

[Rättad PO](../../po/locale-langpack/dpkg-dev.po) · [Original](../../original/locale-langpack/dpkg-dev.po) · [Diff](../../diff/locale-langpack/dpkg-dev.po.diff) · [Metadata](../../metadata/locale-langpack/dpkg-dev.json)

Rättad PO godkänns av `msgfmt --check --check-format`. Diffen återger filen byte för byte. Den kompilerade meddelandetabellen skiljer sig från installerad MO endast genom rättningarna nedan. PO-huvudet är bevarat; rapporten dokumenterar ändringarnas datum.

Råträffar: l10n-lint 112 → 110, svlang 19 → 19. Kvarstående träffar är kandidater och innebär inte verifierade fel.

## F040 · P3 · Stavfel: körnng

Ett överflödigt eller saknat tecken ger ett felstavat svenskt ord.

PO-rad: original 949, rättad 949.

Källtext:

```text
Options:
  -l<library-path>         add directory to private shared library search list.
  -p<package>              generate symbols file for package.
  -P<package-build-dir>    temporary build directory instead of debian/tmp.
  -e<library>              explicitly list libraries to scan.
  -v<version>              version of the packages (defaults to
                           version extracted from debian/changelog).
  -c<level>                compare generated symbols file with the reference
                           template in the debian directory and fail if
                           difference is too important; level goes from 0 for
                           no check, to 4 for all checks (default level is 1).
  -q                       keep quiet and never emit any warnings or
                           generate a diff between generated symbols
                           file and the reference template.
  -I<file>                 force usage of <file> as reference symbols
                           file instead of the default file.
  -O[<file>]               write to stdout (or <file>), not .../DEBIAN/symbols.
  -t                       write in template mode (tags are not
                           processed and included in output).
  -V                       verbose output; write deprecated symbols and pattern
                           matching symbols as comments (in template mode only).
  -a<arch>                 assume <arch> as host architecture when processing
                           symbol files.
  -d                       display debug information during work.
  -?, --help               show this help message.
      --version            show the version.

```

Före:

```text
Flaggor:
  -l<bibliotekssökväg>     lägg till katalog till privat söklista för delade bibliotek.
  -p<paket>                skapar symbolfil för paket.
  -P<paketbyggkatalog>     temporär byggkatalog istället för debian/tmp.
  -e<bibliotek>            explicit lista över bibliotek att söka i.
  -v<version>              version på paketet (förval är versionen
                           som utläses ur debian/changelog).
  -c<nivå>                 jämför genererade symbolfiler med referensfilen
                           i katalogen ”debian” och misslyckas om skillnaderna
                           är för stora; nivå går från 0 för ingen test, till
                           4 för alla tester (förvald nivå är 1).
  -q                       var tyst och skriv aldrig ut några varningar eller
                           generera en diff mellan genererad symbolfil och
                           referensfilen.
  -I<fil>                  tvinga användning av <fil> som symbolreferensfil
                           istället för standardfilen.
  -O[<fil>]                skriv till standard ut/<fil>, inte .../DEBIAN/symbols.
  -t                       skriv i malläge (taggar behandlas inte och
                           tas med i utdata).
  -V                       pratsam utdata; skriv föråldrade symboler och
                           mönster som motsvarar symboler som kommentarer
                           (endast i mall-läget).
  -a<ark>                  förutsätt <ark> som värdarkitektur vid behandling
                           av symbofilen.
  -d                       visa felsökningsinformation under körnng.
  -?, --help               visa detta hjälpmeddelande.
      --version            visa versionsnummer.

```

Efter:

```text
Flaggor:
  -l<bibliotekssökväg>     lägg till katalog till privat söklista för delade bibliotek.
  -p<paket>                skapar symbolfil för paket.
  -P<paketbyggkatalog>     temporär byggkatalog istället för debian/tmp.
  -e<bibliotek>            explicit lista över bibliotek att söka i.
  -v<version>              version på paketet (förval är versionen
                           som utläses ur debian/changelog).
  -c<nivå>                 jämför genererade symbolfiler med referensfilen
                           i katalogen ”debian” och misslyckas om skillnaderna
                           är för stora; nivå går från 0 för ingen test, till
                           4 för alla tester (förvald nivå är 1).
  -q                       var tyst och skriv aldrig ut några varningar eller
                           generera en diff mellan genererad symbolfil och
                           referensfilen.
  -I<fil>                  tvinga användning av <fil> som symbolreferensfil
                           istället för standardfilen.
  -O[<fil>]                skriv till standard ut/<fil>, inte .../DEBIAN/symbols.
  -t                       skriv i malläge (taggar behandlas inte och
                           tas med i utdata).
  -V                       pratsam utdata; skriv föråldrade symboler och
                           mönster som motsvarar symboler som kommentarer
                           (endast i mall-läget).
  -a<ark>                  förutsätt <ark> som värdarkitektur vid behandling
                           av symbofilen.
  -d                       visa felsökningsinformation under körning.
  -?, --help               visa detta hjälpmeddelande.
      --version            visa versionsnummer.

```

## F041 · P3 · Stavfel: klasss

Ett överflödigt eller saknat tecken ger ett felstavat svenskt ord.

PO-rad: original 1649, rättad 1649.

Källtext:

```text
changelog format %s is not a Dpkg::Changelog class
```

Före:

```text
ändringsloggformatet %s är inte en Dpkg::Changelog-klasss
```

Efter:

```text
ändringsloggformatet %s är inte en Dpkg::Changelog-klass
```

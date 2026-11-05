# Xemu PR #2837 – uppströmskontroll 27 oktober 2026

PR [#2837](https://github.com/xemu-project/xemu/pull/2837) är fortsatt öppen
på commit `03e0e9a6a34ff93f22bf133cdcd7863151e8e414`. GitHub visar inga
check-runs och inga underhållargranskningar. Tre äldre botgranskningar finns;
de är kommentarer, inte godkännanden eller avslag.

Den aktuella grenen kontrollerades mot de konkreta botanmärkningarna:

- `xemu_i18n_init()` sätter först processpråket och återställer sedan
  `LC_NUMERIC` till `C`, så svensk decimalnotation inte läcker in i GLSL.
- `meson.build` går alltid in i `po`, medan `po/meson.build` gör
  gettextkatalogen valfri när `xgettext` saknas. Det tar bort det tidigare
  beroendet av GTK för XUI-katalogen.
- `po/POTFILES` tar med XUI-filerna. De levande FilePicker-raderna för
  skärmbildsmapp, spelmapp och avbild finns som aktiva poster i `po/sv.po`.
- Popupmenyknappen översätter etiketten i den gemensamma hjälpfunktionen,
  vilket täcker bland annat Inställningar och Starta om.
- Senaste committen lägger katalogstöd i uppdaterarens framtida paket men
  behåller Windows-uppdateringsarkiv platta under övergången, för kompatibilitet
  med redan utgivna uppdaterare.

Kvarvarande läge är därför extern CI och underhållargranskning, inte en
ytterligare lokalt identifierad korrigering. Full byggning är fortfarande inte
möjlig i den här miljön på grund av saknade Xemu-beroenden.

## Uppdatering 5 november 2026

PR-grenen rebasades konfliktfritt på aktuell uppströms-`master` och pushades
med `--force-with-lease` som commit `51bc740c16`. Katalogen passerar
`msgfmt --check --statistics` (157 översatta meddelanden), `l10n-lint` utan
fel eller varningar, `svlang consistency`, `svlang svengelska`,
blankteckenskontroll och Gitleaks. GitHub visar den nya grenen men rapporterar
fortfarande `UNSTABLE`; inga check-runs har startat. En full Meson-byggning kan
inte köras lokalt eftersom `meson` inte finns installerat i miljön. Nästa
konkreta steg är därför CI- eller maintainerkörning mot den rebasade grenen.

## Uppdatering 5 november 2026, granskning av aktuella kommentarer

Copilot lade efter rebasen tre kommentarer om Windows-arkiv, vald
byggbackend och valfritt gettext. Den kontrollerade koden på `51bc740c16`
täcker redan samtliga: Windows-paketerarna anropar inte
`install_translation_catalogs`, `build_translation_catalogs()` använder
`make qemu-gmo` i stället för ett hårdkodat `ninja`, och både katalogbygget
och installationen avslutas utan fel när gettextkataloger saknas. Svar med
exakta kodhänvisningar har lämnats i respektive diskussion.

PR:n är fortsatt öppen. GitHub visar `UNSTABLE` och inga startade check-runs,
så detta bevisar inte en godkänd helbygge eller merge. Någon ytterligare
källändring är inte motiverad av de tre kommentarerna.

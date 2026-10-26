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

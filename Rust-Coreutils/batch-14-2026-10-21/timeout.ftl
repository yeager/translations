timeout-help-duration = ett flyttal med valfritt suffix: 's' för sekunder, standardvärdet, 'm' för minuter, 'h' för timmar eller 'd' för dagar; en tidslängd på 0 avaktiverar den tillhörande tidsgränsen
timeout-help-command = ett kommando att köra med valfria argument
timeout-after-help = Vid tidsgräns skickas signalen TERM till KOMMANDO om ingen annan SIGNAL har angetts. Signalen TERM avslutar varje process som inte blockerar eller fångar signalen. Det kan vara nödvändigt att använda signalen KILL eftersom den inte går att fånga.

  Avslutningsstatus:
    124  om KOMMANDO får tidsgränsen överskriden och --preserve-status inte har angetts
    125  om kommandot timeout självt misslyckas
    126  om KOMMANDO hittas men inte kan anropas
    127  om KOMMANDO inte kan hittas
    137  om KOMMANDO, eller timeout självt, skickas signalen KILL (9), 128+9
    -    avslutningsstatusen för KOMMANDO i annat fall

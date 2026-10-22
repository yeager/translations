pr-help-date-format = använd FORMAT i 'date'-stil för datumet i sidhuvudet.
pr-help-omit-pagination = utelämna sidhuvuden och sidfötter och ta bort sidindelning
  som skapas av formulärmatningar i indatafiler
pr-help-expand-tabs = expandera inmatade TECKEN, TABBAR, till tabulatorbredden 8
pr-try-help-message = Prova 'pr --help' för mer information.
pr-error-invalid-expand-tab-argument = extra tecken för '-e' eller ogiltigt tal i argumentet: ‘{ $arg }’
pr-error-invalid-number-argument = extra tecken för '-n' eller ogiltigt tal i argumentet: ‘{ $arg }’
pr-error-starting-page-exceeds-page-count = startsidans nummer { $start } överskrider sidantalet { $count }
pr-help-columns = skapa utdata i flera kolumner som ordnas i kolumner.
  Standardvärdet är 1. Texten skrivs nedåt i varje kolumn i den ordning den tas emot från indatafilen. Denna flagga bör inte användas med -m.
  Flaggorna -e och -i förutsätts för utdata med flera textkolumner. Om textkolumner har identiska vertikala längder anges inte, men en textkolumn får aldrig överskrida sidans längd, se flaggan -l.
  Använd minsta antal rader för att skriva utdata med -t.

numfmt-usage = numfmt [FLAGGA]... [TAL]...
numfmt-help-debug = skriv ut varningar om ogiltig inmatning
numfmt-help-grouping = använd språkinställningens gruppering av siffror, till exempel 1,000,000, vilket innebär att flaggan inte har någon effekt i språkinställningen C/POSIX
numfmt-help-unit-separator = använd STRÄNG för att skilja talet från en eventuell enhet vid utskrift. Som standard används ingen avgränsare
numfmt-error-invalid-specific-suffix = ogiltigt suffix i inmatningen { $input }: { $suffix }
numfmt-debug-header-ignored = --header ignoreras med kommandoradsindata
numfmt-error-invalid-unit-argument = ogiltigt argument '{ $arg }' för '{ $opt }'
numfmt-diag-label-number-overflow = talet är för stort
numfmt-diag-label-stray-percent = ett bokstavligt % måste skrivas %%
numfmt-diag-help-format-syntax = ett format är [PREFIX]%[0]['][-][BREDD][.PRECISION]f[SUFFIX], som i "%'-10.2f"
numfmt-diag-help-field-syntax = --field tar N, N-M, N- eller -M, separerade med kommatecken, som i --field=1,3-5
numfmt-diag-label-bad-conversion = f är den enda konvertering numfmt har. %d, %e, %g och de andra C-konverteringarna accepteras inte
numfmt-diag-label-auto-from-only = auto gissar inmatningens enhet, så endast --from tar det
numfmt-diag-help-unit = --from och --to tar none, si, iec eller iec-i. --from tar också auto
numfmt-diag-label-zero-unit-size = enhetsstorleken måste vara minst 1
numfmt-diag-help-unit-size = enhetsstorleken är ett tal, en multiplikator av K, M, G, T, P eller E, eller båda, som i 512, K eller 2Ki
numfmt-diag-label-zero-padding = utfyllnad är en bredd i tecken, så 0 begär ingenting
numfmt-diag-help-padding = --padding tar ett helt tal som inte är noll. Ett negativt tal vänsterjusterar, som i --padding=-10
numfmt-diag-label-zero-header = utelämna --header för att konvertera varje rad
numfmt-diag-help-header = --header tar antalet inledande rader som ska skickas vidare oförändrade, minst 1
numfmt-diag-help-input-no-from = utan --from måste ett tal vara rent. --from=auto läser ett suffix K, M eller Gi
numfmt-diag-help-input-suffixes = suffixen är K, M, G, T, P, E, Z, Y, R och Q, med ett valfritt i vid --from=auto eller iec-i

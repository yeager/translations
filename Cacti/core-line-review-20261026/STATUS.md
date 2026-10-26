# Cacti core: svensk radgranskning

2026-10-26 granskades 5 198 exporterade poster. Den bifogade deltafilen innehåller 732 ändrade poster, inklusive åtta med pluralformer. En annan redaktörs ändring lämnades orörd och tre förslag fanns redan i den hämtade PO-filen.

Uppladdningen via webbläsaren gav ett 502-fel utan kvitto. En efterföljande Weblate-CSV från databasen visar att samtliga 732 poster har den avsedda svenska texten i den form CSV visar. CSV visar bara första pluralformen; de åtta andra pluralformerna är ännu inte verifierade. Weblates övriga kontrollvarningar återstår att granska.

msgfmt --check --check-format och Gitleaks passerade. l10n-lint rapporterade 0 fel och 37 bedömda varningar; svlang, Hunspell och jämförelse med den svenska termbanken kördes. Termbanken innehåller äldre och kontextberoende förslag som inte har ersatt den manuella bedömningen. Den engelska texten om inaktivering vid import är fortsatt oklar och behöver kontroll mot hela kodkedjan.

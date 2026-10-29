# Cacti Core: felaktig PHP-formatmarkering

Källsträngen i `support.php:1594` är märkt `php-format`, trots att texten innehåller procentuttrycket `80%` och ingen faktisk PHP-platsvariabel:

```po
#, php-format
msgid "Reduce MySQL/MariaDB Memory to less than 80% of System Memory. ..."
```

I den svenska översättningen kan ett vanligt procentuttryck som `80 % av systemminnet` därför inte valideras av `msgfmt --check`: det tolkas som en ogiltig PHP-formatsekvens (`% a`). Enbart en ändring av svensk måltext kan inte lösa detta korrekt utan att ändra innebörden eller införa en falsk formatplats.

Åtgärd upstream: ta bort `php-format` från källposten och återskapa POT-filen. Därefter kan svensk måltext åter valideras med `msgfmt`.

## Kontroll efter lokalt delta

2026-10-29 kontrollerades en tillfälligt sammanslagen katalog där
`cacti-core-sv-ldap-and-group-repairs-20261029.delta.po` överlagrar den
aktuella Core-exporten. `l10n-lint` rapporterar då 0 fel och 54 varningar;
de tidigare HTML-taggsfelen och BOM-varningarna är borta. `msgfmt --check`
har fortfarande exakt ett fel, den här felaktiga PHP-formatmarkeringen.
Ingen Cacti-källfil ändrades i kontrollen.

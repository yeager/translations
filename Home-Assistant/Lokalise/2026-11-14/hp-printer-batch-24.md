# Home Assistant Core, Lokalise, svenska: HP Printer-batch 24

Datum: 2026-11-14

Följande feltext gäller när skrivaren på den angivna värden inte är den skrivare
som integrationen tidigare konfigurerats för. Den sparades direkt i Lokalise och
lästes sedan om i redigeraren:

- `component::hp_printer::config::abort::unique_id_mismatch`
  - Skrivaren på den angivna värden är inte den konfigurerade skrivaren.

De närliggande `reconfigure`-posterna lämnades orörda eftersom deras engelska
källor är delade Lokalise-referenser. En fristående svensk måltext där skulle
bryta referensen och ge platshållarfel.

Kontroller: diffkontroll och Gitleaks för arkivändringen. Resursfilbaserade
kontroller kräver en exporterad lokaliseringsfil och är därför inte tillämpliga
på denna direkt sparade Lokalise-batch.

Status: sparad och verifierad upstream i Lokalise. Detta är en avgränsad batch,
inte en fullständig genomgång av projektet.

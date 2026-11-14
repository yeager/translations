# Home Assistant Core, Lokalise, svenska: Hot Spring-batch 10

Datum: 2026-11-14

Felmeddelandet jämför MAC-adressen för enheten på den angivna värden med den
förväntade adressen. Terminologin följer Home Assistants svenska ordlista för
enhet och etablerad nätverksterminologi; båda platshållarna är oförändrade.
Strängen sparades direkt i Lokalise och lästes sedan om i redigeraren:

- `component::hotspring::exceptions::wrong_device::message`
  - Enheten på den angivna värden har MAC-adressen {found}, inte {expected}.

Kontroller: diffkontroll och Gitleaks för arkivändringen. Resursfilbaserade
kontroller kräver en exporterad lokaliseringsfil och är därför inte tillämpliga
på denna direkt sparade Lokalise-batch.

Status: sparad och verifierad upstream i Lokalise. Detta är en avgränsad batch,
inte en fullständig genomgång av projektet.

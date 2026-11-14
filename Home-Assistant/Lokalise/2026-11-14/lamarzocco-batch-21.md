# Home Assistant Core, Lokalise, svenska: La Marzocco-batch 21

Datum: 2026-11-14

Följande felrubrik och åtgärdsbeskrivning gäller när Home Assistant saknar den
Bluetooth-token som krävs för att ansluta en La Marzocco-maskin lokalt. Båda
sparades direkt i Lokalise och lästes sedan om i redigeraren:

- `component::lamarzocco::issues::missing_bluetooth_token::title`
  - Bluetooth-token saknas för {name}
- `component::lamarzocco::issues::missing_bluetooth_token::fix_flow::step::confirm::description`
  - Ditt La Marzocco-konto saknar en Bluetooth-token för "{name}", så Home
    Assistant kan inte ansluta till maskinen via Bluetooth.

    Åtgärda detta genom att ta bort maskinen i La Marzocco-appen, lägga till den
    igen och sedan läsa in integrationen på nytt.

    Om du inte vill använda Bluetooth väljer du **Skicka** för att stänga av
    Bluetooth och offlineläget för maskinen.

Kontroller: diffkontroll och Gitleaks för arkivändringen. Resursfilbaserade
kontroller kräver en exporterad lokaliseringsfil och är därför inte tillämpliga
på denna direkt sparade Lokalise-batch.

Status: sparad och verifierad upstream i Lokalise. Detta är en avgränsad batch,
inte en fullständig genomgång av projektet.

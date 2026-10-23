# Rust Coreutils: återstående svenska poster

Dessa Fluent-filer innehåller 39 verifierade ändringsförslag: sju tidigare tomma poster, två poster som behöver redigeras och 30 rättade QA-träffar. Formuleringarna har jämförts med den granskade GNU Coreutils-mallen i `tp-sv/coreutils-9.12-pre1.sv.po`.

Komponenten `join` var låst i Hosted Weblate eftersom arkivet inte kunde slås samman. Filerna är därför en granskningsbar delta och ska lämnas som förslag tills komponenten låses upp.

`tail-error-notify-error` och `tail-error-recv-timeout-error` är namngivna Rust-feltyper. De ska behålla sina tekniska namn och kontrollen ”Oförändrad översättning” kan avfärdas.

## Aktuell Hosted Weblate-status

Kontrollerad 2026-10-23: de nio ofärdiga posterna har förslag från Daniel Nylander. I `mkdir` har källsträngen ändrats och saknar nu `{ $error }`; den sparade svenska versionen i `mkdir.ftl` följer den nya källsträngen. De två `join`-posterna har korrekta förslag, men komponenten är låst tills Weblate har återställt arkivsammanfogningen.

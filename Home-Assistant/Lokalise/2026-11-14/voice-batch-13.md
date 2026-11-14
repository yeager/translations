# Home Assistant Core, Lokalise, svenska: Voice-batch 13

Datum: 2026-11-14

Den här batchen gäller självständiga status- och rubriksträngar i
Voice-integrationen. De gemensamma referensnycklarna för `host` och `port`
lämnades orörda eftersom de ska ärva sina gemensamma översättningar. Följande
tre strängar sparades direkt i Lokalise och lästes sedan om i redigeraren:

- `component::voice_support::config::step::install_app::title`
  - Installationen av Voice-appen har påbörjats
- `component::voice_support::config::progress::start_app`
  - Startar Voice-appen
- `component::voice_support::config::progress::install_app`
  - Vänta medan installationen av Voice-appen slutförs. Det kan ta flera minuter.

Kontroller: diffkontroll och Gitleaks för arkivändringen. Resursfilbaserade
kontroller kräver en exporterad lokaliseringsfil och är därför inte tillämpliga
på denna direkt sparade Lokalise-batch.

Status: sparad och verifierad upstream i Lokalise. Detta är en avgränsad batch,
inte en fullständig genomgång av projektet.

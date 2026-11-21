# Home Assistant Core – Webhook

Datum: 2026-11-21

Båda Webhook-strängarna har granskats. De är omformulerade, sparade och API-återlästa.

- `trigger_missing_local_only::description` använder nu korrekt konstruktion `webhook-utlösaren ... för automatiseringen` och den konsekventa termen *åtkomlig*.
- `trigger_missing_local_only::title` använder bestämd form: `Uppdatera webhook-utlösaren`.
- Variablerna `{webhook_id}`, `{edit}`, `{automation_name}`, `{entity_id}` samt Markdown-länken och kodmarkeringen är bevarade.

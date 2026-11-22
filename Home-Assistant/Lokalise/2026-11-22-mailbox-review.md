# Home Assistant Core – Mailbox

Datum: 2026-11-22

Samtliga tre Mailbox-strängar är granskade mot källtext och återlästa från
Lokalise API.

| Nyckel | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `component::mailbox::title` | Brevlåda | Brevlåda | Korrekt, oförändrad. |
| `component::mailbox::issues::deprecated_mailbox::title` | Plattformen för brevlådan håller på att tas bort | Brevlådeplattformen håller på att tas bort | Naturligare svensk sammansättning. |
| `component::mailbox::issues::deprecated_mailbox::description` | Plattformen för brevlådan håller på att tas bort. Vänligen rapportera det till författaren av den anpassade integrationen "{integration_domain}". | Brevlådeplattformen håller på att tas bort. Rapportera det till författaren av den anpassade integrationen "{integration_domain}". | Sammansättning och direkt imperativstil. |

Platshållaren `{integration_domain}` är bevarad. Inga pluralformer, länkar
eller markup berörs. svlangs varning för platshållaren är en känd
felklassificering; hunspell-träffen gäller samma platshållare.

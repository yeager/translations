# Uppföljning: timeout → tidsgräns

Sju aktiva inställnings- och tjänsttexter kontrollerades direkt i Lokalise och normaliserades till Core-termen `tidsgräns`.

| Nycklar | Sparad svenska |
| --- | --- |
| `component::wiffi::options::step::init::data::timeout` | `Tidsgräns (minuter)` |
| `component::synology_dsm::options::step::init::data::timeout` | `Tidsgräns (sekunder)` |
| `component::canary::options::step::init::data::timeout` | `Tidsgräns för begäran (sekunder)` |
| `component::keba::services::set_failsafe::fields::failsafe_timeout::description` | `Tidsgräns efter vilken det felsäkra läget utlöses …` |
| `component::keba::services::set_failsafe::fields::failsafe_timeout::name` | `Felsäker tidsgräns` |
| `component::remote::services::learn_command::fields::timeout::description` | `Tidsgräns för kommandot som ska läras in.` |
| `component::zwave_js::services::set_lock_configuration::fields::lock_timeout::name` | `Tidsgräns för lås` |

Alla poster sparades och återlästes via Lokalise API samt lades in i den kanoniska Home Assistant-TMX:en.

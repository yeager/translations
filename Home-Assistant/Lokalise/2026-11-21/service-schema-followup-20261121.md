# Källuppföljning: historiska tjänstnycklar — 2026-11-21

De här fullständiga nycklarna finns i den kanoniska Lokalise-exporten men saknar motsvarande tjänst eller fält i aktuell Home Assistant Core-`services.yaml` (commit `3d340fb5`, 2026-11-20). De är uppföljningsmål, inte automatiska översättningsändringar: ingen svensk text har ändrats.

## Borttagen tjänst

- `component::logi_circle::services::livestream_record::fields::entity_id::description`
- `component::logi_circle::services::livestream_record::name`
- `component::logi_circle::services::livestream_snapshot::fields::entity_id::description`
- `component::logi_circle::services::livestream_snapshot::name`
- `component::logi_circle::services::set_config::description`
- `component::logi_circle::services::set_config::fields::entity_id::description`
- `component::microsoft_face::services::delete_group::description`
- `component::microsoft_face::services::delete_person::description`
- `component::microsoft_face::services::face_person::fields::camera_entity::description`
- `component::microsoft_face::services::face_person::fields::group::description`
- `component::microsoft_face::services::face_person::name`
- `component::modbus::services::restart::description`
- `component::plex::services::scan_for_clients::description`
- `component::rainbird::services::set_rain_delay::fields::config_entry_id::description`
- `component::rainbird::services::set_rain_delay::fields::duration::description`
- `component::rainbird::services::set_rain_delay::name`
- `component::sabnzbd::services::pause::description`
- `component::sabnzbd::services::set_speed::fields::speed::description`
- `component::smtp::services::reload::description`
- `component::snapcast::services::join::description`
- `component::snapcast::services::join::fields::master::description`
- `component::snapcast::services::join::name`
- `component::snips::services::feedback_off::name`
- `component::snips::services::feedback_on::name`
- `component::snips::services::say::fields::site_id::description`
- `component::snips::services::say::fields::text::description`
- `component::snips::services::say_action::fields::intent_filter::description`
- `component::snips::services::say_action::name`
- `component::velux::services::reboot_gateway::description`
- `component::velux::services::reboot_gateway::name`
- `component::google::services::add_event::fields::calendar_id::description`
- `component::google::services::add_event::fields::in::description`
- `component::google::services::add_event::fields::summary::name`
- `component::habitica::services::api_call::fields::name::description`
- `component::habitica::services::api_call::fields::path::description`
- `component::home_connect::services::pause_program::description`
- `component::home_connect::services::resume_program::description`
- `component::home_connect::services::resume_program::name`
- `component::home_connect::services::set_option_active::name`
- `component::home_connect::services::set_option_selected::name`
- `component::home_connect::services::start_program::fields::key::name`
- `component::home_connect::services::start_program::fields::unit::name`
- `component::home_connect::services::start_program::fields::value::name`
- `component::html5::services::dismiss::fields::data::description`
- `component::html5::services::dismiss::fields::target::description`

## Borttaget fält

- `component::sonos::services::snapshot::fields::entity_id::description`
- `component::xiaomi_miio::services::fan_reset_filter::fields::entity_id::name`
- `component::xiaomi_miio::services::light_eyecare_mode_on::fields::entity_id::name`
- `component::xiaomi_miio::services::light_reminder_on::fields::entity_id::description`
- `component::xiaomi_miio::services::light_reminder_on::fields::entity_id::name`
- `component::xiaomi_miio::services::light_set_delayed_turn_off::fields::entity_id::name`
- `component::xiaomi_miio::services::light_set_scene::fields::entity_id::name`
- `component::xiaomi_miio::services::switch_set_power_price::fields::mode::description`
- `component::telegram_bot::services::answer_callback_query::fields::timeout::description`
- `component::telegram_bot::services::answer_callback_query::fields::timeout::name`
- `component::telegram_bot::services::send_animation::fields::timeout::name`
- `component::telegram_bot::services::send_document::fields::timeout::description`
- `component::telegram_bot::services::send_document::fields::timeout::name`
- `component::telegram_bot::services::send_location::fields::target::description`
- `component::telegram_bot::services::send_location::fields::timeout::name`
- `component::telegram_bot::services::send_message::fields::target::description`
- `component::telegram_bot::services::send_message::fields::timeout::description`
- `component::telegram_bot::services::send_message::fields::timeout::name`
- `component::telegram_bot::services::send_photo::fields::target::description`
- `component::telegram_bot::services::send_photo::fields::timeout::description`
- `component::telegram_bot::services::send_photo::fields::timeout::name`
- `component::telegram_bot::services::send_poll::fields::target::description`
- `component::telegram_bot::services::send_poll::fields::timeout::description`
- `component::telegram_bot::services::send_poll::fields::timeout::name`
- `component::telegram_bot::services::send_sticker::fields::timeout::description`
- `component::telegram_bot::services::send_sticker::fields::timeout::name`
- `component::telegram_bot::services::send_video::fields::timeout::description`
- `component::telegram_bot::services::send_video::fields::timeout::name`
- `component::telegram_bot::services::send_voice::fields::timeout::description`
- `component::telegram_bot::services::send_voice::fields::timeout::name`
- `component::velbus::services::sync_clock::fields::interface::description`

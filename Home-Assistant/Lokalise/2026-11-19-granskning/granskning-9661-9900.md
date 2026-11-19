# Home Assistant Core – granskning 9661–9900

Sortering: ”Last added” vid insamlingen. Inget har ändrats i Lokalise. Referenser vars mål inte finns i underlaget markeras för senare kontroll.

## 9661. `component::de_dietrich::entity::sensor::hot_water_temperature::name`

**Engelska:** Hot water temperature

**Befintlig svenska:** Varmvattentemperatur

**Bedömning:** Ingen ändring föreslås.

## 9662. `component::de_dietrich::entity::sensor::fan_speed::name`

**Engelska:** Fan speed

**Befintlig svenska:** Fläkthastighet

**Bedömning:** Ingen ändring föreslås.

## 9663. `component::de_dietrich::entity::sensor::exhaust_temperature::name`

**Engelska:** Flue gas temperature

**Befintlig svenska:** Rökgastemperatur

**Bedömning:** Ingen ändring föreslås.

## 9664. `component::de_dietrich::entity::sensor::circuit_b_room_temperature::name`

**Engelska:** Circuit B room temperature

**Befintlig svenska:** Rumstemperatur i krets B

**Bedömning:** Ingen ändring föreslås.

## 9665. `component::de_dietrich::entity::sensor::circuit_a_room_temperature::name`

**Engelska:** Circuit A room temperature

**Befintlig svenska:** Rumstemperatur i krets A

**Bedömning:** Ingen ändring föreslås.

## 9666. `component::de_dietrich::entity::sensor::calc_boiler_temperature::name`

**Engelska:** Boiler temperature target

**Befintlig svenska:** Målvärde för pannans temperatur

**Bedömning:** Ingen ändring föreslås.

## 9667. `component::de_dietrich::entity::sensor::boiler_temperature::name`

**Engelska:** Boiler temperature

**Befintlig svenska:** Pannans temperatur

**Bedömning:** Ingen ändring föreslås.

## 9668. `component::de_dietrich::config::step::user::description`

**Engelska:** Connect over Modbus TCP. The boiler's register layout is detected automatically.

**Befintlig svenska:** Anslut via Modbus TCP. Pannans registerlayout identifieras automatiskt.

**Bedömning:** Ingen ändring föreslås.

## 9669. `component::de_dietrich::config::step::user::data_description::unit_id`

**Engelska:** The boiler's Modbus unit ID.

**Befintlig svenska:** Pannans Modbus-enhets-ID.

**Bedömning:** Ingen ändring föreslås.

## 9670. `component::de_dietrich::config::step::user::data_description::port`

**Engelska:** The Modbus TCP port used by the bridge.

**Befintlig svenska:** Modbus TCP-porten som används av bryggan.

**Bedömning:** Ingen ändring föreslås.

## 9671. `component::de_dietrich::config::step::user::data_description::host`

**Engelska:** The hostname or IP address of the plain RS485-to-TCP bridge connected to the boiler. It must pass through raw Modbus RTU frames, not translate between Modbus variants.

**Befintlig svenska:** Värdnamnet eller IP-adressen för den enkla RS485-till-TCP-bryggan som är ansluten till pannan. Den måste vidarebefordra råa Modbus RTU-ramar och inte översätta mellan Modbus-varianter.

**Bedömning:** Ingen ändring föreslås.

## 9672. `component::de_dietrich::config::step::user::data::unit_id`

**Engelska:** Modbus unit ID

**Befintlig svenska:** Modbus-enhets-ID

**Bedömning:** Ingen ändring föreslås.

## 9673. `component::de_dietrich::config::step::user::data::port`

**Engelska:** [%key:common::config_flow::data::port%]

**Befintlig svenska:** [%key:common::config_flow::data::port%]

**Bedömning:** Ingen ändring föreslås.

## 9674. `component::de_dietrich::config::step::user::data::host`

**Engelska:** [%key:common::config_flow::data::host%]

**Befintlig svenska:** [%key:common::config_flow::data::host%]

**Bedömning:** Ingen ändring föreslås.

## 9675. `component::de_dietrich::config::error::unsupported_device`

**Engelska:** This device is not supported: {error}

**Befintlig svenska:** Den här enheten stöds inte: {error}

**Bedömning:** Ingen ändring föreslås.

## 9676. `component::de_dietrich::config::error::unknown`

**Engelska:** [%key:common::config_flow::error::unknown%]

**Befintlig svenska:** [%key:common::config_flow::error::unknown%]

**Bedömning:** Ingen ändring föreslås.

## 9677. `component::de_dietrich::config::error::cannot_connect`

**Engelska:** Failed to connect: {error}

**Befintlig svenska:** Det gick inte att ansluta: {error}

**Bedömning:** Ingen ändring föreslås.

## 9678. `component::de_dietrich::config::abort::already_configured`

**Engelska:** [%key:common::config_flow::abort::already_configured_device%]

**Befintlig svenska:** [%key:common::config_flow::abort::already_configured_device%]

**Bedömning:** Ingen ändring föreslås.

## 9679. `component::openevse::entity::select::override_state::state::disabled`

**Engelska:** Disabled

**Befintlig svenska:** Inaktiverad

**Bedömning:** Ingen ändring föreslås.

## 9680. `component::openevse::entity::select::override_state::state::auto`

**Engelska:** Auto

**Befintlig svenska:** Automatisk

**Bedömning:** Ingen ändring föreslås.

## 9681. `component::openevse::entity::select::override_state::state::active`

**Engelska:** Active

**Befintlig svenska:** Aktiv

**Bedömning:** Ingen ändring föreslås.

## 9682. `component::openevse::entity::select::override_state::name`

**Engelska:** Override state

**Befintlig svenska:** Åsidosätt tillstånd

**Förslag:** Åsidosättningens tillstånd

## 9683. `component::discogs::issues::deprecated_yaml_import_issue_cannot_connect::title`

**Engelska:** The {integration_title} YAML configuration is being removed

**Befintlig svenska:** YAML-konfigurationen för ” {integration_title} ” tas bort

**Förslag:** YAML-konfigurationen för {integration_title} tas bort

## 9684. `component::discogs::issues::deprecated_yaml_import_issue_cannot_connect::description`

**Engelska:** Configuring {integration_title} via YAML is deprecated and will be removed in a future release. While importing your YAML configuration, the Discogs API could not be reached or the token was invalid. Please verify your token and restart Home Assistant to retry, or remove the {domain} sensor from your configuration and set up the integration via the UI.

**Befintlig svenska:** Konfigurering av ” {integration_title} ” via YAML är utfasad och kommer att tas bort i en framtida version. Vid importen av din YAML-konfiguration gick det inte att ansluta till Discogs API eller så var token ogiltigt. Kontrollera ditt token och starta om Home Assistant för att försöka igen, eller ta bort sensorn ” {domain} ” från din konfiguration och ställ in integrationen via användargränssnittet.

**Förslag:** Konfigurering av {integration_title} via YAML är föråldrad och tas bort i en framtida version. Vid importen av YAML-konfigurationen gick det inte att nå Discogs-API:t eller så var token ogiltig. Kontrollera din token och starta om Home Assistant för att försöka igen, eller ta bort sensorn {domain} från konfigurationen och konfigurera integreringen via användargränssnittet.

## 9685. `component::discogs::entity::sensor::wantlist::name`

**Engelska:** Wantlist

**Befintlig svenska:** Önskelista

**Bedömning:** Ingen ändring föreslås.

## 9686. `component::discogs::entity::sensor::random_record::name`

**Engelska:** Random record

**Befintlig svenska:** Slumpmässig skiva

**Bedömning:** Ingen ändring föreslås.

## 9687. `component::discogs::entity::sensor::collection::name`

**Engelska:** Collection

**Befintlig svenska:** Samling

**Bedömning:** Ingen ändring föreslås.

## 9688. `component::discogs::config::step::user::data_description::token`

**Engelska:** Personal access token from Discogs developer settings.

**Befintlig svenska:** Personlig åtkomsttoken från utvecklarinställningarna i Discogs.

**Bedömning:** Ingen ändring föreslås.

## 9689. `component::discogs::config::step::user::data::token`

**Engelska:** [%key:common::config_flow::data::api_token%]

**Befintlig svenska:** [%key:common::config_flow::data::api_token%]

**Bedömning:** Ingen ändring föreslås.

## 9690. `component::discogs::config::error::unknown`

**Engelska:** [%key:common::config_flow::error::unknown%]

**Befintlig svenska:** [%key:common::config_flow::error::unknown%]

**Bedömning:** Ingen ändring föreslås.

## 9691. `component::discogs::config::error::invalid_auth`

**Engelska:** [%key:common::config_flow::error::invalid_auth%]

**Befintlig svenska:** [%key:common::config_flow::error::invalid_auth%]

**Bedömning:** Ingen ändring föreslås.

## 9692. `component::discogs::config::error::cannot_connect`

**Engelska:** [%key:common::config_flow::error::cannot_connect%]

**Befintlig svenska:** [%key:common::config_flow::error::cannot_connect%]

**Bedömning:** Ingen ändring föreslås.

## 9693. `component::discogs::config::abort::unknown`

**Engelska:** [%key:common::config_flow::error::unknown%]

**Befintlig svenska:** [%key:common::config_flow::error::unknown%]

**Bedömning:** Ingen ändring föreslås.

## 9694. `component::discogs::config::abort::invalid_auth`

**Engelska:** [%key:common::config_flow::error::invalid_auth%]

**Befintlig svenska:** [%key:common::config_flow::error::invalid_auth%]

**Bedömning:** Ingen ändring föreslås.

## 9695. `component::discogs::config::abort::cannot_connect`

**Engelska:** [%key:common::config_flow::error::cannot_connect%]

**Befintlig svenska:** [%key:common::config_flow::error::cannot_connect%]

**Bedömning:** Ingen ändring föreslås.

## 9696. `component::discogs::config::abort::already_configured`

**Engelska:** [%key:common::config_flow::abort::already_configured_account%]

**Befintlig svenska:** [%key:common::config_flow::abort::already_configured_account%]

**Bedömning:** Ingen ändring föreslås.

## 9697. `component::bosch_shc::entity::switch::child_lock::name`

**Engelska:** Child lock

**Befintlig svenska:** Barnlås

**Bedömning:** Ingen ändring föreslås.

## 9698. `component::pterodactyl::entity::binary_sensor::suspended::name`

**Engelska:** Suspended

**Befintlig svenska:** Pausad

**Bedömning:** Ingen ändring föreslås.

## 9699. `component::jvc_projector::entity::sensor::resolution::state::xga-1024x768`

**Engelska:** XGA 1024x768

**Befintlig svenska:** XGA 1024x768

**Bedömning:** Ingen ändring föreslås.

## 9700. `component::jvc_projector::entity::sensor::resolution::state::wxgapp1600x900`

**Engelska:** WXGA++ 1600x900

**Befintlig svenska:** WXGA++ 1600x900

**Bedömning:** Ingen ändring föreslås.

## 9701. `component::jvc_projector::entity::sensor::resolution::state::wxgap1440x900`

**Engelska:** WXGA+ 1440x900

**Befintlig svenska:** WXGA+ 1440x900

**Bedömning:** Ingen ändring föreslås.

## 9702. `component::jvc_projector::entity::sensor::resolution::state::wxga-1280x800`

**Engelska:** WXGA 1280x800

**Befintlig svenska:** WXGA 1280x800

**Bedömning:** Ingen ändring föreslås.

## 9703. `component::jvc_projector::entity::sensor::resolution::state::wxga-1280x768`

**Engelska:** WXGA 1280x768

**Befintlig svenska:** WXGA 1280x768

**Bedömning:** Ingen ändring föreslås.

## 9704. `component::jvc_projector::entity::sensor::resolution::state::wuxga-1920x1200`

**Engelska:** WUXGA 1920x1200

**Befintlig svenska:** WUXGA 1920x1200

**Bedömning:** Ingen ändring föreslås.

## 9705. `component::jvc_projector::entity::sensor::resolution::state::wsxgap1680x1050`

**Engelska:** WSXGA+ 1680x1050

**Befintlig svenska:** WSXGA+ 1680x1050

**Bedömning:** Ingen ändring föreslås.

## 9706. `component::jvc_projector::entity::sensor::resolution::state::wqxga`

**Engelska:** WQXGA

**Befintlig svenska:** WQXGA

**Bedömning:** Ingen ändring föreslås.

## 9707. `component::jvc_projector::entity::sensor::resolution::state::wqhd-60`

**Engelska:** WQHD 60 Hz

**Befintlig svenska:** WQHD 60 Hz

**Bedömning:** Ingen ändring föreslås.

## 9708. `component::jvc_projector::entity::sensor::resolution::state::wqhd-120`

**Engelska:** WQHD 120 Hz

**Befintlig svenska:** WQHD 120 Hz

**Bedömning:** Ingen ändring föreslås.

## 9709. `component::jvc_projector::entity::sensor::resolution::state::vga-640x480`

**Engelska:** VGA 640x480

**Befintlig svenska:** VGA 640x480

**Bedömning:** Ingen ändring föreslås.

## 9710. `component::jvc_projector::entity::sensor::resolution::state::uxga-1600x1200`

**Engelska:** UXGA 1600x1200

**Befintlig svenska:** UXGA 1600x1200

**Bedömning:** Ingen ändring föreslås.

## 9711. `component::jvc_projector::entity::sensor::resolution::state::sxga-1280x1024`

**Engelska:** SXGA 1280x1024

**Befintlig svenska:** SXGA 1280x1024

**Bedömning:** Ingen ändring föreslås.

## 9712. `component::jvc_projector::entity::sensor::resolution::state::svga-800x600`

**Engelska:** SVGA 800x600

**Befintlig svenska:** SVGA 800x600

**Bedömning:** Ingen ändring föreslås.

## 9713. `component::jvc_projector::entity::sensor::resolution::state::qxga`

**Engelska:** QXGA

**Befintlig svenska:** QXGA

**Bedömning:** Ingen ändring föreslås.

## 9714. `component::jvc_projector::entity::sensor::resolution::state::out-of-range`

**Engelska:** Out of Range

**Befintlig svenska:** Utanför intervallet

**Bedömning:** Ingen ändring föreslås.

## 9715. `component::jvc_projector::entity::sensor::resolution::state::no-signal`

**Engelska:** No Signal

**Befintlig svenska:** Ingen signal

**Bedömning:** Ingen ändring föreslås.

## 9716. `component::jvc_projector::entity::sensor::resolution::state::fwxga-1366x768`

**Engelska:** FWXGA 1366x768

**Befintlig svenska:** FWXGA 1366x768

**Bedömning:** Ingen ändring föreslås.

## 9717. `component::jvc_projector::entity::sensor::resolution::state::8k-7680x4320-60`

**Engelska:** 8K 7680x4320 60 Hz

**Befintlig svenska:** 8K 7680x4320 60 Hz

**Bedömning:** Ingen ändring föreslås.

## 9718. `component::jvc_projector::entity::sensor::resolution::state::8k-7680x4320-50`

**Engelska:** 8K 7680x4320 50 Hz

**Befintlig svenska:** 8K 7680x4320 50 Hz

**Bedömning:** Ingen ändring föreslås.

## 9719. `component::jvc_projector::entity::sensor::resolution::state::8k-7680x4320-48`

**Engelska:** 8K 7680x4320 48 Hz

**Befintlig svenska:** 8K 7680x4320 48 Hz

**Bedömning:** Ingen ändring föreslås.

## 9720. `component::jvc_projector::entity::sensor::resolution::state::8k-7680x4320-30`

**Engelska:** 8K 7680x4320 30 Hz

**Befintlig svenska:** 8K 7680x4320 30 Hz

**Bedömning:** Ingen ändring föreslås.

## 9721. `component::jvc_projector::entity::sensor::resolution::state::8k-7680x4320-25`

**Engelska:** 8K 7680x4320 25 Hz

**Befintlig svenska:** 8K 7680x4320 25 Hz

**Bedömning:** Ingen ändring föreslås.

## 9722. `component::jvc_projector::entity::sensor::resolution::state::8k-7680x4320-24`

**Engelska:** 8K 7680x4320 24 Hz

**Befintlig svenska:** 8K 7680x4320 24 Hz

**Bedömning:** Ingen ändring föreslås.

## 9723. `component::jvc_projector::entity::sensor::resolution::state::720p-60`

**Engelska:** 720p 60 Hz

**Befintlig svenska:** 720p 60 Hz

**Bedömning:** Ingen ändring föreslås.

## 9724. `component::jvc_projector::entity::sensor::resolution::state::720p-50`

**Engelska:** 720p 50 Hz

**Befintlig svenska:** 720p 50 Hz

**Bedömning:** Ingen ändring föreslås.

## 9725. `component::jvc_projector::entity::sensor::resolution::state::720p-3d`

**Engelska:** 720p 3D

**Befintlig svenska:** 720p 3D

**Bedömning:** Ingen ändring föreslås.

## 9726. `component::jvc_projector::entity::sensor::resolution::state::576p`

**Engelska:** 576p

**Befintlig svenska:** 576p

**Bedömning:** Ingen ändring föreslås.

## 9727. `component::jvc_projector::entity::sensor::resolution::state::576i`

**Engelska:** 576i

**Befintlig svenska:** 576i

**Bedömning:** Ingen ändring föreslås.

## 9728. `component::jvc_projector::entity::sensor::resolution::state::4k-4096-60`

**Engelska:** 4K 4096 60 Hz

**Befintlig svenska:** 4K 4096 60 Hz

**Bedömning:** Ingen ändring föreslås.

## 9729. `component::jvc_projector::entity::sensor::resolution::state::4k-4096-50`

**Engelska:** 4K 4096 50 Hz

**Befintlig svenska:** 4K 4096 50 Hz

**Bedömning:** Ingen ändring föreslås.

## 9730. `component::jvc_projector::entity::sensor::resolution::state::4k-4096-30`

**Engelska:** 4K 4096 30 Hz

**Befintlig svenska:** 4K 4096 30 Hz

**Bedömning:** Ingen ändring föreslås.

## 9731. `component::jvc_projector::entity::sensor::resolution::state::4k-4096-25`

**Engelska:** 4K 4096 25 Hz

**Befintlig svenska:** 4K 4096 25 Hz

**Bedömning:** Ingen ändring föreslås.

## 9732. `component::jvc_projector::entity::sensor::resolution::state::4k-4096-24`

**Engelska:** 4K 4096 24 Hz

**Befintlig svenska:** 4K 4096 24 Hz

**Bedömning:** Ingen ändring föreslås.

## 9733. `component::jvc_projector::entity::sensor::resolution::state::4k-3840-60`

**Engelska:** 4K 3840 60 Hz

**Befintlig svenska:** 4K 3840 60 Hz

**Bedömning:** Ingen ändring föreslås.

## 9734. `component::jvc_projector::entity::sensor::resolution::state::4k-3840-50`

**Engelska:** 4K 3840 50 Hz

**Befintlig svenska:** 4K 3840 50 Hz

**Bedömning:** Ingen ändring föreslås.

## 9735. `component::jvc_projector::entity::sensor::resolution::state::4k-3840-30`

**Engelska:** 4K 3840 30 Hz

**Befintlig svenska:** 4K 3840 30 Hz

**Bedömning:** Ingen ändring föreslås.

## 9736. `component::jvc_projector::entity::sensor::resolution::state::4k-3840-25`

**Engelska:** 4K 3840 25 Hz

**Befintlig svenska:** 4K 3840 25 Hz

**Bedömning:** Ingen ändring föreslås.

## 9737. `component::jvc_projector::entity::sensor::resolution::state::4k-3840-24`

**Engelska:** 4K 3840 24 Hz

**Befintlig svenska:** 4K 3840 24 Hz

**Bedömning:** Ingen ändring föreslås.

## 9738. `component::jvc_projector::entity::sensor::resolution::state::4k`

**Engelska:** 4K

**Befintlig svenska:** 4K

**Bedömning:** Ingen ändring föreslås.

## 9739. `component::jvc_projector::entity::sensor::resolution::state::480p`

**Engelska:** 480p

**Befintlig svenska:** 480p

**Bedömning:** Ingen ändring föreslås.

## 9740. `component::jvc_projector::entity::sensor::resolution::state::480i`

**Engelska:** 480i

**Befintlig svenska:** 480i

**Bedömning:** Ingen ändring föreslås.

## 9741. `component::jvc_projector::entity::sensor::resolution::state::4096x2160-p120`

**Engelska:** 4096x2160 120 Hz

**Befintlig svenska:** 4096x2160 120 Hz

**Bedömning:** Ingen ändring föreslås.

## 9742. `component::jvc_projector::entity::sensor::resolution::state::4096x2160-100hz`

**Engelska:** 4096x2160 100 Hz

**Befintlig svenska:** 4096x2160 100 Hz

**Bedömning:** Ingen ändring föreslås.

## 9743. `component::jvc_projector::entity::sensor::resolution::state::3840x2160-p120`

**Engelska:** 3840x2160 120 Hz

**Befintlig svenska:** 3840x2160 120 Hz

**Bedömning:** Ingen ändring föreslås.

## 9744. `component::jvc_projector::entity::sensor::resolution::state::3840x2160-100hz`

**Engelska:** 3840x2160 100 Hz

**Befintlig svenska:** 3840x2160 100 Hz

**Bedömning:** Ingen ändring föreslås.

## 9745. `component::jvc_projector::entity::sensor::resolution::state::3840x1080-p60`

**Engelska:** 3840x1080 60 Hz

**Befintlig svenska:** 3840x1080 60 Hz

**Bedömning:** Ingen ändring föreslås.

## 9746. `component::jvc_projector::entity::sensor::resolution::state::3840x1080-p50`

**Engelska:** 3840x1080 50 Hz

**Befintlig svenska:** 3840x1080 50 Hz

**Bedömning:** Ingen ändring föreslås.

## 9747. `component::jvc_projector::entity::sensor::resolution::state::2048x1080-p60`

**Engelska:** 2048x1080 60 Hz

**Befintlig svenska:** 2048x1080 60 Hz

**Bedömning:** Ingen ändring föreslås.

## 9748. `component::jvc_projector::entity::sensor::resolution::state::2048x1080-p50`

**Engelska:** 2048x1080 50 Hz

**Befintlig svenska:** 2048x1080 50 Hz

**Bedömning:** Ingen ändring föreslås.

## 9749. `component::jvc_projector::entity::sensor::resolution::state::2048x1080-p30`

**Engelska:** 2048x1080 30 Hz

**Befintlig svenska:** 2048x1080 30 Hz

**Bedömning:** Ingen ändring föreslås.

## 9750. `component::jvc_projector::entity::sensor::resolution::state::2048x1080-p25`

**Engelska:** 2048x1080 25 Hz

**Befintlig svenska:** 2048x1080 25 Hz

**Bedömning:** Ingen ändring föreslås.

## 9751. `component::jvc_projector::entity::sensor::resolution::state::2048x1080-p24`

**Engelska:** 2048x1080 24 Hz

**Befintlig svenska:** 2048x1080 24 Hz

**Bedömning:** Ingen ändring föreslås.

## 9752. `component::jvc_projector::entity::sensor::resolution::state::1080p-60`

**Engelska:** 1080p 60 Hz

**Befintlig svenska:** 1080p 60 Hz

**Bedömning:** Ingen ändring föreslås.

## 9753. `component::jvc_projector::entity::sensor::resolution::state::1080p-50`

**Engelska:** 1080p 50 Hz

**Befintlig svenska:** 1080p 50 Hz

**Bedömning:** Ingen ändring föreslås.

## 9754. `component::jvc_projector::entity::sensor::resolution::state::1080p-3d`

**Engelska:** 1080p 3D

**Befintlig svenska:** 1080p 3D

**Bedömning:** Ingen ändring föreslås.

## 9755. `component::jvc_projector::entity::sensor::resolution::state::1080p-30`

**Engelska:** 1080p 30 Hz

**Befintlig svenska:** 1080p 30 Hz

**Bedömning:** Ingen ändring föreslås.

## 9756. `component::jvc_projector::entity::sensor::resolution::state::1080p-25`

**Engelska:** 1080p 25 Hz

**Befintlig svenska:** 1080p 25 Hz

**Bedömning:** Ingen ändring föreslås.

## 9757. `component::jvc_projector::entity::sensor::resolution::state::1080p-24`

**Engelska:** 1080p 24 Hz

**Befintlig svenska:** 1080p 24 Hz

**Bedömning:** Ingen ändring föreslås.

## 9758. `component::jvc_projector::entity::sensor::resolution::state::1080p-120`

**Engelska:** 1080p 120 Hz

**Befintlig svenska:** 1080p 120 Hz

**Bedömning:** Ingen ändring föreslås.

## 9759. `component::jvc_projector::entity::sensor::resolution::state::1080p-100`

**Engelska:** 1080p 100 Hz

**Befintlig svenska:** 1080p 100 Hz

**Bedömning:** Ingen ändring föreslås.

## 9760. `component::jvc_projector::entity::sensor::resolution::state::1080i-60`

**Engelska:** 1080i 60 Hz

**Befintlig svenska:** 1080i 60 Hz

**Bedömning:** Ingen ändring föreslås.

## 9761. `component::jvc_projector::entity::sensor::resolution::state::1080i-50`

**Engelska:** 1080i 50 Hz

**Befintlig svenska:** 1080i 50 Hz

**Bedömning:** Ingen ändring föreslås.

## 9762. `component::jvc_projector::entity::sensor::resolution::state::1080i-3d`

**Engelska:** 1080i 3D

**Befintlig svenska:** 1080i 3D

**Bedömning:** Ingen ändring föreslås.

## 9763. `component::jvc_projector::entity::sensor::resolution::name`

**Engelska:** Resolution

**Befintlig svenska:** Upplösning

**Bedömning:** Ingen ändring föreslås.

## 9764. `component::jvc_projector::entity::sensor::link_rate::state::disable`

**Engelska:** Disabled

**Befintlig svenska:** Inaktiverad

**Bedömning:** Ingen ändring föreslås.

## 9765. `component::jvc_projector::entity::sensor::link_rate::state::8-gbps-4-lanes`

**Engelska:** 8 Gbps 4 Lanes

**Befintlig svenska:** 8 Gbit/s, 4 banor

**Bedömning:** Ingen ändring föreslås.

## 9766. `component::jvc_projector::entity::sensor::link_rate::state::6-gbps-4-lanes`

**Engelska:** 6 Gbps 4 Lanes

**Befintlig svenska:** 6 Gbit/s, 4 banor

**Bedömning:** Ingen ändring föreslås.

## 9767. `component::jvc_projector::entity::sensor::link_rate::state::6-gbps-3-lanes`

**Engelska:** 6 Gbps 3 Lanes

**Befintlig svenska:** 6 Gbit/s, 3 banor

**Bedömning:** Ingen ändring föreslås.

## 9768. `component::jvc_projector::entity::sensor::link_rate::state::3-gbps-3-lanes`

**Engelska:** 3 Gbps 3 Lanes

**Befintlig svenska:** 3 Gbit/s, 3 banor

**Bedömning:** Ingen ändring föreslås.

## 9769. `component::jvc_projector::entity::sensor::link_rate::state::10-gbps-4-lanes`

**Engelska:** 10 Gbps 4 Lanes

**Befintlig svenska:** 10 Gbit/s, 4 banor

**Bedömning:** Ingen ändring föreslås.

## 9770. `component::jvc_projector::entity::sensor::link_rate::name`

**Engelska:** Link Rate

**Befintlig svenska:** Länkhastighet

**Bedömning:** Ingen ändring föreslås.

## 9771. `component::jvc_projector::entity::sensor::colorimetry::state::xvycc-709`

**Engelska:** xvYCC 709

**Befintlig svenska:** xvYCC 709

**Bedömning:** Ingen ändring föreslås.

## 9772. `component::jvc_projector::entity::sensor::colorimetry::state::xvycc-601`

**Engelska:** xvYCC 601

**Befintlig svenska:** xvYCC 601

**Bedömning:** Ingen ändring föreslås.

## 9773. `component::jvc_projector::entity::sensor::colorimetry::state::sycc-601`

**Engelska:** sYCC 601

**Befintlig svenska:** sYCC 601

**Bedömning:** Ingen ändring föreslås.

## 9774. `component::jvc_projector::entity::sensor::colorimetry::state::srgb`

**Engelska:** sRGB

**Befintlig svenska:** sRGB

**Bedömning:** Ingen ändring föreslås.

## 9775. `component::jvc_projector::entity::sensor::colorimetry::state::other`

**Engelska:** Other

**Befintlig svenska:** Annat

**Bedömning:** Ingen ändring föreslås.

## 9776. `component::jvc_projector::entity::sensor::colorimetry::state::no-data`

**Engelska:** No Data

**Befintlig svenska:** Inga data

**Bedömning:** Ingen ändring föreslås.

## 9777. `component::jvc_projector::entity::sensor::colorimetry::state::dci-p3-theater`

**Engelska:** DCI-P3 Theater

**Befintlig svenska:** DCI-P3 Theater

**Bedömning:** Ingen ändring föreslås.

## 9778. `component::jvc_projector::entity::sensor::colorimetry::state::dci-p3-d65`

**Engelska:** DCI-P3 D65

**Befintlig svenska:** DCI-P3 D65

**Bedömning:** Ingen ändring föreslås.

## 9779. `component::jvc_projector::entity::sensor::colorimetry::state::bt-709`

**Engelska:** BT.709

**Befintlig svenska:** BT.709

**Bedömning:** Ingen ändring föreslås.

## 9780. `component::jvc_projector::entity::sensor::colorimetry::state::bt-601`

**Engelska:** BT.601

**Befintlig svenska:** BT.601

**Bedömning:** Ingen ändring föreslås.

## 9781. `component::jvc_projector::entity::sensor::colorimetry::state::bt-2020-non-constant-luminance`

**Engelska:** BT.2020 Non-Constant Luminance

**Befintlig svenska:** BT.2020 utan konstant luminans

**Bedömning:** Ingen ändring föreslås.

## 9782. `component::jvc_projector::entity::sensor::colorimetry::state::bt-2020-constant-luminance`

**Engelska:** BT.2020 Constant Luminance

**Befintlig svenska:** BT.2020 med konstant luminans

**Bedömning:** Ingen ändring föreslås.

## 9783. `component::jvc_projector::entity::sensor::colorimetry::state::adobe-ycc-601`

**Engelska:** Adobe YCC 601

**Befintlig svenska:** Adobe YCC 601

**Bedömning:** Ingen ändring föreslås.

## 9784. `component::jvc_projector::entity::sensor::colorimetry::state::adobe-rgb`

**Engelska:** Adobe RGB

**Befintlig svenska:** Adobe RGB

**Bedömning:** Ingen ändring föreslås.

## 9785. `component::jvc_projector::entity::sensor::colorimetry::name`

**Engelska:** Colorimetry

**Befintlig svenska:** Färgmätning

**Bedömning:** Ingen ändring föreslås.

## 9786. `component::jvc_projector::entity::select::motion_enhance::state::off`

**Engelska:** [%key:common::state::off%]

**Befintlig svenska:** [%key:common::state::off%]

**Bedömning:** Ingen ändring föreslås.

## 9787. `component::jvc_projector::entity::select::motion_enhance::state::low`

**Engelska:** [%key:common::state::low%]

**Befintlig svenska:** [%key:common::state::low%]

**Bedömning:** Ingen ändring föreslås.

## 9788. `component::jvc_projector::entity::select::motion_enhance::state::high`

**Engelska:** [%key:common::state::high%]

**Befintlig svenska:** [%key:common::state::high%]

**Bedömning:** Ingen ändring föreslås.

## 9789. `component::jvc_projector::entity::select::motion_enhance::name`

**Engelska:** Motion Enhance

**Befintlig svenska:** Rörelseförbättring

**Bedömning:** Ingen ändring föreslås.

## 9790. `component::shelly::entity::sensor::storage_free_space::name`

**Engelska:** Free storage space

**Befintlig svenska:** Ledigt lagringsutrymme

**Bedömning:** Ingen ändring föreslås.

## 9791. `component::xbox::exceptions::command_failed::message`

**Engelska:** Command failed.

**Befintlig svenska:** Kommandot misslyckades.

**Bedömning:** Ingen ändring föreslås.

## 9792. `component::neopool::entity::number::smart_temp_low::name`

**Engelska:** Smart lower temperature

**Befintlig svenska:** Smart lägsta temperatur

**Bedömning:** Ingen ändring föreslås.

## 9793. `component::neopool::entity::number::smart_temp_high::name`

**Engelska:** Smart upper temperature

**Befintlig svenska:** Smart högsta temperatur

**Bedömning:** Ingen ändring föreslås.

## 9794. `component::neopool::entity::number::rx1::name`

**Engelska:** Redox setpoint

**Befintlig svenska:** Redoxbörvärde

**Bedömning:** Ingen ändring föreslås.

## 9795. `component::neopool::entity::number::ph2::name`

**Engelska:** pH min limit

**Befintlig svenska:** Lägsta pH-gräns

**Bedömning:** Ingen ändring föreslås.

## 9796. `component::neopool::entity::number::ph1::name`

**Engelska:** pH max limit

**Befintlig svenska:** Högsta pH-gräns

**Bedömning:** Ingen ändring föreslås.

## 9797. `component::neopool::entity::number::hidro_shutdown_temperature::name`

**Engelska:** Hydrolysis shutdown temp. threshold

**Befintlig svenska:** Temperaturtröskel för avstängning av hydrolys

**Bedömning:** Ingen ändring föreslås.

## 9798. `component::neopool::entity::number::hidro_cover_reduction::name`

**Engelska:** Cover reduction (when covered)

**Befintlig svenska:** Reducering när skyddet används

**Bedömning:** Ingen ändring föreslås.

## 9799. `component::neopool::entity::number::hidro::name`

**Engelska:** Hydrolysis target production level

**Befintlig svenska:** Målnivå för hydrolysproduktion

**Bedömning:** Ingen ändring föreslås.

## 9800. `component::neopool::entity::number::heating_temp::name`

**Engelska:** Heating mode temperature

**Befintlig svenska:** Temperatur för uppvärmningsläge

**Bedömning:** Ingen ändring föreslås.

## 9801. `component::neopool::entity::number::cl1::name`

**Engelska:** Chlorine setpoint

**Befintlig svenska:** Klorbörvärde

**Bedömning:** Ingen ändring föreslås.

## 9802. `component::binary_sensor::entity_component::glass_break::state::on`

**Engelska:** Glass break detected

**Befintlig svenska:** Krossat glas upptäckt

**Bedömning:** Ingen ändring föreslås.

## 9803. `component::binary_sensor::entity_component::glass_break::state::off`

**Engelska:** Clear

**Befintlig svenska:** Rensa

**Förslag:** Ingen glaskross upptäckt

## 9804. `component::binary_sensor::entity_component::glass_break::name`

**Engelska:** Glass break

**Befintlig svenska:** Glaskross

**Bedömning:** Ingen ändring föreslås.

## 9805. `component::binary_sensor::device_automation::trigger_type::no_glass_break`

**Engelska:** {entity_name} stopped detecting glass break

**Befintlig svenska:** {entity_name} har slutat upptäcka krossat glas

**Bedömning:** Ingen ändring föreslås.

## 9806. `component::binary_sensor::device_automation::trigger_type::glass_break`

**Engelska:** {entity_name} detected glass break

**Befintlig svenska:** {entity_name} har upptäckt krossat glas

**Bedömning:** Ingen ändring föreslås.

## 9807. `component::binary_sensor::device_automation::condition_type::is_no_glass_break`

**Engelska:** {entity_name} is not detecting glass break

**Befintlig svenska:** {entity_name} upptäcker inte krossat glas

**Bedömning:** Ingen ändring föreslås.

## 9808. `component::binary_sensor::device_automation::condition_type::is_glass_break`

**Engelska:** {entity_name} is detecting glass break

**Befintlig svenska:** {entity_name} upptäcker krossat glas

**Bedömning:** Ingen ändring föreslås.

## 9809. `component::zhong_hong::entity::climate::air_conditioner::state_attributes::fan_mode::state::medium_low`

**Engelska:** Medium low

**Befintlig svenska:** Medellåg

**Bedömning:** Ingen ändring föreslås.

## 9810. `component::zhong_hong::entity::climate::air_conditioner::state_attributes::fan_mode::state::medium_high`

**Engelska:** Medium high

**Befintlig svenska:** Medelhög

**Bedömning:** Ingen ändring föreslås.

## 9811. `component::tplink_omada::entity::update::firmware::name`

**Engelska:** Firmware

**Befintlig svenska:** Inbyggd programvara

**Bedömning:** Ingen ändring föreslås.

## 9812. `component::besen::entity::select::temperature_unit::state::fahrenheit`

**Engelska:** Fahrenheit

**Befintlig svenska:** Fahrenheit

**Bedömning:** Ingen ändring föreslås.

## 9813. `component::besen::entity::select::temperature_unit::state::celsius`

**Engelska:** Celsius

**Befintlig svenska:** Celsius

**Bedömning:** Ingen ändring föreslås.

## 9814. `component::besen::entity::select::temperature_unit::name`

**Engelska:** Temperature unit

**Befintlig svenska:** Temperaturenhet

**Bedömning:** Ingen ändring föreslås.

## 9815. `component::teslemetry::config_subentries::energy_site::initiate_flow::reconfigure`

**Engelska:** Reconfigure energy site

**Befintlig svenska:** Omkonfigurera energianläggning

**Bedömning:** Ingen ändring föreslås.

## 9816. `component::teslemetry::config_subentries::energy_site::abort::reconfigure_successful`

**Engelska:** [%key:common::config_flow::abort::reconfigure_successful%]

**Befintlig svenska:** Omkonfigurationen lyckades

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::abort::reconfigure_successful`; det ingår ännu inte i det insamlade underlaget.

## 9817. `component::airgradient::entity::number::measurement_interval::name`

**Engelska:** Measurement interval

**Befintlig svenska:** Mätintervall

**Bedömning:** Ingen ändring föreslås.

## 9818. `component::zha::exceptions::no_gateway::message`

**Engelska:** ZHA is not loaded, so this action cannot be performed.

**Befintlig svenska:** ZHA är inte inläst, så den här åtgärden kan inte utföras.

**Bedömning:** Ingen ändring föreslås.

## 9819. `component::lifx::exceptions::not_loaded::message`

**Engelska:** LIFX is not loaded, so this action cannot be performed.

**Befintlig svenska:** LIFX är inte inläst, så den här åtgärden kan inte utföras.

**Bedömning:** Ingen ändring föreslås.

## 9820. `component::tuya::entity::sensor::phase_c_reactive_power::name`

**Engelska:** Phase C reactive power

**Befintlig svenska:** Reaktiv effekt fas C

**Förslag:** Reaktiv effekt för fas C

## 9821. `component::tuya::entity::sensor::phase_c_power_factor::name`

**Engelska:** Phase C power factor

**Befintlig svenska:** Effektfaktor fas C

**Förslag:** Effektfaktor för fas C

## 9822. `component::tuya::entity::sensor::phase_c_apparent_power::name`

**Engelska:** Phase C apparent power

**Befintlig svenska:** Skeneffekt fas C

**Förslag:** Skenbar effekt för fas C

## 9823. `component::tuya::entity::sensor::phase_b_reactive_power::name`

**Engelska:** Phase B reactive power

**Befintlig svenska:** Reaktiv effekt fas B

**Förslag:** Reaktiv effekt för fas B

## 9824. `component::tuya::entity::sensor::phase_b_power_factor::name`

**Engelska:** Phase B power factor

**Befintlig svenska:** Effektfaktor fas B

**Förslag:** Effektfaktor för fas B

## 9825. `component::tuya::entity::sensor::phase_b_apparent_power::name`

**Engelska:** Phase B apparent power

**Befintlig svenska:** Skeneffekt fas B

**Förslag:** Skenbar effekt för fas B

## 9826. `component::tuya::entity::sensor::phase_a_reactive_power::name`

**Engelska:** Phase A reactive power

**Befintlig svenska:** Reaktiv effekt fas A

**Förslag:** Reaktiv effekt för fas A

## 9827. `component::tuya::entity::sensor::phase_a_power_factor::name`

**Engelska:** Phase A power factor

**Befintlig svenska:** Effektfaktor fas A

**Förslag:** Effektfaktor för fas A

## 9828. `component::tuya::entity::sensor::phase_a_apparent_power::name`

**Engelska:** Phase A apparent power

**Befintlig svenska:** Skeneffekt fas A

**Förslag:** Skenbar effekt för fas A

## 9829. `component::tuya::entity::switch::keypad_sound::name`

**Engelska:** Keypad sound

**Befintlig svenska:** Knappsatsljud

**Bedömning:** Ingen ändring föreslås.

## 9830. `component::tuya::entity::switch::alarm_push_notifications::name`

**Engelska:** Alarm push notifications

**Befintlig svenska:** Pushnotiser för larm

**Bedömning:** Ingen ändring föreslås.

## 9831. `component::teslemetry::config_subentries::vehicle::abort::bluetooth_not_available`

**Engelska:** Adding a vehicle over Bluetooth needs a Bluetooth adapter on the Home Assistant host or a remote Bluetooth proxy that supports active connections, such as an ESPHome Bluetooth proxy. Shelly devices only listen for Bluetooth devices and cannot connect to a vehicle.

**Befintlig svenska:** Att lägga till ett fordon via Bluetooth kräver en Bluetooth-adapter på värddatorn som kör Home Assistant eller en fjärransluten Bluetooth-proxy med stöd för aktiva anslutningar, till exempel en Bluetooth-proxy från ESPHome. Shelly-enheter lyssnar bara efter Bluetooth-enheter och kan inte ansluta till ett fordon.

**Bedömning:** Ingen ändring föreslås.

## 9832. `component::midea::entity::binary_sensor::water_pump_running::name`

**Engelska:** Water pump running

**Befintlig svenska:** Vattenpumpen körs

**Bedömning:** Ingen ändring föreslås.

## 9833. `component::roborock::exceptions::invalid_q10_zone::message`

**Engelska:** The zone coordinates are not valid for this vacuum

**Befintlig svenska:** Zonkoordinaterna är inte giltiga för den här dammsugaren

**Bedömning:** Ingen ändring föreslås.

## 9834. `component::roborock::exceptions::invalid_q10_coordinate::message`

**Engelska:** Coordinates ({x}, {y}) are not valid for this vacuum

**Befintlig svenska:** Koordinaterna ({x}, {y}) är inte giltiga för den här dammsugaren

**Bedömning:** Ingen ändring föreslås.

## 9835. `component::earn_e_p1::entity::sensor::voltage_phase::name`

**Engelska:** Voltage phase {phase}

**Befintlig svenska:** Spänning fas {phase}

**Förslag:** Spänning för fas {phase}

## 9836. `component::earn_e_p1::entity::sensor::current_phase::name`

**Engelska:** Current phase {phase}

**Befintlig svenska:** Ström fas {phase}

**Förslag:** Ström för fas {phase}

## 9837. `component::mochad::exceptions::turn_on_failed::message`

**Engelska:** Failed to turn on X10 device: {error}

**Befintlig svenska:** Det gick inte att slå på X10-enheten: {error}

**Bedömning:** Ingen ändring föreslås.

## 9838. `component::mochad::exceptions::turn_off_failed::message`

**Engelska:** Failed to turn off X10 device: {error}

**Befintlig svenska:** Det gick inte att stänga av X10-enheten: {error}

**Bedömning:** Ingen ändring föreslås.

## 9839. `component::energyzero::services::get_energy_prices::fields::price_type::name`

**Engelska:** Price type

**Befintlig svenska:** Pristyp

**Bedömning:** Ingen ändring föreslås.

## 9840. `component::energyzero::services::get_energy_prices::fields::price_type::description`

**Engelska:** The type of electricity prices to retrieve. Defaults to market prices.

**Befintlig svenska:** Vilken typ av elpriser som ska hämtas. Standardinställningen är marknadspriser.

**Bedömning:** Ingen ändring föreslås.

## 9841. `component::energyzero::services::get_energy_prices::fields::interval::name`

**Engelska:** Interval

**Befintlig svenska:** Intervall

**Bedömning:** Ingen ändring föreslås.

## 9842. `component::energyzero::services::get_energy_prices::fields::interval::description`

**Engelska:** The interval of electricity prices to retrieve. Defaults to hourly, independently of the electricity price interval configured for entities.

**Befintlig svenska:** Intervallet för de elpriser som ska hämtas. Standardinställningen är per timme, oberoende av det elprisintervall som har konfigurerats för enheterna.

**Bedömning:** Ingen ändring föreslås.

## 9843. `component::energyzero::selector::price_type::options::market`

**Engelska:** Market

**Befintlig svenska:** Marknad

**Bedömning:** Ingen ändring föreslås.

## 9844. `component::energyzero::selector::price_type::options::all_in`

**Engelska:** All-in

**Befintlig svenska:** Totalt (all-in)

**Bedömning:** Ingen ändring föreslås.

## 9845. `component::energyzero::selector::interval::options::quarter`

**Engelska:** [%key:component::energyzero::selector::electricity_price_interval::options::quarter_hourly%]

**Befintlig svenska:** [%key:component::energyzero::selector::electricity_price_interval::options::quarter_hourly%]

**Bedömning:** Ingen ändring föreslås.

## 9846. `component::energyzero::selector::interval::options::hour`

**Engelska:** [%key:component::energyzero::selector::electricity_price_interval::options::hourly%]

**Befintlig svenska:** [%key:component::energyzero::selector::electricity_price_interval::options::hourly%]

**Bedömning:** Ingen ändring föreslås.

## 9847. `component::fritzbox::config::step::user::data_description::verify_ssl`

**Engelska:** [%key:component::fritzbox::common::data_description_ssl_verify%]

**Befintlig svenska:** [%key:component::fritzbox::common::data_description_ssl_verify%]

**Bedömning:** Ingen ändring föreslås.

## 9848. `component::fritzbox::config::step::user::data_description::url`

**Engelska:** [%key:component::fritzbox::common::data_description_url%]

**Befintlig svenska:** [%key:component::fritzbox::common::data_description_url%]

**Bedömning:** Ingen ändring föreslås.

## 9849. `component::fritzbox::config::step::user::data::verify_ssl`

**Engelska:** [%key:common::config_flow::data::verify_ssl%]

**Befintlig svenska:** [%key:common::config_flow::data::verify_ssl%]

**Bedömning:** Ingen ändring föreslås.

## 9850. `component::fritzbox::config::step::user::data::url`

**Engelska:** [%key:common::config_flow::data::url%]

**Befintlig svenska:** [%key:common::config_flow::data::url%]

**Bedömning:** Ingen ändring föreslås.

## 9851. `component::fritzbox::config::step::reconfigure::data_description::verify_ssl`

**Engelska:** [%key:component::fritzbox::common::data_description_ssl_verify%]

**Befintlig svenska:** [%key:component::fritzbox::common::data_description_ssl_verify%]

**Bedömning:** Ingen ändring föreslås.

## 9852. `component::fritzbox::config::step::reconfigure::data_description::url`

**Engelska:** [%key:component::fritzbox::common::data_description_url%]

**Befintlig svenska:** [%key:component::fritzbox::common::data_description_url%]

**Bedömning:** Ingen ändring föreslås.

## 9853. `component::fritzbox::config::step::reconfigure::data::verify_ssl`

**Engelska:** [%key:common::config_flow::data::verify_ssl%]

**Befintlig svenska:** [%key:common::config_flow::data::verify_ssl%]

**Bedömning:** Ingen ändring föreslås.

## 9854. `component::fritzbox::config::step::reconfigure::data::url`

**Engelska:** [%key:common::config_flow::data::url%]

**Befintlig svenska:** [%key:common::config_flow::data::url%]

**Bedömning:** Ingen ändring föreslås.

## 9855. `component::fritzbox::common::data_description_url`

**Engelska:** The URL of your FRITZ!Box.

**Befintlig svenska:** URL-adressen till din FRITZ!Box.

**Bedömning:** Ingen ändring föreslås.

## 9856. `component::fritzbox::common::data_description_ssl_verify`

**Engelska:** Whether to verify the SSL certificate when SSL encryption is used to connect to your FRITZ!Box.

**Befintlig svenska:** Om SSL-certifikatet ska verifieras när SSL-kryptering används för att ansluta till din FRITZ!Box.

**Bedömning:** Ingen ändring föreslås.

## 9857. `component::lyngdorf::entity::sensor::maximum_volume::name`

**Engelska:** Maximum volume

**Befintlig svenska:** Maximal volym

**Bedömning:** Ingen ändring föreslås.

## 9858. `component::uptime_kuma::entity::sensor::type::state::sftp`

**Engelska:** SFTP

**Befintlig svenska:** SFTP

**Bedömning:** Ingen ändring föreslås.

## 9859. `component::besen::entity::sensor::plug_state::state::disconnected`

**Engelska:** [%key:common::state::disconnected%]

**Befintlig svenska:** [%key:common::state::disconnected%]

**Bedömning:** Ingen ändring föreslås.

## 9860. `component::besen::entity::sensor::plug_state::state::connected_unlocked`

**Engelska:** Connected, unlocked

**Befintlig svenska:** Ansluten, olåst

**Bedömning:** Ingen ändring föreslås.

## 9861. `component::besen::entity::sensor::plug_state::state::connected_locked`

**Engelska:** Connected, locked

**Befintlig svenska:** Ansluten, låst

**Bedömning:** Ingen ändring föreslås.

## 9862. `component::besen::entity::sensor::plug_state::name`

**Engelska:** Plug state

**Befintlig svenska:** Kontaktläge

**Bedömning:** Ingen ändring föreslås.

## 9863. `component::besen::entity::sensor::output_state::state::idle`

**Engelska:** [%key:common::state::idle%]

**Befintlig svenska:** [%key:common::state::idle%]

**Bedömning:** Ingen ändring föreslås.

## 9864. `component::besen::entity::sensor::output_state::state::charging`

**Engelska:** [%key:common::state::charging%]

**Befintlig svenska:** [%key:common::state::charging%]

**Bedömning:** Ingen ändring föreslås.

## 9865. `component::besen::entity::sensor::output_state::name`

**Engelska:** Output state

**Befintlig svenska:** Utgångstillstånd

**Bedömning:** Ingen ändring föreslås.

## 9866. `component::besen::entity::sensor::error_state::state::ungrounded`

**Engelska:** Ungrounded

**Befintlig svenska:** Ojordad

**Bedömning:** Ingen ändring föreslås.

## 9867. `component::besen::entity::sensor::error_state::state::short_circuit`

**Engelska:** Short circuit

**Befintlig svenska:** Kortslutning

**Bedömning:** Ingen ändring föreslås.

## 9868. `component::besen::entity::sensor::error_state::state::rtc_failure`

**Engelska:** RTC failure

**Befintlig svenska:** RTC-fel

**Bedömning:** Ingen ändring föreslås.

## 9869. `component::besen::entity::sensor::error_state::state::relay_stick_error`

**Engelska:** Relay stick error

**Befintlig svenska:** Fel på relästav

**Förslag:** Reläet har fastnat

## 9870. `component::besen::entity::sensor::error_state::state::over_voltage`

**Engelska:** Overvoltage

**Befintlig svenska:** Överspänning

**Bedömning:** Ingen ändring föreslås.

## 9871. `component::besen::entity::sensor::error_state::state::over_temperature`

**Engelska:** Overtemperature

**Befintlig svenska:** Övertemperatur

**Bedömning:** Ingen ändring föreslås.

## 9872. `component::besen::entity::sensor::error_state::state::over_current`

**Engelska:** Overcurrent

**Befintlig svenska:** Överström

**Bedömning:** Ingen ändring föreslås.

## 9873. `component::besen::entity::sensor::error_state::state::offline`

**Engelska:** Offline

**Befintlig svenska:** Offline

**Bedömning:** Ingen ändring föreslås.

## 9874. `component::besen::entity::sensor::error_state::state::no_error`

**Engelska:** No error

**Befintlig svenska:** Inget fel

**Bedömning:** Ingen ändring föreslås.

## 9875. `component::besen::entity::sensor::error_state::state::metering_module_failure`

**Engelska:** Metering module failure

**Befintlig svenska:** Fel på mätmodulen

**Bedömning:** Ingen ändring föreslås.

## 9876. `component::besen::entity::sensor::error_state::state::low_voltage`

**Engelska:** Low voltage

**Befintlig svenska:** Lågspänning

**Förslag:** Låg spänning

## 9877. `component::besen::entity::sensor::error_state::state::leakage_protection`

**Engelska:** Leakage protection

**Befintlig svenska:** Läckageskydd

**Bedömning:** Ingen ändring föreslås.

## 9878. `component::besen::entity::sensor::error_state::state::input_power_error`

**Engelska:** Input power error

**Befintlig svenska:** Fel på ingångseffekt

**Bedömning:** Ingen ändring föreslås.

## 9879. `component::besen::entity::sensor::error_state::state::flash_memory_failure`

**Engelska:** Flash memory failure

**Befintlig svenska:** Fel på flashminne

**Bedömning:** Ingen ändring föreslås.

## 9880. `component::besen::entity::sensor::error_state::state::emergency_stop`

**Engelska:** Emergency stop

**Befintlig svenska:** Nödstopp

**Bedömning:** Ingen ändring föreslås.

## 9881. `component::besen::entity::sensor::error_state::state::eeprom_failure`

**Engelska:** EEPROM failure

**Befintlig svenska:** EEPROM-fel

**Bedömning:** Ingen ändring föreslås.

## 9882. `component::besen::entity::sensor::error_state::state::dlb_over_current`

**Engelska:** DLB overcurrent, mains overload

**Befintlig svenska:** DLB-överström, överbelastning av nätet

**Bedömning:** Ingen ändring föreslås.

## 9883. `component::besen::entity::sensor::error_state::state::diode_short_circuit`

**Engelska:** Diode short circuit

**Befintlig svenska:** Diodkortslutning

**Bedömning:** Ingen ändring föreslås.

## 9884. `component::besen::entity::sensor::error_state::state::cp_error`

**Engelska:** CP error

**Befintlig svenska:** CP-fel

**Bedömning:** Ingen ändring föreslås.

## 9885. `component::besen::entity::sensor::error_state::state::cc_error`

**Engelska:** CC error

**Befintlig svenska:** CC-fel

**Bedömning:** Ingen ändring föreslås.

## 9886. `component::besen::entity::sensor::error_state::name`

**Engelska:** Error state

**Befintlig svenska:** Felstatus

**Bedömning:** Ingen ändring föreslås.

## 9887. `component::besen::entity::sensor::current_state::state::waiting_for_swipe`

**Engelska:** Waiting for card swipe

**Befintlig svenska:** Väntar på kortdragning

**Bedömning:** Ingen ändring föreslås.

## 9888. `component::besen::entity::sensor::current_state::state::waiting_for_button`

**Engelska:** Waiting for button

**Befintlig svenska:** Väntar på knapp

**Förslag:** Väntar på knapptryckning

## 9889. `component::besen::entity::sensor::current_state::state::ready_to_charge`

**Engelska:** Ready to charge

**Befintlig svenska:** Redo att ladda

**Bedömning:** Ingen ändring föreslås.

## 9890. `component::besen::entity::sensor::current_state::state::not_connected`

**Engelska:** Not connected

**Befintlig svenska:** Inte ansluten

**Bedömning:** Ingen ändring föreslås.

## 9891. `component::besen::entity::sensor::current_state::state::fault`

**Engelska:** [%key:common::state::fault%]

**Befintlig svenska:** [%key:common::state::fault%]

**Bedömning:** Ingen ändring föreslås.

## 9892. `component::besen::entity::sensor::current_state::state::completed_full_charge`

**Engelska:** Completed, fully charged

**Befintlig svenska:** Färdig, fulladdad

**Bedömning:** Ingen ändring föreslås.

## 9893. `component::besen::entity::sensor::current_state::state::completed`

**Engelska:** Completed

**Befintlig svenska:** Slutförd

**Bedömning:** Ingen ändring föreslås.

## 9894. `component::besen::entity::sensor::current_state::state::charging_reservation`

**Engelska:** Charging reservation

**Befintlig svenska:** Laddningsreservation

**Bedömning:** Ingen ändring föreslås.

## 9895. `component::besen::entity::sensor::current_state::state::charging_fault_2`

**Engelska:** Charging fault 2

**Befintlig svenska:** Laddningsfel 2

**Bedömning:** Ingen ändring föreslås.

## 9896. `component::besen::entity::sensor::current_state::state::charging_fault_1`

**Engelska:** Charging fault 1

**Befintlig svenska:** Laddningsfel 1

**Bedömning:** Ingen ändring föreslås.

## 9897. `component::besen::entity::sensor::current_state::state::charging`

**Engelska:** [%key:common::state::charging%]

**Befintlig svenska:** [%key:common::state::charging%]

**Bedömning:** Ingen ändring föreslås.

## 9898. `component::besen::entity::sensor::current_state::name`

**Engelska:** Current state

**Befintlig svenska:** Nuvarande tillstånd

**Bedömning:** Ingen ändring föreslås.

## 9899. `component::besen::entity::sensor::charging_status::state::waiting`

**Engelska:** Waiting

**Befintlig svenska:** Väntar

**Bedömning:** Ingen ändring föreslås.

## 9900. `component::besen::entity::sensor::charging_status::state::start`

**Engelska:** Start

**Befintlig svenska:** Start

**Bedömning:** Ingen ändring föreslås.

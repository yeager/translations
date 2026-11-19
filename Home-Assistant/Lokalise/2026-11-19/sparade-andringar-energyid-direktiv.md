# Sparade EnergyID-fält

Sparade och återlästa i Home Assistant Core i Lokalise 2026-11-19. Alla svenska fält var tomma före ändringen. Tre referensmål fick samtidigt svenska texter; `{directives_url}` och styckesindelningen bevarades.

## `component::energyid::options::step::init::title`

**Engelska:**

[%key:component::energyid::config::step::directives::title%]

**Sparad svenska:**

[%key:component::energyid::config::step::directives::title%]

## `component::energyid::options::step::init::description`

**Engelska:**

[%key:component::energyid::config::step::directives::description%]

**Sparad svenska:**

[%key:component::energyid::config::step::directives::description%]

## `component::energyid::options::step::init::data_description::enable_directives`

**Engelska:**

Poll EnergyID for every directive this record may access, including directives granted later.

**Sparad svenska:**

Hämta alla direktiv som den här posten har åtkomst till från EnergyID, även direktiv som tillkommer senare.

## `component::energyid::options::step::init::data::enable_directives`

**Engelska:**

[%key:component::energyid::config::step::directives::data::enable_directives%]

**Sparad svenska:**

[%key:component::energyid::config::step::directives::data::enable_directives%]

## `component::energyid::exceptions::directives_update_failed::message`

**Engelska:**

Error communicating with EnergyID while updating directives.

**Sparad svenska:**

Fel vid kommunikation med EnergyID när direktiven uppdaterades.

## `component::energyid::config::step::directives::title`

**Engelska:**

EnergyID directives

**Sparad svenska:**

EnergyID-direktiv

## `component::energyid::config::step::directives::description`

**Engelska:**

Directives tell you when it is a good or bad moment to use electricity. What a directive means for your installation is decided by its provider.

Manage access: {directives_url}

**Sparad svenska:**

Direktiv anger när det är bra eller dåligt att använda el. Vad ett direktiv innebär för din installation bestäms av dess leverantör.

Hantera åtkomst: {directives_url}

## `component::energyid::config::step::directives::data_description::enable_directives`

**Engelska:**

Poll EnergyID for every directive this record may access, including directives granted later. You can change this later in the integration options.

**Sparad svenska:**

Hämta alla direktiv som den här posten har åtkomst till från EnergyID, även direktiv som tillkommer senare. Du kan ändra detta senare i integrationens inställningar.

## `component::energyid::config::step::directives::data::enable_directives`

**Engelska:**

Receive EnergyID directives

**Sparad svenska:**

Ta emot EnergyID-direktiv

## `component::energyid::config::abort::wrong_account`

**Engelska:**

The provided credentials belong to a different EnergyID record than the one this entry is set up for. If you linked this device to that record while signing in, remove that link in EnergyID.

**Sparad svenska:**

De angivna inloggningsuppgifterna tillhör en annan EnergyID-post än den som den här posten är konfigurerad för. Om du kopplade enheten till den posten vid inloggningen ska du ta bort kopplingen i EnergyID.

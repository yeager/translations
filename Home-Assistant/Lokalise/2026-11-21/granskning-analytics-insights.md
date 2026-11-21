# Home Assistant Core – Analytics Insights

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/analytics_insights/strings.json`, Lokalise API med återläsning.

Status: samtliga 29 aktuella bladsträngar är radgranskade. Inga ändringar behövdes.

Granskningen omfattar konfiguration, alternativ, enhetsnamn/-enheter och de fyra undantagsmeddelandena. Platshållarna `{custom_integration_domain}`, `{endpoint}` och `{error}` är oförändrade. Produktnamnet Home Assistant är bevarat. Svensk text är grammatisk och konsekvent med etablerad Core-terminologi, bland annat *integration*, *spåra* och *aktiva installationer*.

De fyra äldre Lokalise-nycklarna för `tracked_addons` har kontrollerats mot aktuell källtext och ingår inte längre i komponentens `strings.json`; de är därför inte aktuella granskningsobjekt. Tidigare dokumentation för de fyra undantagsmeddelandena i 2026-11-19-granskningen har också jämförts med den aktuella källtexten.

Verifiering: direkt API-återläsning stämde med den sparade ögonblicksbilden för aktuella nycklar. `svlang` gav endast väntade egennamns-/platshållarsignaler och inga skrivregelfel; hunspell-sv hittade inga ordformsfel. Swedish FOSS Terminology och Swedish TM användes som stöd och gav inget skäl till ändring.

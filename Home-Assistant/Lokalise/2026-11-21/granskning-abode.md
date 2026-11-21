# Home Assistant Core – Abode

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/abode/strings.json`, aktuell Lokalise-export.

Status: samtliga 29 aktuella bladnycklar är radgranskade utan ändringsförslag.

## Verifierade områden

- Konfigurationsflödena har korrekta svenska texter för e-post, lösenord, MFA-kod och återautentisering. Produktnamnet `Abode` är oförändrat.
- Den gemensamma anslutnings- och autentiseringsreferensen är korrekt upplöst i Lokalise. Den komponentspecifika kontokontrollen använder korrekt svensk ordföljd.
- Tjänsterna för bildtagning, inställningsändring och automationsutlösning använder korrekta termer för entitet, entitets-ID och inställning. Fältet `{error}` i undantaget `change_setting_failed` är intakt.
- De direkta tjänsteetiketterna är idiomatiska imperativ: `Ta en bild`, `Ändra inställning` och `Utlös automatisering`.

Aktuella Lokalise-nyckel-ID:n för de direkta service- och undantagstexterna är `349126460`–`349126473` och `919309662`; konfigurationsnycklarna är `29062251`–`29062253`, `66412960`–`66412965` och `923292992`.

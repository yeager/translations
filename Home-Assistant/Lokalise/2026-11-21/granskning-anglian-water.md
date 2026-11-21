# Home Assistant Core – Anglian Water

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/anglian_water/strings.json`, tidigare rapporter och Lokalise API med direkt återläsning.

Status: samtliga 39 aktuella bladsträngar är radgranskade. Sex korrigeringar är sparade och återlästa.

| Nyckel | Sparad text | Motivering |
|---|---|---|
| `entity::sensor::latest_reading::name` | `Senaste avläsning` | Vattenmätarens *reading* är en avläsning, inte en läsning. |
| `exceptions::service_unavailable::message` | `Anglian Waters webbtjänster är för närvarande inte tillgängliga. Kontrollera loggarna för mer information.` | Bevarar varumärket och delar upp satsen. |
| `config::error::consent_required` | `Du måste godkänna villkoren för ditt Anglian Water-konto innan du använder den här integrationen. Logga in på Anglian Waters webbplats för mer information.` | Tar bort felöversättningen av varumärket. |
| `exceptions::consent_required::message` | `Villkoren för ditt Anglian Water-konto har uppdaterats. Logga in på ditt Anglian Water-konto och godkänn de nya villkoren.` | Varumärket bevarat och tydligare åtgärd. |
| `issues::consent_required::description` | `Villkoren för kontot {account_number} har uppdaterats. Logga in på ditt Anglian Water-konto och godkänn de nya villkoren.\n\nDet här problemet löses automatiskt när de nya villkoren har godkänts vid nästa uppdateringscykel.` | Korrigerar varumärket, dubbla punkter och tidssambandet; platshållaren är bevarad. |
| `issues::consent_required::title` | `Anglian Waters villkor har uppdaterats` | Korrekt svensk possessivform och grammatik. |

Referensmålen för återautentisering och multifaktorflödet är kontrollerade. Anglian Water och Home Assistant används som produktnamn. API-återläsning bekräftade alla sex ändringar; TMX-ledgern är uppdaterad och validerad (1 682 poster).

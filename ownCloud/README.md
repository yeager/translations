# ownCloud, svensk Transifex-granskning

Den 12 november 2026 granskades de då återstående svenska strängarna i
komponenterna `client` och `lib` i Transifex-projektet
`owncloud-org/owncloud`. ownCloud 11.1.0 publicerades den 3 november 2026 och
projektet uppfyller därmed aktualitetskravet.

Sex strängar om klientavslut, inloggningsskydd, apparkiv och kopieringsstatus
granskades, arkiverades och skickades genom separata Transifex API-anrop per
komponent. Den sista strängen, `Copied` i `twofactor_totp`, översattes till
`Kopierad` i statuskontexten.

En efterföljande API-avläsning av samtliga 81 komponenter visar 0 oöversatta
svenska strängar. Rådata för denna kontroll finns i
`Transifex/2026-11-12/verification-all-components.tsv`.

Arbetet är lokalt granskat, arkiverat och uppladdat. Upstreamgranskning eller
publicering är inte verifierad.

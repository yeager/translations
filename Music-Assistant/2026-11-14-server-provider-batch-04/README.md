# Music Assistant Server – svensk leverantörsbatch 4

Datum: 2026-11-14

Komponent: `music-assistant/server`, Lokalise-projektet **MA Server**.

Sex svenska strängar för Apple Musics anslutningsflöde. Tokenetiketterna
utelämnas avsiktligt eftersom Lokalise redan har *MusicKit-apptoken* och
*Manuell Musik-användartoken*. Manifestbeskrivningen utelämnas också eftersom
Lokalise redan har *Streama hela Apple Musics utbud och spellistor.* Apple
Music, MusicKit och Apple-ID behålls som synliga produktnamn. Omgivande
UI-text är svensk.

## Upstreamstatus

Alla sex värden i denna batch är nu sparade och återlästa i MA Server på
Lokalise 2026-11-14. `setup_flow.abort.auth_cancelled` och
`setup_flow.app_token.description` fanns redan sparade.
`setup_flow.app_token.title` och `setup_flow.auth.description` återlästes som
befintliga svenska värden. `setup_flow.auth.title`,
`setup_flow.user.description` och `setup_flow.user.title` sparades nu.
Lokalise-granskning, kodsynkronisering och release är inte verifierade.

`msgfmt` är inte tillämpligt eftersom katalogen är JSON. Övriga kontroller
körs före arkivering.

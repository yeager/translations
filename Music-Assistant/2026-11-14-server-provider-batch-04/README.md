# Music Assistant Server – svensk leverantörsbatch 4

Datum: 2026-11-14

Komponent: `music-assistant/server`, Lokalise-projektet **MA Server**.

Åtta svenska strängar för Apple Musics anslutningsflöde. Tokenetiketterna utelämnas avsiktligt eftersom Lokalise redan har *MusicKit-apptoken* och *Manuell Musik-användartoken*. Apple Music, MusicKit och Apple-ID behålls som synliga produktnamn. Omgivande UI-text är svensk.

## Upstreamstatus

`setup_flow.abort.auth_cancelled` sparades och lästes tillbaka i MA Server på Lokalise 2026-11-14. Övriga deltastringar är ännu inte inskickade och befintliga Lokalise-värden ersätts inte. Lokalise-granskning, kodsynkronisering och release är inte verifierade.

`msgfmt` är inte tillämpligt eftersom katalogen är JSON. Övriga kontroller körs före arkivering.

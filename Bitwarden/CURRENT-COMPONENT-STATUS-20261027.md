# Bitwarden: aktuell komponentstatus

Kontrollen utgår från Bitwardens klientkällkod vid commit
`0866e906e341da366eb265f95ece5ecc6542ca75`. Den senaste observerade
webbklienttaggen är `web-v2026.9.1`; den uppfyller kravet på en release yngre
än 48 månader.

| Komponent | Aktuell engelsk katalog | Saknade svenska måltexter i källträdet | Arkiverat 2026-10-27 | Upstreamstatus |
| --- | ---: | ---: | ---: | --- |
| Web | 4 952 | 263 | 204 | Inte inskickat; arkivdeltan behöver kopplas till aktuella plattforms-id:n före import. |
| Browser | 2 318 | 10 | 10 | Inte inskickat; se `bitwarden-browser-current-missing-sv-20261027.json`. |
| Desktop | 2 014 | 46 | 46 | Inte inskickat; se `bitwarden-desktop-current-missing-sv-20261027.json`. |
| Mobile | Ej del av den grunda klientklonen | Ej fastställt | Ingen ny ändring | Tidigare arkivfiler kräver ny källjämförelse. |
| Authenticator Mobile | Ej del av den grunda klientklonen | Ej fastställt | Ingen ny ändring | Tidigare arkivfiler kräver ny källjämförelse. |

Webbdeltana 01–17 innehåller de första 204 saknade posterna i den ordning de
förekommer i den aktuella engelska katalogen. Desktopfilen återanvänder 33
tidigare API-verifierade arkivtexter och kompletterar 13 nya eller ändrade
poster. Browserdeltat omfattar samtliga tio aktuellt saknade poster.

Alla nya JSON-deltan har kontrollerats för JSON-syntax, platshållare,
trippelidentiska konsonanter, `l10n-lint`, Hunspell, `svlang` och Gitleaks.
`svlang` analyserar även engelska källfält i deltaformatet; dess engelska
träffar räknas därför inte som svenska språkfel. Ingen källkatalog har
ändrats, och ingen post är därmed påstått uppladdad eller godkänd upstream.

Nästa arbete är att fortsätta Web från batch 18 och därefter hämta aktuella
Mobile- och Authenticator-källor innan fler mobilposter granskas.

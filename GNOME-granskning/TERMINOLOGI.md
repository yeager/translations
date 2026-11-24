# Svenska GNOME-termer

Denna lista används vid den lokala radgranskningen i `GNOME-granskning`.
Den följer etablerat svenskt GNOME-språk: korta, tydliga imperativ i menyer
och naturliga svenska i hjälptexter. Källtext och sammanhang avgör alltid;
listan är stöd, inte en ursäkt för mekanisk ersättning.

## Gränssnitt och åtgärder

| Engelska | Rekommenderad svenska | Anmärkning |
|---|---|---|
| Open | Öppna | Menyåtgärd. |
| Open Folder | Öppna mapp | Använd inte *folder* i svensk UI-text. |
| Save | Spara | |
| Save As | Spara som | |
| Close | Stäng | |
| Cancel | Avbryt | |
| Apply | Verkställ | *Tillämpa* bara när något faktiskt tillämpas. |
| Delete | Ta bort | *Radera* endast där det är etablerat i kontexten. |
| Remove | Ta bort | |
| Rename | Byt namn | |
| Edit | Redigera | |
| Preferences | Inställningar | I appmeny och dialogrubrik. |
| Settings | Inställningar | Bevara produktnamnet **Inställningar** där det avses. |
| Properties | Egenskaper | |
| Details | Detaljer | |
| Search | Sök | |
| Select All | Markera alla | |
| Help | Hjälp | |
| About | Om | |
| Quit | Avsluta | |
| Back / Forward | Bakåt / Framåt | |
| Enable / Disable | Aktivera / Inaktivera | |
| Default | Standard | |

## Filer, mappar och data

| Engelska | Rekommenderad svenska | Anmärkning |
|---|---|---|
| file | fil | |
| folder / directory | mapp | Använd *katalog* i teknisk eller filsystemsorienterad text. |
| path | sökväg | |
| filename | filnamn | |
| location | plats | |
| trash | papperskorg | |
| backup | säkerhetskopia | Verb: *säkerhetskopiera*. |
| restore | återställ | |
| import / export | importera / exportera | |
| clipboard | urklipp | |

## System och teknik

| Engelska | Rekommenderad svenska | Anmärkning |
|---|---|---|
| application / app | program | *App* kan användas i produktnamn eller etablerad mobilkontext. |
| extension | tillägg | |
| plugin | insticksmodul | Använd *tillägg* när GNOME-modulen använder termen extension. |
| update | uppdatering | Verb: *uppdatera*. |
| notification | avisering | |
| permission | behörighet | |
| authentication | autentisering | |
| account | konto | |
| password | lösenord | |
| network | nätverk | |
| connection | anslutning | |
| proxy | proxy | Oböjligt i korta UI-etiketter. |
| codec | kodek | |
| decoder | avkodare | Avser komponent/funktion, inte nödvändigtvis appnamnet **Decoder**. |
| encoder | kodare | |
| hardware | maskinvara | |
| firmware | fast programvara | Använd *firmware* när det är projektets etablerade tekniska term. |
| sample (pixbuf) | värde | Kanalsampel för en bildpunkt; här avses värdet, inte själva samplingsprocessen. |
| rowstride | radsteg | Antal byte mellan motsvarande lägen på efterföljande pixelrader. |
| chunk (bildformat) | block | En avgränsad del av en bildfil, exempelvis PNG-textblock. |
| pixbuf | pixbuf | GTK/GdkPixbuf-API-typ; behåll identifieraren och böj vid behov: *pixbufen*. |
| colorspace | färgrymd | Färgrymd som pixelvärdena tolkas i. |

## Form och skydd

- Bevara `printf`-platshållare, Rust-/Python-variabler, XML/HTML-markup,
  URL:er, kommandon, filnamn och radbrytningar exakt.
- Behåll acceleratormarkören `_` men välj om möjligt inte Å, Ä eller Ö som
  acceleratortangent. Kontrollera också kollisioner i samma meny.
- Översätt inte egennamn, utvecklarnamn, GNOME, GTK, GLib, D-Bus, Wayland,
  PipeWire, Flatpak, AppStream, systemd eller etablerade protokollnamn.
- Använd svenska citattecken ”…” i löpande svensk text. Låt citattecken i
  kommandon och kod vara oförändrade.
- Skriv sammansättningar naturligt: *inställningsdialog*, *filhanterare*,
  *säkerhetskopia*. Undvik engelska nominaliseringar när en enkel svensk
  verbform fungerar bättre.

## Valideringsordning

1. Kontrollera betydelse och kontext mot aktuell källsträng.
2. Jämför platshållare, markup, pluraler, acceleratorer och radbrytningar.
3. Kör filformatkontroll, `l10n-lint` och `hunspell-sv`.
4. Dokumentera ett avsiktligt identiskt egennamn eller tekniskt undantag i
   modulens `README.md`.

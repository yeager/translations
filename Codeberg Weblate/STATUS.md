# Svenska översättningar på Codeberg Weblate

Uppdrag: alla offentliga projekt. Användaren bekräftade hela tjänsten, inte bara följda projekt. Lokal Hunspell sv_SE används, med granskning av betydelse och format mot källtext. Ingen automatisk massgodkänning görs.

Inventering 12 september 2026: 605 projekt och 828 befintliga svenska komponenter. Befintliga svenska kataloger omfattade 223 936 strängar, varav 80 867 översatta och 8 201 markerade för redigering före arbetet. Detta omfattar inte nya svenska kataloger i projekt som saknar svenska.

## Aktuellt arbetssätt och projektregister

Varje nytt projekt kontrolleras först mot en offentligt verifierbar release från de senaste två åren (gräns: 2024-09-13). Projekt utan sådan release registreras som **potentiellt obsoleta** och hoppas över. För varje aktiv svensk komponent kontrolleras täckning, osäkra poster, Weblate-kontroller, platshållare och lokal stavning med `hunspell -d sv_SE`. Kompletta, publicerade komponenter speglas till `github.com/yeager/translations`.

### Speglade och granskade projekt

| Projekt | Komponenter | Strängar | Status | Senast verifierade release |
|---|---:|---:|---|---|
| alligator-gozaimasu | app | 80 | Publicerad och granskad; inga osäkra poster eller kontroller | 0.32 (2026-07-27) |
| ampersand | notes, filterqueries, resources, ampersand-lock-dashboard, security, analytics, tag-management, systems, import-export, members, app-settings, other | 374 | Publicerad och granskad; 13 dokumenterade tekniska kontroller | Se detaljerad arbetslogg; ej dokumenterad |
| archives | archives | 72 | Publicerad och granskad; inga osäkra poster eller kontroller | v0.6.0 (2025-07-01) |
| ascomplete | android | 135 | Publicerad och granskad; 2 dokumenterade tekniska kontroller | v0.1.0 (2026-09-09) |
| backintime | common | 540 | Publicerad och granskad; inga osäkra poster eller kontroller | ej dokumenterad |
| bgammon | client, server | 256 | Publicerad och granskad; 14 dokumenterade tekniska kontroller | ej dokumenterad |
| calligraphy | calligraphy | 40 | Publicerad och granskad; inga osäkra poster eller kontroller | v1.3.0 (2026-05-18) |
| censor | censor-glossary | 15 | Publicerad och granskad; inga osäkra poster eller kontroller | Se detaljerad arbetslogg |
| clock | cities, clock | 1026 | Publicerad och granskad; 219 dokumenterade tekniska kontroller | 2.31 (2026-06-28); ej dokumenterad |
| collision | collision | 45 | Publicerad och granskad; inga osäkra poster eller kontroller | v3.14.1 (2026-05-07) |
| comaps | appstore-description, website | 83 | Publicerad och granskad; 3 dokumenterade tekniska kontroller | ej dokumenterad |
| conversations | app-store-metadata | 106 | Publicerad och granskad; 1 dokumenterade tekniska kontroller | ej dokumenterad |
| currencies | changelogs-and-descriptions-fastlane-for-f-droid | 65 | Publicerad och granskad; inga osäkra poster eller kontroller | ej dokumenterad |
| diday-org | faqs | 48 | Publicerad och granskad; inga osäkra poster eller kontroller | ej dokumenterad |
| doable | values | 503 | Publicerad och granskad; 16 dokumenterade tekniska kontroller | v1.17.2 (2024-10-20) |
| door-knocker | main | 140 | Publicerad och granskad; 8 dokumenterade tekniska kontroller | ej dokumenterad |
| elly-code | unboxing, reminduck | 146 | Publicerad och granskad; 2 dokumenterade tekniska kontroller | ej dokumenterad |
| f-droid-classic | privext | 3 | Publicerad och granskad; inga osäkra poster eller kontroller | ej dokumenterad |
| f-droid_build_status | strings-xml, app-store-metadata, glossary | 223 | Publicerad och granskad; inga osäkra poster eller kontroller | 5.15.0 (2026-06-28) |
| fediphoto-lineage | description, strings | 282 | Publicerad och granskad; 3 dokumenterade tekniska kontroller | v8.0 (2025-08-26) |
| feeder | f-droid-and-play-store-metadata | 3 | Publicerad och granskad; inga osäkra poster eller kontroller | ej dokumenterad |
| flohmarkt | backend | 623 | Publicerad och granskad; 14 dokumenterade tekniska kontroller | 0.20.1 (2026-07-13) |
| foss-browser | strings | 158 | Granskad, men minst en komponent är låst | v23 (2026-06-22) |
| ftpclient | strings | 120 | Publicerad och granskad; inga osäkra poster eller kontroller | 3.2.0 (2026-08-23) |
| geoweather | geoweather | 290 | Publicerad och granskad; 4 dokumenterade tekniska kontroller | v3.1.3 (2026-09-10) |
| gnuhealth | health_webdav3_server, health_stock_nursing, health_stock_inpatient, health_contact_tracing, health_insurance, health_mdg6, health_nursing | 269 | Publicerad och granskad; 12 dokumenterade tekniska kontroller | ej dokumenterad |
| guix | website, glossary | 431 | Publicerad och granskad; 4 dokumenterade tekniska kontroller | ej dokumenterad |
| gymroutines | app-string-resources | 84 | Publicerad och granskad; inga osäkra poster eller kontroller | v0.1.1 (2025-04-18) |
| hades-revisited | hades-cloth, hades-dye, hades-food, hades-furnaces, hades-magic-wand, hades-seasons, hades-signs, hades-tiles, hades-vines, mobs-hades, hades-refuit, hades-death-messages, hades-chests, hades-mob-spawner, hades-bushes, hades_flowers, hades-beds-walls, hades-crystals-commands-hunger, hades-grass-greeting, hades-bags-creative-mobs, hades_doors, hades_craftguide, hades_trees, hades_flowerpots, hades_farming, hades_columnia, hades_core, hudbars, hades_skins, hades_itemshow, hades_furniture, hades_fences, hades_windows, hades_simulation, hades_orienteering, hades_tt, glossary, hades_stairs, hades_info, hades_carpets | 2451 | Publicerad och granskad; 43 dokumenterade tekniska kontroller | 0.20.2 (2026-02-16); Se detaljerad arbetslogg; ej dokumenterad |
| heliboard | heliboard | 552 | Publicerad och granskad; 11 dokumenterade tekniska kontroller | v4.1 (2026-08-30) |
| hurrycurry | game, website | 443 | Publicerad och granskad; 15 dokumenterade tekniska kontroller | v3.1.1 (2026-04-30) |
| imagepipe | metadata-for-fdroid, app-strings | 347 | Publicerad och granskad; 9 dokumenterade tekniska kontroller | ej dokumenterad; v0.78 (2026-06-07) |
| jdAnimatedImageEditor | UnixMetadata | 2 | Publicerad och granskad; inga osäkra poster eller kontroller | ej dokumenterad |
| jellybean | jellybean | 109 | Publicerad och granskad; inga osäkra poster eller kontroller | 0.5.1 (2026-03-03) |
| jetbird | app | 182 | Publicerad och granskad; inga osäkra poster eller kontroller | v1.8.10 (2026-09-04) |
| kettu | default | 121 | Publicerad och granskad; 2 dokumenterade tekniska kontroller | ej dokumenterad |
| lask | lask | 342 | Publicerad och granskad; 16 dokumenterade tekniska kontroller | 0.9.0 (2025-03-28) |
| lazarr | lzr_ambience, lzr_tools, lzr_player, lzr_doors, lzr_check_world_backend, lzr_check_movement_settings, _lzr_triggers_abbreviations, lzr_treasure, lzr_panes_functional, lzr_solutions, lzr_core, lzr_gui, lzr_parrot_npc, lzr_editor, lzr_credits, lzr_stairs, lzr_infobooks | 893 | Publicerad och granskad; 13 dokumenterade tekniska kontroller | 2.2.3 (2026-06-06); ej dokumenterad |
| libre-menu-editor | libre-menu-editor | 117 | Publicerad och granskad; inga osäkra poster eller kontroller | v1.10.5 (2026-08-09) |
| medilog | core | 592 | Publicerad och granskad; 1 dokumenterade tekniska kontroller | v3.8.0 (2026-09-11) |
| meshy-for-android | application | 155 | Publicerad och granskad; inga osäkra poster eller kontroller | 26.09.12 (2026-09-12) |
| mintapps | mintapps-basis-komponenten | 1963 | Publicerad och granskad; 24 dokumenterade tekniska kontroller | 2.2.0 (2026-02-04) |
| mitra-web | main | 421 | Publicerad och granskad; 8 dokumenterade tekniska kontroller | v5.10.0 (2026-08-24) |
| moshidon | values | 127 | Publicerad och granskad; 2 dokumenterade tekniska kontroller | ej dokumenterad |
| nitroxy | glossary | 4 | Publicerad och granskad; inga osäkra poster eller kontroller | ej dokumenterad |
| nontrinsic | android-metadata, android, ios, nontrinsic | 178 | Granskad, men minst en komponent är låst | ej dokumenterad |
| open-tracks-osm-dashboard | app-store-metadata | 67 | Publicerad och granskad; 8 dokumenterade tekniska kontroller | ej dokumenterad |
| plants | application | 108 | Publicerad och granskad; 7 dokumenterade tekniska kontroller | ej dokumenterad |
| postmill | messages | 648 | Publicerad och granskad; 3 dokumenterade tekniska kontroller | v2.2.3 (2026-07-20) |
| readeck | application | 643 | Publicerad och granskad; inga osäkra poster eller kontroller | 0.23.2 (2026-08-31) |
| scee | app | 663 | Publicerad och granskad; 15 dokumenterade tekniska kontroller | v63.4 (2026-08-05) |
| searloc | searloc | 78 | Publicerad och granskad; inga osäkra poster eller kontroller | ej dokumenterad |
| sepia-squirt | glossary | 5 | Publicerad och granskad; inga osäkra poster eller kontroller | ej dokumenterad |
| sriracha | sriracha | 582 | Publicerad och granskad; 29 dokumenterade tekniska kontroller | v2.1.2 (2026-09-13) |
| theme-color | handbook-help-daemon, handbook-help-tips, handbook-help-export, handbook-help-colors, handbook-help-general, handbook-help-howto, handbook-help-ui, app | 307 | Publicerad och granskad; 11 dokumenterade tekniska kontroller | ej dokumenterad |
| tiny-weather-forecast-germany | fdroid-metadata, app-strings | 600 | Publicerad och granskad; 19 dokumenterade tekniska kontroller | 0.63.4 (2026-07-24) |
| tournant | glossary, app | 153 | Publicerad och granskad; 1 dokumenterade tekniska kontroller | ej dokumenterad |
| trawelling | traewelling | 1444 | Publicerad och granskad; 94 dokumenterade tekniska kontroller | 2026.09.12 (2026-09-12) |
| turntable | turntable | 139 | Publicerad och granskad; inga osäkra poster eller kontroller | v0.5.1 (2025-12-26) |
| untrackme | untrackme-description, app | 166 | Publicerad och granskad; 49 dokumenterade tekniska kontroller | Se detaljerad arbetslogg; ej dokumenterad |
| wormhole | app | 78 | Publicerad och granskad; inga osäkra poster eller kontroller | ej dokumenterad |

### Potentiellt obsoleta projekt

| Projekt | Senast verifierade release | Status |
|---|---|---|
| Ampersand | Ingen verifierbar offentlig release | Potentiellt obsolet — Ingen offentlig release kunde verifieras via Codeberg-release-API:t; projektet hoppas över enligt tvåårsregeln. |
| auto-tab-opener | v2.10 (2022-10-09) | Potentiellt obsolet — Senaste verifierade release är äldre än två år per 2026-09-13; projektet hoppas över tills en ny release kan verifieras. |
| conversations | Ingen verifierbar offentlig release hittades | Potentiellt obsolet — Ingen offentlig release inom de senaste två åren kunde verifieras via den officiella webbplatsen eller release-API:t per 2026-09-13; projektet hoppas över tills en sådan release kan verifieras. |
| OBS Master | 0.6.3 (2023-11-16) | Potentiellt obsolet — Senaste verifierade release är äldre än två år; projektet hoppades över enligt granskningsregeln. |
| partygames | 2.0.0 (2024-01-08) | Potentiellt obsolet — Senaste verifierade release är äldre än två år per 2026-09-13; projektet hoppas över tills en ny release kan verifieras. |
| weather | 3.21-pre1 (2023-04-12) | Potentiellt obsolet — Senaste verifierade release är äldre än två år per 2026-09-13; projektet hoppas över tills en ny release kan verifieras. |

### Detaljerad arbetslogg

Följande logg beskriver ändringar, låsta komponenter och tekniska kontrollresultat per komponent. Registret ovan är den aktuella sammanställningen per projekt.

| Projekt | Omfattning | Resultat |
|---|---|---|
| mc6 | Samtliga 2 575 strängar | 1 664 poster accepterade vid uppladdning. 100 %, 0 ofärdiga. Fullständig API-återläsning matchar. Formell granskning avstängd. Se ../mc6-review/GRANSKNING.md. |
| OSM Dashboard / strings-xml | Samtliga 125 strängar | 55 rättningar sparade och verifierade med API-svaren. 100 %, 0 ofärdiga, 0 fallerande kontroller. |
| F-Droid Build Status / strings-xml | Samtliga 137 strängar | Granskad. Den enda kontrollvarningen, ”METAdata”, är rättad till ”Metainformation” och sparad. |
| Currencies | Samtliga 208 synliga poster | Granskad. Format och lokal Hunspell kontrollerade; 4 tomma Android-referenser är skrivskyddade. Ingen saklig ändring behövdes. |
| Censor / glossary | Samtliga 15 strängar | Dokument-, PDF- och maskeringstermer översatta. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. Hunspell-träffen ”rasteriserad” är en korrekt fackterm. |
| UntrackMe / description | Samtliga 10 strängar | Fullständig F-Droid-beskrivning och versionsnoteringar översatta; URL:er, listor och produktnamn bevarade. Servern bekräftar 100 %, 0 ofärdiga och 0 fuzzy. Två servervarningar återstår utan enhetskoppling i API-svaret och granskas vidare. |
| Auto Tab Opener | Samtliga 26 strängar | 8 rättningar förberedda och stavningskontrollerade. Servern avvisar skrivning eftersom översättningen är låst. Inga ändringar publicerade. |
| WhiteNoise | Samtliga 121 strängar | Hela musikspelarens svenska katalog är översatt och granskad mot källtexten. Platshållare, HTML, snabbtangenter och lokala Hunspell-träffar är kontrollerade. Servern avvisar samtliga 121 skrivningar eftersom översättningen är låst. Inga ändringar publicerade. |
| RadioMii | Samtliga 67 strängar | 17 rättningar granskade och stavningskontrollerade. Servern avvisar skrivning eftersom översättningen är låst. Inga ändringar publicerade. |
| TBlock GUI | Samtliga 176 strängar | 156 översättningar eller rättningar sparade. Fullständig återläsning: 100 %, 0 ofärdiga, 0 fallerande kontroller. Hunspell och kontroll av platshållare/radbrytningar godkända. |
| Ampersand / dashboard | Samtliga 13 strängar | Den återstående strängen, ”Recent posts”, är översatt till ”Senaste inlägg” och servern bekräftar 100 %, 0 ofärdiga, 0 fallerande kontroller. |
| Mineclonia / mcl_fireworks | Samtliga 2 strängar | ”Flight Duration: @1s” är granskat som ”Flygtid: @1 s”, men servern avvisar skrivning eftersom översättningen är låst. Ingen ändring publicerad. |
| Mineclonia / mcl_craftguide | Samtliga 39 strängar | Receptguide, blockgrupper och reparationsmeddelanden är översatta och granskade med bevarade @1/@2 och ×. Servern avvisar samtliga skrivningar eftersom komponenten är låst. Inga ändringar publicerade. |
| VoxelForge / vlf_amethyst | Samtliga 18 strängar | Ametist-, kalcit- och tonat glas-texter är översatta och granskade. Servern avvisar samtliga skrivningar eftersom komponenten är låst. Inga ändringar publicerade. |
| CoMaps / F-Droid-beskrivning | Samtliga 3 strängar | Titel, korttext och fullständig appbeskrivning är översatta och kontrollerade. HTML, listor och radbrytningar bevarade; titel anpassad till komponentens gräns på 30 tecken. Servern bekräftar 100 %, 0 ofärdiga, 0 fallerande kontroller. |
| CoMaps / Google Play-beskrivning | Samtliga 3 strängar | Den återstående fullständiga beskrivningen är översatt. HTML, listor och radbrytningar kontrollerade; lokal Hunspell använd. Servern bekräftar 100 %, 0 ofärdiga, 0 fallerande kontroller. |
| Lazarr / lzr_mapgen | Samtliga 5 strängar | Den återstående Luanti-inställningstexten är översatt med bevarad @1-platshållare. Servern bekräftar 100 %, 0 ofärdiga, 0 fallerande kontroller. |
| Lazarr / lzr_speech | Samtliga 6 strängar | Den återstående dialogtexten ”Okay” är översatt till ”Okej”. Servern bekräftar 100 %, 0 ofärdiga, 0 fallerande kontroller. |
| Lazarr / lzr_fallout | Samtliga 4 strängar | En tom sträng översatt och en idiomatisk formulering rättad. Servern bekräftar 100 %, 0 ofärdiga, 0 fallerande kontroller. |
| Lazarr / lzr_tt | Samtliga 5 strängar | Två tomma strängar översatta och tre etablerade formuleringar rättade. Servern bekräftar 100 %, 0 ofärdiga, 0 fallerande kontroller. |
| Lazarr / lzr_getitem | Samtliga 9 strängar | Två tomma strängar översatta och sex UI-formuleringar granskade och rättade. Servern bekräftar 100 %, 0 ofärdiga, 0 fallerande kontroller. |
| Lazarr / lzr_hook | Samtliga 3 strängar | Två tomma spelinstruktioner översatta. 100 %, 0 ofärdiga; kvarvarande servervarning gäller den befintliga korrekta termen ”Roterande krok”. |
| Lazarr / lzr_sky | Samtliga 13 strängar | En tom sträng översatt och tre formuleringar förbättrade. Servern bekräftar 100 %, 0 ofärdiga, 0 fallerande kontroller. |
| GNU Health / glossary | Samtliga 3 strängar | Den medicinska termen ”Ambulatory care” är översatt till ”Öppenvård”. Servern bekräftar 100 %, 0 ofärdiga, 0 fallerande kontroller. |
| GNU Health / health_inpatient_calendar | Samtliga 4 strängar | Två tomma strängar översatta och sammansättningen ”Kalenderhändelse” rättad. Servern bekräftar 100 %, 0 ofärdiga, 0 fallerande kontroller. |
| HeliBoard / glossary | Samtliga 4 strängar | ”number row” översatt till ”Sifferrad” och ”Popup” rättad till ”Popupfönster”. Servern bekräftar 100 %, 0 ofärdiga, 0 fallerande kontroller. |
| QML Greed / glossary | Samtliga 2 strängar | ”D-Pad” och ”Game Over” översatta till ”Styrkors” respektive ”Spelet är slut”. Servern bekräftar 100 %, 0 ofärdiga, 0 fallerande kontroller. |
| Offshore / glossary | Samtliga 3 strängar | ”Bookmarks” och ”Bookmark” översatta till ”Bokmärken” och ”Bokmärke”; projektnamnet Open Food Facts bevarat. Servern bekräftar 100 %, 0 ofärdiga, 0 fallerande kontroller. |
| Scripty Bot / glossary | Samtliga 3 strängar | Produkt- och tjänstenamnen Premium, Discord och Scripty kontrollerade och markerade som kompletta. Servern bekräftar 100 %, 0 ofärdiga, 0 fallerande kontroller. |
| Tournant / metadata | Samtliga 3 strängar | Den felaktigt förkortade appbeskrivningen är ersatt med en fullständig svensk översättning. Markdown, emoji och länk bevarade. Servern bekräftar 100 %, 0 ofärdiga, 0 fallerande kontroller. |
| OBS Master / glossary | Samtliga 3 strängar | ”package” och ”project” översatta till ”paket” och ”projekt”; produktnamnet spectacle bevarat. Servern bekräftar 100 %, 0 ofärdiga, 0 fallerande kontroller. |
| AmpMod / glossary | Samtliga 3 strängar | Översättningarna ”block”, ”tillägg” och ”krasch” granskade, men servern avvisar skrivning eftersom komponenten är låst. Inga ändringar publicerade. |
| Flohmarkt / glossary | Samtliga 2 strängar | Termerna ”session” och FediAuth kontrollerade och markerade som kompletta. Servern bekräftar 100 %, 0 ofärdiga, 0 fallerande kontroller. |
| Hades Revisited / hades_game_meta | Samtliga 2 strängar | Projektnamnet bevarat och den fullständiga spelbeskrivningen översatt. Servern bekräftar 100 %, 0 ofärdiga, 0 fallerande kontroller. |
| Hades Revisited / hades_safespawn | Samtliga 2 strängar | Båda säkerhetsteleporteringsmeddelandena översatta. Servern bekräftar 100 %, 0 ofärdiga, 0 fallerande kontroller. |
| Hades Revisited / hades_torches | Samtliga 2 strängar | ”Bright Torch” och ”Weak Torch” översatta. Servern bekräftar 100 %, 0 ofärdiga, 0 fallerande kontroller. |
| Hades Revisited / hades_vessels | Samtliga 2 strängar | ”Empty Glass Bottle” och ”Pile of Glass Fragments” översatta. Servern bekräftar 100 %, 0 ofärdiga, 0 fallerande kontroller. |
| Hades Revisited / hades_food | Samtliga 16 strängar | Alla maträtter och ingredienser översatta, inklusive konsekvent användning av paj och sammansättningar. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. Lokal Hunspell träffade endast den korrekta sammansättningen ”apelsinpaj”. |
| Hades Revisited / hades_cloth | Samtliga 15 strängar | Samtliga färgvarianter av tyg översatta med konsekventa neutrumformer. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. Lokal Hunspell träffade endast den korrekta sammansättningen ”cyanfärgat”. |
| Hades Revisited / hades_seasons | Samtliga 15 strängar | Årstider, kommandobeskrivningar och datumrad översatta med bevarade @1–@3-platshållare. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. Lokal Hunspell godkänd. |
| Hades Revisited / hades_furnaces | Samtliga 13 strängar | Ugnar, status och bränslemeddelanden översatta med bevarade @1/@2-platshållare. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. Hunspell-träffen ”Prismaugn” är en korrekt sammansättning. |
| Hades Revisited / hades_magic_wand | Samtliga 13 strängar | Magiska verktyg, behörighetsmeddelanden och ägarstatus översatta med bevarade @1/@2-platshållare. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. Lokal Hunspell godkänd. |
| Hades Revisited / mobs_hades | Samtliga 14 strängar | Spindelnät och framkallningsägg för varelser översatta. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. Hunspell-träffarna är de avsiktligt bevarade speltermerna Mese och Oerkki. |
| Hades Revisited / hades_dye | Samtliga 15 strängar | Samtliga färgämnen översatta med konsekventa neutrumformer. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. Hunspell-träffen ”cyanfärgat” är en korrekt sammansättning. |
| Hades Revisited / hades_refuit | Samtliga 29 strängar | Årstidsvillkor och knoppar/blommor för fruktträd översatta med bevarade @1-platshållare. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. Hunspell-träffen ”Kakiknopp” är en korrekt sammansättning. |
| Hades Revisited / hades_death_messages | Samtliga 29 strängar | Dödsorsaker och återskapningsknapp översatta med bevarad @1-platshållare och konsekventa namn för varelser. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. Hunspell-träffen ”mese-monster” är en avsiktligt bevarad spelterm. |
| Hades Revisited / hades_chests | Samtliga 33 strängar | Kistor, färgvarianter, lås och ägarskap översatta med bevarade @1/@2-platshållare. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. Hunspell-träffen ”cyanfärgad” är en korrekt sammansättning. |
| Hades Revisited / hades_mob_spawner | Samtliga 30 strängar | Varelsegeneratorns inställningar, felmeddelanden och behörighetstexter översatta med bevarade @1–@3 och ×. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. Lokal Hunspell godkänd. |
| Hades Revisited / hades_bushes | Samtliga 28 strängar | Trädgårdsbuskar, frön, färgvarianter och årstidsvillkor översatta med bevarad @1-platshållare. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. Hunspell-träffarna är korrekta sammansättningar för växtnamn. |
| Hades Revisited / screwdriver | Samtliga 2 strängar | Verktygsnamnet och instruktionen för rotation översatta. Servern bekräftar 100 %, 0 ofärdiga, 0 fallerande kontroller. |
| Hades Revisited / show_wielded_item | Samtliga 2 strängar | Modulnamnet och dess beskrivning översatta. Servern bekräftar 100 %, 0 ofärdiga, 0 fallerande kontroller. |
| GNU Health / health_crypto_lab | Samtliga 15 strängar | Fem ofärdiga strängar översatta och kryptografiska hashvärden, dokumentation samt laboratoriedialoger rättade. Servern bekräftar 100 %, 0 ofärdiga, 0 fallerande kontroller. |
| GNU Health / health_stock_surgery | Samtliga 10 strängar | Fyra ofärdiga strängar översatta och lagerförflyttningar för operationer språkligt och semantiskt rättade. Servern bekräftar 100 %, 0 ofärdiga, 0 fallerande kontroller. |
| GNU Health / health_services_lab | Samtliga 16 strängar | Sex ofärdiga strängar översatta och tio befintliga laboratorietexter granskade. Hunspell träffade endast kodidentifierare. Servern bekräftar 100 %, 0 ofärdiga; en servervarning kvarstår på den flerradiga instruktionen trots bevarad radbrytning och betydelse. |
| GNU Health / health_services_imaging | Samtliga 16 strängar | Fem ofärdiga strängar översatta, befintliga statusmeddelanden rättade och den markerade termen ”Okänd” färdigställd. Hunspell träffade endast kodidentifierare. Servern bekräftar 100 %, 0 ofärdiga; en servervarning kvarstår på den flerradiga instruktionen trots bevarad radbrytning och betydelse. |
| GNU Health / health_archives | Samtliga 21 strängar | Fjorton ofärdiga arkiv- och patientjournalstexter översatta samt statusposten färdigställd. Lokal Hunspell godkänd. Servern bekräftar 100 %, 0 ofärdiga; en servervarning återstår för en befintlig korrekt term. |
| Back In Time / glossary | Samtliga 19 strängar | ”SSH private key” översatt och begreppen säkerhetskopia samt symbolisk länk rättade. Hunspell träffade endast tekniktermen SSH-nyckel. Servern bekräftar 100 %, 0 ofärdiga, 0 fallerande kontroller. |
| Megalodon / metadata | Samtliga 20 strängar granskade | Alla tio saknade versionsnoteringar och den tidigare fuzzy-markerade huvudbeskrivningen är översatta med bevarade HTML-taggar och punktlistor. Hunspell träffade endast produktnamn och korrekta sammansättningar, bland annat Fediverse, Mastodon, Akkoma-användare, filöppnare, följknappen, trådvy, emojireaktioner och emojiväljaren; en stavningsmiss i regellistan rättades före publicering. Servern bekräftar 100 %, 0 ofärdiga och 0 fuzzy; två formatvarningar återstår på punktlistor trots matchande struktur. |
| Rosetta | Samtliga 27 strängar granskade | ”Copy response” rättad till ”Kopiera svar” och två tomma strängar översatta. Servern avvisar skrivning eftersom komponenten är låst. Inga ändringar publicerade. |
| Paroli | Samtliga 30 strängar granskade | Tio felaktiga eller tomma AI- och bildgenereringstexter översatta, inklusive bevarade radbrytningar och acceleratorn `_Speak`. Servern avvisar skrivning eftersom komponenten är låst. Inga ändringar publicerade. |
| CoMaps / glossary | Samtliga 22 strängar | De två oöversatta posterna ”Gate” och ”Willis Island” översatta till ”Grind” och ”Willisön”; egennamn och spärrade tekniska poster bevarade. Hunspell träffade endast egennamnet Willisön. Servern bekräftar 100 %, 0 ofärdiga; en befintlig servervarning återstår. |
| Ampersand / onboarding | Samtliga 16 strängar | Den återstående importinstruktionen översatt med bevarad menyväg. Hunspell och serverkontroller godkända: 100 %, 0 ofärdiga, 0 fallerande kontroller. |
| Ampersand / front-history | Samtliga 24 strängar | Felaktig översättning av ”Confirm” rättad till ”Bekräfta” och ”Summary” översatt. Servern bekräftar 100 %, 0 ofärdiga, 0 fallerande kontroller. |
| Ampersand / journal | Samtliga 24 strängar | Den återstående UI-texten ”Post color” översatt till ”Inläggets färg”. Servern bekräftar 100 %, 0 ofärdiga, 0 fallerande kontroller. |
| Ampersand / reminders | Samtliga 16 strängar | Femton påminnelse- och händelsetexter översatta. Lokal Hunspell och serverkontroller godkända: 100 %, 0 ofärdiga, 0 fallerande kontroller. |
| Veloren / voxygen-char_selection | Samtliga 27 strängar granskade | Den återstående termen ”Height” är översatt till ”Längd”, men servern avvisar skrivning eftersom komponenten är låst. Ingen ändring publicerad. |
| Postmill / validators | Samtliga 19 strängar | De två återstående valideringsmeddelandena översatta. Servern bekräftar 100 %, 0 ofärdiga, 0 fallerande kontroller. |
| Veloren / items/weapon | Samtliga 33 strängar granskade | Den tomma ”Crude Mallet” och stavfelet ”Prommenadkäpp” har översatts/rättats, med bevarad `.desc`-rad. Servern avvisar skrivning eftersom komponenten är låst. Inga ändringar publicerade. |
| CoMaps / android-ui-strings-sdk | Samtliga 35 strängar | Fyra tillgänglighetsinstruktioner för beröringsutforskning översatta. Lokal Hunspell och serverkontroller godkända: 100 %, 0 ofärdiga, 0 fallerande kontroller. |
| Ampersand / accessibility | Samtliga 23 strängar | Sjutton tillgänglighetsinställningar översatta, inklusive lättlästa typsnitt, animationer och färgalternativ. Hunspell träffade enbart typsnittsnamn och apptermen frontning. Servern bekräftar 100 %, 0 ofärdiga; en befintlig servervarning återstår. |
| Ampersand / message-board | 29 av 30 strängar | Tjugofem anslagstavle- och omröstningstexter översatta. Den enda återstående pluralposten `{{count}} voter` är granskad som `{{count}} röstande`, men Weblate-API:t avvisar pluraluppdateringen med felaktigt antal pluralformer. Servern visar 29 översatta, 0 fuzzy och en formatvarning. |
| FediPhoto-Lineage / description | Samtliga 30 strängar granskade | Alla tidigare tomma versionsnoteringar är översatta med bevarade punktlistor. Ett oavsiktligt danskt ord i den liggande layout-noteringen rättades före fortsättning. Servern bekräftar 100 %, 0 ofärdiga och 0 fuzzy; en formatvarning återstår på en teknisk punktlista. |
| Ampersand / about | Samtliga 7 strängar | Tre återstående texter om uppdateringar och tack översatta. Servern bekräftar 100 %, 0 ofärdiga, 0 fallerande kontroller. |
| Ampersand / asset-manager | Samtliga 12 strängar | ”Tags”, ”Save attachment” och ”Select asset” översatta. Servern bekräftar 100 %, 0 ofärdiga, 0 fallerande kontroller. |

Övriga projekt återstår. Filen är en arbetsjournal och innebär inte att alla projekt är färdiga. För varje komponent finns ursprungliga strängar, ändringar, stavningsresultat och API-kvitton i respektive underkatalog. API-nyckeln förvaras utanför arbetskatalogen och får inte inkluderas i rapporter eller ändringsfiler.

| Hades Revisited / hades_vines och hades_signs | Samtliga 31 strängar | Vinväxter, frön och skyltar är översatta. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. |
| Hades Revisited / hades_tiles | Samtliga 18 strängar | Plattor och dekorationsblock är översatta. Servern bekräftar 100 % och 0 fuzzy; API:ts enhetskontroller är rena, medan komponentstatistiken fortsatt visar två äldre, ospecificerade kontrollmarkeringar. |
| Hades Revisited / hades_flowers | Samtliga 47 strängar | Blommor, frön, plantor och årstidsvillkor översatta. Den tvetydiga tidigare texten ”Apelsinblomma” rättades till ”Orange blomma”. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. |
| Hades Revisited / hades_beds | Samtliga 6 strängar | Sängar och återuppståndelsemeddelanden översatta. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. |
| Hades Revisited / hades_walls | Samtliga 7 strängar | Murblock av kullersten och sandsten översatta. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. Hunspell-träffarna på ”kullerstensmur” är korrekta sammansättningar. |
| Kbin / glossary | Samtliga 3 strängar | Grundtermerna e-post, inlägg och bannlysning översatta. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. |
| Hades Revisited / hades_glowcrystals | Samtliga 7 strängar | Glödkristaller, malm, block och facklor översatta. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. |
| Hades Revisited / hades_commands | Samtliga 7 strängar | Kommandosyntax, hälsomeddelanden och simuleringstext översatta med bevarade @1 och kommandon. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. |
| Hades Revisited / hades_hunger | Samtliga 7 strängar | Mättnads- och svältkommandon översatta med bevarad syntax och @1-platshållare. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. |
| Hades Revisited / hades_grass | Samtliga 8 strängar | Gräs, frön och växtvillkor översatta. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. |
| Hades Revisited / hades_greeting | Samtliga 9 strängar | Introduktionsmeddelanden för kreativt läge och överlevnad översatta. Transmissionsmarkörerna och egennamnet Wuzzy bevarade. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. |
| Hades Revisited / hades_bags | Samtliga 9 strängar | Väskor, storlekar och inventarieplatser översatta med bevarad @1-platshållare. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. |
| Hades Revisited / hades_creative | Samtliga 10 strängar | Kreativ inventering, sidnavigering och kategorier översatta med bevarade @1/@2. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. |
| Hades Revisited / mobs | Samtliga 20 strängar | Varelsehantering, tämjning och administratörsverktyg översatta med bevarade @1/@2 och ×. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. Hunspell-träffar på ”tamd” och ”varelseavskräckare” är sakligt korrekta böjnings- och sammansättningsformer. |
| jdAnimatedImageEditor / UnixMetadata | Samtliga 3 strängar granskade | Två onaturliga formuleringar med ”simpelt” rättade till ”enkelt”; format och produktnamn bevarade. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. |
| Postmill / security | Samtliga 1 sträng | Kontosanktionen rättad till den idiomatiska formuleringen ”Ditt konto har bannlysts.” Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. |
| Theme Color / handbook-help-daemon | Samtliga 6 strängar | Hjälpavsnittet om övervakningsdemonen, dess inställningar och nattläge översatt. Kursivering och produktnamnen ThemeColor/Ambience är bevarade. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. |
| Mineclonia / sex korta komponenter | Samtliga 6 strängar granskade | Elytra, skruvmejsel, misstänkt gryta, spelbeskrivning, tomrumsvarning och avancerade block har svenska förslag, men samtliga komponenter är låsta och inga ändringar kunde publiceras. |
| Theme Color / handbook-help-tips | Samtliga 6 strängar | Tips om paletter, färgscheman och återställning översatta. HTML-radbrytning, Cupboard/PullUp och dconf-kommandon är bevarade. Servern bekräftar 100 % och 0 fuzzy; komponentstatistiken visar två ospecificerade kontrollmarkeringar, men API:ts enhetsnivå visar inga kontroller på någon av de sex posterna. |
| Theme Color / handbook-help-export | Samtliga 10 strängar | Exporthandbok för Ambience-teman översatt. `.ambience`, RPM, dconf, Builder, lipstick och HTML-markup är bevarade. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. |
| Elly Code / glossary | Samtliga 6 strängar granskade | Produktnamnen Jorts, Unboxing, Reminduck och Roll-It har kontrollerats och färdigställts där de är skrivbara. En Jorts-post är skrivskyddad; inga sakliga ändringar gjordes av produktnamn. Servern visar 100 %, 0 fuzzy och 0 fallerande kontroller. |
| Theme Color / handbook-help-colors | Samtliga 11 strängar | Färgdokumentationen översatt och den tidigare felaktiga svenska introduktionen rättad. Konfigurationsnycklar, produktnamn och den officiella HTML-länken är bevarade. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. |
| Nontrinsic / android-metadata | Samtliga 9 strängar | Fullständig svensk F-Droid-beskrivning och samtliga versionsnoteringar översatta. HTML-lista, emstreck, Android-versioner och produktnamn bevarade. Åtta skrivningar accepterades; den identiska produktnamnsposten är skrivskyddad. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. |
| Nontrinsic / android | 6 riktade rättningar | Fel i API-inställningen, e-postinstruktionen, sammansättningen `nonsensinlägg`, API-terminologi och den tomma knappen ”Uppdatera” rättade. Alla sex skrivningar accepterades. Komponenten har kvar sex andra, icke berörda oöversatta/särskilda poster och fem befintliga servervarningar. |
| Nontrinsic / android | Återstående 6 poster | Nyhets-, galax- och språkklassificeringstexter översatta. Komponenten är nu 106/106 översatt och har 0 fuzzy. Fem tidigare servervarningar kvarstår på komponentnivå; de sex nya enheterna har inga enhetsvarningar. |
| Nontrinsic / ios | Samtliga 106 strängar | De åtta återstående inställnings-, widget-, nyhets- och språkklassificeringstexterna översatta. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. |
| Tournant / glossary | Samtliga 1 sträng | Felaktig språkbenämning rättad från ”svenska” till ”engelska”, med bevarad `%s`-platshållare. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. |
| F-Droid Classic / privext | Samtliga 3 strängar | Enhetsägarens rubriker och bekräftelsedialog språkrättade. `%s`-platshållaren har bevarats utan det tidigare felplacerade blanksteget. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. |
| Feeder / F-Droid- och Play Store-metadata | Samtliga 3 strängar granskade | Huvudbeskrivningen språkrättad med korrekta termer för fjärrservrar, bilagelänkar, OPML-import/-export och ändringslogg. HTML-strukturen och GitHub-länken är bevarade. En ny, onödig tagg som först orsakade en kontrollvarning togs bort. Servern bekräftar 100 %, 0 fuzzy och 0 fallerande kontroller. |
| Sepia Squirt / glossary | Samtliga 5 strängar | Betalningsförkortningarna IBAN, EUR och CHF har bevarats; båda QR Code-posterna är översatta till ”QR-kod”. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. |
| Ampersand / notes | Samtliga 9 strängar | Anteckningsvyn, sökning, arkivering och borttagningsbekräftelse översatta. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. |
| Ampersand / filterqueries | Samtliga 10 strängar | Filterfrågor, redigering och borttagningsbekräftelse översatta med konsekvent fråge-terminologi. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. |
| Ampersand / resources | Samtliga 10 strängar | Resurssida för webbplats, blogg, wiki och kodförråd översatt. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. |
| Ampersand / lock och dashboard | 4 riktade rättningar | Rättade lösenordsinstruktion, knappimperativ, statusformulering och anslagstavleåtgärd. Berörda komponenter bekräftar 100 %, 0 fuzzy och 0 fallerande kontroller. |
| Ampersand / security | Samtliga 17 strängar | App-lås, biometri, lösenordsflöden, extern data och säkerhetsvarningen översatta. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. |
| Ampersand / analytics | Samtliga 24 strängar | Analysvy, datum, närvaro, perioder och fyra pluralsträngar översatta. `{{count}}` och svenska singular-/pluralformer är verifierade. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. |
| Ampersand / tag-management | Samtliga 29 strängar | Taggar för medlemmar, journal och resurser samt tre pluralsträngar översatta med bevarade `{{count}}` och `{{tagID}}`. Servern bekräftar 100 % och 0 fuzzy; två ospecificerade komponentvarningar kvarstår, medan API:ts enhetsnivå inte visar kontroller på de uppdaterade posterna. |
| Ampersand / systems | 5 återstående strängar | Färg, avatarform, listvisning, namnformat och statusöversikt för dissociativa tillstånd översatta med bevarade platshållare. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. |
| Ampersand / import-export | Samtliga 41 strängar | Importer, exporter, gamla säkerhetskopior, rapporter och Discord-ID översatta. Produktnamn, `ampdb`, JSON och versionsgränsen `< 0.2.0` är bevarade. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. |
| Ampersand / members | Samtliga 43 strängar | Medlemsvy, frontstatus, fält, taggar, journalposter och pluralform översatta. Platshållare och statusdatum är bevarade. Servern bekräftar 100 % och 0 fuzzy; en ospecificerad komponentvarning återstår. |
| Nitroxy / glossary | Samtliga 4 strängar | De internationella standardförkortningarna MOD och EAN är granskade och bevarade. Servern bekräftar 100 %, 0 ofärdiga, 0 fuzzy och 0 fallerande kontroller. |
- Meshy for Android / application (sv): release 26.09.12 (2026-09-12) verifierad; 155/155 översatta, 0 osäkra och 0 kontrollfel. Granskad med hunspell -d sv_SE; tekniska namn är bedömda.
- MediLog / core (sv): release v3.8.0 (2026-09-11) verifierad; 592/592 översatta, 0 osäkra och 1 teknisk kontroll för bevarad radbrytning i en kraschrapport. Granskad med hunspell -d sv_SE.
- F-Droid Build Status / strings.xml, app store metadata och glossary (sv): release 5.15.0 (2026-06-28) verifierad; 223/223 översatta, 0 osäkra och 0 kontrollfel. Danska reststrängar rättade och granskade med hunspell -d sv_SE.
- MintApps / basiskomponenten (sv): release 2.2.0 (2026-02-04) verifierad; 1963/1963 översatta, 0 osäkra och 24 tekniska kontrollträffar för facktermer/länkar. Granskad med hunspell -d sv_SE.
- LASK / lask (sv): release 0.9.0 (2025-03-28) verifierad; 342/342 översatta, 0 osäkra och 16 tekniska kontrollträffar. Granskad med hunspell -d sv_SE.
- Hades Revisited / hudbars (sv): release 0.20.2 (2026-02-16) verifierad; 3/3 översatta, 0 osäkra och 0 kontrollfel. Granskad med hunspell -d sv_SE.
- Hades Revisited / skins (sv): release 0.20.2 (2026-02-16) verifierad; 32/32 översatta, 0 osäkra och 2 tekniska kontrollträffar för plaggnamn. Granskad med hunspell -d sv_SE.
- Hades Revisited / itemshow (sv): release 0.20.2 (2026-02-16) verifierad; 21/21 översatta, 0 osäkra och 0 kontrollfel. Granskad med hunspell -d sv_SE.
- Hades Revisited / furniture (sv): release 0.20.2 (2026-02-16) verifierad; 21/21 översatta, 0 osäkra och 0 kontrollfel. Granskad med hunspell -d sv_SE.
- Hades Revisited / fences (sv): release 0.20.2 (2026-02-16) verifierad; 22/22 översatta, 0 osäkra och 0 kontrollfel. Granskad med hunspell -d sv_SE.
- Hades Revisited / windows (sv): release 0.20.2 (2026-02-16) verifierad; 23/23 översatta, 0 osäkra och 0 kontrollfel. Granskad med hunspell -d sv_SE.
- Hades Revisited / simulation (sv): release 0.20.2 (2026-02-16) verifierad; 47/47 översatta, 0 osäkra och 0 kontrollfel. Granskad med hunspell -d sv_SE.
- Hades Revisited / orienteering (sv): release 0.20.2 (2026-02-16) verifierad; 42/42 översatta, 0 osäkra och 1 teknisk kontroll för verktygsnamnet Triangulator. Granskad med hunspell -d sv_SE.
- Hades Revisited / hades_tt (sv): release 0.20.2 (2026-02-16) verifierad; 22/22 översatta, 0 osäkra och 0 kontrollfel. Granskad med hunspell -d sv_SE.
- Hades Revisited / glossary (sv): release 0.20.2 (2026-02-16) verifierad; 29/29 översatta, 0 osäkra och 0 kontrollfel. Granskad med hunspell -d sv_SE.

- Hades Revisited / hades_stairs (sv): release 0.20.2 (2026-02-16) verifierad; 938/938 översatta, 0 osäkra och 26 tekniska kontrollträffar för fiktiva/geologiska materialnamn. Fullständigt granskad med hunspell -d sv_SE; äldre språkfel som ”stensten” och ”kullrad” har rättats.

- Imagepipe / app-strings (sv): release v0.78 (2026-06-07) verifierad; 308/308 översatta, 0 osäkra och 0 kontrollfel. Behörigheter, bildbehandling, Exif/GPS-fält, licensvillkor och länkar har granskats med hunspell -d sv_SE.

- Tiny Weather Forecast Germany / F-Droid-metadata (sv): release 0.63.4 (2026-07-24) verifierad; 65/65 översatta, 0 osäkra och 15 tekniska kontrollträffar för historiska ändringsloggar/produktnamn. Fullständigt granskad med hunspell -d sv_SE.

- Tiny Weather Forecast Germany / app-strings (sv): release 0.63.4 (2026-07-24) verifierad; 535/535 översatta, 0 osäkra och 4 tekniska kontrollträffar för HTTPS, Logcat och återkommande facktermer. Fullständigt granskad med hunspell -d sv_SE; äldre fel i molnhöjdstexter rättade.

- Doable / values (sv): release v1.17.2 (2024-10-20) verifierad; 503/503 översatta, 0 osäkra och 16 automatiska tekniska/dubblettkontroller för bland annat WebDAV, APK och F-Droid. Fullständigt granskat med hunspell -d sv_SE; platshållare och ICU-pluraler är bevarade.

- Sriracha / sriracha (sv): release v2.1.2 (2026-09-13) verifierad; 582/582 översatta, 0 osäkra och 29 automatiska dubblettkontroller för korrekta återanvända termer. Fullständigt granskat med hunspell -d sv_SE; pluraler, formatparametrar och forumsyntax är bevarade.

- Mitra Web / main (sv): release v5.10.0 (2026-08-24) verifierad; 421/421 översatta, 0 osäkra och 8 automatiska dubblettkontroller för korrekta återanvända termer. Fullständigt granskat med hunspell -d sv_SE utan återstående träffar; variabler och pluralformat är bevarade.

- flohmarkt / backend (sv): release 0.20.1 (2026-07-13) verifierad; 623/623 översatta, 0 osäkra och 14 tekniska/återanvändningskontroller. Fullständigt granskat med hunspell -d sv_SE och msgfmt -c; åtta äldre stav- och sakfel har rättats.

- Lazarr! / lzr_infobooks (sv): release 2.2.3 (2026-06-06) verifierad; 234/234 översatta, 0 osäkra och 4 automatiska tekniska kontroller. Granskad med hunspell -d sv_SE; tangentmarkörer, kommandon och filnamn är bevarade.

- Lazarr! / lzr_core (sv): release 2.2.3 (2026-06-06) verifierad; 51/51 översatta, 0 osäkra och 1 automatisk dubblettkontroll för Sand. Fullständigt granskat med hunspell -d sv_SE; äldre materialnamn och sammansättningar rättade.

- OBS Master: **potentiellt obsolet**. Senaste verifierade release 0.6.3 (2023-11-16) är äldre än två år; projektet har hoppats över.

- Hades Revisited / hades_core (sv): release 0.20.2 (2026-02-16) verifierad; 214/214 översatta, 0 osäkra och 7 spelterm-/teknikkontroller. Copper Ingot rättad till Koppartacka; granskad med hunspell -d sv_SE.

- Hades Revisited / hades_info (sv): release 0.20.2 (2026-02-16) verifierad; 133/133 översatta, 0 osäkra och 5 tekniska/återanvändningskontroller. Fullständigt granskat med hunspell -d sv_SE och msgfmt -c.

- Hades Revisited / hades_carpets (sv): release 0.20.2 (2026-02-16) verifierad; 22/22 översatta, 0 osäkra och 0 kontrollfel. Granskad med hunspell -d sv_SE.

- GeoWeather / geoweather (sv): release v3.1.3 (2026-09-10) verifierad; 290/290 översatta, 0 osäkra och 4 automatiska kontroller för två korrekta dubbletter samt standardbeteckningarna Fahrenheit (°F) och mmHg. Fullständigt granskat med hunspell -d sv_SE; produktnamn, format och tekniska termer har bedömts.

- Clock / clock (sv): release 2.31 (2026-06-28) verifierad; 675/675 översatta, 0 osäkra och 23 automatiska dubblett-/terminologikontroller för korrekta återanvända termer, standardnamn och geografiska namn. Fullständigt granskat med hunspell -d sv_SE; Android-platshållare, pluraler, HTML och radbrytningar är bevarade.

- HeliBoard / heliboard (sv): release v4.1 (2026-08-30) verifierad; 552/552 översatta, 0 osäkra och 11 automatiska kontroller för korrekta layout-/språknamn och konsekventa språkbytesformuleringar. Fullständigt granskat med hunspell -d sv_SE; HTML, länkar, parametrar och radbrytningar är bevarade.

- Weather: potentiellt obsolet. Senaste verifierade release 3.21-pre1 (2023-04-12), äldre än två år; projektet hoppas över.

- GymRoutines / app-string-resources (sv): release v0.1.1 (2025-04-18) verifierad; 84/84 översatta, 0 osäkra och 0 kontrollfel. Granskad med hunspell -d sv_SE utan träffar.

- SCEE / app (sv): release v63.4 (2026-08-05) verifierad; 663/663 översatta, 0 osäkra och 15 automatiska tekniska/dubblettkontroller för korrekta taggar, standardförkortningar och återanvända formuleringar. Fullständigt granskat med hunspell -d sv_SE; tre språkfel rättade.

- Träwelling / traewelling (sv): release 2026.09.12 (2026-09-12) verifierad; 1444/1444 översatta, 0 osäkra och 94 automatiska dubblett-/tekniska kontroller. Fullständigt granskat med hunspell -d sv_SE; sex faktiska språkfel rättade och format, variabler, pluraler samt länkar bevarade.

- Conversations: potentiellt obsolet enligt releasekriteriet. Ingen offentlig release inom två år kunde verifieras 2026-09-13; projektet hoppas över tills en sådan release kan verifieras.

- PartyGames: potentiellt obsolet. Senaste verifierade release 2.0.0 (2024-01-08), äldre än två år; projektet hoppas över.

- AutoTabOpener: potentiellt obsolet. Senaste verifierade release v2.10 (2022-10-09), äldre än två år; projektet hoppas över.

- FOSS Browser / strings (sv): release v23 (2026-06-22) verifierad; 155/158 översatta, 1 osäker och 0 kontrollfel. Tre rättningar granskade med hunspell -d sv_SE, men Weblate returnerade 403 eftersom komponenten är låst; inga ändringar kunde publiceras.

- Jellybean / jellybean (sv): release 0.5.1 (2026-03-03) verifierad; 109/109 översatta, 0 osäkra och 0 kontrollfel. Granskad med hunspell -d sv_SE; produktnamn och facktermer bedömda.

- alligator-gozaimasu / app (sv): release 0.32 (2026-07-27) verifierad; 80/80 översatta, 0 osäkra och 0 kontrollfel. Granskad med hunspell -d sv_SE; egennamn, licens- och ljudformatstermer bedömda.

- FTPClient / strings (sv): release 3.2.0 (2026-08-23) verifierad; 120/120 översatta, 0 osäkra och 0 kontrollfel. Granskad med hunspell -d sv_SE; ”SSH-äktheter” rättat till ”SSH-autentiseringar”.

- Libre Menu Editor / libre-menu-editor (sv): release v1.10.5 (2026-08-09) verifierad; 117/117 översatta, 0 osäkra och 0 kontrollfel. Granskad med hunspell -d sv_SE utan träffar.

- Hurry Curry / game (sv): release v3.1.1 (2026-04-30) verifierad; 387/387 översatta, 0 osäkra och 15 kontrollfel. Granskad med hunspell -d sv_SE; fyra språkfel har rättats. Återstående kontroller gäller egennamn, grafiktermer och avsiktliga skiljeteckensskillnader.

- Hurry Curry / website (sv): release v3.1.1 (2026-04-30) verifierad; 56/56 översatta, 0 osäkra och 0 kontrollfel. Granskad med hunspell -d sv_SE; produktnamn och tekniktermer bedömda.

- JetBird / app (sv): release v1.8.10 (2026-09-04) verifierad; 182/182 översatta, 0 osäkra och 0 kontrollfel. Granskad med hunspell -d sv_SE; sju språk- och terminologifel i nätverks- och ruttinställningar har rättats.

- Readeck / application (sv): release 0.23.2 (2026-08-31) verifierad; 643/643 översatta, 0 osäkra och 0 kontrollfel. Granskad med hunspell -d sv_SE; sex språkfel har rättats, bland annat produktnamn, webbläsare och delningsåtgärd.

- FediPhoto-Lineage / description (sv): release v8.0 (2025-08-26) verifierad; 30/30 översatta, 0 osäkra och 1 kontrollfel. Granskad med hunspell -d sv_SE; kontrollen gäller en avsiktligt avvikande formulering i ändringsloggen.

- FediPhoto-Lineage / strings (sv): release v8.0 (2025-08-26) verifierad; 252/252 översatta, 0 osäkra och 2 kontrollfel. Granskad med hunspell -d sv_SE; 162 saknade eller felaktiga strängar har översatts eller rättats. Kontrollerna gäller samma avsiktliga term i separata etiketter.

- Ampersand: potentiellt obsolet enligt releasekriteriet. Ingen offentlig release kunde verifieras 2026-09-13; projektet hoppas över tills en sådan release kan verifieras.

- Postmill / messages (sv): release v2.2.3 (2026-07-20) verifierad; 648/648 översatta, 0 osäkra och 3 kontrollfel. Granskad med hunspell -d sv_SE; tolv språk- och terminologifel har rättats. Kontrollerna gäller avsiktliga facktermer och rollnamn.

- Turntable / turntable (sv): release v0.5.1 (2025-12-26) verifierad; 139/139 översatta, 0 osäkra och 0 kontrollfel. Granskad med hunspell -d sv_SE; två språkfel har rättats.

- Archives / archives (sv): release v0.6.0 (2025-07-01) verifierad; 72/72 översatta, 0 osäkra och 0 kontrollfel. Granskad med hunspell -d sv_SE; åtta språk- och terminologifel har rättats.

- Calligraphy / calligraphy (sv): release v1.3.0 (2026-05-18) verifierad; 40/40 översatta, 0 osäkra och 0 kontrollfel. Granskad med hunspell -d sv_SE; sju språk- och UI-fel har rättats.

- Collision / collision (sv): release v3.14.1 (2026-05-07) verifierad; 45/45 översatta, 0 osäkra och 0 kontrollfel. Granskad med hunspell -d sv_SE; tolv språk-, sammansättnings- och UI-fel har rättats.

- Endurain / nav, footer och userProfile (sv): release v0.19.2 (2026-09-02) verifierad; 84/84 översatta, 0 osäkra. Fyra språkfel har identifierats vid granskning med hunspell -d sv_SE via API-lästa måltexter. Weblate returnerar 403 både för skrivning och export; inga ändringar kunde publiceras och spegelkopia väntar på åtkomst.

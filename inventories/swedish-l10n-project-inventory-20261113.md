# Inventering av svensk lokalisering

Kontrollerad 13 november 2026. Listan omfattar 250 aktiva öppenkällkodsprojekt med verifierad GitHub-utgåva från de senaste 24 månaderna. GIMP, GNOME, KDE, Inkscape och projekt med tydlig tidigare arkivering har filtrerats bort. Dokumentationsprojekt ligger längst ned.

Statusen ”ingen svensk resurs i Git” är inte ett påstående om att svenska saknas upstream. Externa plattformar som Crowdin, Weblate och Transifex måste kontrolleras separat innan översättningsarbete startar. Sökningen omfattar språkvarianterna `sv`, `sv_SE`, `sv-SE` och `svSE`. ”Senaste bidrag” är den senast offentligt synliga committen för den första relevanta svenska resursen och kan vara en robot.

Prioritet 1 betyder bred slutanvändarnytta, 2 produktivitets- och samarbetsprogram, 3 drift och utveckling samt 4 spel eller specialiserade verktyg. Inom varje prioritet är projekten sorterade alfabetiskt.

| Prio | Projekt | Senaste utgåva | Svensk status i Git | Senaste synliga svenska bidrag |
| --- | --- | --- | --- | --- |
| 1 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | 2026-10-08 | Svensk resurs: `core/assets/bundles/bundle_sv.properties`; 13 server- och modbläddrarposter inskickade som [PR #12833](https://github.com/Anuken/Mindustry/pull/12833), väntar på granskning | 2026-09-11, Github Actions |
| 1 | [AppFlowy-IO/AppFlowy](https://github.com/AppFlowy-IO/AppFlowy) | 2026-11-02 | Svensk resurs: `frontend/resources/translations/sv-SE.json`; 178 kontextgranskade UI-poster för sidtyper, färger, datum, inläsning, Sök och ersätt, aviseringar, favoritsidor, filåterkoppling, snabbanteckningar, redigeraren, titelraden, snabbinfogningsmenyn samt arbetsytans åtkomst-, godkännande- och inbjudningsflöden är inskickade som [PR #9132](https://github.com/AppFlowy-IO/AppFlowy/pull/9132), väntar på granskning | 2025-05-12, FakhriAzzouz |
| 1 | [audacity/audacity](https://github.com/audacity/audacity) | 2026-11-02 | Svensk resurs: `au3/locale/sv.po` | 2024-10-15, Igor |
| 1 | [brave/brave-browser](https://github.com/brave/brave-browser) | 2026-11-12 | Transifex `brave_en`: svenska 99 %; ingen svensk resurs i Git | Senaste projektaktivitet: 2025-03-18 |
| 1 | [BrowserWorks/waterfox](https://github.com/BrowserWorks/waterfox) | 2026-11-07 | Svensk resurs: `browser/extensions/newtab/webext-glue/locales/sv-SE` | 2026-06-14, Maxx Crawford |
| 1 | [darktable-org/darktable](https://github.com/darktable-org/darktable) | 2026-10-04 | Svensk resurs: `po/sv.po`; verifierad komplett den 13 november: 6 732 översatta, 0 oöversatta och 0 luddiga | 2026-11-08, Philipp Lutz |
| 1 | [element-hq/element-x-android](https://github.com/element-hq/element-x-android) | 2026-11-06 | Ingen svensk resurs i aktuella `develop`; den tidigare sökvägsträffen kunde inte återskapas 2026-11-13 | Ej offentligt fastställt |
| 1 | [element-hq/element-x-ios](https://github.com/element-hq/element-x-ios) | 2026-11-05 | Svensk resurs: `ElementX/Resources/Localizations/sv.lproj` | 2026-11-09, Element CI |
| 1 | [elementary/os](https://github.com/elementary/os) | 2025-12-11 | elementary Weblate: 22 komponenter helt översatta; Settings har 1 svensk post som behöver redigeras (`accent color` → `Accentfärg`) | 2026-10-19, yeager |
| 1 | [Floorp-Projects/Floorp](https://github.com/Floorp-Projects/Floorp) | 2026-11-13 | Svensk resurs: `browser-features/pages-aboutDialog/src/lib/i18n/locales/sv-SE.json`; Om-dialogen verifierad komplett: 30 av 30 nycklar | 2026-11-13, Ryosuke Asano |
| 1 | [FossifyOrg/Calendar](https://github.com/FossifyOrg/Calendar) | 2026-11-07 | Svensk resurs: `app/src/main/res/values-sv/strings.xml`; 260 av 260 översättningsbara nycklar täcks. Två FAQ-rättningar är inskickade som [PR #1425](https://github.com/FossifyOrg/Calendar/pull/1425) | 2026-11-04, fossifybot[bot] |
| 1 | [FossifyOrg/Clock](https://github.com/FossifyOrg/Clock) | 2026-01-30 | Svensk resurs: `app/src/main/res/values-sv`; 50 av 50 översättningsbara resurser täcks. Fem UI-rättningar inskickade som [PR #538](https://github.com/FossifyOrg/Clock/pull/538); relevanta projektkontroller är godkända | 2025-05-29, P.O |
| 1 | [FossifyOrg/Contacts](https://github.com/FossifyOrg/Contacts) | 2026-01-30 | Svensk resurs: `app/src/main/res/values-sv`; 79 av 79 översättningsbara resurser täcks. FAQ-rättning inskickad som [PR #647](https://github.com/FossifyOrg/Contacts/pull/647) | 2026-01-26, Naveen Singh |
| 1 | [FossifyOrg/File-Manager](https://github.com/FossifyOrg/File-Manager) | 2026-11-07 | Svensk resurs: `app/src/main/res/values-sv`; 44 av 44 resurser täcks. Sju UI-rättningar inskickade som [PR #525](https://github.com/FossifyOrg/File-Manager/pull/525) | 2024-02-11, Vsnmrn |
| 1 | [FossifyOrg/Gallery](https://github.com/FossifyOrg/Gallery) | 2026-11-07 | Svensk resurs: `app/src/main/res/values-sv` | 2026-09-10, Daniel Nylander |
| 1 | [FossifyOrg/Launcher](https://github.com/FossifyOrg/Launcher) | 2026-02-17 | Svensk resurs: `app/src/main/res/values-sv`; 19 av 19 nycklar täcks. Fyra UI-rättningar inskickade som [PR #479](https://github.com/FossifyOrg/Launcher/pull/479) | 2026-02-11, en2sv |
| 1 | [FossifyOrg/Messages](https://github.com/FossifyOrg/Messages) | 2026-10-24 | Svensk resurs: `app/src/main/res/values-sv` | 2026-10-16, en2sv |
| 1 | [FossifyOrg/Music-Player](https://github.com/FossifyOrg/Music-Player) | 2026-10-24 | Svensk resurs: `app/src/main/res/values-sv` | 2025-05-18, P.O |
| 1 | [FossifyOrg/Notes](https://github.com/FossifyOrg/Notes) | 2026-01-30 | Svensk resurs: `app/src/main/res/values-sv` | 2025-07-13, en2sv |
| 1 | [FossifyOrg/Paint](https://github.com/FossifyOrg/Paint) | 2026-01-30 | Svensk resurs: `app/src/main/res/values-sv` | 2025-11-24, en2sv |
| 1 | [FossifyOrg/Phone](https://github.com/FossifyOrg/Phone) | 2026-02-03 | Svensk resurs: `app/src/main/res/values-sv`; 77 av 77 översättningsbara nycklar täcks. FAQ-stavfel inskickat som [PR #943](https://github.com/FossifyOrg/Phone/pull/943) | 2025-09-28, en2sv |
| 1 | [FossifyOrg/Voice-Recorder](https://github.com/FossifyOrg/Voice-Recorder) | 2026-10-24 | Svensk resurs: `app/src/main/res/values-sv` | 2026-02-14, en2sv |
| 1 | [godotengine/godot](https://github.com/godotengine/godot) | 2026-08-18 | Svensk resurs: `editor/translations/editor/sv.po` | 2026-11-12, Hugo Locurcio |
| 1 | [Heroic-Games-Launcher/HeroicGamesLauncher](https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher) | 2026-10-15 | Svensk resurs: `public/locales/sv` | 2026-11-08, Weblate (bot) |
| 1 | [ImranR98/Obtainium](https://github.com/ImranR98/Obtainium) | 2026-11-01 | Svensk resurs: `assets/translations/sv.json` | 2026-11-01, ImranR |
| 1 | [krille-chan/fluffychat](https://github.com/krille-chan/fluffychat) | 2026-11-06 | Svensk Flutter-resurs `lib/l10n/intl_sv.arb`; 57 saknade call- och mediatexter är färdiggranskade och pushade till fork, men PR-behörighet nekades | 2020-12-18, Christian Pauly |
| 1 | [laurent22/joplin](https://github.com/laurent22/joplin) | 2026-10-28 | Resursträff kräver UI-kontroll: `Assets/TinyMCE/langs/sv_SE.js` | 2020-11-05, Laurent Cozic |
| 1 | [LibreCAD/LibreCAD](https://github.com/LibreCAD/LibreCAD) | 2026-10-17 | Svensk resurs: `librecad/support/library/elektro/source/sv.dxf` | 2026-09-05, Dongxu Li |
| 1 | [localsend/localsend](https://github.com/localsend/localsend) | 2026-08-21 | Svensk resurs: `app/assets/i18n/_missing_translations_sv.json`; tre aktuella UI-strängar inskickade som [PR #3706](https://github.com/localsend/localsend/pull/3706), väntar på granskning | 2026-08-10, Tien Do Nam |
| 1 | [luanti-org/luanti](https://github.com/luanti-org/luanti) | 2026-10-29 | Motorgränssnittet förvaltas i Weblate; 26 inbyggda svenska kommando- och serverposter är inskickade som [PR #17754](https://github.com/luanti-org/luanti/pull/17754), väntar på granskning | 2026-08-14, Jonatan Nyberg |
| 1 | [mozilla-mobile/firefox-ios](https://github.com/mozilla-mobile/firefox-ios) | 2026-11-06 | Svensk resurs: `firefox-ios/Client/sv.lproj` | 2026-09-10, github-actions[bot] |
| 1 | [music-assistant/server](https://github.com/music-assistant/server) | 2026-10-30 | Svensk resurs: `music_assistant/translations/sv_SE.json` | 2026-07-21, github-actions[bot] |
| 1 | [obsidianmd/obsidian-releases](https://github.com/obsidianmd/obsidian-releases) | 2026-11-12 | Svenska är komplett i det separata, officiella arkivet [obsidian-translations](https://github.com/obsidianmd/obsidian-translations): app, webb och hjälp | Appen uppdaterades senast av lishid 2026-11-03; senaste svenska bidraget är ReineW 2026-07-15 |
| 1 | [OpenBoard-org/OpenBoard](https://github.com/OpenBoard-org/OpenBoard) | 2026-03-30 | Svensk resurs: `resources/i18n/OpenBoard_sv.ts`; webbläsar- och hämtningsbatch inskickad som [PR #1581](https://github.com/OpenBoard-org/OpenBoard/pull/1581), huvudfönsterverktyg som [PR #1582](https://github.com/OpenBoard-org/OpenBoard/pull/1582) | 2026-03-23, Clément Fauconnier |
| 1 | [OpenMW/openmw](https://github.com/OpenMW/openmw) | 2026-06-19 | Svensk resurs: `files/data-mw/l10n/Calendar/sv.yaml` | 2024-05-18, Alexei Kotov |
| 1 | [OpenRCT2/OpenRCT2](https://github.com/OpenRCT2/OpenRCT2) | 2026-11-01 | Svensk resurs förvaltas i [`OpenRCT2/Localisation`](https://github.com/OpenRCT2/Localisation); 50 panel-, status-, färg- och formatposter är inskickade som [PR #3571](https://github.com/OpenRCT2/Localisation/pull/3571), väntar på granskning | 2026-09-13, OpenRCT2 git bot |
| 1 | [OpenShot/openshot-qt](https://github.com/OpenShot/openshot-qt) | 2026-11-02 | Svensk resurs: `src/language/OpenShot_sv.qm` | 2026-07-25, Jonathan Thomas |
| 1 | [OpenTTD/OpenTTD](https://github.com/OpenTTD/OpenTTD) | 2026-04-04 | Svenska förvaltas i officiella WebTranslator: 4 792 aktuella, 9 inaktuella och 6 saknade; lokal 15-posters delta klar | Senaste svenska översättare är inte offentligt angiven; skrivrätt för yeager nekades 2026-11-13 |
| 1 | [organicmaps/organicmaps](https://github.com/organicmaps/organicmaps) | 2026-11-11 | Resursträff kräver UI-kontroll | 2026-11-11, yanatalia |
| 1 | [PintaProject/Pinta](https://github.com/PintaProject/Pinta) | 2026-04-02 | Svensk resurs: `po/sv.po` | 2026-10-18, Åke Engelbrektson |
| 1 | [PrismLauncher/PrismLauncher](https://github.com/PrismLauncher/PrismLauncher) | 2026-09-28 | Svenska finns i officiella `PrismLauncher/Translations`; 3 lokalt färdiggranskade poster väntar på Weblate-inskick | Senaste källsynkning: PrismAutomata 2026-11-12 |
| 1 | [prusa3d/PrusaSlicer](https://github.com/prusa3d/PrusaSlicer) | 2026-11-02 | Svensk resurs: `resources/localization/wx_locale/sv.po` | 2021-12-21, YuSanka |
| 1 | [Ranchero-Software/NetNewsWire](https://github.com/Ranchero-Software/NetNewsWire) | 2026-10-20 | Ingen svensk lokal i de använda Xcode-katalogerna; ingen extern plattform funnen. Ny lokal kräver först diskussion enligt CONTRIBUTING.md | Ej offentligt fastställt |
| 1 | [session-foundation/session-desktop](https://github.com/session-foundation/session-desktop) | 2026-11-13 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 1 | [signalapp/Signal-Android](https://github.com/signalapp/Signal-Android) | 2026-11-09 | Svensk resurs: `app/src/main/res/values-sv` | 2026-11-11, Greyson Parrelli |
| 1 | [signalapp/Signal-Desktop](https://github.com/signalapp/Signal-Desktop) | 2026-11-11 | Svensk resurs: `_locales/sv` | 2026-11-11, Fedor Indutny |
| 1 | [standardnotes/app](https://github.com/standardnotes/app) | 2026-10-23 | Ny JSON-baserad web- och mobillokalisering, men svenska saknas; ingen extern plattform funnen och funktionen är under intern utrullning | Ej offentligt fastställt |
| 1 | [TeamAmaze/AmazeFileManager](https://github.com/TeamAmaze/AmazeFileManager) | 2026-10-15 | Svenska förvaltas i Transifex: 72 % och aktivitet 2026-11-09. Git-kopian saknar 216 av 723 aktuella källnycklar och är inte säker importkälla. | Senaste publikt synliga Git-ändring: 2026-01-05, Raymond Lai; aktuell Transifex-översättare ej offentligt fastställd |
| 1 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | 2026-11-10 | Svensk resurs: `app/src/main/res/values-sv` | 2026-11-02, TobiGr |
| 1 | [thunderbird/thunderbird-android](https://github.com/thunderbird/thunderbird-android) | 2026-11-10 | Svensk resurs: `app-common/src/main/res/values-sv` | 2025-11-05, Hosted Weblate |
| 1 | [toeverything/AFFiNE](https://github.com/toeverything/AFFiNE) | 2026-08-18 | Svensk resurs: `packages/frontend/i18n/src/resources/sv-SE.json` | 2026-08-10, DarkSky |
| 1 | [tuskyapp/Tusky](https://github.com/tuskyapp/Tusky) | 2025-05-17 | Svensk resurs: `app/src/main/res/values-sv` | 2025-05-08, Anonymous |
| 1 | [tutao/tutanota](https://github.com/tutao/tutanota) | 2026-11-10 | Resursträff kräver UI-kontroll | 2023-11-03, arm |
| 1 | [Ultimaker/Cura](https://github.com/Ultimaker/Cura) | 2026-11-05 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 1 | [wireapp/wire-desktop](https://github.com/wireapp/wire-desktop) | 2026-11-02 | Svensk resurs: `electron/src/locale/sv-SE.json` | 2026-10-08, Crowdin Bot |
| 1 | [xournalpp/xournalpp](https://github.com/xournalpp/xournalpp) | 2026-09-26 | Svensk resurs: `po/sv.po` | 2026-09-23, github-actions[bot] |
| 1 | [Zettlr/Zettlr](https://github.com/Zettlr/Zettlr) | 2026-10-25 | Svensk resurs: `static/csl-locales/locales-sv-SE.xml` | 2026-06-14, GitHub Action |
| 2 | [1Panel-dev/1Panel](https://github.com/1Panel-dev/1Panel) | 2026-11-12 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [AdguardTeam/AdGuardHome](https://github.com/AdguardTeam/AdGuardHome) | 2026-11-03 | Svensk resurs: `client/src/__locales-services/sv.json` | 2026-02-09, Eugene Burkov |
| 2 | [akaunting/akaunting](https://github.com/akaunting/akaunting) | 2026-11-11 | Svensk resurs: `resources/lang/sv-SE` | 2026-09-27, Akaunting |
| 2 | [appsmithorg/appsmith](https://github.com/appsmithorg/appsmith) | 2026-11-12 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [aristocratos/btop](https://github.com/aristocratos/btop) | 2026-10-25 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [audacious-media-player/audacious](https://github.com/audacious-media-player/audacious) | 2026-10-19 | Svensk resurs: `po/sv.po` | 2026-10-19, Thomas Lange |
| 2 | [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | 2025-02-09 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [bagisto/bagisto](https://github.com/bagisto/bagisto) | 2026-11-06 | Svensk resurs: `public/themes/admin/default/build/assets/sv.es-BfPUYcV1.js` | 2026-07-07, Devansh Bawari |
| 2 | [baserow/baserow](https://github.com/baserow/baserow) | 2026-11-11 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [bevyengine/bevy](https://github.com/bevyengine/bevy) | 2026-10-28 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [bitfireAT/davx5-ose](https://github.com/bitfireAT/davx5-ose) | 2026-10-15 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [BookStackApp/BookStack](https://github.com/BookStackApp/BookStack) | 2026-11-11 | Svensk resurs: `lang/sv` | 2026-09-29, Crowdin Bot |
| 2 | [bookwyrm-social/bookwyrm](https://github.com/bookwyrm-social/bookwyrm) | 2026-10-29 | Svensk resurs: `locale/sv_SE` | 2026-10-21, Mouse Reeve |
| 2 | [Budibase/budibase](https://github.com/Budibase/budibase) | 2026-11-10 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [calcom/cal.diy](https://github.com/calcom/cal.diy) | 2026-03-01 | Resursträff kräver UI-kontroll | 2023-05-23, jemiluv8 |
| 2 | [caprover/caprover](https://github.com/caprover/caprover) | 2026-11-03 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [cinnyapp/cinny](https://github.com/cinnyapp/cinny) | 2026-10-25 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [cloudreve/cloudreve](https://github.com/cloudreve/cloudreve) | 2026-09-18 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [coollabsio/coolify](https://github.com/coollabsio/coolify) | 2026-11-10 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [directus/directus](https://github.com/directus/directus) | 2026-11-04 | Svensk resurs: `app/src/lang/translations/sv-SE.yaml` | 2026-10-27, Rijk van Zanten |
| 2 | [documenso/documenso](https://github.com/documenso/documenso) | 2026-11-13 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [dokku/dokku](https://github.com/dokku/dokku) | 2026-10-30 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [domoticz/domoticz](https://github.com/domoticz/domoticz) | 2026-10-01 | Svensk resurs: `www/i18n/domoticz-sv.json.gz` | 2026-04-23, GizMoCuz |
| 2 | [drawpile/Drawpile](https://github.com/drawpile/Drawpile) | 2026-10-21 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [esphome/esphome](https://github.com/esphome/esphome) | 2026-11-02 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [Etar-Group/Etar-Calendar](https://github.com/Etar-Group/Etar-Calendar) | 2026-07-27 | Svensk resurs: `app/src/main/res/values-sv` | 2026-05-19, Zhouzhishi808 |
| 2 | [falkTX/Carla](https://github.com/falkTX/Carla) | 2025-07-31 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [ferdium/ferdium-app](https://github.com/ferdium/ferdium-app) | 2026-09-07 | Svensk resurs: `src/i18n/locales/sv.json` | 2025-03-08, ferdium-bot |
| 2 | [filegator/filegator](https://github.com/filegator/filegator) | 2026-11-04 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [firefly-iii/firefly-iii](https://github.com/firefly-iii/firefly-iii) | 2026-10-11 | Resursträff kräver UI-kontroll: `public/v1/js/lib/moment/sv_SE.js` | 2022-10-08, James Cole |
| 2 | [flarum/flarum](https://github.com/flarum/flarum) | 2026-10-09 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [floccusaddon/floccus](https://github.com/floccusaddon/floccus) | 2026-11-08 | Svensk resurs: `_locales/sv` | 2026-11-01, transifex-integration[bot] |
| 2 | [FontManager/font-manager](https://github.com/FontManager/font-manager) | 2026-11-05 | Svensk resurs: `help/sv` | 2022-01-13, Weblate (bot) |
| 2 | [formbricks/formbricks](https://github.com/formbricks/formbricks) | 2026-11-13 | Svensk resurs: `apps/web/locales/sv-SE.json` | 2026-11-12, Tiago |
| 2 | [FOSSBilling/FOSSBilling](https://github.com/FOSSBilling/FOSSBilling) | 2026-10-23 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [FreshRSS/FreshRSS](https://github.com/FreshRSS/FreshRSS) | 2026-10-21 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [friendica/friendica](https://github.com/friendica/friendica) | 2026-05-21 | Svensk resurs: `view/lang/sv` | 2026-11-11, Tobias Diekershoff |
| 2 | [gaphor/gaphor](https://github.com/gaphor/gaphor) | 2026-05-02 | Svensk resurs: `po/sv.po` | 2026-04-07, Dan Yeaw |
| 2 | [getfider/fider](https://github.com/getfider/fider) | 2026-11-03 | Svensk resurs: `locale/sv-SE` | 2026-10-14, Kevin Papst |
| 2 | [getgrav/grav](https://github.com/getgrav/grav) | 2026-11-11 | Svensk resurs: `system/languages/sv.yaml` | 2026-03-31, Andy Miller |
| 2 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | 2026-11-11 | Svensk resurs: `public/locales/sv` | 2026-11-11, github-actions[bot] |
| 2 | [getumbrel/umbrel](https://github.com/getumbrel/umbrel) | 2026-11-01 | Svensk resurs: `packages/ui/public/locales/sv.json` | 2026-11-03, github-actions[bot] |
| 2 | [ghostfolio/ghostfolio](https://github.com/ghostfolio/ghostfolio) | 2026-11-07 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [glpi-project/glpi](https://github.com/glpi-project/glpi) | 2026-11-12 | Svensk resurs: `locales/sv_SE.po` | 2026-11-12, Johan Cwiklinski |
| 2 | [gotify/server](https://github.com/gotify/server) | 2026-09-15 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [gristlabs/grist-core](https://github.com/gristlabs/grist-core) | 2026-10-29 | Svensk resurs: `assets/locales/sv.client.json` | 2026-11-09, Martin Harari Thuresson |
| 2 | [grocy/grocy](https://github.com/grocy/grocy) | 2026-09-04 | Svensk resurs: `localization/sv_SE` | 2026-09-04, Bernd Bestel |
| 2 | [homarr-labs/homarr](https://github.com/homarr-labs/homarr) | 2026-11-06 | Svensk resurs: `packages/translation/src/lang/sv.json` | 2026-11-13, homarr-crowdin[bot] |
| 2 | [humhub/humhub](https://github.com/humhub/humhub) | 2026-11-09 | Svensk resurs: `protected/humhub/messages/sv` | 2026-10-06, HumHub Translations |
| 2 | [invoke-ai/InvokeAI](https://github.com/invoke-ai/InvokeAI) | 2026-11-03 | Svensk resurs: `invokeai/frontend/webv1/public/locales/sv.json` | 2026-09-29, Josh Corbett |
| 2 | [jitsi/jitsi-meet](https://github.com/jitsi/jitsi-meet) | 2026-09-14 | Svensk resurs: `lang/main-sv.json` | 2026-11-12, Saúl Ibarra Corretgé |
| 2 | [joomla/joomla-cms](https://github.com/joomla/joomla-cms) | 2026-10-13 | Svensk resurs: `installation/language/sv-SE` | 2026-11-12, joomla-translation-bot |
| 2 | [k3s-io/k3s](https://github.com/k3s-io/k3s) | 2026-11-03 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [karakeep-app/karakeep](https://github.com/karakeep-app/karakeep) | 2026-10-22 | Svensk resurs: `apps/mobile/lib/i18n/locales/sv.json` | 2026-11-08, Mohamed Bassem |
| 2 | [keybase/client](https://github.com/keybase/client) | 2026-06-03 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [KiCad/kicad-source-mirror](https://github.com/KiCad/kicad-source-mirror) | 2026-11-06 | Svensk resurs: `thirdparty/sentry-native/external/breakpad/src/client/mac/sender/sv.lproj` | 2022-04-02, Mark Roszko |
| 2 | [Kong/insomnia](https://github.com/Kong/insomnia) | 2026-10-29 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [koreader/koreader](https://github.com/koreader/koreader) | 2026-08-01 | Svensk resurs: `frontend/ui/data/keyboardlayouts/sv_keyboard.lua` | 2024-09-16, NiLuJe |
| 2 | [lapce/lapce](https://github.com/lapce/lapce) | 2026-01-21 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [LemmyNet/lemmy](https://github.com/LemmyNet/lemmy) | 2026-10-26 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [linkwarden/linkwarden](https://github.com/linkwarden/linkwarden) | 2026-11-10 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [lissy93/dashy](https://github.com/lissy93/dashy) | 2026-10-23 | Svensk resurs: `src/assets/locales/sv.json` | 2026-11-02, Alicia Sykes |
| 2 | [logseq/logseq](https://github.com/logseq/logseq) | 2026-10-07 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [louislam/dockge](https://github.com/louislam/dockge) | 2025-03-30 | Svensk resurs: `frontend/src/lang/sv-SE.json` | 2024-10-21, Gunnar Norin |
| 2 | [M66B/FairEmail](https://github.com/M66B/FairEmail) | 2026-11-13 | Svensk resurs: `app/src/main/assets/SETUP-sv-rSE.md` | 2021-04-25, M66B |
| 2 | [magento/magento2](https://github.com/magento/magento2) | 2026-10-13 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [marktext/marktext](https://github.com/marktext/marktext) | 2026-10-21 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [martinrotter/rssguard](https://github.com/martinrotter/rssguard) | 2026-11-12 | Svensk resurs: `localization/qtbase_sv.ts` | 2023-08-23, Martin Rotter |
| 2 | [mastodon/mastodon](https://github.com/mastodon/mastodon) | 2026-11-03 | Svensk resurs: `app/javascript/mastodon/locales/sv.json` | 2026-11-11, github-actions[bot] |
| 2 | [matomo-org/matomo](https://github.com/matomo-org/matomo) | 2026-10-22 | Svensk resurs: `lang/sv.json` | 2026-10-28, Weblate (bot) |
| 2 | [mattermost/mattermost](https://github.com/mattermost/mattermost) | 2026-11-04 | Svensk resurs: `i18n/glossary/sv.json` | 2026-10-19, Jesse Hallam |
| 2 | [maybe-finance/maybe](https://github.com/maybe-finance/maybe) | 2025-07-24 | Svensk resurs: `config/locales/defaults/sv-FI.yml` | 2024-10-02, Zach Gollwitzer |
| 2 | [MbinOrg/mbin](https://github.com/MbinOrg/mbin) | 2026-11-10 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [mealie-recipes/mealie](https://github.com/mealie-recipes/mealie) | 2026-11-13 | Svensk resurs: `frontend/app/lang/dateTimeFormats/sv-SE.json` | 2026-04-08, Kuchenpirat |
| 2 | [medplum/medplum](https://github.com/medplum/medplum) | 2026-11-11 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [meetfranz/franz](https://github.com/meetfranz/franz) | 2025-04-09 | Svensk resurs: `src/i18n/locales/sv.json` | 2024-12-20, Stefan Malzner |
| 2 | [miniflux/v2](https://github.com/miniflux/v2) | 2026-11-02 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [misskey-dev/misskey](https://github.com/misskey-dev/misskey) | 2026-11-12 | Svensk resurs: `locales/sv-SE.yml` | 2026-06-08, syuilo |
| 2 | [mixxxdj/mixxx](https://github.com/mixxxdj/mixxx) | 2026-03-27 | Svensk resurs: `res/translations/mixxx_sv.qm` | 2026-08-05, Daniel Schürmann |
| 2 | [mullvad/mullvad-browser](https://github.com/mullvad/mullvad-browser) | 2026-11-10 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [muse-sequencer/muse](https://github.com/muse-sequencer/muse) | 2026-10-19 | Svensk resurs: `src/share/locale/muse_sv_SE.ts.stale` | 2021-10-03, Robert Jonsson |
| 2 | [nautobot/nautobot](https://github.com/nautobot/nautobot) | 2026-11-09 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [navidrome/navidrome](https://github.com/navidrome/navidrome) | 2026-09-24 | Svensk resurs: `resources/i18n/sv.json` | 2026-09-20, Jonatan Nyberg |
| 2 | [Nheko-Reborn/nheko](https://github.com/Nheko-Reborn/nheko) | 2025-08-10 | Svensk resurs: `resources/langs/nheko_sv.ts` | 2026-03-02, Nicolas Werner |
| 2 | [nocobase/nocobase](https://github.com/nocobase/nocobase) | 2026-11-12 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [nocodb/nocodb](https://github.com/nocodb/nocodb) | 2026-10-29 | Svensk resurs: `packages/nc-gui/lang/sv.json` | 2026-11-06, Fendy Heryanto |
| 2 | [NodeBB/NodeBB](https://github.com/NodeBB/NodeBB) | 2026-11-12 | Svensk resurs: `public/language/sv` | 2026-09-15, Misty Release Bot |
| 2 | [nukeop/nuclear](https://github.com/nukeop/nuclear) | 2026-11-06 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [ollama/ollama](https://github.com/ollama/ollama) | 2026-11-09 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [onionshare/onionshare](https://github.com/onionshare/onionshare) | 2026-11-07 | Svensk resurs: `desktop/onionshare/resources/countries/sv.json` | 2022-02-13, Micah Lee |
| 2 | [ONLYOFFICE/DocumentServer](https://github.com/ONLYOFFICE/DocumentServer) | 2026-10-12 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [open-source-parsers/jsoncpp](https://github.com/open-source-parsers/jsoncpp) | 2026-06-14 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [open-telemetry/opentelemetry.io](https://github.com/open-telemetry/opentelemetry.io) | 2026-10-04 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | 2026-11-08 | Svensk resurs: `src/lib/i18n/locales/sv-SE` | 2026-11-08, Timothy Jaeryang Baek |
| 2 | [openemr/openemr](https://github.com/openemr/openemr) | 2026-10-27 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [openfoodfacts/smooth-app](https://github.com/openfoodfacts/smooth-app) | 2026-08-24 | Svensk resurs: `packages/smooth_app/ios/Runner/sv.lproj` | 2024-11-11, Open Food Facts Bot |
| 2 | [opengisch/QField](https://github.com/opengisch/QField) | 2026-11-12 | Svensk resurs: `i18n/qfield_sv.ts` | 2026-11-13, Translation update 💬 |
| 2 | [openhab/openhab-android](https://github.com/openhab/openhab-android) | 2026-07-31 | Svensk resurs: `assets/store_descriptions/sv-SE` | 2024-08-24, mueller-ma |
| 2 | [OpenTracksApp/OpenTracks](https://github.com/OpenTracksApp/OpenTracks) | 2025-08-24 | Resursträff kräver UI-kontroll | 2025-01-04, Kristoffer Grundström |
| 2 | [opf/openproject](https://github.com/opf/openproject) | 2026-11-09 | Svensk resurs: `config/locales/crowdin/js-sv.yml` | 2026-11-12, OpenProject Actions CI |
| 2 | [outline/outline](https://github.com/outline/outline) | 2026-10-23 | Svensk resurs: `shared/i18n/locales/sv_SE` | 2026-11-09, Translate-O-Tron |
| 2 | [owncast/owncast](https://github.com/owncast/owncast) | 2026-09-03 | Svensk resurs: `web/i18n/sv` | 2026-10-12, github-actions[bot] |
| 2 | [owncloud/android](https://github.com/owncloud/android) | 2026-08-31 | Svensk resurs: `owncloudApp/src/main/res/values-sv` | 2026-09-23, Jorge Aguado Recio |
| 2 | [pixelfed/pixelfed](https://github.com/pixelfed/pixelfed) | 2026-10-21 | Svensk resurs: `lang/sv-SE` | 2026-11-05, Shlee |
| 2 | [plausible/analytics](https://github.com/plausible/analytics) | 2026-05-15 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [PolyMC/PolyMC](https://github.com/PolyMC/PolyMC) | 2026-10-03 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [PostHog/posthog](https://github.com/PostHog/posthog) | 2026-11-12 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [PrestaShop/PrestaShop](https://github.com/PrestaShop/PrestaShop) | 2026-11-09 | Resursträff kräver UI-kontroll | 2019-11-20, Pablo Borowicz |
| 2 | [ProtonVPN/android-app](https://github.com/ProtonVPN/android-app) | 2026-10-22 | Resursträff kräver UI-kontroll | 2026-10-09, Marcin Simonides |
| 2 | [ProtonVPN/ios-mac-app](https://github.com/ProtonVPN/ios-mac-app) | 2026-11-03 | Svensk resurs: `apps/ios/ProtonVPN/Resources/Settings.bundle/sv.lproj` | 2025-12-09, L10n bot |
| 2 | [quodlibet/quodlibet](https://github.com/quodlibet/quodlibet) | 2025-05-31 | Svensk resurs: `po/sv.po` | 2026-10-05, Hosted Weblate |
| 2 | [RawTherapee/RawTherapee](https://github.com/RawTherapee/RawTherapee) | 2026-07-26 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [readest/readest](https://github.com/readest/readest) | 2026-11-05 | Svensk resurs: `apps/readest-app/extensions/send-to-readest/_locales/sv` | 2026-05-22, Huang Xin |
| 2 | [saleor/saleor](https://github.com/saleor/saleor) | 2026-11-12 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [SeaDve/Kooha](https://github.com/SeaDve/Kooha) | 2026-06-05 | Svensk resurs: `po/sv.po` | 2026-06-07, Hosted Weblate |
| 2 | [seerr-team/seerr](https://github.com/seerr-team/seerr) | 2026-11-12 | Svensk resurs: `server/i18n/locale/sv.json` | 2026-04-19, seerr-automation-bot |
| 2 | [sigoden/dufs](https://github.com/sigoden/dufs) | 2026-10-17 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [SkyTubeTeam/SkyTube](https://github.com/SkyTubeTeam/SkyTube) | 2026-10-29 | Svensk resurs: `app/src/main/res/values-sv` | 2026-08-03, Jonatan Nyberg |
| 2 | [status-im/status-app](https://github.com/status-im/status-app) | 2026-11-05 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [status-im/status-legacy](https://github.com/status-im/status-legacy) | 2025-10-28 | Svensk resurs: `translations/sv.json` | 2023-12-11, BalogunofAfrica |
| 2 | [strapi/strapi](https://github.com/strapi/strapi) | 2026-11-12 | Svensk resurs: `packages/core/admin/admin/src/translations/sv.json` | 2026-10-21, Nas |
| 2 | [strawberrymusicplayer/strawberry](https://github.com/strawberrymusicplayer/strawberry) | 2026-10-02 | Svensk resurs: `src/translations/strawberry_sv_SE.ts` | 2026-10-17, Jonas Kvinge |
| 2 | [tasks/tasks](https://github.com/tasks/tasks) | 2026-10-14 | Svensk resurs: `app/src/main/res/values-sv` | 2026-11-11, Alex Baker |
| 2 | [Tautulli/Tautulli](https://github.com/Tautulli/Tautulli) | 2026-11-10 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [teableio/teable](https://github.com/teableio/teable) | 2026-11-13 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [team-spotube/spotube](https://github.com/team-spotube/spotube) | 2026-11-10 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [ToolJet/ToolJet](https://github.com/ToolJet/ToolJet) | 2026-11-12 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [twentyhq/twenty](https://github.com/twentyhq/twenty) | 2026-11-09 | Svensk resurs: `packages/twenty-emails/src/locales/generated/sv-SE.ts` | 2026-11-10, twenty-pr[bot] |
| 2 | [umami-software/umami](https://github.com/umami-software/umami) | 2026-11-12 | Resursträff kräver UI-kontroll | 2024-07-29, Mike Cao |
| 2 | [ungoogled-software/ungoogled-chromium](https://github.com/ungoogled-software/ungoogled-chromium) | 2026-11-10 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [wallabag/android-app](https://github.com/wallabag/android-app) | 2026-06-01 | Svensk resurs: `app/src/main/res/values-sv` | 2021-11-20, Dmitriy Bogdanov |
| 2 | [wallabag/wallabag](https://github.com/wallabag/wallabag) | 2026-10-28 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [wekan/wekan](https://github.com/wekan/wekan) | 2026-11-13 | Svensk resurs: `imports/i18n/data/sv.i18n.json` | 2026-11-11, Lauri Ojansivu |
| 2 | [writefreely/writefreely](https://github.com/writefreely/writefreely) | 2026-11-09 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [zed-industries/zed](https://github.com/zed-industries/zed) | 2026-11-11 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [zerotier/ZeroTierOne](https://github.com/zerotier/ZeroTierOne) | 2026-05-28 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 2 | [zulip/zulip](https://github.com/zulip/zulip) | 2026-11-13 | Svensk resurs: `locale/sv` | 2026-11-05, Mateusz Mandera |
| 2 | [zwave-js/zwave-js-ui](https://github.com/zwave-js/zwave-js-ui) | 2026-11-10 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 3 | [appwrite/appwrite](https://github.com/appwrite/appwrite) | 2026-11-12 | Resursträff kräver UI-kontroll | 2019-05-09, eldadfux |
| 3 | [beekeeper-studio/beekeeper-studio](https://github.com/beekeeper-studio/beekeeper-studio) | 2026-11-06 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 3 | [cockpit-project/cockpit](https://github.com/cockpit-project/cockpit) | 2026-11-10 | Svensk resurs: `po/sv.po` | 2026-10-27, GitHub Workflow |
| 3 | [coder/coder](https://github.com/coder/coder) | 2026-11-10 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 3 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | 2026-11-01 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 3 | [dgtlmoon/changedetection.io](https://github.com/dgtlmoon/changedetection.io) | 2026-11-09 | Resursträff kräver UI-kontroll | 2026-01-12, dgtlmoon |
| 3 | [gitbutlerapp/gitbutler](https://github.com/gitbutlerapp/gitbutler) | 2026-11-11 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 3 | [go-gitea/gitea](https://github.com/go-gitea/gitea) | 2026-11-01 | Svensk resurs: `options/locale/locale_sv-SE.json` | 2026-11-09, GiteaBot |
| 3 | [grafana-cold-storage/oncall](https://github.com/grafana-cold-storage/oncall) | 2026-02-11 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 3 | [grafana/grafana](https://github.com/grafana/grafana) | 2026-11-10 | Svensk resurs: `apps/advisor/pkg/translations/sv-SE` | 2026-09-23, grafana-pr-automation[bot] |
| 3 | [grafana/loki](https://github.com/grafana/loki) | 2026-11-13 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 3 | [grafana/tempo](https://github.com/grafana/tempo) | 2026-10-21 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 3 | [gravitl/netmaker](https://github.com/gravitl/netmaker) | 2026-08-31 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 3 | [hasura/graphql-engine](https://github.com/hasura/graphql-engine) | 2026-11-11 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 3 | [helix-editor/helix](https://github.com/helix-editor/helix) | 2025-07-18 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 3 | [jesseduffield/lazygit](https://github.com/jesseduffield/lazygit) | 2026-11-07 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 3 | [kubernetes-retired/dashboard](https://github.com/kubernetes-retired/dashboard) | 2025-10-30 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 3 | [kubernetes-sigs/headlamp](https://github.com/kubernetes-sigs/headlamp) | 2026-10-15 | Svensk resurs: `frontend/src/i18n/locales/sv` | 2026-03-11, Joaquim Rocha |
| 3 | [lite-xl/lite-xl](https://github.com/lite-xl/lite-xl) | 2025-06-08 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 3 | [louislam/uptime-kuma](https://github.com/louislam/uptime-kuma) | 2026-11-12 | Svensk resurs: `src/lang/sv-SE.json` | 2026-10-30, Anton Palmqvist |
| 3 | [micro-editor/micro](https://github.com/micro-editor/micro) | 2025-12-31 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 3 | [netbirdio/netbird](https://github.com/netbirdio/netbird) | 2026-11-10 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 3 | [netbox-community/netbox](https://github.com/netbox-community/netbox) | 2026-11-10 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 3 | [netdata/netdata](https://github.com/netdata/netdata) | 2026-11-04 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 3 | [openziti/ziti](https://github.com/openziti/ziti) | 2026-10-08 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 3 | [openziti/ziti-console](https://github.com/openziti/ziti-console) | 2026-11-03 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 3 | [pi-hole/pi-hole](https://github.com/pi-hole/pi-hole) | 2026-11-11 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 3 | [portainer/portainer](https://github.com/portainer/portainer) | 2026-10-21 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 3 | [PowerDNS-Admin/PowerDNS-Admin](https://github.com/PowerDNS-Admin/PowerDNS-Admin) | 2026-11-07 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 3 | [prometheus/prometheus](https://github.com/prometheus/prometheus) | 2026-11-05 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 3 | [rancher/rancher](https://github.com/rancher/rancher) | 2026-10-29 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 3 | [shlinkio/shlink](https://github.com/shlinkio/shlink) | 2026-10-21 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 3 | [supabase/supabase](https://github.com/supabase/supabase) | 2026-08-07 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 3 | [TechnitiumSoftware/DnsServer](https://github.com/TechnitiumSoftware/DnsServer) | 2026-10-17 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 3 | [TwiN/gatus](https://github.com/TwiN/gatus) | 2026-10-28 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 3 | [usebruno/bruno](https://github.com/usebruno/bruno) | 2026-10-22 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 3 | [VictoriaMetrics/VictoriaMetrics](https://github.com/VictoriaMetrics/VictoriaMetrics) | 2026-11-09 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 3 | [VSCodium/vscodium](https://github.com/VSCodium/vscodium) | 2026-10-28 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 3 | [wazuh/wazuh](https://github.com/wazuh/wazuh) | 2026-11-09 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 3 | [webmin/webmin](https://github.com/webmin/webmin) | 2026-09-21 | Svensk resurs: `acl/lang/sv` | 2026-07-14, Ilia Ross |
| 3 | [woodpecker-ci/woodpecker](https://github.com/woodpecker-ci/woodpecker) | 2026-10-29 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 4 | [biolab/orange3](https://github.com/biolab/orange3) | 2026-11-08 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 4 | [endless-sky/endless-sky](https://github.com/endless-sky/endless-sky) | 2026-10-31 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 4 | [gnu-octave/octave](https://github.com/gnu-octave/octave) | 2026-07-10 | Svensk resurs: `liboctgui/languages/sv_SE.ts` | 2026-09-11, Rik |
| 4 | [jamovi/jamovi](https://github.com/jamovi/jamovi) | 2026-05-23 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 4 | [jasp-stats/jasp-desktop](https://github.com/jasp-stats/jasp-desktop) | 2026-10-21 | Resursträff kräver UI-kontroll: `Desktop/html/js/plotly0/lib/plotlyjs/locales/sv.js` | 2026-03-05, Don van den Bergh |
| 4 | [naev/naev](https://github.com/naev/naev) | 2025-07-08 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 4 | [openframeworks/openFrameworks](https://github.com/openframeworks/openFrameworks) | 2026-11-13 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 4 | [OpenRA/OpenRA](https://github.com/OpenRA/OpenRA) | 2025-03-30 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 4 | [OrcaSlicer/OrcaSlicer](https://github.com/OrcaSlicer/OrcaSlicer) | 2026-11-07 | Svensk resurs: `localization/i18n/sv` | 2026-11-06, Kris Austin |
| 4 | [processing/processing4](https://github.com/processing/processing4) | 2026-09-24 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 4 | [sagemath/sage](https://github.com/sagemath/sage) | 2026-09-28 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 4 | [scipy/scipy](https://github.com/scipy/scipy) | 2026-08-21 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 4 | [solvespace/solvespace](https://github.com/solvespace/solvespace) | 2026-10-21 | Ingen svensk resurs i Git, extern kanal ej verifierad | Ej offentligt fastställt |
| 4 | [supercollider/supercollider](https://github.com/supercollider/supercollider) | 2025-11-24 | Svensk resurs: `editors/sc-ide/translations/scide_sv.ts` | 2020-03-01, Dennis Braun |

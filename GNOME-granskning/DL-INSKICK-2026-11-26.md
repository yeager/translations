# Damned Lies-inskickningar — 2026-11-26

Färdiggranskade kataloger som kontrollerats mot aktuell POT och laddats upp via API med kommentaren ”Granskad och klar”. Aktivitetssida och slutstatistik verifierades. Uppladdningar på äldre gnome-grenar i tabellen är historiska; den aktiva kön följer nu endast main, master och gnome-51.

| Modul | Gren | Domän | Ändrade PO-poster | API-statistik |
|---|---|---|---:|---:|
| gimp-help | master | menus~edit | 72 | 274/0/0 |
| gimp-help | master | menus~colors~map | 150 | 149/0/18 (18 @@image:) |
| gimp-help | master | menus~colors~components | 145 | 136/0/26 (26 @@image:) |
| gimp-help | master | using | 630 | 1 105/0/0 |
| gimp-help | master | filters~generic | 165 | 303/0/0 |
| gimp-help | master | filters~decor | 132 | 289/0/0 |
| gimp-help | master | menus~colors~tone-mapping | 58 | 113/0/0 |
| gimp-help | master | menus~filters | 48 | 118/0/0 |
| gimp-help | master | po-windows-installer | 2 | 5/0/0 |
| gimp-help | master | gimp-keys | 57 | 262/0/0 |
| gimp | master | po-libgimp | 7 | 675/0/0 |
| gimp | master | po-python | 99 | 231/0/0 |
| gimp | master | po-script-fu | 141 | 330/0/0 |
| gimp | master | po-plug-ins | 155 | 3 723/0/0 |
| gimp-help | master | toolbox~selection | 310 | 330/0/0 |
| gimp | master | po | 1 | 6 142/0/0 (aktivitetssida) |
| ashpd | main | demo-client | 4 | 38/0/0 |
| blurble | main | po | 1 | 29/0/0 |
| console | gnome-50 | po | 12 | verifierad |
| cups-pk-helper | master | po | 19 | 22/0/0 |
| emblem | master | po | 3 | 39/0/0 |
| evolution-activesync | master | po | 4 | 60/0/0 |
| evolution-etesync | master | po | 5 | 21/0/0 |
| four-in-a-row | master | help | 34 | 60/0/0 |
| gcolor3 | master | po | 7 | 59/0/0 |
| gdm | gnome-50 | po | 10 | verifierad |
| gimp-help | master | introduction | 1 | 3/0/0 |
| gimp-help | master | preface | 2 | 37/0/0 |
| gimp-help — GIMP User Manual | master | filters~enhance | 65 | verifierad |
| gnome-2048 | master | help | 9 | 32/0/0 |
| gnome-applets | master | drivemount | 25 | 58/0/0 |
| gnome-applets | master | geyes | 1 | 42/0/0 |
| gnome-applets | master | trash | 25 | 43/0/0 |
| gnome-browser-extension | master | po | 4 | 39/0/0 |
| gnome-characters | main | po | 8 | 56/0/0 |
| gnome-color-manager | master | help | 3 | 26/0/0 |
| gnome-connections | master | help | 2 | 26/0/0 |
| gnome-desktop | master | po | 1 | 31/0/0 |
| gnome-klotski | master | help | 15 | 53/0/0 |
| gnome-logs | master | help | 7 | 23/0/0 |
| gnome-menus | master | po | 3 | 27/0/0 |
| gnome-multi-writer | master | po | 4 | 58/0/0 |
| gnome-network-displays | master | po | 4 | 35/0/0 |
| gnome-panel | master | fish | 25 | 57/0/0 |
| gnome-remote-desktop | gnome-50 | po | 36 | 50/0/0 |
| gnome-remote-desktop | main | po | 4 | 50/0/0 |
| gnome-session | gnome-50 | po | 21 | 43/0/0 |
| gnome-session | main | po | 10 | 43/0/0 |
| gnome-tetravex | master | help | 37 | verifierad |
| gnome-tour | main | po | 4 | 23/0/0 |
| gnome-weather | main | po | 4 | 50/0/0 |
| gparted | master | po | 1 | 18/0/0 |
| grilo | master | po | 5 | 36/0/0 |
| grilo-plugins | master | help | 7 | 52/0/0 |
| gstreamer | main | plugins-bad | 1 | 29/0/0 |
| gstreamer | main | plugins-ugly | 1 | 10/0/0 |
| hieroglyphic — Find LaTeX symbols | main | po | 2 | 28/0/0 |
| hitori | main | help | 3 | 43/0/0 |
| hitori | main | po | 2 | 61/0/0 |
| icon-library | master | po | 1 | 59/0/0 |
| json-glib | main | po | 4 | 48/0/0 |
| libgedit-gfls | main | po | 3 | 36/0/0 |
| malcontent | main | help | 39 | 49/0/0 |
| network-manager-iodine | master | po | 5 | 25/0/0 |
| NetworkManager-fortisslvpn | main | po | 4 | 33/0/0 |
| phosh-tour | main | po | 13 | 48/0/0 |
| raider | main | po | 4 | 38/0/0 |
| solanum | main | po | 2 | 44/0/0 |
| stevia | main | po | 4 | 14/0/0 |
| sushi | gnome-50 | po | 2 | 19/0/0 |
| sysprof | master | help | 31 | 49/0/0 |
| tali | master | help | 38 | verifierad |
| telegnome | master | help | 12 | 31/0/0 |
| Warp Hjälp | main | help | 28 | 55/0/0 |

## Aktuella hinder

- `gedit-plugins/gnome-50/help` (18 ändrade PO-poster): API HTTP 500 (serverfel); behöver återförsök.
- `postr/master/po` (4 ändrade PO-poster): API HTTP 429; spärrtid okänd sekunder.
- `gtk-vnc/master/po` (2 ändrade PO-poster): Nu tillgänglig endast åtgärd: WriteAComment.
- `gimp-help/master/po-windows-installer` (2 ändrade PO-poster): Nu tillgänglig endast åtgärd: WriteAComment.
- `xdg-user-dirs-gtk/master/po` (3 ändrade PO-poster): Nu tillgänglig endast åtgärd: WriteAComment.
- `avahi/master/po` (3 ändrade PO-poster): Nu tillgänglig endast åtgärd: WriteAComment.

## Status

- Inskickade och verifierade kataloger 2026-11-26: **74**.
- 404-felen från tidigare URL-sluggar har rättats med modulernas kanoniska REST API-namn och återförsöken har inletts.
- Övriga färdiggranskade kataloger står fortsatt som `Klar lokalt` tills uppladdning kan bekräftas.

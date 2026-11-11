# VirtualBox, svensk terminologi

Datum: 2026-11-11. Listan gäller den granskade Qt-katalogen
`VirtualBox_sv.ts` och är ett granskningsstöd, inte en ersättning för
sammanhanget i gränssnittet.

| Engelska | Rekommenderad svenska | Kontext och undantag |
| --- | --- | --- |
| virtual machine, VM | virtuell maskin | `VM` behålls i snäva etiketter och tekniska namn. |
| host | värd | `värdoperativsystem`, `värdsystem`, `värddator` enligt vad källan avser. |
| guest | gäst | `gästoperativsystem`, `gästsystem`. |
| snapshot | ögonblicksbild | Används för VirtualBox-snapshots, inte `skärmbild`. |
| host-only network | endast-värd-nätverk | `endast-värd-nätverkskort` för adaptern. |
| chipset | kretsuppsättning | `kretsuppsättningstyp` i systemdetaljer. |
| nested paging | nästlad sidindelning | Fackterm för funktionen VT-x/AMD-V. |
| hardware virtualization | maskinvaruvirtualisering | Inte direktöversättning med `hårdvaru-` när det blir otydligt. |
| shared clipboard | delat urklipp | `urklippsdata` för innehållet. |
| Guest Additions | Gästtillägg | VirtualBox-produktnamn, med stor begynnelsebokstav. |
| Extension Pack | tilläggspaket | Behåll `VirtualBox Extension Pack` när det är det synliga produktnamnet. |
| appliance | appliance | OVF-domänterm. Skriv `appliance-fil` och `appliance-arkiv` där formatet behöver förtydligas. |
| differencing disk | differenshårddisk | `differensmedium` när objektet inte specifikt är en hårddisk. |
| medium, media | medium, medier | Singular: `mediet`; undvik engelskt plural `media` i svensk löptext. |
| controller | styrkort | Exempel: `USB-styrkort`, `lagringsstyrkort`. |
| port forwarding | portomdirigering | Inte `postomdirigering`. |
| console | konsol | Sammansättningar: `molnkonsol`, `konsolprogram`, `konsolfel`. |
| disk image | diskavbildning | `ISO-avbildning` för ISO-filer. |
| unattended installation | obevakad installation | Omfattar installation av gästoperativsystem. |
| clone | klon | `kloningstyp` för Clone Type. |
| graphics controller | grafikkontroller | Inte `grafikkort` när den emulerade kontrollertypen avses. |
| serial port | seriell port | Inte `serieport`; plural `seriella portar`. |
| remote desktop server port | fjärrskrivbordsserverport | Används som sammanhållen detaljetikett. |
| VM exits | VM-exits | Tekniskt räknarmått, inte `VM-avslut` som kan betyda avstängda maskiner. |
| guest CPU, VMM CPU | gäst-CPU, VMM-CPU | Exempel: `gäst-CPU-belastning`. |
| disk I/O | disk-I/O | Behåll förkortningen `I/O`; skriv inte `disk in/ut`. |
| drag and drop | dra-och-släpp | Bindestreck i sammansättningar, exempelvis `dra-och-släpp-läge`. |
| cloud VM | molnmaskin | Inte `virtuell molnmaskin`; en molnmaskin är redan virtuell i denna kontext. |
| provisioning | förbereder | Status för molnmaskin; undvik engelska `provisionerar`. |
| terminating, terminated | avslutas, avslutad | Statusord. Använd inte `stänger av` när processen eller sessionen avslutas. |
| public key | offentlig nyckel | Undvik direktöversättningen `publik nyckel`. |
| secure boot | säker start | Följ projektets användargränssnitt, inte `säker uppstart`, om samma funktion avses. |
| VFS explorer | VFS-utforskaren | Behåll förkortningen, böj den svenska efterleden. |
| I/O cache | I/O-cache | Exempel: `värdens I/O-cache`; undvik hybridformen `I/O-cachingförmåga`. |
| solid-state drive | SSD-enhet | Produktnära UI-term; accelerator kan placeras på `SSD`. |
| optical disk | optisk skiva | Använd `optisk enhet` endast för själva läsaren eller drivaren. |
| file manager | filhanterare | `filhanterarfönster` för fönstret. |
| progress | förlopp | `förloppsnotis`, inte `progress` i löpande UI-text. |

## Format och kod

- Bevara kommandon, sökvägar, URL:er, platshållare, XML/HTML och filformat
  exakt. Exempel: `mount -t vboxsf share mount_point`, `myvbox`,
  `hostname:port`, `OVF`, `VDI` och `UUID`.
- Använd bindestreck där det klargör sammansättning eller förebygger tre lika
  konsonanter, till exempel `SSD-enhet`, `VirtualBox-VM` och
  `endast-värd-nätverk`.
- Behåll synliga protokoll- och formatnamn oförändrade, till exempel
  `NEGOTIATE`, `TLS`, `RDP`, `ATAPI`, `VSD`, `VFS`, `VDI`, `VMDK` och `QCOW`.
  Översätt bara den förklarande löptexten runt namnet.

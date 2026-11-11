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

## Format och kod

- Bevara kommandon, sökvägar, URL:er, platshållare, XML/HTML och filformat
  exakt. Exempel: `mount -t vboxsf share mount_point`, `myvbox`,
  `hostname:port`, `OVF`, `VDI` och `UUID`.
- Använd bindestreck där det klargör sammansättning eller förebygger tre lika
  konsonanter, till exempel `SSD-enhet`, `VirtualBox-VM` och
  `endast-värd-nätverk`.

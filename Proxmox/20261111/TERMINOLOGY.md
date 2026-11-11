# Proxmox, svensk terminologi

Denna lista gäller den samlade katalogen för Proxmox VE, Proxmox Backup
Server, Proxmox Mail Gateway och Proxmox Datacenter Manager.

| Engelska | Svenska | Sammanhang och undantag |
| --- | --- | --- |
| backup | säkerhetskopia | `backup job` blir säkerhetskopieringsjobb. |
| datastore | datalager | PBS:s logiska lagringsobjekt; skiljs från fysisk lagring. |
| storage | lagring | Generisk lagringsresurs i PVE/PBS. |
| remote | fjärrvärd | Proxmox konfigurationsobjekt. `remote server` blir däremot fjärrserver. |
| node | nod | Klusternod. |
| guest | gäst | Virtuell maskin eller container när det gemensamma begreppet används. |
| virtual machine, VM | virtuell maskin, VM | `VM` behålls i korta UI-etiketter och API-/konfigurationsnamn. |
| container, CT | container, CT | Produktens etablerade tekniska begrepp behålls. |
| snapshot | ögonblicksbild | Används konsekvent även för PBS-säkerhetskopior. |
| retention | bevarande | Exempel: bevarandekonfiguration och bevarandepolicy. |
| prune | rensa | Avser borttagning enligt bevaranderegler. |
| thread | tråd | `worker thread` = arbetstråd, `read thread` = lästråd. |
| controller | styrenhet | I SDN/EVPN-sammanhang. Ceph `monitor` behålls som monitor. |
| header | huvudfält | HTTP- och e-posthuvudfält; kodnamn som `If-None-Match` bevaras. |
| claim | anspråk | OpenID Connect, till exempel användarnamnsanspråk. |
| authentication realm | autentiseringsområde | Den synliga produkttermen `realm` behålls när den är ett identifierarnamn. |
| live migration | direktmigrering | Virtuell maskin flyttas utan avbrott. |
| pull / push | hämta / sända | I synkroniseringsriktningar: hämtningsriktning respektive sändriktning. |
| fencing | isolering | HA-åtgärd, exempelvis watchdog-baserad isolering. |
| Secure Boot | Secure Boot | Produkt- och tekniknamn, med etablerad versalisering. |
| WebAuthn | WebAuthn | Standardnamn, inte `Webauthn`. |
| Ceph / CephFS | Ceph / CephFS | Produktnamn bevaras. |

Tekniska identifierare, API-namn, konfigurationsnycklar, exempeldata och
protokollnamn är oförändrade, till exempel `keep-daily`, `preferred_username`,
`keyctl`, `vzdump.conf`, JSON-exemplen och `pveproxy`.

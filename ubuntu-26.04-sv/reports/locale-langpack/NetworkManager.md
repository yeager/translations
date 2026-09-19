# locale-langpack/NetworkManager

2 rättade översättningsposter. Ursprung: `/usr/share/locale-langpack/sv/LC_MESSAGES/NetworkManager.mo`.

Jämförelsen gäller översatta meddelanden, utan metadatahuvudet. Gettext kan normalisera det kompilerade huvudets teckenkodning och skapandedatum; före/efter finns i metadata. PO-filerna och diffarna behåller ursprunglig teckenkodning (OpenSP: ISO-8859-1).

Upstream: [NetworkManager](https://networkmanager.dev/). [Källkod](https://gitlab.freedesktop.org/NetworkManager/NetworkManager).

[Ubuntu-källpaket](https://launchpad.net/ubuntu/+source/network-manager). Installerat ägarpaket: `language-pack-sv-base 1:26.04+20260818`.

[Rättad PO](../../po/locale-langpack/NetworkManager.po) · [Original](../../original/locale-langpack/NetworkManager.po) · [Diff](../../diff/locale-langpack/NetworkManager.po.diff) · [Metadata](../../metadata/locale-langpack/NetworkManager.json)

Rättad PO godkänns av `msgfmt --check --check-format`. Diffen återger filen byte för byte. Den kompilerade meddelandetabellen skiljer sig från installerad MO endast genom rättningarna nedan. PO-huvudet är bevarat; rapporten dokumenterar ändringarnas datum.

Råträffar: l10n-lint 142 → 140, svlang 9 → 9. Kvarstående träffar är kandidater och innebär inte verifierade fel.

## F035 · P3 · Stavfel: rutttyp

Ett överflödigt eller saknat tecken ger ett felstavat svenskt ord.

PO-rad: original 87, rättad 87.

Källtext:

```text
%s is not a valid route type
```

Före:

```text
%s är inte en giltig rutttyp
```

Efter:

```text
%s är inte en giltig ruttyp
```

## F036 · P3 · Stavfel: huvudrutttabellen

Ett överflödigt eller saknat tecken ger ett felstavat svenskt ord.

PO-rad: original 7022, rättad 7022.

Källtext:

```text
Whether to configure MPTCP endpoints and the address flags. If MPTCP is enabled in NetworkManager, it will configure the addresses of the interface as MPTCP endpoints. Note that IPv4 loopback addresses (127.0.0.0/8), IPv4 link local addresses (169.254.0.0/16), the IPv6 loopback address (::1), IPv6 link local addresses (fe80::/10), IPv6 unique local addresses (ULA, fc00::/7) and IPv6 privacy extension addresses (rfc3041, ipv6.ip6-privacy) will be excluded from being configured as endpoints. If "disabled" (0x1), MPTCP handling for the interface is disabled and no endpoints are registered. The "enabled" (0x2) flag means that MPTCP handling is enabled. This flag can also be implied from the presence of other flags. Even when enabled, MPTCP handling will by default still be disabled unless "/proc/sys/net/mptcp/enabled" sysctl is on. NetworkManager does not change the sysctl and this is up to the administrator or distribution. To configure endpoints even if the sysctl is disabled, "also-without-sysctl" (0x4) flag can be used. In that case, NetworkManager doesn't look at the sysctl and configures endpoints regardless. Even when enabled, NetworkManager will only configure MPTCP endpoints for a certain address family, if there is a unicast default route (0.0.0.0/0 or ::/0) in the main routing table. The flag "also-without-default-route" (0x8) can override that. When MPTCP handling is enabled then endpoints are configured with the specified address flags "signal" (0x10), "subflow" (0x20), "backup" (0x40), "fullmesh" (0x80). See ip-mptcp(8) manual for additional information about the flags. If the flags are zero (0x0), the global connection default from NetworkManager.conf is honored. If still unspecified, the fallback is "enabled,subflow". Note that this means that MPTCP is by default done depending on the "/proc/sys/net/mptcp/enabled" sysctl. NetworkManager does not change the MPTCP limits nor enable MPTCP via "/proc/sys/net/mptcp/enabled". That is a host configuration which the admin can change via sysctl and ip-mptcp. Strict reverse path filtering (rp_filter) breaks many MPTCP use cases, so when MPTCP handling for IPv4 addresses on the interface is enabled, NetworkManager would loosen the strict reverse path filtering (1) to the loose setting (2).
```

Före:

```text
Huruvida MPTCP-ändpunkter och adressflaggor ska konfigureras. Om MPTCP är aktiverat i NetworkManager kommer den att konfigurera gränssnittets adresser som MPTCP-slutpunkter. Observera att IPv4 loopback-adresser (127.0.0.0/8), IPv4-länk lokala adresser (169.254.0.0/16), IPv6 loopback-adress (::1), IPv6-länk lokala adresser (fe80::/10), IPv6 unik lokal adresser (ULA, fc00::/7) och IPv6 integritetstilläggsadresser (rfc3041, ipv6.ip6-privacy) kommer att uteslutas från att konfigureras som slutpunkter. Om "inaktiverad" (0x1) är MTCP-hantering för gränssnittet inaktiverad och inga slutpunkter registreras. Flaggan "enabled" (0x2) betyder att MPTCP-hantering är aktiverad. Denna flagga kan också antydas från närvaron av andra flaggor. Även när den är aktiverad, kommer MPTCP-hantering som standard fortfarande att vara inaktiverad om inte "/proc/sys/net/mptcp/enabled" sysctl är på. NetworkManager ändrar inte sysctl och detta är upp till administratören eller distributionen. För att konfigurera slutpunkter även om sysctl är inaktiverat kan flaggan "also-without-sysctl" (0x4) användas. I så fall tittar NetworkManager inte på sysctl och konfigurerar slutpunkter oavsett. Även när den är aktiverad kommer NetworkManager endast att konfigurera MPTCP-slutpunkter för en viss adressfamilj, om det finns en unicast-standardrutt (0.0.0.0/0 eller ::/0) i huvudrutttabellen. Flaggan "även-utan-default-route" (0x8) kan åsidosätta det. När MPTCP-hantering är aktiverad konfigureras slutpunkter med de angivna adressflaggorna "signal" (0x10), "subflow" (0x20), "backup" (0x40), "fullmesh" (0x80). Se ip-mptcp(8) manual för ytterligare information om flaggorna. Om flaggorna är noll (0x0), uppfylls den globala anslutningsstandarden från NetworkManager.conf. Om den fortfarande är ospecificerad är reservfunktionen "enabled,subflow". Observera att detta betyder att MPTCP görs som standard beroende på "/proc/sys/net/mptcp/enabled" sysctl. NetworkManager ändrar inte MPTCP-gränserna eller aktiverar MPTCP via "/proc/sys/net/mptcp/enabled". Det är en värdkonfiguration som administratören kan ändra via sysctl och ip-mptcp. Strikt omvänd sökvägsfiltrering (rp_filter) bryter många MPTCP-användningsfall, så när MPTCP-hantering för IPv4-adresser på gränssnittet är aktiverad, skulle NetworkManager lossa den strikta omvända sökvägsfiltreringen (1) till den lösa inställningen (2).
```

Efter:

```text
Huruvida MPTCP-ändpunkter och adressflaggor ska konfigureras. Om MPTCP är aktiverat i NetworkManager kommer den att konfigurera gränssnittets adresser som MPTCP-slutpunkter. Observera att IPv4 loopback-adresser (127.0.0.0/8), IPv4-länk lokala adresser (169.254.0.0/16), IPv6 loopback-adress (::1), IPv6-länk lokala adresser (fe80::/10), IPv6 unik lokal adresser (ULA, fc00::/7) och IPv6 integritetstilläggsadresser (rfc3041, ipv6.ip6-privacy) kommer att uteslutas från att konfigureras som slutpunkter. Om "inaktiverad" (0x1) är MTCP-hantering för gränssnittet inaktiverad och inga slutpunkter registreras. Flaggan "enabled" (0x2) betyder att MPTCP-hantering är aktiverad. Denna flagga kan också antydas från närvaron av andra flaggor. Även när den är aktiverad, kommer MPTCP-hantering som standard fortfarande att vara inaktiverad om inte "/proc/sys/net/mptcp/enabled" sysctl är på. NetworkManager ändrar inte sysctl och detta är upp till administratören eller distributionen. För att konfigurera slutpunkter även om sysctl är inaktiverat kan flaggan "also-without-sysctl" (0x4) användas. I så fall tittar NetworkManager inte på sysctl och konfigurerar slutpunkter oavsett. Även när den är aktiverad kommer NetworkManager endast att konfigurera MPTCP-slutpunkter för en viss adressfamilj, om det finns en unicast-standardrutt (0.0.0.0/0 eller ::/0) i huvudruttabellen. Flaggan "även-utan-default-route" (0x8) kan åsidosätta det. När MPTCP-hantering är aktiverad konfigureras slutpunkter med de angivna adressflaggorna "signal" (0x10), "subflow" (0x20), "backup" (0x40), "fullmesh" (0x80). Se ip-mptcp(8) manual för ytterligare information om flaggorna. Om flaggorna är noll (0x0), uppfylls den globala anslutningsstandarden från NetworkManager.conf. Om den fortfarande är ospecificerad är reservfunktionen "enabled,subflow". Observera att detta betyder att MPTCP görs som standard beroende på "/proc/sys/net/mptcp/enabled" sysctl. NetworkManager ändrar inte MPTCP-gränserna eller aktiverar MPTCP via "/proc/sys/net/mptcp/enabled". Det är en värdkonfiguration som administratören kan ändra via sysctl och ip-mptcp. Strikt omvänd sökvägsfiltrering (rp_filter) bryter många MPTCP-användningsfall, så när MPTCP-hantering för IPv4-adresser på gränssnittet är aktiverad, skulle NetworkManager lossa den strikta omvända sökvägsfiltreringen (1) till den lösa inställningen (2).
```

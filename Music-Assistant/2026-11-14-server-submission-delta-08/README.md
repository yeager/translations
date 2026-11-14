# Music Assistant Server — svensk inskickningsdelta 08

Datum: 2026-11-14

## Omfattning

- 85 unika, lokalt granskade svenska strängar för Music Assistant Server.
- Underlaget förenar batcherna authentication/network 01, network/content 02,
  player/audio/options 03, ABC Radio/network 04, AcoustID 05,
  AirPlay/ambient 06 och ARD Audiothek 07.
- Den tidigare Ambient Sounds-deltan med åtta strängar överlappar helt med
  batch 06 och ingår därför utan dubbletter.

## Kontroller

- 85/85 nycklar finns i aktuell engelsk källfil.
- `l10n-lint --language sv`: godkänd.
- `svlang skrivregler`: godkänd.
- Hunspell-svenska körd; kvarvarande träffar är produktnamn, protokoll,
  egennamn eller facktermer som har granskats i kontext.
- Gitleaks: inga hemligheter hittades.
- JSON-struktur och diff kontrollerade.

## Status

Arkiverad och klar för uppladdning till Lokalise. Inte uppladdad, inskickad,
granskad eller integrerad upstream vid arkiveringstillfället. API-token saknas
i den avsedda Nyckelring-posten, och den sparade Lokalise-sessionen kunde inte
öppna redigeraren via automatiseringen (timeout). `sv_SE.delta.json` är den
enda fil som ska importeras när åtkomst finns; den ersätter inte hela katalogen.

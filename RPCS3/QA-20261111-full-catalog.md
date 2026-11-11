# RPCS3, svensk fullkontroll

Datum: 11 november 2026

Kontrollerad fil: `rpcs3_sv.ts`, den arkiverade svenska huvudkatalogen med
3 618 färdiga översättningar.

## Kontroller

- `lrelease`: skapade en QM-fil med 3 618 färdiga och 0 oavslutade
  översättningar.
- `l10n-lint --language sv`: 0 fel, 3 varningar och 91 informationsposter.
- Gitleaks: inga hemligheter.

De tre varningarna gäller intervallen `0-9`, `A-F` och tillåtna tecken i
RPCN:s användarnamn och token. De återger protokollets teckenuppsättning och
är inte svenska talintervall, så de ska behålla bindestreck.

Informationsposterna gäller Qt-pluralformer, kortkommandon, spel- och
produktnamn, formatsträngar samt avsiktliga svenska skiljetecken. Ingen ny
översättningsändring skapades i denna kontroll.

## Upstream-status

Crowdin-kontrollen tidigare samma dag visar 100 % översatt och 97 % granskat
för `rpcs3_template.ts`. Den senaste lokala renderingsterminologirättelsen är
sparad som Crowdin-förslag, men detta dokument påstår inte att den har
godkänts, exporterats till källkoden eller ingår i en release.

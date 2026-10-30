# Bitwarden Web – PAM-inskick via Crowdin-redigeraren

## Resultat

Den 30 oktober 2026 kunde den vanliga XLIFF-uppladdningen inte öppna en
systemfilväljare i den inbyggda webbläsaren och gav därför ingen import.
Det ersattes med en direkt, radvis inskickning i Crowdins Web-redigerare för
den aktuella filen `main/src/locales/en/Bitwarden Web Vault - Strings to
translate` (fil 58, svenska).

Crowdin bekräftade två tidigare grupper om 47 respektive 40 nya förslag.
Därefter sparades en grupp om 48 och slutligen 2 ytterligare PAM-strängar.
Totalt sparades **137 svenska förslag** i denna redigerarsession. De två sista
var `pamTargetSystemAssignConnectorLabel` → `Åtkomstanslutning` och
`pamTargetSystemStatusActive` → `Aktiv`.

Efter den sista sparningen rapporterade Crowdin **No unsaved translations**
och filtret **Untranslated** visade **0 strings**. Förslagen är skickade som
oautogodkända Crowdin-förslag; detta är inte samma sak som
underhållargodkännande eller publicering.

## Spårbarhet

- Källrevision: `bitwarden/clients` `41f307c001f55f8aa65cae80b7d2de193e762f6d`.
- Källfiler: PAM-häfte 38 och 39 i samma katalog.
- Kvalitetssäkring före inskick: JSON, platshållarjämförelse, `l10n-lint`,
  `svlang skrivregler`, Hunspell och Gitleaks.
- Inskickssätt: Crowdin Web Editor; ingen automatisk godkänning användes.

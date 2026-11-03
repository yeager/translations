# qBittorrent: svensk pluginöversättning, granskningsdelta

Datum: 2026-11-03

## Omfattning

Den aktuella upstreamkatalogen innehåller nya, tomma svenska översättningar för pluginhantering. Den publika Transifex-resursen visar samtidigt 100 % för svenska, så den här deltan ska inte användas för att skriva över befintliga Crowdin- eller Transifex-översättningar. Den är ett granskat förslag för nya uppströmssträngar.

Källan är `src/lang/qbittorrent_sv.ts` på qBittorrents huvudgren. De tomma posterna ligger i `PluginsDialog` och `PluginsEngine`; se särskilt [raderna 9051-9270](https://raw.githubusercontent.com/qbittorrent/qBittorrent/master/src/lang/qbittorrent_sv.ts).

## Beslut

- *plugin* översätts konsekvent till **insticksmodul**.
- Qt-platshållarna `%1`, `%2` och `%3`, samt inbäddade radbrytningar, är oförändrade.
- `invoke` är ett kodnamn och lämnas på engelska.
- Svenska citattecken används för visade namn och felvärden.

## Kontroller

| Kontroll | Resultat |
| --- | --- |
| XML-syntax (`xmllint`) | Godkänd |
| l10n-lint 1.23.31 | 27 poster, 0 fel, 0 varningar |
| svlang 0.2.23: skrivregler | 0 träffar |
| svlang 0.2.23: svengelska | 0 träffar |
| hunspell-sv | Endast `invoke`; avsiktligt kodnamn |

Granskningsfil: `qbt-plugin-review-sv-20261103.ts`.

## Begränsning

Den lokala nätverksmiljön stoppade hämtning och kloning av qBittorrent-källträdet. Därför har den kompletta källfilen granskats via GitHubs råfilsvy, och den här deltan omfattar endast de uttryckligen verifierade, tomma pluginposterna. Ingen import har skickats till Transifex eller Crowdin eftersom den publika resursen redan rapporterar 100 %.

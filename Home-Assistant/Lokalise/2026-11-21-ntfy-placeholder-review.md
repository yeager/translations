# Home Assistant Core: ntfy — platshållarrättning

En käll-/mål-jämförelse hittade ett formatfel i `component::ntfy::issues::topic_protected::fix_flow::step::confirm::description`.

- `{name}` återställdes efter `**{topic}**`.
- Ett felaktigt extra `*` efter `**Bekräfta**` togs bort.
- Markdown, `{topic}` och samtliga radbrytningar bevarades.

Ändringen sparades med Lokalise API och återlästes. TMX-manifest: `Home-Assistant/2026-11-21-ntfy-placeholder-verified.json`.

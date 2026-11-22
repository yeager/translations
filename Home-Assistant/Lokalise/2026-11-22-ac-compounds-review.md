# Home Assistant Core – AC-sammansättningar

Tretton KNX- och Victron-etiketter rättades till svenska AC-sammansättningar.
Det inkluderar den semantiskt felaktiga `AC ingångsström` för `AC-in power`,
som nu är `AC-ingångseffekt`, samt konsekventa former för in-/utgångar,
spänning, börvärde och AC-enheter. Platshållaren i belastningsetiketten
bevarades. Varje ändring sparades och återlästes via Lokalise API.

# Home Assistant Core – Update: duration label

En efterföljande live-kontroll av samtliga sex ID:n visade att den gamla lokala
exporten hade kopplat dem till fel nycklar (bland annat `temperature`, `todo`
och `timer`). Hela det ursprungliga `update`-manifestet och dess sex TMX-rader
har därför dragits tillbaka. Inga av dessa poster ska användas som
översättningsminne för `update` förrän den verkliga live-nyckelmappningen har
granskats på nytt.

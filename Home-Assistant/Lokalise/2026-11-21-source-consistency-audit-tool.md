# Home Assistant Core – källkonsistenskontroll

Granskningsverktyget för korta, återanvända källsträngar kompletterades med
säkert stöd för avgränsad rörledningsutdata. Det kan nu användas tillsammans
med exempelvis `head` och `rg` utan att rapportera ett falskt fel när
mottagaren avslutar tidigt. Verktyget skriver inga översättningar och dess
träffar är fortfarande endast kandidater för efterföljande Lokalise-kontroll.

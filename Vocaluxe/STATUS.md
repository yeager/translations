# Vocaluxe: svensk översättning

2026-10-26: Huvudresursen på utvecklingsgrenen innehöll 403 engelska och 304 svenska strängar. Ett lokalt utkast lägger till de 99 saknade strängarna utan att ändra de tidigare 304. Källor: `Output/Languages/en.xml` och `sv.xml`, utvecklingsrevision 336d08040ee31312acb13d860b5cbbd7aef10d8d. Utkastet är inte skickat till Transifex. Projektets tidigare länk till Transifex gav 404; en aktuell översättningslänk behöver verifieras. Partylägen och webbappen har separata resurser som ännu inte har granskats.

Den officiella versionskandidaten 0.5.0.rc publicerades 2024-12-01 och faller inom 48 månader. Senaste stabila versionen 0.4.1 publicerades 2020-03-10; en nattversion från 2026-10-26 finns också. Källor: https://github.com/Vocaluxe/Vocaluxe/releases och https://www.vocaluxe.org/.

Kontroller av de 99 tilläggen: alla nycklar finns och platshållarna `%s`, `%d` och `{0}` med flera matchar källan. L10n-lint och svlang gav inga fynd; Hunspell markerade tekniska namn och sammansättningar. XML-filen har inte testats i programmet. Före inskick behövs jämförelse med aktuella strängar i Transifex och fortsatt språk- och kontextgranskning.

2026-10-26: [Partnerbyte](partylagen/partnerswap-sv-utkast.xml) har ett utkast för samtliga 39 strängar; i [Challenge](partylagen/challenge-sv-utkast.xml) har två saknade strängar lagts till i den befintliga svenska filen. Källan är utvecklingsgrenens filer från revision 336d08040ee31312acb13d860b5cbbd7aef10d8d. Nycklar och platshållare jämfördes mot engelskan. L10n-lint och svlang gav inga fynd; Hunspell markerade förkortningen ”Plac.” och symbolen Ø. Filerna är inte inskickade eller testade i programmet. Övriga fyra partylägen och webbappen återstår, liksom jämförelse med eventuell aktuell Transifex-data.

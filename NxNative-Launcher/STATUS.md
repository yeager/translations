# NxNative Launcher – svensk lokalisering

Senast uppdaterad: 2026-10-28

## Underlag

- Upstream: <https://github.com/rennan101/nxnative_Launcher>
- Granskad revision: `2cca1871ac6348878c2ca808e7b89cb4860d27be`
- Senaste upstreamändring: 2026-10-28. Projektet uppfyller därmed
  arkivets färskhetskrav på högst 48 månader.
- Arbetsgren: `l10n/swedish`, commit `538a4b2f3c1d6680583547e4b52cc59bc7ec667e`.
- Upstream: [PR #3](https://github.com/rennan101/nxnative_Launcher/pull/3),
  skickad 2026-10-28 och väntar på underhållargranskning.

## Leverans

Projektet hade ingen befintlig l10n-struktur. Leveransen lägger till
SwiftPM-resurser, `L10n`, `L10nText` och `L10nLabel`, så att framtida språk
enbart behöver få en egen `.lproj/Localizable.strings`-fil. Den svenska
katalogen innehåller 366 kontrollerade nycklar för navigering, bibliotek,
portningsflöde, kontroller, systemdialoger, loggar och personlig anpassning.
Den senare etappen täcker förutsättningsbanners, målplattform och utdata,
avancerade byggval samt porteringens resultatlägen. Bibliotekets sök- och
katalogreglage samt centrala system-, nyckel- och lagringsinställningar ingår.
Systemets byggverktyg och källarkivsvy är också lokaliserade.
Informationsrutan och uppdateringsbannrarnas synliga texter är lokaliserade.
Uppdateringsdialogens status- och åtgärdstexter är också lokaliserade.
Spelinställningarnas bildfrekvens-, visnings- och upplösningsreglage ingår.
Omslag, moddar och hantering av sparfiler är också lokaliserade.
Kompatibilitetsvyns rubriker, filter och anteckningslänkar är lokaliserade.
iPhone/iPad-installationens kontroller och distributionsstatus ingår.
Handkontrollens kalibrering, tangentbordslayouter och mappningshjälp ingår.
Spelval, filimport och terminalutdata i realtid är också lokaliserade.
Utseende, systemkrediter, patchar och beroendeinstallation är lokaliserade.

`Localizable.strings`, hjälpkoden, en lokaliseringsguide och
`check_localization.py` är arkiverade här som en exakt kopia av leveransen.

## Kontroller

- `swift build` – godkänd.
- `plutil -lint` – godkänd.
- `check_localization.py` – 366 använda nycklar finns i svenska katalogen.
- `l10n-lint --language sv` – godkänd utan anmärkningar.
- `svlang skrivregler` – godkänd utan anmärkningar.
- Hunspell-träffar granskade: `NxNative`, `Launcher`, `.app`, `.ipa`, `Xbox`
  och tekniska sammansättningar är avsiktliga.
- Gitleaks på den nya resurskatalogen – inga hemligheter.

## Upstreamresultat

PR #3 stängdes 2026-10-28 utan merge. Projektägaren förklarade i
[slutkommentaren](https://github.com/rennan101/nxnative_Launcher/pull/3#issuecomment-6477884610)
att projektet hade bytt till en reaktiv språkmotor med inbyggd språkväxlare.
Hela den svenska katalogen importerades i den nya systemet som **Svenska**,
med kreditering till bidraget, och ägaren uppgav att den är live i release
`v1.6.3`.

Det här är därför en faktisk uppströmsleverans, även om GitHub-PR:n inte
mergades. Kvarvarande råa litteraler är produktnamn, titel- och versions-ID:n,
sökvägar, loggrader eller tekniska värden och ska inte översättas. Följ endast
nya källsträngar och senare releaser.

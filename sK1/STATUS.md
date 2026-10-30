# sK1 svensk översättning

2026-10-26: Pågående utkast, 890 av 890 meddelanden från sk1-wx/po-sk1/sk1.pot. Ej färdigt eller inskickat. Baseras på lokalt granskade översättningar och förslag från Inkscapes svenska översättningsminne. Alla mallens strängar har utkast; hela katalogen behöver slutgranskas mot källkod och aktuell extraktion.

Senaste versionens utgivningsdatum är inte verifierat. GitHub har inga listade releaser eller taggar; projektets nedladdningssida anger 2.0 RC5. Källkoden har aktivitet 2025, vilket inte fastställer utgivningsdatumet.

msgfmt, l10n-lint och svlangs skrivregler körda på utkastet. l10n-lint gav informationsmeddelanden samt en varning för B&W, där ampersanden ingår i förkortningen och inte är en avsedd åtkomsttangent. Hunspell flaggade tekniska namn och svenska sammansättningar som behöver granskas igen när katalogen är klar.

2026-10-26: Tillkomna kontroller: sidintervallet 1,2,5-6 är avsedd inmatningssyntax och bevarar bindestrecket.

2026-10-26: Alla 890 mallposter har text. l10n-lint ger nio varningar, främst filformatsnamn som upprepas efter formatkod samt B&W och sidintervall. Slutgranskning och kontroll av aktuell mall återstår.

2026-10-26: xgettext med standardnyckeln `_` kördes separat på 158 Pythonfiler i sK1 (08fcdd0cea179e7d7a9be2883cc6208454dafa75) och på UniConvertor (973d5b6f8fccce7e7bf9bc88e91bc80f9f9d9472). Inga nya msgid jämfört med den befintliga mallen hittades: 752 respektive 146 unika källsträngar. Detta omfattar inte andra extraktionsnycklar, resurser eller beroenden. Alla 890 mallposter finns i utkastet och ingen översättning är tom. Slutgranskning återstår. Metadata saknar verifierad översättare och språkgrupp; msgfmt rapporterar detta som två varningar.

2026-10-26: Delvis slutgranskning av de första 350 katalogposterna. Källkodskontroll visar att ”File” används om en fil i dokumentinformation och felmeddelanden, så ”Arkiv” ändrades till ”Fil”. Inline-transformeringen tillämpar matrisen på kurvans punkter och nollställer transformationsmatrisen; termen ändrades till ”Baka in transformationer”. Övrig slutgranskning återstår.

2026-10-26: Katalogposterna 350–559 har granskats. Huvudmenyns åtkomsttangenter jämfördes med menubar.py; tangenterna för Arrangera och Rasterbilder ändrades för att undvika krockar med Arkiv och Redigera. Linjalens markörfärg förtydligades till graderingsfärg efter kontroll av koden. Fortsätt slutgranskningen från post 560.

2026-10-26: Katalogposterna 560–749 har granskats. Menykoden visar att ”Convert to B&W” är en menytext; tidigare antagande att & inte var åtkomsttangent var fel. Översättningen har nu en åtkomsttangent. Åtkomsttangenterna för spegling har också justerats för att undvika krockar i transformationsmenyn. Antalet markerade noder formuleras så att både ett och flera fungerar. Fortsätt från post 750.

2026-10-26: Katalogposterna 750–889 har granskats. Källkodens close-metod frigör dokumentmodellen, så ”förstörts” ändrades till ”frigjorts”. msgfmt --check godkänner katalogen men varnar fortfarande för de två saknade metadatafälten. Ingen körning av själva programmet har verifierats.

Utgivningskontroll: projektets nedladdningssida anger fortfarande 2.0 RC5. Den arkiverade källkodens appconst.py anger byggdatum 2021-08-31 (https://fossies.org/linux/misc/old/sk1-2.0rc5.tar.gz/sk1-2.0rc5/src/sk1/appconst.py), medan en extern releaseförteckning anger 2023-07-19 (https://freshcode.club/projects/sk1). Uppgifterna är motstridiga och inget officiellt publiceringsdatum har verifierats. 48-månaderskravet kan därför inte fastställas. Översättningen är fortsatt ett utkast och inte inskickad.

2026-10-26: Projektets byggverktyg använder PO-filnamnet som språkkod: po-sk1/sv.po ger sv/LC_MESSAGES/sk1.mo. Inställningsdialogen hittar installerade språkkataloger dynamiskt. En kompilerad MO-fil har lästs med Python gettext och gav ”Fil” för ”File”; detta är inte ett test av själva programmets gränssnitt. Arkivets releasepolicy kräver en bekräftat högst 48 månader gammal utgåva innan översättningsarbetet återupptas. Ingen inskickning har gjorts.

2026-10-26: Förnyad kontroll: projektets officiella nedladdningssida anger 2.0 RC5 men inget publiceringsdatum. Fossies arkiv anger 2021-08-31 för källpaketet; Freshcode anger 2023-07-19 för RC5. Datumen kan inte förenas med säkerhet och 48-månadersvillkoret är därför fortsatt inte styrkt. Utan verifierat releasedatum fortsätter ingen ytterligare översättningsgranskning enligt `RELEASE-FRESHNESS-POLICY.md`. En identisk arbetskopia ligger lokalt i `work/sk1-wx/po-sk1/sv.po` och är inte inskickad. Den arkiverade filen jämfördes med aktuell mall: 890 aktiva poster, inga saknade eller tomma. msgfmt godkände den med två metadataförbehåll; l10n-lint rapporterade åtta varningar, svlang inga skrivregelfel och Gitleaks inga fynd i filen. Programkörning är inte verifierad.

2026-10-27: En förnyad kontroll av den officiella sidan `sk1project.net`
visar fortfarande en odaterad nedladdning för 2.0 RC5. Den senaste daterade
officiella releaseposten som kunde verifieras är 2.0 RC4 från 2019-05-27.
Det styrker inte en aktuell RC5-utgåva och uppfyller inte 48-månaderskravet.
Utkastet lämnas därför arkiverat och oskickat.

2026-10-28: Officiella sK1-sidan och utvecklarresurserna kontrollerades igen.
De erbjuder fortfarande RC5 som nedladdning, men utan publiceringsdatum, och
beskriver dagliga byggen som icke-stabila snapshots. Den senaste verifierbara
officiella releaseposten är fortsatt RC4 från 2019-05-27. Kravet på en
verifierat högst 48 månader gammal release är alltså inte uppfyllt; ingen
fortsatt granskning eller uppladdning av det svenska utkastet görs.

2026-10-28: Undantag från utgåvekravet godkändes uttryckligen. Katalogen är
slutgranskad och komplett: 890 av 890 aktiva poster är översatta, utan osäkra
eller tomma poster. `msgfmt --check` passerar. l10n-lint rapporterar inga fel;
åtta varningar avser avsiktlig inmatningssyntax och filformatetiketter där
formatnamnet medvetet upprepas. Hunspell-träffarna är filformat, produktnamn
och etablerade facktermer. En avgränsad Gitleaks-kontroll hittade inga
hemligheter. Filens översättar- och språkgruppsmetadata har kompletterats.
Katalogen är färdig som lokalt och arkiverat svenskt underlag, men ännu inte
inskickad till något uppströmsflöde.

2026-10-29: Den färdiga katalogen skickades som
[PR #348](https://github.com/sk1-project/sk1-wx/pull/348) till `sk1-wx` den
28 oktober. PR:en har huvudcommit
`f3aee8b36f31aed68cbe46816d062c3b96334d23`, är mergebar och har inga öppna
kommentarer eller konfigurerade CI-kontroller. Den väntar på
underhållargranskning.

2026-10-30: GitHubs aktuella API-status bekräftar samma läge: PR #348 är
öppen, inte ett utkast, `mergeable: true` och `mergeable_state: clean` mot
`main`. Den har fortfarande inga granskningar, radkommentarer eller
check-körningar. Ingen ändring av den granskade katalogen behövs innan
underhållaren återkommer.

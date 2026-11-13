# RetroArch: upprepade bildrutor och nya kärnsträngar

Åtta nya svenska översättningar har granskats och skickats till RetroArchs Crowdin-projekt. De täcker inställningen för att hoppa över upprepade bildrutor, snabb bläddring i menyn och de nya Beetle PSX-, PCSX2- och Xemu-texterna om bildrutetaktning.

Varje Crowdin-post skapades via API och lästes sedan tillbaka med exakt måltext. Projektets svenska status är efter inskicket 10 015 av 10 015 fraser och 72 689 av 72 689 ord översatta. Ingen av de åtta nya posterna är godkänd i Crowdins granskningsflöde, så de är inskickade och synliga men inte verifierat godkända, mergade eller utgivna.

Kontrollerna omfattade JSON-validering, l10n-lint, Hunspell-sv, terminologikontroll mot [TERMINOLOGY.md](TERMINOLOGY.md), diffkontroll och Gitleaks. `msgfmt` är inte tillämpligt eftersom inskicket består av Crowdins JSON-enheter. Hunspell markerar endast produktnamn, förkortningar och sammansatta facktermer; inga stavfel hittades. Se [detaljerat underlag](retroarch-sv-frame-repeat-batch-20261113.json).

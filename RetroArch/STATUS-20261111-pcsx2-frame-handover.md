# RetroArch PCSX2: bildruteöverlämning

- Plattform: Crowdin, RetroArch (projekt-id `380544`), språk `sv-SE`.
- Komponent: `pcee2-libretro.json` (fil-id `60503`).
- Omfattning: Alla fem då oöversatta strängar i komponenten.
- Lokala deltafiler: `retroarch-sv-pcsx2-frame-handover-20261111.json` och
  `retroarch-sv-pcsx2-frame-handover-20261111.po`.

Granskningen gäller PCSX2:s bilinjär filtrering och inställningen för vilken
färdig bildruta som lämnas över till RetroArch. Den använder *renderare* för
den komponent som återger grafik samt *bildruteöverlämning*,
*bildrutetakt* och *inmatningsfördröjning* för det konkreta bildruteflödet.

Kontroller: `msgfmt --check` kompilerar PO-filen. Den minimala deltafilen
saknar avsiktligt fullständiga katalogmetadata, vilket ger fem ofarliga
huvudvarningar. l10n-lint godkänner både JSON- och PO-filen utan anmärkning.
Hunspell-SV markerar endast produktnamn, förkortningar, den avsiktliga
samordnade sammansättningen `maskin- och programvarurenderare` och nya
facktermer. Svlang ger två falska V2-larm för den korrekta inledningen
`I läget Samma steg väntar RetroArch ...` och för de fristående UI-etiketterna.
Taggar och platshållare, em dash-regeln, diffkontroll och Gitleaks är
godkända.

Arkivstatus: lokalt granskat och arkiverat. Upstream-inskick, godkännande och
publicerad projektversion dokumenteras först efter verifierad åtgärd.

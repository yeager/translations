# PCSX2: VU-spelfixar, 14 november 2026

Sex kryssrutor för VU-relaterade spelfixar var fortfarande helt engelska i
både helskärmsgränssnittet och Qt-inställningarna. Källkommentarerna anger
att `VU`, `Add`, `I Bit` och `XGKick` är namn på processor- eller
maskininstruktioner. De behålls därför oförändrade. Den övriga texten
normaliseras till PCSX2:s etablerade svenska tekniska form: `-hack` som i
`TLB-hack`, samt `synkronisering` för `Sync`.

Kontroller före inskick: XML, l10n-lint, platshållare, Hunspell-sv med sänkt
prioritet på endast de nya måltexterna, svlang, diffkontroll och Gitleaks.
`msgfmt` är inte tillämpligt på XLIFF. Upstream-resultat dokumenteras efter
API-import och återläsning.

## Verifierat inskick

Crowdins API importerade deltan till projekt `561203`, fil `15`, språk
`sv-SE`. Direkt återläsning bekräftar kandidaterna `450049` för `8745`,
`450051` för `9951`, `450053` för `9961`, `450055` för `10013`, `450057`
för `10015` och `450059` för `10021`. Kandidaterna är inskickade upstream,
men inte upstreamgranskade, automatiskt godkända eller valda som aktiva
översättningar.

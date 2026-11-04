# Terminologiverifiering: Blender-komponenter

Datum: 2026-11-04

## Underlag och avgränsning

Granskningen omfattar de lokala exporter som finns i
`exports/2026-11-04`:

| Komponent | Underlag | Resultat |
| --- | --- | --- |
| Blender UI | `blender-ui-ui-sv.po` | Källtermerna och deras kontextposter har jämförts mot `TERMINOLOGY.md` och tidigare granskad Blender-data. `msgfmt --check` godkänns. |
| Blender Manual | `blender-manual-manual-sv.po` | Termträffar har jämförts mot termlistan och UI-exporten. Hela råexporten innehåller 58 dubblettdefinitioner och kan därför inte valideras som en enda PO-fil med `msgfmt`; detta är ett källartefaktfel, inte ett fel i en deltafil. Deltafiler valideras var för sig. |
| Manual-webbgränssnitt | `blender-manual-manual-web-ui-4-5-sv.po` | `msgfmt --check` och l10n-lint godkänns. Komponentens begränsade termmängd ger ingen avvikelse från huvudtermerna. |
| Manualens ordlista | `blender-manual-glossary-sv.tbx` | Innehåller belagda former för `AOV` / `Godtyckliga utgångsvariabler`, `Parent` / `Förälder`, `Shape Key` / `Formnyckel` och `Working Plane` / `Arbetsplan`. |

Det externa underlaget
`work/swedish-foss-terminology/reviewed/data/blender.jsonl` har också
använts som översättningsminne. Äldre poster där är evidens för tidigare
granskning, men utgör inte en generell normaliseringsregel utan UI-kontext.

## Belagda och godkända termer

| Engelska | Rekommenderad svensk form | Belägg och omfattning |
| --- | --- | --- |
| data-block / Data-Block | datablock / Datablock | Lokal termlista, UI-exporten och det granskade FOSS-underlaget. API-identifierare behålls oförändrade. |
| vertex | hörnpunkt / hörn | *Hörnpunkt* i mesh- och verktygskontext; *Hörn* får stå kvar i korta vy- eller orienteringsetiketter. |
| bevel | avfasning; avfasningsmodifierare | UI-underlag och den dubbelgranskade mesh-dokumentationen. Verbformerna är `Fasa hörnpunkter` och `Fasa kanter`. |
| displacement | förskjutning | UI-exporten och FOSS-underlaget är samstämmiga. `Vector Displacement` hanteras som `vektorförskjutning` när den är synlig UI-text. |
| Adaptive Subdivision | adaptiv underindelning | Belagd UI-form; ersätter den mindre precisa bokstavliga formen *adaptiv indelning*. |
| slot | slot | Blender-specifik animerings- och UI-term. `Slott` är fel i denna kontext. Sammansättningar: `slothandtag`, `slotidentifierare`, `slotvisningsnamn`, `åtgärdsslothandtag`. |
| action | åtgärd | Gäller animeringsdata och instruktionstext. Formella API- och datatypsnamn som `Action` lämnas oförändrade. |
| F-Curve | F-kurva | Samstämmigt i UI, manual och tidigare granskat termunderlag. |
| Library Override | biblioteksåsidosättning / biblioteksöverskrivning | Kontextstyrd UI-term; se avvikelser nedan. |
| Append | Lägg till | Verbet för Blenders dataläggning. FOSS-underlag och UI stödjer formen. |
| Link | Länka / Länk | `Länka` för operatorn, `länk` för substantiv. Måste väljas efter ordklass. |
| USD Preview | USD Preview | Synligt produkt-/nodnamn. Ska inte försvenskas till *USD-förhandsgranskning*. |
| AOV | AOV; godtyckliga utgångsvariabler | Behåll den korta UI-etiketten. Använd den svenska förklarande TBX-formen i dokumentation. |
| Parent | förälder | Belagd i TBX och UI-hierarki. |
| Shape Key | formnyckel | Belagd i TBX och UI. |
| Working Plane | arbetsplan | Belagd i TBX. |

## Avvikelser som kräver strängkontext

| Term | Observation | Beslut |
| --- | --- | --- |
| Library Override | Äldre FOSS-termdata innehåller `Biblioteksöverstyrning`, medan den aktuella lokala UI-katalogen och termlistan använder både *biblioteksåsidosättning* och *biblioteksöverskrivning*. | Ändra inte globalt. Följ den närliggande operatorn/panelen och dokumentera varje ny form i deltafilen. |
| Mesh | Äldre FOSS-data innehåller även `Nät`; den aktuella Blender-terminologin använder *mesh* när det är Blender-datatyp eller etablerad UI-beteckning. | Behåll *mesh* i Blender-specifik kontext. *Nät* kan endast användas där UI- eller saktextens betydelse faktiskt är ett geometriskt nät. |
| Link | Tidigare termdata innehåller `Länk`, medan operatorn i UI är `Länka`. | Bestäm efter ordklass och om strängen är en synlig operator. |
| Vertex | Både `Hörn` och `Hörnpunkt` är korrekta i skilda UI-kontexter. | Ingen maskinell ersättning. Kontrollera verktyg, orientering och meshkontext. |
| Shader och nodnamn | Engelska namn kan vara etablerade Blender-namn, medan omgivande förklaring ska vara svensk. | Bevara produkt-/nodnamn; översätt beskrivande text och generiska sammansättningar. |

## Säkra tillägg till `TERMINOLOGY.md`

Följande tillägg är belagda men har ännu inte förts in i termlistan:

| Engelska | Svenska | Anmärkning |
| --- | --- | --- |
| bevel | avfasning | Operation och sakbegrepp. |
| Bevel Modifier | avfasningsmodifierare | Blendermodifierare i UI och manual. |
| Bevel Vertices / Bevel Edges | Fasa hörnpunkter / Fasa kanter | Synliga operatornamn. |
| displacement | förskjutning | Shader- och materialkontext. |
| Vector Displacement | vektorförskjutning | Synlig UI- och manualterm. |
| Adaptive Subdivision | adaptiv underindelning | UI-belagd form. |
| Material Output | materialutdata | UI-belagd form i renderingskontext. |
| USD Preview | USD Preview | Skyddad produkt-/nodetikett, översätt inte. |

## Verktygsspår

- `msgfmt --check` godkände UI- och manual-webbgränssnittsexporterna.
- Hela manualexporten stoppas av 58 dubblettdefinitioner i källan. Detta
  hanteras genom separata deltafiler med exakta källposter, där `msgfmt`
  godkänns.
- l10n-lint godkände manual-webbgränssnittsexporten utan fel eller varningar.
- Träffar i Hunspell för tekniska identiteter, RST och API-namn bedöms inte
  som stavningsfel utan kontext.
- Denna rapport ändrar inte några PO- eller TBX-filer.

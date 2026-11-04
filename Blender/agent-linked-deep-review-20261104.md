# Huvudgranskning av kandidater: länkade bibliotek

Datum: 2026-11-04  
Underlag: råexporten, Blender-UI-katalogen och
`agent-linked-deep-candidates-20261104.md`.

| Referens | Bedömning | Godkänd måltext eller skäl |
| --- | --- | --- |
| `library_overrides.rst:385` | Godkänd | `Tvinga omsynkronisering`. Den exakta UI-posten `Resync Enforce` använder redan denna översättning. |
| `library_overrides.rst:411` | Godkänd | `Ta bort hela biblioteksåsidosättningshierarkin och ersätt alla dessa åsidosättningsdatablock med deras ursprungliga länkade datablock. Detta återställer *Make*-åtgärden helt.` |
| `link_append.rst:3` | Godkänd | `Länka och lägg till`. *Append* är här en Blender-åtgärd, inte en bilaga. |
| `link_append.rst:11` | Godkänd | `I stället för att använda menyn kan du också länka till eller lägga till blend-filer genom att dra och släppa dem i Blender-fönstret.` |
| `link_append.rst:72` | Godkänd | `Instanssamlingar`. Sammansättningen beskriver samlingar som används för instansiering utan att vända relationen som i den gamla måltexten. |
| `link_append.rst:81` | Skjut upp | `Instance Object Data` saknar tillräcklig UI-evidens för den föreslagna sammansättningen `Instansobjektdata`. Den kan läsas som objektdata som själv är en instans, medan källan beskriver instansiering av objektdata. Ändra inte förrän aktuell panel- eller operatortext har jämförts. |
| `link_append.rst:253` | Godkänd | `Inställningar på scennivå`. |
| `link_append.rst:265` | Godkänd | `Att referera till :ref:`komprimerade <files-blend-compress>` blend-filer kan kräva mycket minne eftersom de måste läsas in helt, även om du bara länkar till eller lägger till en liten del av dem. När datablocken väl har lästs in är minnesanvändningen dock densamma.` |

## Markup och terminologi

`Resync Enforce` har verifierats mot den aktuella UI-katalogen. RST-målet
`files-blend-compress`, markeringen `*Make*` och det etablerade formatnamnet
*blend-fil* måste bevaras i en senare deltafil. Sju av åtta kandidater kan
alltså gå vidare till radvis inarbetning; en är medvetet uppskjuten.

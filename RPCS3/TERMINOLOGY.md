# RPCS3, svensk terminologi

Senast kontrollerad: 2026-11-11.

| Engelska | Svenska | Kontext och avgränsning |
| --- | --- | --- |
| `render` | **rendera** | Verb för GPU:ns grafikframställning. |
| `rendering` | **rendering** | Substantiv för själva GPU-processen, exempelvis `Hybridrenderingsläge`. I annan, tydligt visningsinriktad kontext kan `återgivning` vara rätt. |
| `renderer` | **renderare** | Programkomponent som renderar. Behåll API- och drivrutinsnamn oförändrade. |
| `interpreter` | **tolk** | Beräkningskomponent. Använd sammansättningen `shader-tolk` när den specificeras av `shader`. |
| `recompiler` | **omkompilerare** | Exempelvis `PPU-omkompileraren` och `Asynkron omkompilerare`. |
| `shader` | **shader** | Etablerad grafikteknisk term i RPCS3. Skriv sammansättningar som `shadercache`, `shaderkompilering` och `shader-tolk` efter den konkreta UI-kontexten. |

Underlag: den befintliga svenska RPCS3-katalogen, särskilt dess
shaderinterpreter- och kompilatorsträngar, samt den lokala
`rpcs3_sv-SE_crowdin-20261109-rendering-terminology.ts`.

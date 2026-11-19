# Sparade ändringar för Google Generative AI

Sparade och återlästa i Lokalise 2026-11-19 efter jämförelse med tidigare granskningsrapport.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::google_generative_ai_conversation::config_subentries::conversation::step::set_options::data_description::thinking_level` | Thinking level for Gemini 3 and later text models, including the latest aliases. Unsupported levels use the model default; the saved choice is kept. Gemini 2.5 uses the thinking budget instead. "Minimal" does not guarantee that thinking is off. | Tankenivå för Gemini 3-modeller. Ignoreras för Gemini 2.5-modeller, som använder tankebudgeten istället. "Lägsta" garanterar inte att tänkandet är felaktigt. | Tankenivå för textmodeller från Gemini 3 och senare, inklusive alias för de senaste modellerna. Om nivån inte stöds används modellens standardnivå, men ditt val sparas. Gemini 2.5 använder tankebudgeten i stället. ”Lägsta” garanterar inte att tänkandet är avstängt. |

Den tidigare texten utelämnade villkoren för modellens standardnivå och uttryckte ”off” felaktigt.

## Återställda referenser

Båda följande källnycklar hänvisar till den gemensamma texten ovan. Svenskan bestod tidigare av en separat text, ”Resonemangsnivå för Gemini 3 och senare textmodeller, inklusive de senaste aliasen. Nivåer som inte stöds använder modellens standardvärde. Det sparade valet behålls. Gemini 2.5 använder i stället tokenbudgeten. "Minimal" garanterar inte att resonemang är avstängt.” Referensen återställdes i båda och lästes tillbaka:

- `component::google_generative_ai_conversation::config_subentries::stt::step::set_options::data_description::thinking_level`
- `component::google_generative_ai_conversation::config_subentries::ai_task_data::step::set_options::data_description::thinking_level`

Sparat referensvärde: `[%key:component::google_generative_ai_conversation::config_subentries::conversation::step::set_options::data_description::thinking_level%]`. Referenser registreras separat från TMX-textpar.

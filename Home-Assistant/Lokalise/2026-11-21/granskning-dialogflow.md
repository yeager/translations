# Home Assistant Core – Dialogflow

Datum: 2026-11-21

Alla 9 aktuella strängar jämfördes med Core `2fdaa177` och direkt återlästes från Lokalise. Markdown, kodformaterade URL:er, Dialogflow-länkar och `{dialogflow_url}`, `{webhook_url}` samt `{docs_url}` kontrollerades.

| Nyckel | Befintlig text | Sparad text | Motivering |
| --- | --- | --- | --- |
| `config::create_entry::default` | Indrag före `Fyll ...` | Indrag borttaget | Bevarar korrekt Markdown-layout. |
| `config::abort::reconfigure_successful` | `Metod` / `Innehållstyp` | `Method` / `Content Type` | Samma Dialogflow-inställningsetiketter som i grundflödet. |
| `config::step::reconfigure::title` | `Dialogflow webhook` | `Dialogflow-webbhook` | Korrekt svensk sammansättning. |

Ändringarna PUT-sparades och direkt återlästes. Det verifierade Core-TMX-minnet validerades efter uppdateringen till 2 066 poster.

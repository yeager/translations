# Frigate NVR – svensk terminologi

Senast uppdaterad: 2026-11-15  
Källor: Frigate UI och konfiguration på `dev`, redan granskade svenska batcher,
svensk FOSS-terminologi.

| Engelska | Rekommenderad svenska | Sammanhang och undantag |
| --- | --- | --- |
| camera | kamera | Allmänt gränssnitt och konfiguration. |
| camera group | kameragrupp | Navigering och ordning. |
| stream | ström | Video- eller ljudström. |
| restream | återströmning | Används för go2rtc. |
| live view | livevy | Vy, panel och uppspelning. |
| live playback | liveuppspelning | Inställning eller meny. |
| object detection | objektdetektering | Detektering av objekt. |
| detection | detektering | Behåll distinktionen mot tracking. |
| tracked object | spårat objekt | Objekt som följs över tid. |
| tracking | spårning | Objektspårning i UI och varningar. |
| motion detection | rörelsedetektering | Feature eller inställning. |
| motion mask | rörelsemask | Mask för att utesluta rörelse. |
| object mask | objektmask | Mask för att utesluta objekt. |
| zone | zon | Kamerazon. |
| bounding box | begränsningsruta | Detekteringsgeometri. |
| snapshot | ögonblicksbild | Inte “skärmbild”. |
| thumbnail | miniatyrbild | Förhandsbild för händelse. |
| preview | förhandsvisning | Videoförhandsvisning eller bild. |
| recording | inspelning | Inspelad video. |
| review | granskning | Substantiv i vyer och inställningar. |
| review item | granskningsobjekt | Element i granskningsvyn. |
| event | händelse | Allmän händelse i Frigate. |
| alert | varning | Händelsekategori, inte systemfel. |
| retention | lagringstid | Konfigurationssammanhang. |
| media sync | mediesynkronisering | Underhållsfunktion. |
| orphaned file | överbliven fil | Fil utan databasreferens. |
| region grid | regionsrutnät | Frigates optimeringsfunktion. |
| face recognition | ansiktsigenkänning | Feature/enrichment. |
| face detection | ansiktsdetektering | Skilj från igenkänning. |
| license plate recognition | registreringsskyltigenkänning | LPR i förklarande text. |
| LPR | LPR | Behåll förkortningen i tekniska värden/namn. |
| semantic search | semantisk sökning | Funktion och meny. |
| embedding | inbäddning | Modell- och databasbegrepp. |
| audio transcription | ljudtranskribering | Funktion. |
| classifier/classification | klassificerare/klassificering | Modeller och inställningar. |
| enrichment | berikning | Funktion som förbättrar objektdata. |
| confidence | säkerhet | Poäng eller tröskel för detektering. |
| threshold | tröskelvärde | Inte “tröskel” i UI när värde avses. |
| override | åsidosättning | Konfiguration och profiler. |
| profile | profil | Konfigurationsprofil. |
| base configuration | baskonfiguration | Profilernas utgångspunkt. |
| global configuration | global konfiguration | Konfiguration för alla kameror. |
| default | standardvärde | “default” som kodvärde lämnas oförändrat. |
| preset | förinställning | FFmpeg- och PTZ-val. |
| inference | inferens | Teknisk modellkörning. |
| model | modell | Detekterings- och AI-modeller. |
| model size | modellstorlek | `small`/`large` lämnas oförändrade som värden. |
| device | enhet | Valbar beräkningsenhet. |
| hardware acceleration | maskinvaruacceleration | Video och modeller. |
| object label | objektetikett | Identifierare i modeller. |
| label map | etikettkarta | Modellens klassmappning. |
| role | roll | Ström- eller användarroll; skilj via kontext. |
| role mapping | rollmappning | Autentisering. |
| API key | API-nyckel | Standardterm. |
| reverse proxy | omvänd proxy | Nätverkskonfiguration. |
| secure context | säkert sammanhang | Webbläsarkrav för push. |
| web push notification | web push-avisering | UI-funktion. |
| configuration file | konfigurationsfil | YAML nämns explicit när relevant. |
| restart required | omstart krävs | Kort UI-text. |
| save | spara | Verb i knapp och återkoppling. |
| apply | tillämpa | Göra konfigurationsändring verksam. |

## Lämnas oförändrat

Frigate, Frigate+, Birdseye, go2rtc, FFmpeg, MQTT, ONVIF, TLS, RTSP, RTMP,
HTTP, URL, YAML, GenAI, GPU, CPU, NPU, LPR, OCR, VAAPI, CUDA, VideoToolbox,
H.264, H.265, AAC, Opus, PCM, MP3, Raspberry Pi, NVIDIA, Intel QuickSync,
Ubiquiti, Reolink och Blue Iris. Bevara även platshållare som `{{cameraName}}`,
HTML-markup, URL:er och kodvärden som `'small'`, `'large'`, `'recordings'` och
`'descriptions'` exakt.

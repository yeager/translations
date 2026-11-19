# RetroArch – VBlank-baserad bildsynkronisering, svensk granskningsbatch 2026-11-19

Den sista av de 81 oöversatta svenska strängarna i RetroArchs huvudfil msg_hash_us.json har granskats från aktuella Crowdin API-svar. Förslaget är inte sparat eller skickat till Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 6237565 | With Threaded Video Display Pacing, V-Sync off and fullscreen, release each core frame on the display's own vblank events instead of a timer. Applies where the display server has those events (Windows, KMS, X11, Wayland) and the video driver's present tears rather than waits (Direct3D 11/12, Vulkan; OpenGL through DXGI, on KMS, or past the compositor); the timer paces elsewhere, and wherever the events stop or keep no fixed rate. The tear line then stays at one height. Off: the timer, as before. | — | Med trådad bildsynkronisering, avstängd V-Sync och helskärm släpps varje bildruta från kärnan vid skärmens egna vblank-händelser i stället för med en timer. Detta gäller där bildskärmsservern har sådana händelser (Windows, KMS, X11, Wayland) och videodrivrutinens presentering släpper igenom tearing i stället för att vänta (Direct3D 11/12, Vulkan; OpenGL via DXGI, på KMS eller förbi kompositorn). Timern styr i stället takten på andra ställen samt när händelserna upphör eller saknar fast frekvens. Tearinglinjen ligger då kvar på samma höjd. Av: timern, som tidigare. |

## Kontroll och terminologi

- Teknologier, versionsnummer och plattformsnamn är oförändrade: V-Sync, Windows, KMS, X11, Wayland, Direct3D 11/12, Vulkan, OpenGL och DXGI.
- *vblank-händelser*, *presentering*, *tearing* och *kompositorn* används som tekniska termer för att bevara betydelsen i den ursprungliga prestandabeskrivningen.
- Inga platshållare, markup-taggar eller URL:er förekommer.
- RetroArchs projekt-TM saknade en relevant tillräckligt nära träff.
- l10n-lint med svenska regler passerade utan anmärkningar.
- Hunspell-sv och Crowdins förhandsvalidering markerade tekniska termer, men ingen annan QA-kategori flaggade strängen.

## Omfattning

Detta slutför utkastgranskningen av de 81 strängar som saknade svensk översättning i huvudfilen vid API-hämtningen. Alla förslag är fortfarande osparade i Crowdin.

# RetroArch – extra shaderbildrutor, svensk QA-rättning 2026-11-19

En befintlig svensk översättning i `msg_hash_us.json` har granskats via Crowdins QA-API. Förslaget är inte sparat eller skickat till Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 5124358 | Inserts extra shader frame(s) inbetween frames for any possible shader effects that are designed to run faster than content rate. Only use option designated for your current display refresh rate. Not for use at refresh rates that are non-multiples of 60Hz such as 144Hz, 165Hz, etc. Do not combine with Swap Interval > 1, BFI, Frame Delay, or Sync to Exact Content Framerate. Leaving system VRR on is ok, just not that setting. | Lägger in extra shaderbildrutor mellan bildrutorna för shader-effekter som är avsedda att köras snabbare än innehållets hastighet. Använd bara alternativet som är avsett för bildskärmens aktuella uppdateringsfrekvens. Använd det inte vid uppdateringsfrekvenser som inte är multiplar av 60 Hz, till exempel 144 Hz och 165 Hz. Kombinera det inte med växlingsintervall över 1, BFI, bildrutefördröjning eller synkronisering med innehållets exakta bildfrekvens. Systemets VRR kan vara på, men inte den här inställningen. | Lägger in extra shaderbildrutor (en eller flera) mellan bildrutorna för shader-effekter som är avsedda att köras snabbare än innehållets hastighet. Använd bara alternativet som är avsett för bildskärmens aktuella uppdateringsfrekvens. Använd det inte vid uppdateringsfrekvenser som inte är multiplar av 60 Hz, till exempel 144 Hz och 165 Hz. Kombinera det inte med växlingsintervall över 1, BFI, bildrutefördröjning eller synkronisering med innehållets exakta bildfrekvens. Systemets VRR kan vara på, men inte den här inställningen. |

## Kontroller

- Källans parentesmarkering för `frame(s)` är återställd som ”(en eller flera)”; Crowdins ursprungliga parentes-QA-träff är därmed löst.
- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` och Crowdins slutliga QA markerar bara shaderbildrutor, shader-effekter och bildrutefördröjning: korrekta tekniska sammansättningar.
- Tal, jämförelseoperatorn `> 1` och övrig teknisk formatering är bevarade.

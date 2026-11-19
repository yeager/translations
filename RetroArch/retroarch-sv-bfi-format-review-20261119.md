# RetroArch – svarta bildrutor, svensk QA-rättning 2026-11-19

En befintlig svensk översättning i `msg_hash_us.json` har granskats via Crowdins QA-API. Förslaget är inte sparat eller skickat till Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 5124352 | Inserts black frame(s) inbetween frames for enhanced motion clarity. Only use option designated for your current display refresh rate. Not for use at refresh rates that are non-multiples of 60Hz such as 144Hz, 165Hz, etc. Do not combine with Swap Interval > 1, sub-frames, Frame Delay, or Sync to Exact Content Framerate. Leaving system VRR on is ok, just not that setting. If you notice -any- temporary image retention, you should disable at 120hz, and for higher hz adjust the dark frames setting below. | Lägger in svarta bildrutor mellan bildrutorna för att öka rörelseklarheten. Använd bara alternativet som är avsett för bildskärmens aktuella uppdateringsfrekvens. Använd det inte vid uppdateringsfrekvenser som inte är multiplar av 60 Hz, till exempel 144 Hz och 165 Hz. Kombinera det inte med växlingsintervall över 1, delbildrutor, bildrutefördröjning eller synkronisering med innehållets exakta bildfrekvens. Systemets VRR kan vara på, men inte den här inställningen. Om du märker tillfälliga efterbilder ska du inaktivera funktionen vid 120 Hz. Vid högre frekvenser justerar du inställningen för mörka bildrutor nedan. | Lägger in svarta bildrutor (en eller flera) mellan bildrutorna för att öka rörelseklarheten. Använd bara alternativet som är avsett för bildskärmens aktuella uppdateringsfrekvens. Använd det inte vid uppdateringsfrekvenser som inte är multiplar av 60 Hz, till exempel 144 Hz och 165 Hz. Kombinera det inte med växlingsintervall över 1, delbildrutor, bildrutefördröjning eller synkronisering med innehållets exakta bildfrekvens. Systemets VRR kan vara på, men inte den här inställningen. Om du märker tillfälliga efterbilder ska du inaktivera funktionen vid 120 Hz. Vid högre frekvenser justerar du inställningen för mörka bildrutor nedan. |

## Kontroller

- Källans parentesmarkering för `frame(s)` är återställd som ”(en eller flera)”; Crowdins ursprungliga parentes-QA-träff är därmed löst.
- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` markerar VRR och bildrutefördröjning; Crowdins slutliga QA markerar endast den korrekta sammansättningen bildrutefördröjning.
- Tal, jämförelseoperatorn `> 1` och övrig teknisk formatering är bevarade.

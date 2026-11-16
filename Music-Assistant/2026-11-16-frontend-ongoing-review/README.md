# Music Assistant Frontend – pågående svensk granskning

Datum: 16 november 2026

Gränssnittets 2 880 svenska strängar granskas rad för rad. Detta underlag
beskriver endast det arbete som är färdigt och sparat hittills; det innebär
inte att hela komponenten är färdiggranskad.

603 strängar har rättats och återlästs via Lokalise API. Rättningarna omfattar
bland annat inläsning och hämtning, svenska benämningar för tillägg, mål i
stället för destination, en felkopplad mobilvytext, nollbreddsmellanslag och
felaktig engelskpåverkad terminologi. Den senaste genomgången omfattar också
frågesport, AI-radio, DSP, faltning, spelarkonfiguration, behörigheter,
lagring, poddar, statistik, marknadsplatsen och MilkDrop.

Den uppdaterade resursen passerar svlang. l10n-lint hittar inga fel, men 10
befintliga katalogomfattande varningar återstår för bland annat skiljetecken
och terminologisk konsekvens utanför denna delgenomgång. Hunspell-sv har körts
med begränsad CPU-tid och markerar bara kända produktnamn, protokoll, format,
platshållare och sammansättningar som saknas i ordlistan. Inga tomma svenska
strängar finns enligt Lokalise API.

En sparad och återläst översättning betyder inte att en ny version av
gränssnittet har byggts eller publicerats.

# Music Assistant Frontend – komplett svensk granskning

Datum: 16 november 2026

Gränssnittets samtliga 2 880 svenska strängar har granskats rad för rad och
återlästs från Lokalise API.

934 strängar har rättats och återlästs via Lokalise API. Rättningarna omfattar
bland annat inläsning och hämtning, svenska benämningar för tillägg, mål i
stället för destination, en felkopplad mobilvytext, nollbreddsmellanslag och
felaktig engelskpåverkad terminologi. Den senaste genomgången omfattar också
frågesport, AI-radio, DSP, faltning, spelarkonfiguration, behörigheter,
lagring, poddar, statistik, marknadsplatsen och MilkDrop.

Den uppdaterade resursen passerar svlang och l10n-lint utan fel eller
varningar. Hunspell-sv har körts med begränsad CPU-tid och markerar 169
kända produktnamn, protokoll, format, platshållare och sammansättningar som
saknas i ordlistan. Gitleaks hittar inga hemligheter. Inga tomma svenska
strängar finns enligt Lokalise API.

En sparad och återläst översättning betyder inte att en ny version av
gränssnittet har byggts eller publicerats.

En senare [livekontroll](../2026-11-16-non-server-live-status/README.md)
bekräftar också 100 % och 0 återstående svenska ord för Frontend, Desktop och
Mobile.

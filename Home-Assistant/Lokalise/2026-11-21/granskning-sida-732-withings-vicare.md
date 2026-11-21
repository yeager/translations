# Home Assistant Core – sida 732: granskningsstatus

Datum: 2026-11-21  
Plattform: Lokalise API  
Omfattning: 100 aktiva nycklar, sida 732 av 752 (`limit=100`)

## Käll- och API-kontroll

- Batchen hämtades färskt från Lokalise med engelska och svenska mål i samma svar.
- Berörda Core-källfiler kontrollerades i den rena lokala Core-kopian för `withings`, `vicare`, `izone`, `edifier_infrared`, `open_router`, `system_bridge`, `ezviz`, `fressnapf_tracker` och `bosch_shc`.
- Inga tomma svenska synliga mål, platshållaravvikelser eller pluralavvikelser finns i batchen.

## Bedömning

Withings träningsformer (bland annat `Gymnastics`, `Handcycling`, `Indoor rowing`, `Nordic skiing`, `Stand-up paddleboarding` och `Water skiing`) är semantiskt korrekta och konsekvent formulerade. Teknik- och sportnamn som `HIIT`, `Padel`, `Qigong`, `Teqball`, `Ultimate frisbee` och `Spikeball` behölls avsiktligt.

ViCare-statusarna, iZone-meddelandet, Edifier-linjeingången, OpenRouter-resonemangsnivåerna, System Bridge-feltexterna, Ezviz MFA-flödet, Fressnapf Tracker-prenumerationsstatusen och Bosch SHC-orienteringsbelysningen stämmer mot engelsk källa. Platshållarna `{name}`, `{exit_code}` och `{error}` är bevarade.

## Resultat

Inga ändringar föreslogs eller sparades för sida 732. Batchen är dokumenterat radgranskad mot aktuell API- och Core-källtext.

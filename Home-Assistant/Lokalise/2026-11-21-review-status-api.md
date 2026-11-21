# Lokalise – markering som granskad

Datum: 2026-11-21

För de dokumenterat radgranskade Core-strängarna testades Lokalises API-flagga `is_reviewed` med aktuell måltext bevarad i begäran. API:t returnerade konsekvent HTTP 403 med meddelandet `No permission to update translation status`.

Tokenen kan läsa och uppdatera själva svenska översättningstexten, men den tillhörande Lokalise-rollen saknar behörighet att ändra granskningsstatus. Kontrolläsning av representativa strängar bekräftade att de fortfarande har `is_reviewed: false`; inga oavsiktliga statusändringar gjordes.

När tokenen eller projektrollen får rättigheten att uppdatera translation status kan samma verifierade komponenturval markeras i batch utan att någon svensk text skrivs om.

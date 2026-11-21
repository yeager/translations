# Home Assistant Core – Weather

Datum: 2026-11-21

Alla 50 Weather-strängar har granskats mot aktuell källa och tidigare backup. Tre fel är rättade, sparade och API-återlästa.

`Lightning, rainy` har en naturlig svensk kombinationsstatus. Enhetstjänsten använder nu samma tydliga verbform som flertalsvarianten, och avvecklingsmeddelandet bevarar åtgärdens kodnamn som inline-kod. Övriga väderstatusar, attribut och prognossträngar är korrekta.

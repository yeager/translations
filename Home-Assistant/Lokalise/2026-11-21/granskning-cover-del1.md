# Home Assistant Core – Cover, kärna och tidsfält

Datum: 2026-11-21

68 aktuella Cover-strängar för titel, tillstånd, enhetsautomationer, serviceåtgärder och gemensamma fält kontrollerades mot Core `2fdaa177` och direkt återlästes. Två gemensamma tidsfält korrigerades från `I åtminstone` till `I minst`; de refererade underfälten återlästes och följer ändringen. `{entity_name}`, `{speed}` och `{supported_speeds}` är intakta. TMX-minnet är validerat till 2 013 poster.

I nästa triggerdel korrigerades även `component::cover::triggers::window_opened::fields::fully_opened::name` från `Helt öppnad` till `Helt öppet`; språkparet är verifierat i TMX-minnet, som validerades till 2 014 poster.

Återstående Cover-trigger- och villkorsfamiljer granskas separat.

# Zammad development: chattvy, 13 november 2026

Nitton svenska strängar i den nya chattvyn granskades och uppdaterades via Zammads Weblate-API. Gruppen innehöll både tomma strängar och felaktiga äldre måltexter, till exempel att en åtgärd för att avsluta en konversation hade ärvt texten för att starta en ny.

Varje post kontrollerades mot aktuell källtext före PATCH-begäran och lästes sedan tillbaka med tillståndet `translated`. Efter inskicket visar komponenten 5 343 av 5 418 översatta strängar; 60 behöver fortfarande redigeras och fyra har felande Weblate-kontroller. Inga poster från denna batch är godkända av en särskild granskare ännu.

Källunderlaget finns i [zammad-development-chat-repair-20261113.json](zammad-development-chat-repair-20261113.json). Zammad 7.4.0-alpha från 6 november 2026 bekräftar att projektet ligger inom den fastställda releasegränsen.

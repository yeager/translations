# Hosted Weblate: inskickad korrigering

`weblate-application-sv-pending-qa-fix-20261019.po` innehåller en verifierad pluralrättning:

- Den svenska pluralformen för ”The following component will lose access to its repository” avslutas med kolon, precis som singularformen och källtexten.

Den 19 oktober 2026 svarade Hosted Weblate först med HTTP 502. När tjänsten åter svarade skapades en XLIFF-deltafil med den exporterade enhetens oförändrade identitet. Weblates XLIFF-import kunde dock inte matcha någon av de två pluralenheterna. Samma lilla delta som PO importerades därefter korrekt: 1 av 1 enheter accepterades. En efterföljande XLIFF-export från Hosted Weblate bekräftade den uppdaterade pluralformen.

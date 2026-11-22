# Validerare: gettext-kontexter

Full validering av `swedish-tm` hittade ett verktygsfel: `sv-gnome.po` har 2 420 giltiga aktiva gettext-kontexter som redan finns med i motsvarande TMX, men valideraren avvisade dem generellt.

`scripts/validate.py` behandlar nu `(msgctxt, msgid)` som PO-identitet och jämför därefter PO- och TMX-parens multipliciteter. Därmed fångas fortfarande verkliga dubbletter och formatfel utan att giltiga kontextposter avvisas. Ändringen är pushad i `yeager/swedish-tm` på `ha-tmx-validator` (`4a8ffca`).

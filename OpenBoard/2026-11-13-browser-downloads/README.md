# OpenBoard, svensk granskning av webbläsare och hämtningar, 13 november 2026

OpenBoard är en fri digital skrivtavla för undervisning och presentationer. Den här avgränsade UI-batchen omfattar den inbyggda webbläsarens navigering, certifikatvarning och hämtningsfönster.

Ändringarna omfattar 21 färdigmarkerade Qt-strängar, bland annat:

- navigering och visning av hämtningar
- saklig varning vid overifierat TLS-certifikat
- hämtningens status, storleksenheter, avbrott och filöppning

Kontroller:

- Qt lrelease: 469 färdiga och 31 ofärdiga strängar, jämfört med 448 färdiga och 33 ofärdiga före batchen
- Hunspell-sv för ändrade svenska ord: godkänd
- diffkontroll: godkänd
- Gitleaks för deltan: godkänd
- l10n-lint: inga nya relevanta fel; rapporterar den befintliga platshållaren TextLabel, identiska enhetssymboler och avslutande blanktecken i källtexten
- svlang: katalogomfattande rapport med befintliga tekniska och engelska källsträngar; den används som granskningsunderlag, inte som godkännande för hela äldre katalogen

Upstream: inskickat som [OpenBoard PR #1581](https://github.com/OpenBoard-org/OpenBoard/pull/1581) den 13 november 2026. PR:en är öppen och väntar på granskning.

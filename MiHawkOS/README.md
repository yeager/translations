# MihawkOS – svenska

Utgångspunkt: `mihawk-99/PS5_MihawkOS` vid commit
`b91f6eeef116d824c4307129547dd35adbf42cbe` (2026-10-21).

Den svenska lokaliseringskomponenten omfattar den fullständiga
förstagångsguiden: 60 texter, `sv-SE.UTF-8`, Sveriges flagga och riktade
värdtester för språkval, platshållare, skrivbara tecken och decimalformat.

## Arkiverade filer

- `pw_setup_sv-20261026.c` – den kompletta svenska språktabellen.
- `test_pw_setup_sv-20261026.c` – testet utökat till tio tillgängliga språk.
- `se.svg` och `flags_SOURCE.json` – Sveriges flagga från den redan pinnade
  flag-icons-källan, med kontrollsumma.
- `swedish-setup-20261026.patch` – den begränsade uppströmsdiffen.
- `webui-sv-review-20261029.md` – granskning av den fullständiga svenska
  WebUI-katalogen och dess riktade tester.

## Granskning

- 60 av 60 textnycklar har svenska översättningar och samma platshållare som
  engelska källtexten.
- Riktat `test_pw_setup` godkänt: 10 av 10 språk har komplett text,
  skrivbara tecken, platsmarkörer och korrekt svenskt decimalformat.
- Hunspell-SV rapporterar bara etablerade produkt- och teknikord.
- `git diff --check` och Gitleaks för samtliga ändrade filer är godkända.
- WebUI:s `sv-SE` har 307 av 307 aktuella textnycklar, med korrekta
  platshållare och flaggresurs; se granskningsrapporten från 29 oktober.
- Projektets hela värdtestsvit kunde inte starta i denna fristående checkout,
  eftersom den förväntade syskonkatalogen `PS5_Vulkan` saknas. Ingen
  konsolkörning har utförts.

## Status

Ändringen är arkiverad och inskickad som
[PR #32](https://github.com/mihawk-99/PS5_MihawkOS/pull/32) den 27 oktober
2026. Pull requesten är öppen och ren, men ännu inte granskad eller sammanslagen.
Projektets fulla värdtestsvit återstår att köra i en miljö där syskonkatalogen
`PS5_Vulkan` finns tillgänglig.

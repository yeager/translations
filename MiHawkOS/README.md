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

## Granskning

- 60 av 60 textnycklar har svenska översättningar och samma platshållare som
  engelska källtexten.
- Riktat `test_pw_setup` godkänt: 10 av 10 språk har komplett text och
  skrivbara tecken.
- Hunspell-SV rapporterar bara etablerade produkt- och teknikord.
- `git diff --check` och Gitleaks för samtliga ändrade filer är godkända.
- Projektets hela värdtestsvit kunde inte starta i denna fristående checkout,
  eftersom den förväntade syskonkatalogen `PS5_Vulkan` saknas. Ingen
  konsolkörning har utförts.

## Status

Ändringen är klar som lokaliseringsunderlag och arkiverad. Ingen uppströms-Push
eller PR har skapats i denna körning: projektets instruktioner kräver en
uttrycklig pushbegäran i den aktuella uppgiften samt en full miljö för dess
publiceringskontroll.

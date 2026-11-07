# Svenska l10n-batcher – 7 november 2026

## RetroAchievements

25 oöversatta ärendeflödessträngar granskades i
`RetroAchievements/retroachievements-sv-20261107-ticket-flow-batch-04.json`.
React-taggar och platshållare kontrollerades före inskick. `l10n-lint` gav
inga fel. Crowdin API skapade 25 vanliga, ogranskade förslag och återkontroll
visade 0 oöversatta svenska strängar (1 763 av 1 763 översatta). Dessa förslag
är inte automatiskt godkända.

## PCSX2 Emulator

Den enda oöversatta svenska HTML-hjälptexten granskades i
`PCSX2/pcsx2-sv-20261107-cover-download-template.json`. URL-mallar,
Qt-/mallvariabler och HTML-entities jämfördes med källan; `l10n-lint` gav inga
fel. Crowdin API skapade ett ogranskat förslag. Återkontroll visade 0
oöversatta svenska strängar (5 313 av 5 313 översatta).

## RetroArch

32 oöversatta strängar för NFS, SMB, Androids Vulkan-drivrutin och
Vita3K/Xenia granskades i
`RetroArch/retroarch-sv-20261107-nfs-vulkan-vita3k-xenia.json`.
Platshållare och formatkontroll passerade. `l10n-lint` gav inga fel. Crowdin
API skapade 32 ogranskade förslag och återkontroll visade 0 oöversatta svenska
strängar (9 533 av 9 533 översatta). Befintliga QA-varningar granskas separat.

## Eden Emulator

De 190 nytillkomna oöversatta Qt-strängarna granskades i fem avgränsade
batcher: styrenheter och Steam, inmatningsprofiler, spelartilldelning,
spelaråterkoppling samt återstående styrenhetsgränssnitt. Underlagen är
`Eden-Emulator/eden-qt-sv-20261107-*-batch-0[1-5].json`.

Qt-platshållare, radbrytningar och produktnamn bevarades; svenska procenttal
fick standardmellanrum. `l10n-lint` gav inga fel för varje batch. Transifex
API uppdaterade 190 poster och varje inskickad måltext återlästes exakt.
Slutlig resursstatistik visar 2 122 av 2 122 svenska Qt-strängar översatta och
0 oöversatta. Android-resursen är fortsatt komplett. Översättningarnas
granskningsstatus hanteras separat av projektets Transifex-flöde.

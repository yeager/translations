# Zammad development – API-uppföljning 2026-11-13

## Aktuell komponentstatus

Weblates API lästes tillbaka för `zammad/zammad-development/sv`:

- 5 418 av 5 418 strängar är översatta (100 %),
- 0 poster är osäkra eller markerade för redigering,
- 0 Weblate-kontroller fallerar,
- 2 enheter har sammanlagt fem öppna förslag, och
- den senast sparade ändringen är en bakgrundscommit 2026-11-13 22:11 CET.

Den nedladdade PO-filen passerar `msgfmt --check`. `l10n-lint` rapporterar 19 varningar, främst avsiktligt oförändrade produkt-, protokoll- och API-namn. Två varningar gäller de öppna förslagen och är sakligt korrekta: ett extra blanksteg före kolon respektive punkt före smiley.

## Granskade förslag

- `No unread notifications for you. :)` bör vara `Inga olästa notifieringar. :)`, med samma punkt som i källan.
- `Did you know? You can help translating %s at:` bör vara `Visste du att du kan hjälpa till att översätta %s här:`, utan extra frågetecken och blanksteg före kolon.

## Inskick

API-tokenet kan läsa komponenten och förslagen, men saknar rättigheten att uppdatera enheter eller godkänna översättningar. Två explicita `PUT`-försök mot enheterna nekades med HTTP 403. Inga ändringar sparades, skickades eller godkändes upstream i denna uppföljning.

När tokenet har skrivbehörighet kan exakt de två granskade strängarna uppdateras och återläsas via Weblate-API:t.

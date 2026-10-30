# Hermes Agent: pågående svenska kataloger

Datum: 2026-10-30.

Detta är en återställningskopia av tre oinscheckade svenska kataloger från
den lokala arbetskopian. De hör **inte** till den redan inskickade,
avsiktligt partiella desktopkatalogen i PR #101116 och ska inte beskrivas som
uppströmsarbete.

| Fil | SHA-256 | Status |
| --- | --- | --- |
| `static-sv.yaml` | `451194825ae203369ad22e43d99147a4698ef87a1b8fa9a5e7f5b8cd423b003a` | YAML kan tolkas; behöver nyckelparitet och kontextgranskning. |
| `tui-sv.ts` | `2082ef37d960485217084576bdf2058dc86cfc2748c460280dc8ea252de1d1a6` | Behöver strukturmigrering, typkontroll, tester och radgranskning mot den engelska katalogen. |
| `web-sv.ts` | `754bb731e87c8b69a9aa3a54f0b7a19eaf1704b60c4889f5dfebc3fd89b0b19d` | Behöver typkontroll, tester och radgranskning mot den engelska katalogen. |

Gitleaks hittade inga hemligheter i någon av filerna. Ingen av dessa filer har
pushats eller skickats uppströms i detta steg.

## Typkontroll 2026-10-30

Den första TUI-typkontrollen hittade en gammal import av `Translations`; den
är rättad till `./types.js`. Därefter visar kontrollen tre verkliga
strukturavvikelser i katalogen: faktureringsblocket `autoReload` har blivit ett
underobjekt, abonnemangstexterna har flyttats till underblock och
hjälpkommandona ligger nu under `help.commands`. Katalogen ska därför inte
skickas in förrän den har synkats mot den aktuella engelska katalogstrukturen.

Webbkatalogen är däremot kompatibel med den aktuella koden: `npm run
typecheck --prefix web` passerar och `npm run test --prefix web` passerar med
69 testfiler och 473 tester. Vites och jsdoms kända miljövarningar om
`localStorage`, `window.open()` och canvas förekommer i testutskriften men
testsviten godkändes. Detta bevisar typ- och testkompatibilitet, inte att
webbens svenska text är radgranskad eller uppströmsinskickad.

## Statisk YAML-paritet 2026-10-30

En rekursiv jämförelse mot aktuell `locales/en.yaml` ger 3 510 engelska
bladnycklar och 371 svenska. 3 140 engelska nycklar saknas; den enda extra
svenska nyckeln är `gateway.status.free_tier`. Den statiska katalogen är
alltså en äldre partiell katalog, inte ett säkert underlag för inkrementell
insändning. Den behöver skapas om från den aktuella nyckelstrukturen och
granskas i hanterbara batcher.

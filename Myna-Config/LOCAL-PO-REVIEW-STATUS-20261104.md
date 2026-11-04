# Myna Config: lokal PO-granskning

Datum: 2026-11-04

Arbetsfil: `/Users/danielnylander/Downloads/ubuntu-desktop-translations-myna-config-sv.po`

## Projektkontext

Myna är Canonicals lokala tal-till-text för Ubuntu Desktop. Användaren
startar och stoppar diktering med en tangentbordsgenväg. En lokal,
konfinerad talmodell transkriberar ljudet och Myna matar in den färdiga
texten i det fokuserade programmet via IBus. Myna Settings installerar
modeller och skrivbordskomponenter, väljer aktiv modell samt hanterar
indikator, ljudåterkoppling och diagnostik. Aktuell release är 0.3.1,
publicerad 2026-10-29.

## Status

| Kontrollpunkt | Antal |
| --- | ---: |
| Strängar totalt | 417 |
| Översatta i råexporten | 20 |
| Lokalt granskade i arbetsfilen | 416 |
| Avsiktligt tomma metadatafält | 1 (`translator-credits`) |
| Återstående översättningssträngar | 0 |
| Upstream-verifierade i Weblate | 416 |

Slutlig lokal kandidat:
`candidates/2026-11-04/myna-config-sv-local-complete-review.po`

## Genomförd radgranskning

Granskningen omfattar introduktion, installation, kortkommando, lokal
integritet, modellval, modellinstallation, felåterställning, IBus,
diagnostik, modellanslutningar, inställningsåterläsning och
modellstatus. `{model}`, `{setting}`, `{size}`, `{percent}`, `{step}` samt
pluraler och radbrytningar har bevarats. `snapd`, `D-Bus`, IBus och GNOME
Shell behandlas som etablerade tekniska namn.

## Kontroller

- `msgfmt --check`: godkänd; endast den exporterade standardvarningen om
  `Project-Id-Version` återstår.
- `git diff --check`: godkänd.
- Gitleaks: inga hemligheter.
- `l10n-lint`: en avsiktligt tom `translator-credits`-post, en kontextuell
  musikterm-varning för ljudtemat *Röst* samt platshållar- och UI-fragment som
  kända falska positiva träffar.
- `svlang skrivregler`: inga skrivregelfel. Den bredare naturlighetskontrollen
  flaggar främst imperativ, UI-fragment, platshållare och tekniska token som
  falska positiva träffar.
- Hunspell-SV: endast produktnamn, standarder, platshållare och tekniska
  sammansättningar återstår i ordlistan.

## Upstreamstatus

API-batch 01 med 20 strängar skickades först till Hosted Weblate och lästes
tillbaka med `state: 20` och `translated: true`. Därefter skickades den
slutliga hela PO-filen via Weblates filuppladdning 2026-11-04. Weblate
rapporterade: **417 bearbetade, 20 hoppade över, 0 saknades och 396
uppdaterades**. De 20 hoppade över var redan identiska med den lokala
kandidaten. Totalt är därmed 416 UI-strängar inskickade som översättningar
som behöver redigeras; det enda tomma fältet är avsiktliga
`translator-credits`.

Weblate rapporterar fyra kontroller: en på den inskickade strängen och tre på
fortfarande tomma strängar. Den inskickade kontrollen är verifierat falsk
positiv: `Refresh` → `Uppdatera` jämförs med den andra engelska källan
`Update`. Båda är korrekt `Uppdatera` i respektive UI-kontext och ska inte
förvanskas för att undgå en återanvändningskontroll.

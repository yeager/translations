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
| Lokalt granskade i arbetsfilen | 178 |
| Återstående lokalt | 239 |
| Upstream-verifierade i Weblate | 20 |

Checkpointfil: `candidates/2026-11-04/myna-config-sv-local-178-reviewed.po`

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
- `l10n-lint` och `svlang` saknas i den aktuella skalets sökväg; deras
  kontrollområden har granskats manuellt för denna checkpoint.

## Upstreamstatus

API-batch 01 med 20 strängar har skickats till Hosted Weblate och lästs
tillbaka med `state: 20` och `translated: true`. Återstående lokala ändringar
är inte skickade.

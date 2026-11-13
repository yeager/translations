# PCSX2: ljud-, omslags- och emuleringsgranskning, 14 november 2026

Den här batchen omfattar nio svenska UI-strängar i den aktiva Crowdin-filen
`15`. Den rättar konkreta språkfel i ljudlatens, förinläsning, omslagsbilder,
emuleringshjälp och skalningshjälp.

| Sträng-ID | Kontext | Rättning |
| --- | --- | --- |
| `11282`, `11286` | SoundTouch-latens | Ersätter kvarlämnade engelska former av `expand` med `utvidgning`. |
| `13856` | skivförinläsning | Ersätter `precaching` med `förinläsning`. |
| `3805`, `11944`, `11946` | omslagsbilder | Ger idiomatisk text och samma synliga namn på filnamnsvalet i etikett och hjälptext. |
| `4295`, `4299` | emuleringsinställningar | Rättar trasig satskonstruktion respektive kvarlämnat `&apos;s`. |
| `8231` | FullscreenUI | Rättar den felöversatta beskrivningen av pixelkvoten. |

Filen `pcsx2-sv-audio-cover-emulation-batch-93-20261114.xliff` är en
deltafil med exakt dessa nio poster. Källtext och sammanhang har lästs i den
aktuella XLIFF-exporten från 11 november.

Kontroller före inskick:

- `xmllint --noout` och l10n-lint passerade.
- Platshållarna `%1` till `%4` och `:.2f` stämmer mellan käll- och måltext.
- Hunspell-sv kördes med sänkt prioritet enbart på batchens måltexter. Dess
  enda träffar är produktnamnen `PCSX2`, `GameDB`, `SOTC` och formatet `:.2f`.
- Svlang markerar tekniska namn och falska V2-varningar för etiketter och
  korrekta svenska satser. Varje träff har lästs manuellt.
- `git diff --check` och Gitleaks passerade.

`msgfmt` är inte tillämpligt på XLIFF. Upstream-resultatet fylls i först efter
verifierad Crowdin-import och återläsning.

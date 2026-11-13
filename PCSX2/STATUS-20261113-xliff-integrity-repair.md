# PCSX2: integritetskontroll av svensk XLIFF-export

- Datum: 2026-11-13
- Underlag: `pcsx2-qt_en_sv-SE.xliff`, hämtad 2026-11-11
- Exportens SHA-256: `4a3b0aca533492d382daa314bc090b6e28bc00e7649b3da5b8227c213e66fe72`
- Deltakatalog: `pcsx2-sv-xlf-integrity-repair-20261113.xliff`

Den kompletta exporten innehåller 5 345 enheter, alla med status
`translated`. En körning av `l10n-lint` på hela exporten hittade fem verkliga
fel där målet hade hamnat på fel källsträng:

- en radbrytning saknades i dialogen för anpassade inmatningsprofiler,
- två `Vulkan`-etiketter innehöll i stället en feltext för initiering,
- tidsformatet `{}` följt av `s` innehöll en orelaterad feltext, och
- USB-etiketten `B 1` innehöll en orelaterad kontotext.

Den femposter stora deltafilen återställer dessa mål och använder svenskt
mellanslag före sekundenheten. `l10n-lint` godkänner deltafilen utan fynd.
`xmllint --noout`, diffkontroll och Gitleaks passerar. Hunspell-sv och
svlang är körda på den svenska löptexten utan fynd.

Filen är arkiverad lokalt och pushad till vårt arkiv. Projektbindningen är
verifierad via Crowdin API: projekt 561203, `PCSX2 Emulator`,
[`pcsx2-emulator`](https://crowdin.com/project/pcsx2-emulator), med mål-
språket `sv-SE` och källfilen `pcsx2-qt_en.ts` (fil-ID 15). Den tidigare
sluggen `pcsx2` var alltså fel.

Deltafilen importerades den 13 november 2026 som oattesterade översättningar:
2 strängar och 47 ord uppdaterades, 0 strängar godkändes, och 3 strängar
hoppades över eftersom översättning och källtext medvetet är lika. Inga
strängar hoppades över av QA eller därför att de är dolda. Importresultatet är
API-verifierat; ingen separat upstreamgranskning eller merge är verifierad.

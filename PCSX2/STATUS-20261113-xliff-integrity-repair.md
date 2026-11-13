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

Filen är arkiverad lokalt. Den är ännu inte importerad till Crowdin i denna
statuspost; importresultat och eventuell upstreamgranskning ska verifieras
separat.

# Nextcloud Introvox – svenska batch 8, 2026-11-12

- Komponent: `o:nextcloud:p:nextcloud:r:introvox`.
- Omfattning: 25 strängar, index 175–199 i den aktuella API-exporten. Batchen gäller Administration, Inställningar, media och tillgänglighet.
- Kontroller: platshållarna `{size}` och `{megapixels}`, markup, em dash och tredubbla konsonanter bevarade; l10n-lint och Gitleaks godkända; svlangs V2-/fragmentträffar är kontextberoende; Hunspell-träffar är förväntade filformat och produktnamn (`WebVTT`, `PNG`, `JPEG`, `GIF`, `MP4`, `WebM`, `IntroVox`). `msgfmt` är inte tillämpligt för JSON-resursen.
- Upstream: inte uppladdat på grund av `locked`-taggar. Transifex API returnerar HTTP 409 för översättningsuppdatering.
- Status: lokalt granskat och väntar på upplåsning.

# ownCloud Android – svenska, 2026-11-12

- Komponent: `o:owncloud-org:p:owncloud-android:r:android`.
- Versionskälla: ownCloud Android v4.8.4, släppt 2026-08-31.
- Omfattning: 14 tidigare oöversatta UI- och versionsnotissträngar granskades mot Android-kontext och befintlig svensk katalog.
- Ändringar: 14. Råexport: 762 svenska översättningsposter i sex API-sidor efter uppladdningen.
- Kontroller: egen kontroll av JSON, platshållaren `%1$s`, markup, em dash och tredubbla konsonanter; `l10n-lint` utan träffar; `svlang` med endast falska positiva V2-/längdträffar när fristående UI-fragment analyseras tillsammans; `hunspell-sv` endast produktnamnet Infinite Scale; diffkontroll och Gitleaks godkända. `msgfmt` är inte tillämpligt för Transifex JSON-resursen.
- Upstream: en Transifex API-batch med 14 poster accepterades med HTTP 200. Samtliga 14 lästes tillbaka med exakt värde. Kontroll efteråt: 0 oöversatta strängar och ingen nästa sida.
- Status: uppladdat och verifierat i Transifex. Ingen separat merge-status finns för denna direktredigerade komponent.

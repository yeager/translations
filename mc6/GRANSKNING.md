# Svensk översättning av M-Commander (mc6)

Projekt: https://github.com/blue-panels/mc6
Weblate: https://translate.codeberg.org/projects/mc6/mc6/sv/
Granskad källrevision: 4fa8085, 12 september 2026.

Samtliga 2 575 aktiva katalogposter har översatts och språkgranskats mot de engelska källsträngarna. Den befintliga svenska översättningen hade 1 039 färdiga poster i den aktuella mallen. Weblate hade dessutom 632 poster markerade för redigering och 904 tomma poster.

Uppladdning via Codeberg Weblates API accepterade 1 664 nya eller ändrade poster och hoppade över 911 oförändrade poster. Servern visar 2 575 översatta poster och 0 ofärdiga. Formell granskningsstatus är avstängd för komponenten; servern accepterade därför metoden ”translate”, inte ”approve”. Språkgranskning är genomförd, men posterna har inte fått formell godkännandestatus.

Kontroller:

- Lokal Hunspell med /usr/share/hunspell/sv_SE.dic och sv_SE.aff. Utslaget i hunspell-sv.txt har granskats: kvarvarande träffar är huvudsakligen produktnamn, kod, förkortningar och sammansättningar som ordlistan saknar. Ingen extern stavningstjänst användes.
- msgfmt --check --check-format: 2 575 översatta meddelanden, inga fel.
- Separat kontroll av formatvariabler, pluralformer, radbrytningar, inledande/avslutande blanktecken, antal snabbtangentsmarkörer och sexteckensgränsen för knappraden: inga avvikelser.
- Ny extraktion med xgettext gav samma uppsättning strängnycklar som projektets mall.
- Q_ i lib/util.c verifierades: kontextprefixet före | tas bort vid visning. Äldre prefix i översättningar och nya översättningar utan prefix fungerar båda.

Exempel på rättningar i äldre text: extra ”1” före oktala rättigheter, ”flikar” i stället för tabulatorer, ”chatta” i chattr-fel, ”Markör” för cirkumflex samt saknad översättning av Shadows. Terminologin för teckenkodning, redigerare, filstatus och säkerhetskopiering har förbättrats.

Känd källbegränsning: sex strängar i projektets mall slutar mitt i en formatsträng vid GLib-makron som G_GSIZE_FORMAT/G_GINT64_FORMAT. De katalognycklar som projektet faktiskt använder har översatts; källkodens extraktionsproblem har inte ändrats inom översättningsarbetet. Det kan göra att dessa meddelanden förblir engelska vid körning. Ingen fullständig interaktiv körning av programmet har utförts.

Återläsning via API av samtliga 2 575 poster bekräftade att serverns översättningar exakt matchar den granskade filen. Kvarvarande 37 Weblate-varningar har inspekterats; de gäller huvudsakligen oförändrade tekniska namn, knappradsförkortningar, kontextnycklar, korrekt svensk plural av ”block”, avsiktlig kolumnjustering och terminologiförslag. De har inte massignorerats.

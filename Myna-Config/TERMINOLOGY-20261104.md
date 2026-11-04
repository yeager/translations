# Myna Config: svensk terminologi

Datum: 2026-11-04

Myna är lokal tal-till-text för Ubuntu: en tangentbordsgenväg styr en lokal
modell, och den färdiga transkriptionen matas in i det fokuserade programmet
via IBus. Termerna nedan har granskats mot denna användning och Myna-källans
UI- och inställningskontext.

| Engelska | Svenska | Sammanhang och undantag |
| --- | --- | --- |
| Dictation | diktering | Funktionen som fångar tal och matar in text; stor bokstav endast när det är ett egennamn eller rubrikdel. |
| speech-to-text model | tal-till-text-modell | Lokal modell som kör inferensen. |
| model | modell | Vald eller tillgänglig talmodell. |
| engine / inference engine | motor / inferensmotor | Programvarumotor som modellen körs på; undvik *maskin*. |
| input method | indatametod | IBus-baserad metod som matar in färdig text. |
| shortcut | tangentbordsgenväg | Skrivbordets aktiveringsgenväg. |
| indicator | dikteringsindikator | GNOME Shell-indikator för dikteringsstatus. |
| transcript / transcription | transkription | Resultatet av taligenkänningen; *transkriptionsblock* för den interna delen. |
| chunk commit | bekräfta transkriptionsblock | Intern inställning som fastställer ett delresultat efter tal eller paus. |
| streaming output | strömmande utdata | Partiella resultat medan tal bearbetas. |
| diagnostics | diagnostik | Integritetsskyddande system- och modellstatus, utan ljud eller transkription. |
| privacy-safe | integritetsskyddande | Används om diagnostiken, inte som absolut säkerhetsgaranti. |
| snapd | snapd | Produkt- och processnamn; översätts inte. |
| D-Bus | D-Bus | Teknisk plattformsterm; `D-Bus-anrop` i UI. |

## Granskningsanmärkningar

- `offset`, `cpu`, `memory`, `io`, BCP 47, IBus, GNOME Shell, PipeWire och
  platshållare behålls när de är API-, standard- eller programnamn.
- *Voice* i ljudstilsbeskrivningen avser ett ljudtema, inte en musikstämma;
  därför är **Röst** korrekt trots en generell musikterm-varning från
  l10n-lint.
- `translator-credits` lämnas tom: den posten ska innehålla frivilliga
  personuppgifter och får inte fyllas med en gissad eller oönskad identitet.

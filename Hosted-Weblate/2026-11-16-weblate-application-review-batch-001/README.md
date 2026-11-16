# Weblate Application – svenska, granskningsbatch 001

Datum: 2026-11-16  
Projekt: Hosted Weblate / Weblate  
Komponent: Application  
Arbetssätt: radvis granskning i Hosted Weblate

## Omfattning

Tio befintliga svenska översättningar med statusen **Behöver redigeras** granskades i sin konkreta gränssnitts- och aktivitetskontext och sparades direkt i Hosted Weblate.

| Engelska | Sparad svenska |
| --- | --- |
| Team administrator access to {team} was granted by {username}. | Administratörsåtkomst till gruppen {team} beviljades av {username}. |
| Team administrator access to {team} was removed by {username}. | Administratörsåtkomst till gruppen {team} togs bort av {username}. |
| Site-wide | Hela webbplatsen |
| Team created | Grupp skapad |
| Team changed | Senaste teamändring |
| Team deleted | Grupp borttagen |
| Team member added | Gruppmedlem tillagd |
| Team member removed | Gruppmedlem borttagen |
| Team member access changed | Gruppmedlems åtkomst ändrad |
| Connection timeout | Tidsgränsen för anslutningen överskreds |

## Status och verifiering

- Lokal granskning: klar, 10/10 strängar.
- Sparat upstream: klart, direkt i Hosted Weblate.
- Import/uppladdning: inte tillämpligt; varje sträng sparades i Weblates editor.
- Avläsning efter sparning: filtret `state:needs-editing` minskade från 59 till 49 strängar.
- Upstream-granskning och merge: inte separata steg för dessa direkt sparade Weblate-enheter och inte påstådda som utförda.

## Kontroller

- Radvis kontroll mot källtext, källplats och Weblates ordlista.
- Platshållarna `{team}` och `{username}` bevarades exakt.
- Diffkontroll: utförd mot den arkiverade batchposten.
- Gitleaks: passerade utan fynd.
- `msgfmt`: inte tillämpligt; ingen lokal gettext-export ingick i arbetet.
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda eftersom Hosted Weblate inte gav någon lokal katalogfil i denna batch.

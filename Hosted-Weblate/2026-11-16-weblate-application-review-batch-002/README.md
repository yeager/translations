# Weblate Application – svenska, granskningsbatch 002

Datum: 2026-11-16  
Projekt: Hosted Weblate / Weblate  
Komponent: Application  
Arbetssätt: radvis granskning i Hosted Weblate

## Omfattning

Tio strängar med statusen **Behöver redigeras** granskades mot källtext, källplats och Weblates ordlista. Varje färdig formulering sparades direkt i Hosted Weblate.

| Engelska | Sparad svenska |
| --- | --- |
| How many seconds to allow for connection and channel setup per attempt. | Hur många sekunder som får användas för anslutning och kanalupprättande per försök. |
| How many seconds to allow for sending and the broker delivery acknowledgement per attempt, after connection setup. | Hur många sekunder som får användas för sändning och meddelandeförmedlarens leveransbekräftelse per försök efter att anslutningen har upprättats. |
| Repository add-ons must be installed on the component owning the repository. | Förrådstillägg måste installeras på den komponent som äger förrådet. |
| a component you cannot access | en komponent som du inte har åtkomst till |
| You need to log in to upload translations. | Du måste logga in för att ladda upp översättningar. |
| Team audit log | Gruppens granskningslogg |
| Team audit entry | Gruppens granskningspost |
| Restricted components are not allowed by this billing plan. | Det här abonnemanget tillåter inte begränsade komponenter. |
| Externally managed billings cannot be merged. | Externhanterade faktureringar kan inte slås samman. |
| Format matching exceeded its time limit. | Formatmatchningen överskred tidsgränsen. |

## Status och verifiering

- Lokal granskning: klar, 10/10 strängar.
- Sparat upstream: klart, direkt i Hosted Weblate.
- Import/uppladdning: inte tillämpligt; varje sträng sparades i Weblates editor.
- Avläsning efter sparning: filtret `state:needs-editing` minskade från 49 till 39 strängar.
- Upstream-granskning och merge: inga separata steg för dessa direkt sparade Weblate-enheter; inget sådant påstås vara gjort.

## Kontroller

- Radvis kontroll mot källtext, källplats och tillämplig Weblate-ordlista.
- Diffkontroll: utförd mot den arkiverade batchposten.
- Gitleaks: passerade utan fynd.
- `msgfmt`: inte tillämpligt; ingen lokal gettext-export ingick i batchen.
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda eftersom Hosted Weblate inte gav någon lokal katalogfil i batchen.

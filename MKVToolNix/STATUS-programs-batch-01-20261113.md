# MKVToolNix `programs`: svensk UI-granskning, batch 01

Datum: 13 november 2026
Resurs: `moritz-bunkus/mkvtoolnix/programs` i Transifex
Omfattning: 9 av 3 134 aktiva svenska poster

## Genomförd radgranskning

Batchen rättar en felaktig versal intern sammansättning, ett oöversatt
`directories`, fyra saknade kortkommandon och tre accelerator- eller
UI-formuleringar. Källkontexten är kapitelredigeraren, inställningarna och
filhanteringsåtgärder i MKVToolNix GUI.

Den fullständiga radgranskningen av `programs` är **påbörjad, inte klar**.
Den tidigare täckningssiffran 3 134/3 134 betyder endast att alla poster har
en svensk måltext.

## Kontroller

- Färsk svensk PO-export från Transifex passerar `msgfmt --check`.
- Deltat är giltig JSON; l10n-lint rapporterar 0 problem.
- Acceleratorpariteten är kontrollerad för samtliga 9 poster.
- Hunspell-sv träffar bara acceleratorfragment samt tekniska termerna `UID`
  och `escape`.
- svlangs automatiska avvikelser kommer från sammanslagna GUI-etiketter och
  tekniska termer; de är bedömda i respektive kontext.
- Gitleaks och `git diff --check` passerade.
- `msgfmt` är inte tillämpligt direkt på JSON-deltat; kontrollen kördes på
  den hämtade PO-katalogen.

## Upstream

Alla 9 ändringar skickades i ett enda Transifex API-anrop 13 november 2026
18:13:46 UTC. API-svaret och en individuell återläsning per post bekräftar
exakt sparad måltext med `origin: API`. Ändringarna är inskickade men inte
markerade som granskade av projektet.

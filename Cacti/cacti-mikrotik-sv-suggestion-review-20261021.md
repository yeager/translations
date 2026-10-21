# Cacti MikroTik: granskningslogg, 2026-10-21

Granskningen omfattade samtliga externa förslag i Weblate-sökningen `has:suggestion AND NOT suggestion_author:yeager74`.

- `Interfaces` och `CPUs`: förslagen ändrade endast begynnelsebokstav och avvisades för att behålla rubrikstilen.
- `CPU %%%`: förslaget tog bort två procenttecken och avvisades.
- `Used Mem`: förslaget blandade språk och förkortning på ett otydligt sätt och avvisades.
- `Delete Device(s)`: förslaget lade in ett felaktigt mellanrum före `(er)` och avvisades.
- `%d Process`, `%d Processes`, `%d Minute`, `%d Week`, `%d Weeks`, `%d Months` och `%d Year`: samtliga förslag bytte `%d` mot `% d`, vilket bryter PHP-formatet; avvisade.

Efter granskningen gav samma Weblate-sökning inga träffar. Komponenten har 241 av 241 strängar översatta utan problem.

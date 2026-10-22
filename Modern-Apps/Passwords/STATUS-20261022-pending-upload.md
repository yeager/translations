# Modern Apps Passwords – väntande rättning

Kontrollerat rad för rad i Hosted Weblate 2026-10-22.

- Fem kontrollposter är produktnamn: Bitwarden, Google Chrome, LastPass, Dashlane och Proton Pass.
- Den engelska WebAuthn-termen `passkey` förekom i sex svenska måltexter. I aktuell svensk Apple-dokumentation används `nyckel` för samma lösenordsfria inloggningsmetod.
- Exporten använder därför `Nyckel`, `Nycklar`, `nyckeln` och `nyckelbegäran` i dessa måltexter.

Kontroller: XML-tolkning, `svlang skrivregler`, Hunspell-granskning och Gitleaks. Hunspellträffarna är produktnamn samt tekniska fil- och protokolltermer.

Hosted Weblate är i underhållsläge. Exporten ska jämföras med en färsk serverexport och skickas in när spärren har släppts.
